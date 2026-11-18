#!/usr/bin/env python3
"""Export the ads database to marketing/facebook-ads/dashboard/data.json for the dashboard page.

  python3 export_dashboard.py

The page cannot reach Supabase from the artifact sandbox, so it reads this snapshot; Claude republishes it after each sync.
"""
import datetime as dt, json
from pathlib import Path
from upload_draft import load_env, ENV_PATH
from db_sync import DB

OUT = Path(__file__).resolve().parents[1] / "dashboard/data.json"


def main():
    env = load_env(ENV_PATH)
    db = DB(env["SUPABASE_URL"], env["SUPABASE_SERVICE_ROLE_KEY"])
    ads = db.select("ad_performance", "select=*")
    daily = db.select("ad_metrics_daily", "select=ad_key,date,impressions,spend,video_3s,thruplays,link_clicks,add_to_cart,purchases,purchase_value&order=date")
    tests = db.select("tests", "select=test_id,product_id,name,status,primary_metric,started_on,ended_on")
    products = db.select("products", "select=product_id,name,break_even_cpa,break_even_roas&product_id=in.("
                         + ",".join(sorted({a["product_id"] for a in ads})) + ")")
    data = {"generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="minutes"),
            "gates": {"hook_kill": 0.18, "hook_red": 0.21, "hook_advance": 0.28},
            "ads": ads, "daily": daily, "tests": tests, "products": products}
    OUT.write_text(json.dumps(data, indent=1, default=str))
    print(f"wrote {OUT} ({len(ads)} ads, {len(daily)} ad-days)")


if __name__ == "__main__":
    main()
