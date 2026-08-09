#!/usr/bin/env python3
"""Standardized ad-draft uploader.

Reads a product's ad-content.json (see products/<id>/ads/ad-content.json),
ENFORCES the copy-format standard (line-break/scannable, never a wall of text),
and builds the whole draft on Meta — campaign → ad set → video → creatives →
ads — all PAUSED. This replaces hand-rolled upload scripts so every product is
uploaded the same way with the same formatting guarantees.

Usage:
  python3 upload_draft.py <path/to/ad-content.json> --validate-only   # lint + preview, no writes
  python3 upload_draft.py <path/to/ad-content.json>                    # build the PAUSED draft
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]                 # engine -> facebook-ads -> marketing -> repo
ENV_PATH = HERE.parent / ".env"
REPORTS = HERE.parent / "reports"

MAX_LINE = 160  # a single primary-text line longer than this should be split

# Doc-aligned test structure (Facebook-Testing-Scaling-Research.md Part 5).
STAGE_RULES = {
    "validate": {"budget": (20, 30), "ads": (2, 3), "note": "Part 5 Stage 1 — validate product/offer"},
    "iterate":  {"budget": (30, 50), "ads": (3, 5), "note": "Part 5 Stage 2 — iterate creative"},
}


def validate_structure(content: dict) -> tuple[str, str, list[str]]:
    """Enforce doc-aligned campaign STRUCTURE (Parts 3/4/5/8). Returns (stage, test_variable, warnings)."""
    warns = []
    stage = content.get("stage", "validate")
    if stage not in STAGE_RULES:
        sys.exit(f"STRUCTURE ERROR: unknown stage '{stage}' — use 'validate' or 'iterate'.")
    rules = STAGE_RULES[stage]
    aset = content["adset"]

    # Part 4: test on ABO (budget on the ad set), never CBO.
    camp = content.get("campaign", {})
    if camp.get("daily_budget_usd") or camp.get("lifetime_budget_usd"):
        sys.exit("STRUCTURE ERROR: test campaigns must be ABO (budget on the ad set), not CBO (Part 4). Remove campaign budget.")
    # Part 4: lowest-cost (auto) bid for testing.
    if aset.get("bid_strategy") != "LOWEST_COST_WITHOUT_CAP":
        warns.append(f"bid_strategy is '{aset.get('bid_strategy')}' — Part 4 says TEST on lowest-cost (auto); cost/bid cap is for scaling.")
    # Part 5: budget range for the stage.
    b, (blo, bhi) = aset["daily_budget_usd"], rules["budget"]
    if not (blo <= b <= bhi):
        warns.append(f"ad-set budget ${b}/day is outside the {stage} range ${blo}-{bhi}/day (Part 5).")
    # Part 5: creative count for the stage.
    n, (nlo, nhi) = len(content["ads"]), rules["ads"]
    if not (nlo <= n <= nhi):
        warns.append(f"{n} creatives — {stage} stage wants {nlo}-{nhi} (Part 5).")
    # Part 5: broad audience for a clean test.
    if aset.get("interests") or aset.get("custom_audiences") or aset.get("lookalikes"):
        warns.append("targeting has interests/LAL/custom audiences — Part 5 tests on BROAD audience for a clean read.")
    # Part 3 mistake #2 / Part 8: isolate ONE variable, declared.
    tv = content.get("test_variable")
    if not tv:
        warns.append("no test_variable declared — Part 3 mistake #2: isolate ONE variable per test (Part 8: angle is a good one).")
    return stage, tv or "?", warns


def load_env(p):
    d = {}
    for line in Path(p).read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line and "-" not in line.split("=")[0]:
            k, v = line.split("=", 1)
            d[k.strip()] = v.strip()
    return d


# ---- format standard --------------------------------------------------------
def validate_and_render(content: dict) -> tuple[list[dict], list[str]]:
    """Enforce the copy-format standard. Returns (ads_with_rendered_text, warnings)."""
    warnings, rendered = [], []
    for ad in content["ads"]:
        label = ad.get("label", "?")
        pt = ad.get("primary_text")
        if not isinstance(pt, list):
            sys.exit(f"FORMAT ERROR [{label}]: primary_text must be an ARRAY OF LINES, not a string. "
                     f"This is what keeps copy scannable.")
        if len([l for l in pt if l.strip()]) < 2:
            sys.exit(f"FORMAT ERROR [{label}]: primary_text needs at least 2 non-empty lines (structure).")
        for l in pt:
            if len(l) > MAX_LINE:
                warnings.append(f"[{label}] line >{MAX_LINE} chars, consider splitting: “{l[:60]}…”")
        h = ad.get("headline", "")
        if not h:
            sys.exit(f"FORMAT ERROR [{label}]: missing headline.")
        if len(h) > 255:
            warnings.append(f"[{label}] headline is long ({len(h)} chars).")
        rendered.append({**ad, "message": "\n".join(pt)})
    return rendered, warnings


# ---- Meta write client (upload scope) --------------------------------------
class Uploader:
    def __init__(self, token, account, version):
        self.t, self.a, self.v = token, account, version
        self.g = f"https://graph.facebook.com/{version}"

    def _req(self, node, params, method="POST", files=None):
        url = f"{self.g}/{node}"
        if files:  # multipart (video upload) — minimal encoder
            import mimetypes, uuid
            boundary = uuid.uuid4().hex
            body = b""
            for k, val in {**params, "access_token": self.t}.items():
                body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{val}\r\n").encode()
            for k, fp in files.items():
                fp = Path(fp); ctype = mimetypes.guess_type(str(fp))[0] or "application/octet-stream"
                body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"; filename=\"{fp.name}\"\r\n"
                         f"Content-Type: {ctype}\r\n\r\n").encode() + fp.read_bytes() + b"\r\n"
            body += f"--{boundary}--\r\n".encode()
            req = urllib.request.Request(url, data=body, method="POST",
                                         headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
        else:
            data = urllib.parse.urlencode({**params, "access_token": self.t}).encode()
            req = urllib.request.Request(url, data=data, method=method)
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            sys.exit(f"Meta API error on {node}: {e.read().decode()}")

    def get(self, node, params):
        q = urllib.parse.urlencode({**params, "access_token": self.t})
        with urllib.request.urlopen(f"{self.g}/{node}?{q}", timeout=90) as r:
            return json.loads(r.read().decode())

    def upload_video(self, path, name):
        vid = self._req(f"{self.a}/advideos", {"name": name}, files={"source": path})["id"]
        for _ in range(24):  # poll up to ~2 min
            st = self.get(vid, {"fields": "status"}).get("status", {}).get("video_status")
            if st == "ready":
                return vid
            time.sleep(5)
        sys.exit(f"video {vid} not ready after polling")

    def preferred_thumb(self, vid):
        t = self.get(f"{vid}/thumbnails", {"fields": "uri,is_preferred"})["data"]
        return next((x["uri"] for x in t if x.get("is_preferred")), t[0]["uri"])


def main() -> int:
    ap = argparse.ArgumentParser(description="Standardized ad-draft uploader")
    ap.add_argument("content", help="path to ad-content.json")
    ap.add_argument("--validate-only", action="store_true", help="lint + preview copy, write nothing")
    args = ap.parse_args()

    content = json.loads(Path(args.content).read_text())
    ads, warnings = validate_and_render(content)
    stage, tv, swarns = validate_structure(content)
    warnings = warnings + swarns

    aset = content["adset"]
    print(f"\n=== {content['product_id']} — STRUCTURE ({STAGE_RULES[stage]['note']}) ===")
    print(f"ABO · lowest-cost · 1 broad ad set ({'/'.join(aset['countries'])} {aset['age_min']}-{aset['age_max']}) · "
          f"{len(ads)} creatives · ${aset['daily_budget_usd']}/day · isolates '{tv}' (video/audience/LP held constant)")

    print(f"\n=== {content['product_id']} — copy preview (enforced format) ===")
    for ad in ads:
        print(f"\n--- {ad['label']} · headline: {ad['headline']}")
        print(ad["message"])
    if warnings:
        print("\n⚠️ warnings:")
        for w in warnings:
            print(f"  - {w}")
    print("\n✅ format OK" + (" (with warnings)" if warnings else ""))
    if args.validate_only:
        print("validate-only: no changes made.")
        return 0

    env = load_env(ENV_PATH)
    up = Uploader(env["META_SYSTEM_USER_TOKEN"], env["META_AD_ACCOUNT_ID"], env.get("META_API_VERSION", "v26.0"))
    pid = content["product_id"]
    cset, aset = content["campaign"], content["adset"]

    print("\ncreating campaign…")
    cid = up._req(f"{up.a}/campaigns", {
        "name": f"{pid} | {content['product_name']} | {content['campaign_suffix']}",
        "objective": cset["objective"], "status": "PAUSED",
        "special_ad_categories": "[]", "is_adset_budget_sharing_enabled": "false"})["id"]

    print("creating ad set…")
    targeting = {"geo_locations": {"countries": aset["countries"]},
                 "age_min": aset["age_min"], "age_max": aset["age_max"]}
    asid = up._req(f"{up.a}/adsets", {
        "name": f"{pid} | {'/'.join(aset['countries'])} Broad | Purchase",
        "campaign_id": cid, "status": "PAUSED",
        "daily_budget": int(aset["daily_budget_usd"] * 100),
        "billing_event": "IMPRESSIONS", "optimization_goal": aset["optimization_goal"],
        "bid_strategy": aset["bid_strategy"],
        "promoted_object": json.dumps({"pixel_id": aset["pixel_id"], "custom_event_type": aset["custom_event_type"]}),
        "targeting": json.dumps(targeting)})["id"]

    print("uploading video…")
    vid = up.upload_video(str(REPO / content["video"]), f"{pid} {Path(content['video']).stem}")
    thumb = up.preferred_thumb(vid)

    print("creating creatives + ads…")
    made = []
    for ad in ads:
        name = f"{pid}_{ad['label']}_v1"
        oss = {"page_id": content["page_id"], "video_data": {
            "video_id": vid, "image_url": thumb, "title": ad["headline"],
            "message": ad["message"], "link_description": content["description"],
            "call_to_action": {"type": content["cta"], "value": {"link": content["product_url"]}}}}
        crid = up._req(f"{up.a}/adcreatives", {"name": name, "object_story_spec": json.dumps(oss)})["id"]
        adid = up._req(f"{up.a}/ads", {"name": name, "adset_id": asid,
                                       "creative": json.dumps({"creative_id": crid}), "status": "PAUSED"})["id"]
        made.append({"label": ad["label"], "creative_id": crid, "ad_id": adid})
        print(f"  ✓ {name}  ad={adid}")

    REPORTS.mkdir(exist_ok=True)
    out = REPORTS / f"{pid}-draft-ids.json"
    out.write_text(json.dumps({"campaign_id": cid, "adset_id": asid, "video_id": vid, "ads": made}, indent=2))
    acct = up.a.replace("act_", "")
    print(f"\nDONE (all PAUSED). IDs → {out}")
    print(f"Review: https://adsmanager.facebook.com/adsmanager/manage/ads?act={acct}&selected_campaign_ids={cid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
