#!/usr/bin/env python3
"""Sync the MJ4U ads database (Supabase project mj4u-ads).

  python3 db_sync.py seed            # upsert products/tests/cells/hooks/creatives from the git CSVs (canonical)
  python3 db_sync.py pull --days 7   # pull daily ad-level Meta insights into ad_metrics_daily (read-only on Meta)
  python3 db_sync.py media           # ad preview link, post, video, thumbnail (+ links new ads to their Meta id by name)
  python3 db_sync.py all  --days 7   # seed + media + pull
  python3 db_sync.py rebuild         # re-derive typed metric columns from stored raw rows (after changing typed_from_raw)

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
# Naming convention (research/reference/video-team/README.md §4a):
#   ad key   {PRODUCT}_{ROUND}_{CONCEPT}{EXEC}-{HOOK}_{VAR}_v{NN}      e.g. MJ4U-003_C0_K01X1-H07_E0_v01   (goes in the Meta ad name)
#   file     {PRODUCT}_{ROUND}_{CONCEPT}{EXEC}-{HOOK}_{VAR}_{RATIO}_v{NN}   e.g. MJ4U-003_C0_K01X1-H07_E0_916_v01
#   ROUND    C0 | C1 | C2 | H1 | H2 | B | S   (deep plan; must match cells.round_type)
AD_KEY_RE = re.compile(r"\b(?P<base>[A-Z0-9]+-\d{3}_(?:C[0-2]|H[12]|B|S)_K\d{2}X\d+-H\d{2}_[A-Z]\d+)_(?:(?:916|45)_)?v(?P<v>\d{2})\b")


def ad_key_of(name: str):
    m = AD_KEY_RE.search(name or "")
    return f"{m['base']}_v{m['v']}" if m else None
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
        key = ad_key_of(cid)
        if not key:
            sys.exit(f"ad-creatives.csv: creative_id {cid!r} doesn't follow the naming convention (README §4a)")
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


# Every ad-level Ads Insights field we know of. Fields the API version rejects are dropped automatically (and logged),
# so nothing Meta offers is silently missed. The FULL response row is stored in ad_metrics_daily.raw.
INSIGHT_FIELDS_ALL = (
    "account_currency,account_id,account_name,ad_id,ad_name,adset_id,adset_name,campaign_id,campaign_name,objective,optimization_goal,"
    "buying_type,attribution_setting,date_start,date_stop,impressions,reach,frequency,spend,social_spend,cpm,cpp,clicks,ctr,cpc,"
    "unique_clicks,unique_ctr,cost_per_unique_click,inline_link_clicks,inline_link_click_ctr,cost_per_inline_link_click,"
    "unique_inline_link_clicks,unique_inline_link_click_ctr,cost_per_unique_inline_link_click,unique_link_clicks_ctr,"
    "outbound_clicks,outbound_clicks_ctr,cost_per_outbound_click,unique_outbound_clicks,unique_outbound_clicks_ctr,"
    "cost_per_unique_outbound_click,website_ctr,inline_post_engagement,cost_per_inline_post_engagement,"
    "actions,unique_actions,action_values,cost_per_action_type,cost_per_unique_action_type,conversions,conversion_values,"
    "cost_per_conversion,purchase_roas,website_purchase_roas,mobile_app_purchase_roas,converted_product_quantity,"
    "converted_product_value,catalog_segment_value,video_play_actions,video_continuous_2_sec_watched_actions,"
    "video_30_sec_watched_actions,video_p25_watched_actions,video_p50_watched_actions,video_p75_watched_actions,"
    "video_p95_watched_actions,video_p100_watched_actions,video_thruplay_watched_actions,cost_per_thruplay,"
    "video_avg_time_watched_actions,video_time_watched_actions,video_play_curve_actions,full_view_impressions,full_view_reach,"
    "estimated_ad_recallers,estimated_ad_recall_rate,cost_per_estimated_ad_recallers,quality_ranking,engagement_rate_ranking,"
    "conversion_rate_ranking,instant_experience_clicks_to_open,instant_experience_clicks_to_start,"
    "instant_experience_outbound_clicks,canvas_avg_view_percent,canvas_avg_view_time")
INVALID_FIELD_RE = re.compile(r"\(#100\)\s*([a-z0-9_]+) is not valid for fields param")


def typed_from_raw(d: dict) -> dict:
    """The ONE transform from a raw Meta insights row to the typed columns the dashboard reads.
    Change counting rules here, then run `db_sync.py rebuild` to re-derive every stored day from `raw`."""
    return {
        "meta_ad_id": d["ad_id"], "date": d["date_start"], "ad_name": d.get("ad_name"),
        "adset_id": d.get("adset_id"), "campaign_id": d.get("campaign_id"),
        "impressions": int(float(d.get("impressions", 0))), "reach": int(float(d.get("reach", 0))),
        "spend": float(d.get("spend", 0)), "link_clicks": int(float(d.get("inline_link_clicks", 0))),
        "video_plays": int(first(d, "video_play_actions")), "video_3s": int(acts(d, "actions", ("video_view",))),
        **{f"video_p{p}": int(first(d, f"video_p{p}_watched_actions")) for p in (25, 50, 75, 95, 100)},
        "thruplays": int(first(d, "video_thruplay_watched_actions")),
        "avg_watch_s": first(d, "video_avg_time_watched_actions") or None,
        "add_to_cart": int(acts(d, "actions", ATC)), "checkouts": int(acts(d, "actions", CHK)),
        "purchases": int(acts(d, "actions", PUR)), "purchase_value": acts(d, "action_values", PUR)}


def rebuild(db: DB):
    """Re-derive every typed metric column from the stored raw Meta rows. No Meta calls."""
    rows, n = [], 0
    while True:
        page = db.select("ad_metrics_daily", f"select=meta_ad_id,date,ad_key,raw&raw=not.is.null&order=meta_ad_id,date&limit=1000&offset={n}")
        rows += page; n += len(page)
        if len(page) < 1000:
            break
    out = [{**typed_from_raw(r["raw"]), "ad_key": r["ad_key"]} for r in rows]
    if out:
        db.upsert("ad_metrics_daily", out, "meta_ad_id,date")
    print(f"  rebuild: {len(out)} ad-days re-derived from stored raw rows")


def pull(db: DB, env: dict, days: int):
    acct = env["META_AD_ACCOUNT_ID"]
    acct = acct if acct.startswith("act_") else f"act_{acct}"
    since = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    until = dt.date.today().isoformat()
    fields = INSIGHT_FIELDS_ALL.split(",")
    known = db.select("ads", "select=ad_key,meta_ad_id")
    keys = {a["ad_key"] for a in known}
    by_id = {a["meta_ad_id"]: a["ad_key"] for a in known if a["meta_ad_id"]}
    base = f"https://graph.facebook.com/{env.get('META_API_VERSION', 'v26.0')}/{acct}/insights?"
    dropped, out, skipped = [], [], set()
    while True:                                     # drop any field this API version rejects, then retry
        q = {"level": "ad", "time_increment": 1, "fields": ",".join(fields), "limit": 200,
             "time_range": json.dumps({"since": since, "until": until}), "access_token": env["META_SYSTEM_USER_TOKEN"]}
        try:
            page = json.loads(urllib.request.urlopen(base + urllib.parse.urlencode(q), timeout=120).read())
            break
        except urllib.error.HTTPError as e:
            msg = json.loads(e.read().decode(errors="replace")).get("error", {}).get("message", "")
            m = INVALID_FIELD_RE.search(msg)
            if not m or m.group(1) not in fields:
                sys.exit(f"Meta insights: HTTP {e.code} {msg}")
            fields.remove(m.group(1)); dropped.append(m.group(1))
    fields_used = ",".join(fields)
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    while True:
        for d in page.get("data", []):
            key = by_id.get(d["ad_id"]) or (ad_key_of(d.get("ad_name")) if ad_key_of(d.get("ad_name")) in keys else None)
            if not key:                              # not built under the framework (not registered): don't store
                skipped.add(d.get("ad_name")); continue
            out.append({**typed_from_raw(d), "ad_key": key, "raw": d, "fields_requested": fields_used, "pulled_at": now})
        nxt = page.get("paging", {}).get("next")
        if not nxt:
            break
        page = json.loads(urllib.request.urlopen(nxt, timeout=120).read())
    if out:
        db.upsert("ad_metrics_daily", out, "meta_ad_id,date")
    db.ad_days = len(out)
    print(f"  {len(out)} ad-days stored {since}..{until} ({len(fields)} insight fields; dropped by API: {', '.join(dropped) or 'none'})")
    if skipped:
        print(f"  skipped {len(skipped)} unregistered ads (not in the creative log): " + "; ".join(sorted(skipped)[:10]))


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
    fields = ("id,name,status,effective_status,configured_status,created_time,updated_time,campaign_id,adset_id,bid_amount,"
              "tracking_specs,conversion_specs,preview_shareable_link,"
              "creative{id,name,title,body,call_to_action_type,thumbnail_url,image_url,video_id,effective_object_story_id,"
              "object_story_spec,asset_feed_spec,url_tags}")
    page = graph(env, f"{acct}/ads", {"fields": fields, "limit": 200})
    n, now = 0, dt.datetime.now(dt.timezone.utc).isoformat()
    while True:
        for a in page.get("data", []):
            key = by_id.get(a["id"]) or (ad_key_of(a.get("name")) if ad_key_of(a.get("name")) in keys else None)
            if not key:
                continue
            c = a.get("creative") or {}
            vid = c.get("video_id") or ((c.get("object_story_spec") or {}).get("video_data") or {}).get("video_id") \
                or next((v.get("video_id") for v in (c.get("asset_feed_spec") or {}).get("videos", [])), None)
            row = {"meta_ad_id": a["id"], "meta_ad_name": a.get("name"), "meta_status": a.get("effective_status"),
                   "preview_url": a.get("preview_shareable_link"), "thumbnail_url": c.get("thumbnail_url"),
                   "post_url": ("https://www.facebook.com/{}/posts/{}".format(*c["effective_object_story_id"].split("_", 1))
                                if "_" in (c.get("effective_object_story_id") or "") else None),
                   "media_refreshed_at": now, "meta_raw": a}
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
    ap.add_argument("cmd", choices=["seed", "media", "pull", "all", "rebuild"])
    ap.add_argument("--days", type=int, default=7)
    a = ap.parse_args()
    env = load_env(ENV_PATH)
    missing = [k for k in ("SUPABASE_URL", "SUPABASE_SERVICE_ROLE_KEY") if not env.get(k)]
    if missing:
        sys.exit(f"missing in {ENV_PATH}: {', '.join(missing)}")
    db = DB(env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"])
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    try:
        run(db, env, a)
    except BaseException as e:                       # record the failure (incl. sys.exit messages), then fail loudly
        if not isinstance(e, SystemExit) or e.code not in (0, None):
            heartbeat(db, a.cmd, started, False, getattr(db, "ad_days", None), str(e)[:500])
        raise
    heartbeat(db, a.cmd, started, True, getattr(db, "ad_days", None), "ok")


def heartbeat(db, cmd, started, ok, ad_days, message):
    import socket
    try:
        db._post("sync_runs", [{"started_at": started, "finished_at": dt.datetime.now(dt.timezone.utc).isoformat(), "command": cmd,
                                "ok": ok, "ad_days": ad_days, "message": message, "host": socket.gethostname()}], "run_id")
    except BaseException as e:                       # a failed heartbeat must not hide the real error
        print(f"  (heartbeat not recorded: {e})")


def run(db, env, a):
    if a.cmd == "rebuild":
        return rebuild(db)
    if a.cmd in ("seed", "all"):
        seed(db)
    if a.cmd in ("media", "all"):
        media(db, env)
    if a.cmd in ("pull", "all"):
        pull(db, env, a.days)


if __name__ == "__main__":
    main()
