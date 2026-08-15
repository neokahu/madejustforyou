#!/usr/bin/env python3
"""PHASE 2 (cold-start ladder): relaunch the WINNING creative only, one rung up.

Phase 1 (LPV traffic test) did its two jobs: fixed delivery (CPM $250 -> ~$15)
and crowned the creative winner (chatcut-reveal, hook 51% vs 26-30%). LPV traffic
is view-only and can't judge purchase CVR, so we climb to a real CONVERSION event.

We optimize ADD_TO_CART (not ViewContent, not Purchase):
- NOT Purchase     -> cold pixel has no purchase history = the $250-CPM trap.
- NOT ViewContent  -> its intent is barely above LPV; a weak, redundant rung.
- ADD_TO_CART      -> the real buyer-intent jump. It's a COMMON event across all
                      of Meta, so its global model predicts ATC-likely users fine
                      even on a cold pixel (unlike rare Purchase). User confirmed
                      the ATC flow fires, so real ATC signal will accumulate and
                      season the pixel toward buyers. Climb ATC -> Purchase once
                      purchase volume approaches ~50/ad-set/week.

Winner creative only (chatcut-reveal); the two Meadowlark cuts are dropped.
REUSES the exact existing creative (creative_id 1018838394117593) so it's the
SAME ad/post — any accumulated social proof carries over, no rebuild. All PAUSED.
See research/reference/new-pixel-coldstart-methodology.md
"""
import json
from upload_draft import Uploader, load_env, ENV_PATH, REPO, REPORTS

CONTENT = REPO / "products/MJ4U-111-grandmas-garden-candle-warmer/ads/reveal/ad-content.json"
DAILY = 50                      # concentrate spend on ONE ad set so ATC can clear ~50 events/wk.
EVENT = "ADD_TO_CART"           # the rung we optimize for
WINNER_LABEL = "chatcut-reveal"


def winner_creative_id() -> str:
    """Reuse the exact chatcut-reveal creative already built during the A/B test."""
    ab = json.loads((REPORTS / "mj4u-111-video-ab-ids.json").read_text())["adsets"]
    for a in ab:
        if a["label"] == WINNER_LABEL:
            return a["creative_id"]
    raise SystemExit(f"no creative_id for {WINNER_LABEL} in mj4u-111-video-ab-ids.json")


def main() -> int:
    c = json.loads(CONTENT.read_text())
    aset = c["adset"]

    env = load_env(ENV_PATH)
    up = Uploader(env["META_SYSTEM_USER_TOKEN"], env["META_AD_ACCOUNT_ID"],
                  env.get("META_API_VERSION", "v26.0"))

    print(f"creating SALES campaign optimizing {EVENT} (winner only, reusing existing ad)…")
    cid = up._req(f"{up.a}/campaigns", {
        "name": "MJ4U-111 | Grandma's Garden | phase-2 AddToCart (winner: chatcut-reveal)",
        "objective": "OUTCOME_SALES", "status": "PAUSED",
        "special_ad_categories": "[]", "is_adset_budget_sharing_enabled": "false"})["id"]
    print(f"  campaign {cid}")

    targeting = {"geo_locations": {"countries": aset["countries"]},
                 "age_min": aset["age_min"], "age_max": aset["age_max"]}
    asid = up._req(f"{up.a}/adsets", {
        "name": f"MJ4U-111 | sales-ATC | {WINNER_LABEL}", "campaign_id": cid, "status": "PAUSED",
        "daily_budget": DAILY * 100, "billing_event": "IMPRESSIONS",
        "optimization_goal": aset["optimization_goal"],          # OFFSITE_CONVERSIONS
        "bid_strategy": aset["bid_strategy"],                     # LOWEST_COST_WITHOUT_CAP
        "promoted_object": json.dumps({"pixel_id": aset["pixel_id"], "custom_event_type": EVENT}),
        "targeting": json.dumps(targeting)})["id"]
    print(f"  ad set {asid}")

    crid = winner_creative_id()
    name = f"MJ4U-111_sales-ATC_{WINNER_LABEL}"
    adid = up._req(f"{up.a}/ads", {"name": name, "adset_id": asid,
                                   "creative": json.dumps({"creative_id": crid}), "status": "PAUSED"})["id"]
    print(f"  ✓ {name}  adset={asid} ad={adid} (reused creative {crid})")

    REPORTS.mkdir(exist_ok=True)
    (REPORTS / "mj4u-111-phase2-addtocart-ids.json").write_text(json.dumps({
        "campaign_id": cid, "objective": "OUTCOME_SALES", "optimize": EVENT, "daily_usd": DAILY,
        "adset_id": asid, "ad_id": adid, "creative_id": crid}, indent=2))
    acct = up.a.replace("act_", "")
    print(f"\nDONE (all PAUSED). Phase-2 campaign {cid}")
    print(f"Review: https://adsmanager.facebook.com/adsmanager/manage/ads?act={acct}&selected_campaign_ids={cid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
