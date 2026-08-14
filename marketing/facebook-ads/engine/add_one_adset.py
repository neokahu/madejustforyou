#!/usr/bin/env python3
"""Add ONE more ad set to the existing MJ4U-111 campaign for the video A/B test.
Same copy/targeting/budget/optimization as the other test ad sets — only the video differs.
All PAUSED. Usage: python3 add_one_adset.py "<abs video path>" "<label>"
"""
import json, sys
from pathlib import Path
from upload_draft import Uploader, load_env, ENV_PATH, REPO, REPORTS

CAMPAIGN_ID = "120251785507510556"
CONTENT = REPO / "products/MJ4U-111-grandmas-garden-candle-warmer/ads/reveal/ad-content.json"

def main() -> int:
    vpath = Path(sys.argv[1]); label = sys.argv[2]
    assert vpath.exists(), f"missing video: {vpath}"
    c = json.loads(CONTENT.read_text()); aset = c["adset"]; copy = c["shared_copy"]
    message = "\n".join(copy["primary_text"]); headline = copy["headline"]

    env = load_env(ENV_PATH)
    up = Uploader(env["META_SYSTEM_USER_TOKEN"], env["META_AD_ACCOUNT_ID"], env.get("META_API_VERSION", "v26.0"))
    targeting = {"geo_locations": {"countries": aset["countries"]}, "age_min": aset["age_min"], "age_max": aset["age_max"]}

    print(f"=== {label} ===\n  creating ad set (identical settings, PAUSED)…")
    asid = up._req(f"{up.a}/adsets", {
        "name": f"MJ4U-111 | video-test | {label}", "campaign_id": CAMPAIGN_ID, "status": "PAUSED",
        "daily_budget": int(aset["daily_budget_usd"] * 100), "billing_event": "IMPRESSIONS",
        "optimization_goal": aset["optimization_goal"], "bid_strategy": aset["bid_strategy"],
        "promoted_object": json.dumps({"pixel_id": aset["pixel_id"], "custom_event_type": aset["custom_event_type"]}),
        "targeting": json.dumps(targeting)})["id"]
    print(f"  ad set {asid}; uploading video…")
    vid = up.upload_video(str(vpath), f"MJ4U-111 {vpath.stem}")
    thumb = up.preferred_thumb(vid)
    oss = {"page_id": c["page_id"], "video_data": {"video_id": vid, "image_url": thumb, "title": headline,
           "message": message, "link_description": c["description"],
           "call_to_action": {"type": c["cta"], "value": {"link": c["product_url"]}}}}
    name = f"MJ4U-111_video-test_{label}"
    crid = up._req(f"{up.a}/adcreatives", {"name": name, "object_story_spec": json.dumps(oss)})["id"]
    adid = up._req(f"{up.a}/ads", {"name": name, "adset_id": asid, "creative": json.dumps({"creative_id": crid}), "status": "PAUSED"})["id"]
    rec = {"label": label, "adset_id": asid, "video_id": vid, "creative_id": crid, "ad_id": adid}
    REPORTS.mkdir(exist_ok=True)
    (REPORTS / f"mj4u-111-adset-{label}.json").write_text(json.dumps({"campaign_id": CAMPAIGN_ID, **rec}, indent=2))
    print(f"  ✓ {name}  adset={asid} ad={adid}\nDONE (PAUSED).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
