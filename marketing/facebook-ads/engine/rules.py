"""Decision engine — encodes the kill / keep / scale methodology.

Source of truth: sop-docs Facebook-Testing-Scaling-Research.md.
- Leading indicators kill the *clearly dead* early (hook + CTR + no ATC).
- Lagging indicators (CPA/ROAS vs break-even) confirm winners.
- Every threshold is relative to the product's own break-even (economics.py).

READ-ONLY: this module only computes a verdict + reasons. It never acts.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from economics import Economics

PRODUCT_CODE_RE = re.compile(r"\bMJ4U-\d{3}\b")

# Meta action_type aliases we treat as add-to-cart / purchase.
ATC_TYPES = {
    "offsite_conversion.fb_pixel_add_to_cart", "onsite_web_add_to_cart",
    "onsite_web_app_add_to_cart", "omni_add_to_cart", "add_to_cart",
}
PURCHASE_TYPES = {
    "offsite_conversion.fb_pixel_purchase", "onsite_web_purchase",
    "onsite_web_app_purchase", "omni_purchase", "purchase",
}

# Verdicts
KILL = "KILL"
KEEP = "KEEP"
SCALE = "SCALE"
WATCH = "WATCH"
INSUFFICIENT = "INSUFFICIENT_DATA"
UNMAPPED = "UNMAPPED"


def load_thresholds(path: str | Path) -> dict:
    return json.loads(Path(path).read_text())


def product_code(campaign_name: str | None) -> str | None:
    if not campaign_name:
        return None
    m = PRODUCT_CODE_RE.search(campaign_name)
    return m.group(0) if m else None


def _sum_actions(actions, wanted: set[str]) -> float:
    if not actions:
        return 0.0
    return sum(float(a.get("value", 0)) for a in actions if a.get("action_type") in wanted)


def _first_value(items) -> float:
    if not items:
        return 0.0
    try:
        return float(items[0].get("value", 0))
    except (TypeError, ValueError):
        return 0.0


@dataclass
class Metrics:
    campaign_name: str = ""
    adset_name: str = ""
    adset_id: str = ""
    ad_name: str = ""
    ad_id: str = ""
    effective_status: str = ""
    age_days: int | None = None
    impressions: float = 0.0
    spend: float = 0.0
    link_clicks: float = 0.0
    ctr_link: float | None = None      # fraction (0-1)
    cpc_link: float | None = None
    cpm: float | None = None
    frequency: float | None = None
    hook_rate: float | None = None     # 3s video views / impressions
    atc: float = 0.0
    purchases: float = 0.0
    revenue: float = 0.0
    roas: float | None = None
    cost_per_atc: float | None = None
    cpa: float | None = None
    # per-day series (oldest→newest) for sustained-profit + fatigue-trend checks
    daily_roas: list = field(default_factory=list)
    daily_cpm: list = field(default_factory=list)
    daily_ctr: list = field(default_factory=list)


def daily_series(daily_rows: list[dict]) -> tuple[list, list, list]:
    """Per-day raw rows for ONE ad (any order) -> (roas[], cpm[], ctr[]) oldest→newest."""
    rows = sorted(daily_rows, key=lambda r: r.get("date_start", ""))
    roas, cpm, ctr = [], [], []
    for r in rows:
        spend = float(r.get("spend", 0) or 0)
        rev = _sum_actions(r.get("action_values"), PURCHASE_TYPES)
        roas.append(rev / spend if spend else 0.0)
        cpm.append(float(r["cpm"]) if r.get("cpm") not in (None, "") else None)
        c = r.get("inline_link_click_ctr")
        ctr.append(float(c) / 100.0 if c not in (None, "") else None)
    return roas, cpm, ctr


def normalize_row(row: dict) -> Metrics:
    """Raw Meta insights row (or sample row) -> flat Metrics."""
    _d = row.get("_daily") or {}
    impressions = float(row.get("impressions", 0) or 0)
    spend = float(row.get("spend", 0) or 0)
    link_clicks = float(row.get("inline_link_clicks", 0) or 0)
    # hook-rate numerator: 3-sec views if present (sample), else video plays (v26 live)
    video_3s = _first_value(row.get("video_3_sec_watched_actions") or row.get("video_play_actions"))
    atc = _sum_actions(row.get("actions"), ATC_TYPES)
    purchases = _sum_actions(row.get("actions"), PURCHASE_TYPES)
    revenue = _sum_actions(row.get("action_values"), PURCHASE_TYPES)

    # Meta gives ctr/inline_link_click_ctr as PERCENT strings -> convert to fraction.
    def _pct(v):
        return float(v) / 100.0 if v not in (None, "") else None

    return Metrics(
        campaign_name=row.get("campaign_name", ""),
        adset_name=row.get("adset_name", ""),
        adset_id=str(row.get("adset_id", "")),
        ad_name=row.get("ad_name", ""),
        ad_id=str(row.get("ad_id", "")),
        effective_status=row.get("effective_status", ""),
        age_days=row.get("_age_days"),
        impressions=impressions,
        spend=spend,
        link_clicks=link_clicks,
        ctr_link=_pct(row.get("inline_link_click_ctr")),
        cpc_link=float(row["cpc"]) if row.get("cpc") not in (None, "") else None,
        cpm=float(row["cpm"]) if row.get("cpm") not in (None, "") else None,
        frequency=float(row["frequency"]) if row.get("frequency") not in (None, "") else None,
        hook_rate=(video_3s / impressions) if impressions and video_3s else None,
        atc=atc,
        purchases=purchases,
        revenue=revenue,
        roas=(revenue / spend) if spend else None,
        cost_per_atc=(spend / atc) if atc else None,
        cpa=(spend / purchases) if purchases else None,
        daily_roas=_d.get("roas", []),
        daily_cpm=_d.get("cpm", []),
        daily_ctr=_d.get("ctr", []),
    )


@dataclass
class Decision:
    verdict: str
    headline: str
    reasons: list[str] = field(default_factory=list)
    leading: list[str] = field(default_factory=list)   # human-readable leading-indicator read
    flags: list[str] = field(default_factory=list)


def _leading_readout(m: Metrics, thr: dict, be_cpa: float) -> list[str]:
    L = thr["leading"]
    out = []
    if m.hook_rate is not None:
        tag = "weak" if m.hook_rate < L["hook_rate_kill_below"] else ("healthy" if m.hook_rate >= L["hook_rate_healthy_at"] else "ok")
        out.append(f"hook {m.hook_rate*100:.0f}% ({tag})")
    if m.ctr_link is not None:
        tag = "weak" if m.ctr_link < L["ctr_link_kill_below"] else ("healthy" if m.ctr_link >= L["ctr_link_healthy_at"] else "ok")
        out.append(f"CTR-link {m.ctr_link*100:.2f}% ({tag})")
    if m.cpc_link is not None:
        tag = "high" if m.cpc_link > L["cpc_link_high_above"] else "ok"
        out.append(f"CPC ${m.cpc_link:.2f} ({tag})")
    if m.cost_per_atc is not None:
        tag = "healthy" if m.cost_per_atc < be_cpa * L["cost_per_atc_healthy_frac_of_be_cpa"] else ("ok" if m.cost_per_atc < be_cpa else "high")
        out.append(f"cost/ATC ${m.cost_per_atc:.2f} ({tag})")
    elif m.atc == 0 and m.spend > 0:
        out.append("cost/ATC n/a (0 ATC)")
    return out


def decide(m: Metrics, econ: Economics | None, thr: dict) -> Decision:
    """Apply the kill/keep/scale methodology to one ad."""
    if econ is None:
        code = product_code(m.campaign_name)
        why = (f"campaign has code {code} but no economics configured in products.json"
               if code else "no MJ4U-NNN product code in campaign name — cannot compute break-even")
        return Decision(UNMAPPED, "Unmapped — no break-even", [why])

    be_cpa = econ.break_even_cpa
    be_roas = econ.break_even_roas
    K, KS, J = thr["kill"], thr["keep_scale"], thr["judgement"]
    leading = _leading_readout(m, thr, be_cpa)
    flags = []

    # --- daily-series signals: sustained profit (for scale) + fatigue trend ---
    sustained_days = 0  # trailing consecutive days with daily ROAS >= break-even
    for x in reversed(m.daily_roas):
        if x >= be_roas:
            sustained_days += 1
        else:
            break

    def _trend(arr):
        vals = [x for x in arr if x is not None]
        if len(vals) < 4:
            return None
        h = len(vals) // 2
        return sum(vals[h:]) / len(vals[h:]) - sum(vals[:h]) / len(vals[:h])

    cpm_rising = (_trend(m.daily_cpm) or 0) > 0 and _trend(m.daily_cpm) is not None
    ctr_falling = (_trend(m.daily_ctr) or 0) < 0 and _trend(m.daily_ctr) is not None

    # Fatigue overlay (advisory) — methodology Part 7: frequency high AND CPM rising AND CTR falling
    if m.frequency is not None and m.frequency > thr["fatigue"]["frequency_high_above"]:
        if cpm_rising and ctr_falling:
            flags.append(f"creative fatigue: freq {m.frequency:.1f} + CPM rising + CTR falling → refresh creative")
        else:
            flags.append(f"frequency {m.frequency:.1f} high — watch for fatigue (CPM/CTR not yet trending down)")

    # 0) EARLY fast-kill — clearly-dead creative, before wasting a full CPA (methodology Part 2).
    #    Fires only on the FULL combination so it can't false-kill: enough impressions to read,
    #    bad hook, bad link-CTR, and zero add-to-cart. CPM/CPC are context, not triggers.
    EK = thr.get("early_kill")
    if (EK and m.atc == 0 and m.impressions >= EK["min_impressions"]
            and m.hook_rate is not None and m.hook_rate < EK["hook_rate_below"]
            and m.ctr_link is not None and m.ctr_link < EK["ctr_link_below"]):
        return Decision(
            KILL,
            f"Clearly dead early — hook {m.hook_rate*100:.0f}% + link-CTR {m.ctr_link*100:.2f}% + 0 ATC over {m.impressions:,.0f} impr",
            [f"all leading signals failing with zero intent — kill now, don't burn a full ${be_cpa:.0f} CPA"],
            leading, flags,
        )

    # 1) Insufficient spend to judge anything yet
    if m.spend < be_cpa * J["insufficient_spend_frac_of_be_cpa"]:
        return Decision(
            INSUFFICIENT,
            f"Too little spend to judge (${m.spend:.0f} < 1× break-even CPA ${be_cpa:.0f})",
            [f"accumulate to ≥ ${be_cpa:.0f} spend before deciding"],
            leading, flags,
        )

    # 2) Hard KILL — clearly dead creative: no add-to-cart after 1× break-even CPA
    if m.atc == 0 and m.spend >= be_cpa * K["no_atc_spend_mult_of_be_cpa"]:
        return Decision(
            KILL,
            f"0 add-to-cart after ${m.spend:.0f} (≥ 1× break-even CPA ${be_cpa:.0f})",
            ["creative isn't converting attention → intent; kill and move on"],
            leading, flags,
        )

    # 3) KILL — ATC but no purchase by ~2.5× CPA (offer/checkout/price weak)
    if m.purchases == 0 and m.atc > 0 and m.spend >= be_cpa * K["atc_no_purchase_spend_mult_of_be_cpa"]:
        return Decision(
            KILL,
            f"{m.atc:.0f} ATC but 0 purchases by ${m.spend:.0f} (≥ {K['atc_no_purchase_spend_mult_of_be_cpa']}× CPA)",
            ["intent but no conversion → offer/price/checkout problem, or just weak"],
            leading, flags,
        )

    # 4) Has purchases — judge on ROAS vs break-even
    if m.purchases >= KS["keep_min_purchases"] and m.roas is not None:
        ratio = m.roas / be_roas if be_roas else 0
        base = [f"ROAS {m.roas:.2f} vs break-even {be_roas:.2f} ({ratio:.2f}×) · CPA ${m.cpa:.0f} vs ${be_cpa:.0f} · {int(m.purchases)} purchases"]
        if m.roas >= be_roas * KS["scale_roas_mult_of_be_roas"]:
            need = KS["scale_min_days"]
            # Part 6: scale only on sustained profit — N consecutive profitable days, not one lucky day.
            if (m.age_days or 0) >= need and sustained_days >= need:
                return Decision(SCALE, f"Winner — ROAS {ratio:.2f}× break-even, profitable {sustained_days} days running",
                                base + ["scale +20%/2–3d (vertical) or duplicate to new audience (horizontal); watch CPA creep"], leading, flags)
            why = (f"only {m.age_days}d old" if (m.age_days or 0) < need
                   else f"only {sustained_days} consecutive profitable day(s), need {need} — guards against a one-day fluke")
            return Decision(KEEP, f"Strong ROAS ({ratio:.2f}×) but {why}",
                            base + [f"hold until ≥{need} consecutive profitable days, then scale"], leading, flags)
        if m.roas >= be_roas:
            return Decision(KEEP, f"Profitable ({ratio:.2f}× break-even) — accumulate",
                            base + ["above break-even but below scale bar; keep gathering data"], leading, flags)
        # below break-even
        if m.spend >= be_cpa * K["underperform_roas_spend_mult_of_be_cpa"] and (m.age_days or 99) >= J["min_days_before_kill_on_lagging"]:
            return Decision(KILL, f"ROAS {m.roas:.2f} below break-even {be_roas:.2f} at ${m.spend:.0f}",
                            base + ["unprofitable past the spend/age bar → kill"], leading, flags)
        return Decision(WATCH, f"Below break-even ({ratio:.2f}×) but not yet at kill bar",
                        base + ["hasn't hit the spend/age threshold to kill; watch closely"], leading, flags)

    # 5) Spent past 1× CPA, has ATC, no purchase yet, but under the 2.5× kill bar
    return Decision(
        WATCH,
        f"{m.atc:.0f} ATC, 0 purchases at ${m.spend:.0f} — under the {K['atc_no_purchase_spend_mult_of_be_cpa']}× kill bar",
        [f"kill if still 0 purchases by ${be_cpa*K['atc_no_purchase_spend_mult_of_be_cpa']:.0f}"],
        leading, flags,
    )
