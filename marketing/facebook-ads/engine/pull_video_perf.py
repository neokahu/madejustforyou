#!/usr/bin/env python3
"""Read-only: pull per-ad video performance (hook + retention) for a campaign."""
import sys, json
from upload_draft import Uploader, load_env, ENV_PATH

CAMPAIGN = sys.argv[1] if len(sys.argv) > 1 else "120251953447920556"  # traffic test

def v(row, key):
    a = row.get(key)
    if isinstance(a, list) and a:
        try: return float(a[0].get("value", 0))
        except Exception: return 0.0
    return 0.0

def main():
    env = load_env(ENV_PATH)
    up = Uploader(env["META_SYSTEM_USER_TOKEN"], env["META_AD_ACCOUNT_ID"], env.get("META_API_VERSION", "v26.0"))
    fields = ("ad_name,impressions,spend,cpm,inline_link_clicks,inline_link_click_ctr,"
              "video_3_sec_watched_actions,video_p25_watched_actions,video_p50_watched_actions,"
              "video_p75_watched_actions,video_p95_watched_actions,video_p100_watched_actions,"
              "video_avg_time_watched_actions,video_thruplay_watched_actions,actions")
    try:
        r = up.get(f"{CAMPAIGN}/insights", {"fields": fields, "level": "ad", "date_preset": "today"})
    except Exception:
        r = up.get(f"{CAMPAIGN}/insights", {"fields": fields, "level": "ad"})
    rows = r.get("data", [])
    if not rows:
        print("no delivery data yet."); return 0
    for d in rows:
        imp = float(d.get("impressions", 0)) or 1
        s3 = v(d, "video_3_sec_watched_actions")
        p25, p50, p75, p95, p100 = (v(d, f"video_p{x}_watched_actions") for x in (25, 50, 75, 95, 100))
        thru = v(d, "video_thruplay_watched_actions")
        avg = v(d, "video_avg_time_watched_actions")
        atc = next((float(a["value"]) for a in d.get("actions", []) if a["action_type"] in
                    ("add_to_cart", "offsite_conversion.fb_pixel_add_to_cart", "onsite_web_add_to_cart")), 0.0)
        lc = float(d.get("inline_link_clicks", 0))
        print(f"\n=== {d.get('ad_name')} ===")
        print(f"  spend ${float(d.get('spend',0)):.2f} | impr {int(imp)} | CPM ${float(d.get('cpm',0)):.2f}"
              f" | link-clicks {int(lc)} | link-CTR {float(d.get('inline_link_click_ctr',0)):.2f}%")
        print(f"  HOOK (3s/impr): {s3/imp*100:5.1f}%   ThruPlay/impr: {thru/imp*100:5.1f}%   avg watch: {avg:.1f}s")
        print(f"  RETENTION (of impressions):  25%={p25/imp*100:5.1f}  50%={p50/imp*100:5.1f}"
              f"  75%={p75/imp*100:5.1f}  95%={p95/imp*100:5.1f}  100%={p100/imp*100:5.1f}")
        if s3:
            print(f"  HOLD (of 3s viewers):        50%={p50/s3*100:5.1f}%  100%={p100/s3*100:5.1f}%")
        print(f"  Add-to-Cart: {int(atc)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
