#!/usr/bin/env python3
"""Sync the MJ4U ads database (Supabase project mj4u-ads).

  python3 db_sync.py seed            # upsert products/tests/cells/hooks/creatives from the git CSVs (canonical)
  python3 db_sync.py pull --days 7   # pull daily ad-level Meta insights into ad_metrics_daily (read-only on Meta)
  python3 db_sync.py media           # ad preview link, post, video, thumbnail (+ links new ads to their Meta id by name)
  python3 db_sync.py all  --days 7   # seed + media + pull

The git CSVs stay the source of truth for what we BUILT; the database adds what Meta MEASURED.
Needs in ../.env: META_SYSTEM_USER_TOKEN, META_AD_ACCOUNT_ID, META_API_VERSION, SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY.
Stdlib only, like the rest of the engine.
"""
from __future__ import annotations
import argparse, csv, datetime as dt, json, re, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path
from upload_draft import load_env, ENV_PATH

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
REG = REPO / "products/_registry"
LED = REPO / "marketing/facebook-ads/_ledgers"
AD_KEY_RE = re.compile(r"\b([A-Za-z0-9-]+_[A-Za-z0-9]+-[A-Za-z0-9]+_[A-Za-z0-9]+)_(?:916|45)?_?v(\d{2})\b")
# Meta reports ONE event under several aliases (add_to_cart, offsite_conversion.fb_pixel_add_to_cart, onsite_web_add_to_cart,
# omni_add_to_cart...). Never sum them (that triple-counted ATC on 2026-11-18): take the first alias present, in this order.
ATC = ("omni_add_to_cart", "add_to_cart", "offsite_conversion.fb_pixel_add_to_cart")
CHK = ("omni_initiated_checkout", "initiate_checkout", "offsite_conversion.fb_pixel_initiate_checkout")
PUR = ("omni_purchase", "purchase", "offsite_conversion.fb_pixel_purchase")


# ---------- Supabase (PostgREST) ----------
class DB:
    def __init__(self, url: str, key: str):
        self.base = url.rstrip("/") + "/rest/v1/"
        self.h = {"apikey": key, "Content-Type": "application/json"}
        if not key.startswith("sb_"):            # legacy JWT service_role key also goes in Authorization;
            self.h["Authorization"] = f"Bearer {key}"   # new sb_secret_ keys are sent in the apikey header only

    def upsert(self, table: str, rows: list[dict], on_conflict: str):
        groups = {}                                       # PostgREST bulk insert needs identical keys per request;
        for r in rows:                                    # group by key set so an omitted column is left untouched
            groups.setdefault(tuple(sorted(r)), []).append(r)
        for batch in groups.values():
            self._post(table, batch, on_conflict)
        print(f"  {table}: {len(rows)} upserted")

    def _post(self, table: str, rows: list[dict], on_conflict: str):
        for i in range(0, len(rows), 500):
            req = urllib.request.Request(
                self.base + table + "?on_conflict=" + on_conflict, method="POST",
                data=json.dumps(rows[i:i + 500]).encode(),
                headers={**self.h, "Prefer": "resolution=merge-duplicates,return=minimal"})
            try:
                urllib.request.urlopen(req, timeout=60).read()
            except urllib.error.HTTPError as e:
                sys.exit(f"{table}: HTTP {e.code} {e.read().decode(errors='replace')[:500]}")

    def patch(self, table: str, match: str, values: dict):
        req = urllib.request.Request(self.base + table + "?" + match, method="PATCH", data=json.dumps(values).encode(),
                                     headers={**self.h, "Prefer": "return=minimal"})
        urllib.request.urlopen(req, timeout=60).read()

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

    db.upsert("codebook", [{k: clean(v) for k, v in r.items()} for r in rows(LED / "codebook.csv")], "dimension,code")
    db.upsert("tests", [{k: clean(v) for k, v in r.items()} for r in rows(LED / "tests.csv")], "test_id")
    db.upsert("concepts", [{**{k: clean(v) for k, v in r.items()}, "critic_score": clean(r["critic_score"], float),
                            "critic_spread": clean(r["critic_spread"], float)} for r in rows(LED / "concepts.csv")], "concept_id")
    db.upsert("executions", [{**{k: clean(v) for k, v in r.items()}, "is_bundle": clean(r["is_bundle"], bool) or False,
                              "critic_score": clean(r["critic_score"], float), "critic_spread": clean(r["critic_spread"], float)}
                             for r in rows(LED / "executions.csv")], "execution_id")
    db.upsert("cells", [{**{k: clean(v) for k, v in r.items()}, "is_control": clean(r["is_control"], bool)}
                        for r in rows(LED / "cells.csv")], "cell_id")
    db.upsert("hooks", [{**{k: clean(v) for k, v in r.items()}, "paid_by_s": clean(r["paid_by_s"], float),
                         "critic_score": clean(r["critic_score"], float), "critic_spread": clean(r["critic_spread"], float),
                         "onset_s": clean(r.get("onset_s"), float), "caption_on_s": clean(r.get("caption_on_s"), float),
                         "caption_words": clean(r.get("caption_words"), int), "truth_frame_s": clean(r.get("truth_frame_s"), float)}
                        for r in rows(LED / "hooks.csv")], "hook_id")
    cell_map = {r["cell_id"]: r for r in rows(LED / "cells.csv")}
    ads, cr = {}, []
    for r in rows(REG / "ad-creatives.csv"):
        cid = r["creative_id"]
        m = AD_KEY_RE.search(cid)
        key = f"{m.group(1)}_v{m.group(2)}" if m else cid
        ad = ads.setdefault(key, {"ad_key": key, "product_id": r["product_id"], "test_id": clean(r["test_id"]),
                                  "cell_id": clean(r["cell_id"]), "hook_id": clean(r["hook_id"]),
                                  "concept_code": clean(r["concept"]), "variant": clean(r["variant"]),
                                  "version": clean(r["version"], int), "length_s": clean(r["length_s"], float),
                                  "has_vo": clean(r["has_vo"], bool), "caption_style": clean(r["caption_style"]),
                                  "structure_desc": clean(r["structure"]), "ai_people": clean(r["ai_people"], bool),
                                  "concept_id": clean(cell_map.get(r["cell_id"], {}).get("concept_id")),
                                  "execution_id": clean(cell_map.get(r["cell_id"], {}).get("execution_id")),
                                  "meta_ad_id": None})
        ad["meta_ad_id"] = ad["meta_ad_id"] or clean(r["meta_ad_id"])   # one Meta ad carries both ratios
        cr.append({"creative_id": cid, "ad_key": key, "product_id": r["product_id"], "test_id": clean(r["test_id"]),
                   "ratio": clean(r["ratio"]), "music_source": clean(r["music_source"]),
                   "ai_people": clean(r["ai_people"], bool), "local_path": clean(r["local_path"]),
                   "drive_path": clean(r["drive_path"]), "sha256": clean(r["sha256"]), "recipe": clean(r["recipe"]),
                   "qa_status": clean(r["qa_status"]), "qa_report": clean(r["qa_report"]), "waivers": clean(r["waivers"]),
                   "notes": clean(r["notes"])})
    for r in rows(LED / "ads-legacy.csv"):            # ads launched before the ad_key naming rule
        ads[r["ad_key"]] = {"ad_key": r["ad_key"], "product_id": r["product_id"], "test_id": clean(r["test_id"]),
                            "concept_code": clean(r["concept_code"]), "variant": clean(r["variant"]),
                            "version": clean(r["version"], int), "meta_ad_id": clean(r["meta_ad_id"]),
                            "notes": clean(r["notes"])}
    for a in ads.values():
        if not a.get("meta_ad_id"):
            a.pop("meta_ad_id", None)      # keep the id `media` found on Meta; the CSV may not know it yet
    db.upsert("ads", list(ads.values()), "ad_key")
    db.upsert("creatives", cr, "creative_id")


