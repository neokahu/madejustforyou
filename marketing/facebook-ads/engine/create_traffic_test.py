#!/usr/bin/env python3
"""PHASE 1 (cold-start ladder): a TRAFFIC-objective campaign to A/B 3 videos on
cost-per-Landing-Page-View — cheap delivery on a new pixel, seasons the pixel,
reads the creative test. 3 SEPARATE ad sets (one video each -> no starvation).
Reuses already-uploaded video assets. All PAUSED.
See research/reference/new-pixel-coldstart-methodology.md
"""
import json
from pathlib import Path
from upload_draft import Uploader, load_env, ENV_PATH, REPO, REPORTS

CONTENT = REPO / "products/MJ4U-111-grandmas-garden-candle-warmer/ads/reveal/ad-content.json"
DAILY = 25

def video_ids():
    ab = json.loads((REPORTS / "mj4u-111-video-ab-ids.json").read_text())["adsets"]
    m = {a["label"]: a["video_id"] for a in ab}
    m1080 = json.loads((REPORTS / "mj4u-111-adset-auto-meadowlark-1080p.json").read_text())
    return [
        ("chatcut-reveal",        m["chatcut-reveal"]),
        ("auto-meadowlark-720p",  m["auto-meadowlark"]),
        ("auto-meadowlark-1080p", m1080["video_id"]),
    ]

def adset(up, cid, aset, pixel, label):
    params = {
        "name": f"MJ4U-111 | traffic-LPV | {label}", "campaign_id": cid, "status": "PAUSED",
        "daily_budget": DAILY * 100, "billing_event": "IMPRESSIONS",
        "optimization_goal": "LANDING_PAGE_VIEWS", "bid_strategy": aset["bid_strategy"],
        "targeting": json.dumps({"geo_locations": {"countries": aset["countries"]},
                                 "age_min": aset["age_min"], "age_max": aset["age_max"]}),
        "promoted_object": json.dumps({"pixel_id": pixel}),
    }
    try:
        return up._req(f"{up.a}/adsets", params)["id"]
    except SystemExit:
        params.pop("promoted_object")           # LPV may not need it under Traffic
        return up._req(f"{up.a}/adsets", params)["id"]

def main() -> int:
    c = json.loads(CONTENT.read_text()); aset = c["adset"]; copy = c["shared_copy"]
    message = "\n".join(copy["primary_text"]); headline = copy["headline"]
    env = load_env(ENV_PATH)
    up = Uploader(env["META_SYSTEM_USER_TOKEN"], env["META_AD_ACCOUNT_ID"], env.get("META_API_VERSION", "v26.0"))

    print("creating TRAFFIC campaign…")
    cid = up._req(f"{up.a}/campaigns", {
        "name": "MJ4U-111 | Grandma's Garden | traffic-LPV video test (phase-1 coldstart)",
        "objective": "OUTCOME_TRAFFIC", "status": "PAUSED",
        "special_ad_categories": "[]", "is_adset_budget_sharing_enabled": "false"})["id"]
    print(f"  campaign {cid}")

    made = []
    for label, vid in video_ids():
        print(f"  {label}: ad set…")
        asid = adset(up, cid, aset, aset["pixel_id"], label)
        thumb = up.preferred_thumb(vid)
        oss = {"page_id": c["page_id"], "video_data": {
            "video_id": vid, "image_url": thumb, "title": headline, "message": message,
            "link_description": c["description"],
            "call_to_action": {"type": c["cta"], "value": {"link": c["product_url"]}}}}
        name = f"MJ4U-111_traffic_{label}"
        crid = up._req(f"{up.a}/adcreatives", {"name": name, "object_story_spec": json.dumps(oss)})["id"]
        adid = up._req(f"{up.a}/ads", {"name": name, "adset_id": asid,
                                       "creative": json.dumps({"creative_id": crid}), "status": "PAUSED"})["id"]
        made.append({"label": label, "adset_id": asid, "ad_id": adid, "video_id": vid})
        print(f"    ✓ adset={asid} ad={adid}")

    REPORTS.mkdir(exist_ok=True)
    (REPORTS / "mj4u-111-traffic-test-ids.json").write_text(
        json.dumps({"campaign_id": cid, "objective": "OUTCOME_TRAFFIC", "adsets": made}, indent=2))
    acct = up.a.replace("act_", "")
    print(f"\nDONE (all PAUSED). Traffic campaign {cid}")
    print(f"Review: https://adsmanager.facebook.com/adsmanager/manage/ads?act={acct}&selected_campaign_ids={cid}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
