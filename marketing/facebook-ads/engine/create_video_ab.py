#!/usr/bin/env python3
"""Create 2 NEW ad sets in an EXISTING campaign to A/B two videos.

Everything held constant (copy, headline, CTA, targeting, budget, optimization,
pixel, landing page) EXCEPT the video — so the test isolates the creative.
Reuses upload_draft.Uploader so uploads/creatives/ads follow the same proven path.
All objects created PAUSED. Re-run safe? No — creates new objects each run.
"""
import json
from pathlib import Path
from upload_draft import Uploader, load_env, ENV_PATH, REPO, REPORTS

CAMPAIGN_ID = "120251785507510556"          # existing MJ4U-111 campaign
CONTENT = REPO / "products/MJ4U-111-grandmas-garden-candle-warmer/ads/reveal/ad-content.json"
OUT = REPO / "products/MJ4U-111-grandmas-garden-candle-warmer/ads/reveal/video/out"

VARIANTS = [
    {"label": "chatcut-reveal",  "video": OUT / "grandmas-garden-reveal-chatcut-1080p60.mp4"},
    {"label": "auto-meadowlark", "video": OUT / "Preliminary Gold Meadowlark 720p.mp4"},
]

def main() -> int:
    c = json.loads(CONTENT.read_text())
    aset = c["adset"]
    copy = c["shared_copy"]
    message = "\n".join(copy["primary_text"])
    headline = copy["headline"]

    env = load_env(ENV_PATH)
    up = Uploader(env["META_SYSTEM_USER_TOKEN"], env["META_AD_ACCOUNT_ID"],
                  env.get("META_API_VERSION", "v26.0"))

    targeting = {"geo_locations": {"countries": aset["countries"]},
                 "age_min": aset["age_min"], "age_max": aset["age_max"]}
    made = []
    for v in VARIANTS:
        label, vpath = v["label"], v["video"]
        assert vpath.exists(), f"missing video: {vpath}"
        print(f"\n=== {label} ===")
        print("  creating ad set (identical settings, PAUSED)…")
        asid = up._req(f"{up.a}/adsets", {
            "name": f"MJ4U-111 | video-test | {label}",
            "campaign_id": CAMPAIGN_ID, "status": "PAUSED",
            "daily_budget": int(aset["daily_budget_usd"] * 100),
            "billing_event": "IMPRESSIONS",
            "optimization_goal": aset["optimization_goal"],
            "bid_strategy": aset["bid_strategy"],
            "promoted_object": json.dumps({"pixel_id": aset["pixel_id"],
                                           "custom_event_type": aset["custom_event_type"]}),
            "targeting": json.dumps(targeting)})["id"]
        print(f"  ad set {asid}; uploading video…")
        vid = up.upload_video(str(vpath), f"MJ4U-111 {vpath.stem}")
        thumb = up.preferred_thumb(vid)
        print(f"  video {vid} ready; creating creative + ad…")
        oss = {"page_id": c["page_id"], "video_data": {
            "video_id": vid, "image_url": thumb, "title": headline,
            "message": message, "link_description": c["description"],
            "call_to_action": {"type": c["cta"], "value": {"link": c["product_url"]}}}}
        name = f"MJ4U-111_video-test_{label}"
        crid = up._req(f"{up.a}/adcreatives", {"name": name, "object_story_spec": json.dumps(oss)})["id"]
        adid = up._req(f"{up.a}/ads", {"name": name, "adset_id": asid,
                                       "creative": json.dumps({"creative_id": crid}),
                                       "status": "PAUSED"})["id"]
        made.append({"label": label, "adset_id": asid, "video_id": vid, "creative_id": crid, "ad_id": adid})
        print(f"  ✓ {name}  adset={asid} ad={adid}")

    REPORTS.mkdir(exist_ok=True)
    out = REPORTS / "mj4u-111-video-ab-ids.json"
    out.write_text(json.dumps({"campaign_id": CAMPAIGN_ID, "adsets": made}, indent=2))
    acct = up.a.replace("act_", "")
    print(f"\nDONE (all PAUSED). IDs -> {out}")
    print(f"Review: https://adsmanager.facebook.com/adsmanager/manage/ads?act={acct}&selected_campaign_ids={CAMPAIGN_ID}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
