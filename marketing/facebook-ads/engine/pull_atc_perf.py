#!/usr/bin/env python3
"""Read-only: pull ATC-campaign performance (spend/CPM/CTR + add-to-cart + cost/ATC)."""
import sys, json
from upload_draft import Uploader, load_env, ENV_PATH

CAMPAIGN = sys.argv[1] if len(sys.argv) > 1 else "120251963479950556"  # phase-2 ATC
ATC_TYPES = ("offsite_conversion.fb_pixel_add_to_cart", "onsite_web_add_to_cart", "add_to_cart")
IC_TYPES  = ("offsite_conversion.fb_pixel_initiate_checkout", "onsite_web_initiate_checkout", "initiate_checkout")
PUR_TYPES = ("offsite_conversion.fb_pixel_purchase", "onsite_web_purchase", "purchase")

def pick(lst, types):
    if not isinstance(lst, list): return 0.0
    for t in types:
        for a in lst:
            if a.get("action_type") == t:
                try: return float(a.get("value", 0))
                except Exception: return 0.0
    return 0.0

def main():
    env = load_env(ENV_PATH)
    up = Uploader(env["META_SYSTEM_USER_TOKEN"], env["META_AD_ACCOUNT_ID"], env.get("META_API_VERSION", "v26.0"))
    fields = ("ad_name,impressions,reach,frequency,spend,cpm,cpc,ctr,"
              "inline_link_clicks,inline_link_click_ctr,actions,cost_per_action_type")
    r = up.get(f"{CAMPAIGN}/insights", {"fields": fields, "level": "ad", "date_preset": "maximum"})
    rows = r.get("data", [])
    if not rows:
        print("no delivery data yet."); return 0
    for d in rows:
        imp = float(d.get("impressions", 0)) or 0
        spend = float(d.get("spend", 0))
        lc = float(d.get("inline_link_clicks", 0))
        atc = pick(d.get("actions"), ATC_TYPES)
        ic  = pick(d.get("actions"), IC_TYPES)
        pur = pick(d.get("actions"), PUR_TYPES)
        cpatc = pick(d.get("cost_per_action_type"), ATC_TYPES)
        print(f"\n=== {d.get('ad_name')} ===")
        print(f"  spend ${spend:.2f} | impr {int(imp)} | reach {int(float(d.get('reach',0)))} "
              f"| freq {float(d.get('frequency',0)):.2f} | CPM ${float(d.get('cpm',0)):.2f}")
        print(f"  link-clicks {int(lc)} | link-CTR {float(d.get('inline_link_click_ctr',0)):.2f}% "
              f"| CPC ${float(d.get('cpc',0)):.2f}")
        print(f"  ADD-TO-CART {int(atc)}  | cost/ATC ${cpatc:.2f}  | ATC-rate {(atc/lc*100 if lc else 0):.1f}% of clicks")
        print(f"  initiate-checkout {int(ic)} | purchases {int(pur)}")
    # campaign totals
    tot = up.get(f"{CAMPAIGN}/insights", {"fields": "spend,impressions,inline_link_clicks,actions", "date_preset": "maximum"}).get("data", [])
    if tot:
        t = tot[0]
        print(f"\n--- CAMPAIGN TOTAL ---  spend ${float(t.get('spend',0)):.2f} | impr {int(float(t.get('impressions',0)))} "
              f"| clicks {int(float(t.get('inline_link_clicks',0)))} | ATC {int(pick(t.get('actions'), ATC_TYPES))} "
              f"| IC {int(pick(t.get('actions'), IC_TYPES))} | purch {int(pick(t.get('actions'), PUR_TYPES))}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
