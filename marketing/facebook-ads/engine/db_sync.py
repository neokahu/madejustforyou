#!/usr/bin/env python3
"""Sync the MJ4U ads database (Supabase project mj4u-ads).

  python3 db_sync.py seed            # upsert products/tests/cells/hooks/creatives from the git CSVs (canonical)
  python3 db_sync.py pull --days 7   # pull daily ad-level Meta insights into ad_metrics_daily (read-only on Meta)
  python3 db_sync.py all  --days 7   # both

The git CSVs stay the source of truth for what we BUILT; the database adds what Meta MEASURED.
Needs in ../.env: META_SYSTEM_USER_TOKEN, META_AD_ACCOUNT_ID, META_API_VERSION, SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY.
Stdlib only, like the rest of the engine.
"""
from __future__ import annotations
import argparse, csv, datetime as dt, json, re, sys, urllib.parse, urllib.request
from pathlib import Path
from upload_draft import load_env, ENV_PATH

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
REG = REPO / "products/_registry"
LED = REPO / "marketing/facebook-ads/_ledgers"
AD_KEY_RE = re.compile(r"\b([A-Za-z0-9-]+_[A-Za-z0-9]+-[A-Za-z0-9]+_[A-Za-z0-9]+)_(?:916|45)?_?v(\d{2})\b")
ATC = ("add_to_cart", "offsite_conversion.fb_pixel_add_to_cart", "onsite_web_add_to_cart")
CHK = ("initiate_checkout", "offsite_conversion.fb_pixel_initiate_checkout", "onsite_web_initiate_checkout")
PUR = ("purchase", "offsite_conversion.fb_pixel_purchase", "onsite_web_purchase")


# ---------- Supabase (PostgREST) ----------
class DB:
    def __init__(self, url: str, key: str):
        self.base = url.rstrip("/") + "/rest/v1/"
        self.h = {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}

    def upsert(self, table: str, rows: list[dict], on_conflict: str):
        for i in range(0, len(rows), 500):
            req = urllib.request.Request(
                self.base + table + "?on_conflict=" + on_conflict, method="POST",
                data=json.dumps(rows[i:i + 500]).encode(),
                headers={**self.h, "Prefer": "resolution=merge-duplicates,return=minimal"})
            urllib.request.urlopen(req, timeout=60).read()
        print(f"  {table}: {len(rows)} upserted")

    def select(self, table: str, q: str) -> list[dict]:
        req = urllib.request.Request(self.base + table + "?" + q, headers=self.h)
        return json.loads(urllib.request.urlopen(req, timeout=60).read())


def clean(v, kind=str):
    if v is None or str(v).strip() == "":
        return None
    v = str(v).strip()
    if kind is bool:
        return v.lower() in ("true", "yes", "1", "y")
    if kind in (int, float):
        try:
            return kind(float(v))
        except ValueError:
            return None
    return v


def rows(path: Path) -> list[dict]:
    return list(csv.DictReader(open(path, newline=""))) if path.exists() else []


# ---------- seed ----------
def seed(db: DB):
    econ = json.load(open(HERE / "config/products.json"))["products"]
    prods = []
    for r in rows(REG / "product-tracker.csv"):
        prods.append({"product_id": r["product_id"], "name": r["product_name"], "recipient": clean(r["recipient"]),
                      "stage": clean(r["stage"]), "store_url": clean(r["store_url"]), "notes": clean(r["notes"])})
    known = {p["product_id"] for p in prods}
    for r in rows(REG / "ad-creatives.csv"):           # products built before getting an MJ4U id
        if r["product_id"] not in known:
            prods.append({"product_id": r["product_id"], "name": r["product_id"].replace("-", " "), "stage": "ads"})
            known.add(r["product_id"])
    for p in prods:
        e = econ.get(p["product_id"])
        if e:
            contrib = e["revenue_per_order"] - e["cogs_all_in"] - e["fee_pct"] * e["revenue_per_order"]
            p["price"] = e.get("reported_value_per_order")
            p["break_even_cpa"] = round(contrib, 2)
            p["break_even_roas"] = round(e["reported_value_per_order"] / contrib, 3) if contrib > 0 else None
    db.upsert("products", prods, "product_id")

    db.upsert("tests", [{k: clean(v) for k, v in r.items()} for r in rows(LED / "tests.csv")], "test_id")
    db.upsert("cells", [{**{k: clean(v) for k, v in r.items()}, "is_control": clean(r["is_control"], bool)}
                        for r in rows(LED / "cells.csv")], "cell_id")
    db.upsert("hooks", [{**{k: clean(v) for k, v in r.items()}, "paid_by_s": clean(r["paid_by_s"], float),
                         "critic_score": clean(r["critic_score"], float), "critic_spread": clean(r["critic_spread"], float)}
                        for r in rows(LED / "hooks.csv")], "hook_id")
    cr = []
    for r in rows(REG / "ad-creatives.csv"):
        cid = r["creative_id"]
        m = AD_KEY_RE.search(cid)
        cr.append({"creative_id": cid, "ad_key": f"{m.group(1)}_v{m.group(2)}" if m else cid,
                   "product_id": r["product_id"], "test_id": clean(r["test_id"]), "cell_id": clean(r["cell_id"]),
                   "hook_id": clean(r["hook_id"]), "concept_code": clean(r["concept"]), "variant": clean(r["variant"]),
                   "ratio": clean(r["ratio"]), "version": clean(r["version"], int), "length_s": clean(r["length_s"], float),
                   "has_vo": clean(r["has_vo"], bool), "caption_style": clean(r["caption_style"]),
                   "structure": clean(r["structure"]), "music_source": clean(r["music_source"]),
                   "ai_people": clean(r["ai_people"], bool), "local_path": clean(r["local_path"]),
                   "drive_path": clean(r["drive_path"]), "sha256": clean(r["sha256"]), "recipe": clean(r["recipe"]),
                   "qa_status": clean(r["qa_status"]), "qa_report": clean(r["qa_report"]), "waivers": clean(r["waivers"]),
                   "meta_ad_id": clean(r["meta_ad_id"]), "notes": clean(r["notes"])})
    db.upsert("creatives", cr, "creative_id")