# ---------- pull ----------
def acts(row, key, types) -> float:
    vals = {a.get("action_type"): float(a.get("value", 0)) for a in row.get(key, []) or []}
    return next((vals[t] for t in types if t in vals), 0.0)   # first alias present; aliases are the same event


def first(row, key) -> float:
    a = row.get(key)
    return float(a[0].get("value", 0)) if isinstance(a, list) and a else 0.0


def pull(db: DB, env: dict, days: int):
    acct = env["META_AD_ACCOUNT_ID"]
    acct = acct if acct.startswith("act_") else f"act_{acct}"
    since = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    until = dt.date.today().isoformat()
    fields = ("ad_id,ad_name,adset_id,campaign_id,impressions,reach,spend,inline_link_clicks,video_play_actions,"
              "video_p25_watched_actions,video_p50_watched_actions,video_p75_watched_actions,"
              "video_p95_watched_actions,video_p100_watched_actions,video_thruplay_watched_actions,"
              "video_avg_time_watched_actions,actions,action_values")
    q = {"level": "ad", "time_increment": 1, "fields": fields, "limit": 500,
         "time_range": json.dumps({"since": since, "until": until}), "access_token": env["META_SYSTEM_USER_TOKEN"]}
    url = f"https://graph.facebook.com/{env.get('META_API_VERSION', 'v26.0')}/{acct}/insights?" + urllib.parse.urlencode(q)
    known = db.select("ads", "select=ad_key,meta_ad_id")
    keys = {a["ad_key"] for a in known}
    by_id = {a["meta_ad_id"]: a["ad_key"] for a in known if a["meta_ad_id"]}
    out = []
    while url:
        try:
            page = json.loads(urllib.request.urlopen(url, timeout=120).read())
        except urllib.error.HTTPError as e:
            err = json.loads(e.read().decode(errors="replace")).get("error", {})
            sys.exit(f"Meta insights: HTTP {e.code} {err.get('message')} (code {err.get('code')}, subcode {err.get('error_subcode')})")
        for d in page.get("data", []):
            m = AD_KEY_RE.search(d.get("ad_name", ""))
            out.append({
                "meta_ad_id": d["ad_id"], "date": d["date_start"], "ad_name": d.get("ad_name"),
                "ad_key": by_id.get(d["ad_id"]) or ((f"{m.group(1)}_v{m.group(2)}" if m else None)
                                                    if m and f"{m.group(1)}_v{m.group(2)}" in keys else None),
                "adset_id": d.get("adset_id"), "campaign_id": d.get("campaign_id"),
                "impressions": int(float(d.get("impressions", 0))), "reach": int(float(d.get("reach", 0))),
                "spend": float(d.get("spend", 0)), "link_clicks": int(float(d.get("inline_link_clicks", 0))),
                "video_plays": int(first(d, "video_play_actions")), "video_3s": int(acts(d, "actions", ("video_view",))),   # Meta's 3-second video view (v26 dropped video_3_sec_watched_actions)
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


# ---------- media (ad preview links, post, video, thumbnail) ----------
def graph(env: dict, path: str, params: dict) -> dict:
    q = {**params, "access_token": env["META_SYSTEM_USER_TOKEN"]}
    url = f"https://graph.facebook.com/{env.get('META_API_VERSION', 'v26.0')}/{path}?" + urllib.parse.urlencode(q)
    try:
        return json.loads(urllib.request.urlopen(url, timeout=120).read())
    except urllib.error.HTTPError as e:
        err = json.loads(e.read().decode(errors="replace")).get("error", {})
        sys.exit(f"Meta {path}: HTTP {e.code} {err.get('message')}")


def media(db: DB, env: dict):
    acct = env["META_AD_ACCOUNT_ID"]
    acct = acct if acct.startswith("act_") else f"act_{acct}"
    known = db.select("ads", "select=ad_key,meta_ad_id")
    keys = {a["ad_key"] for a in known}
    by_id = {a["meta_ad_id"]: a["ad_key"] for a in known if a["meta_ad_id"]}
    fields = ("id,name,effective_status,preview_shareable_link,creative{thumbnail_url,video_id,effective_object_story_id,"
              "object_story_spec{video_data{video_id}},asset_feed_spec{videos{video_id}}}")
    page = graph(env, f"{acct}/ads", {"fields": fields, "limit": 200})
    n, now = 0, dt.datetime.now(dt.timezone.utc).isoformat()
    while True:
        for a in page.get("data", []):
            m = AD_KEY_RE.search(a.get("name", ""))
            key = by_id.get(a["id"]) or (f"{m.group(1)}_v{m.group(2)}" if m and f"{m.group(1)}_v{m.group(2)}" in keys else None)
            if not key:
                continue
            c = a.get("creative") or {}
            vid = c.get("video_id") or ((c.get("object_story_spec") or {}).get("video_data") or {}).get("video_id") \
                or next((v.get("video_id") for v in (c.get("asset_feed_spec") or {}).get("videos", [])), None)
            row = {"meta_ad_id": a["id"], "meta_ad_name": a.get("name"), "meta_status": a.get("effective_status"),
                   "preview_url": a.get("preview_shareable_link"), "thumbnail_url": c.get("thumbnail_url"),
                   "post_url": ("https://www.facebook.com/{}/posts/{}".format(*c["effective_object_story_id"].split("_", 1))
                                if "_" in (c.get("effective_object_story_id") or "") else None),
                   "media_refreshed_at": now}
            if vid:
                v = graph(env, vid, {"fields": "permalink_url,picture,length"})
                row["video_url"] = "https://www.facebook.com" + v["permalink_url"] if v.get("permalink_url", "").startswith("/") else v.get("permalink_url")
                row["video_length_s"] = float(v["length"]) if v.get("length") else None
                row["thumbnail_url"] = row["thumbnail_url"] or v.get("picture")
            db.patch("ads", "ad_key=eq." + urllib.parse.quote(key), row)
            n += 1
        nxt = page.get("paging", {}).get("next")
        if not nxt:
            break
        page = json.loads(urllib.request.urlopen(nxt, timeout=120).read())
    print(f"  ads media: {n} ads updated (preview/post/video/thumbnail)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["seed", "media", "pull", "all"])
    ap.add_argument("--days", type=int, default=7)
    a = ap.parse_args()
    env = load_env(ENV_PATH)
    missing = [k for k in ("SUPABASE_URL", "SUPABASE_SERVICE_ROLE_KEY") if not env.get(k)]
    if missing:
        sys.exit(f"missing in {ENV_PATH}: {', '.join(missing)}")
    db = DB(env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"])
    if a.cmd in ("seed", "all"):
        seed(db)
    if a.cmd in ("media", "all"):
        media(db, env)
    if a.cmd in ("pull", "all"):
        pull(db, env, a.days)


if __name__ == "__main__":
    main()