# ---------- pull ----------
def acts(row, key, types) -> float:
    return sum(float(a.get("value", 0)) for a in row.get(key, []) or [] if a.get("action_type") in types)


def first(row, key) -> float:
    a = row.get(key)
    return float(a[0].get("value", 0)) if isinstance(a, list) and a else 0.0


def pull(db: DB, env: dict, days: int):
    acct = env["META_AD_ACCOUNT_ID"]
    acct = acct if acct.startswith("act_") else f"act_{acct}"
    since = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    until = dt.date.today().isoformat()
    fields = ("ad_id,ad_name,adset_id,campaign_id,impressions,reach,spend,inline_link_clicks,video_play_actions,"
              "video_3_sec_watched_actions,video_p25_watched_actions,video_p50_watched_actions,video_p75_watched_actions,"
              "video_p95_watched_actions,video_p100_watched_actions,video_thruplay_watched_actions,"
              "video_avg_time_watched_actions,actions,action_values")
    q = {"level": "ad", "time_increment": 1, "fields": fields, "limit": 500,
         "time_range": json.dumps({"since": since, "until": until}), "access_token": env["META_SYSTEM_USER_TOKEN"]}
    url = f"https://graph.facebook.com/{env.get('META_API_VERSION', 'v26.0')}/{acct}/insights?" + urllib.parse.urlencode(q)
    by_id = {c["meta_ad_id"]: c["ad_key"] for c in db.select("creatives", "select=meta_ad_id,ad_key&meta_ad_id=not.is.null")}
    out = []
    while url:
        page = json.loads(urllib.request.urlopen(url, timeout=120).read())
        for d in page.get("data", []):
            m = AD_KEY_RE.search(d.get("ad_name", ""))
            out.append({
                "meta_ad_id": d["ad_id"], "date": d["date_start"], "ad_name": d.get("ad_name"),
                "ad_key": by_id.get(d["ad_id"]) or (f"{m.group(1)}_v{m.group(2)}" if m else None),
                "adset_id": d.get("adset_id"), "campaign_id": d.get("campaign_id"),
                "impressions": int(float(d.get("impressions", 0))), "reach": int(float(d.get("reach", 0))),
                "spend": float(d.get("spend", 0)), "link_clicks": int(float(d.get("inline_link_clicks", 0))),
                "video_plays": int(first(d, "video_play_actions")), "video_3s": int(first(d, "video_3_sec_watched_actions")),
                **{f"video_p{p}": int(first(d, f"video_p{p}_watched_actions")) for p in (25, 50, 75, 95, 100)},
                "thruplays": int(first(d, "video_thruplay_watched_actions")),
                "avg_watch_s": first(d, "video_avg_time_watched_actions") or None,
                "add_to_cart": int(acts(d, "actions", ATC)), "checkouts": int(acts(d, "actions", CHK)),
                "purchases": int(acts(d, "actions", PUR)), "purchase_value": acts(d, "action_values", PUR),
                "pulled_at": dt.datetime.now(dt.timezone.utc).isoformat()})
        url = page.get("paging", {}).get("next")
    if out:
        db.upsert("ad_metrics_daily", out, "meta_ad_id,date")
    unmapped = sorted({r["ad_name"] for r in out if not r["ad_key"]})
    print(f"  {len(out)} ad-days {since}..{until}; unmapped ads (no ad_key): {len(unmapped)}")
    for n in unmapped[:20]:
        print("   -", n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["seed", "pull", "all"])
    ap.add_argument("--days", type=int, default=7)
    a = ap.parse_args()
    env = load_env(ENV_PATH)
    missing = [k for k in ("SUPABASE_URL", "SUPABASE_SERVICE_ROLE_KEY") if not env.get(k)]
    if missing:
        sys.exit(f"missing in {ENV_PATH}: {', '.join(missing)}")
    db = DB(env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"])
    if a.cmd in ("seed", "all"):
        seed(db)
    if a.cmd in ("pull", "all"):
        pull(db, env, a.days)


if __name__ == "__main__":
    main()
