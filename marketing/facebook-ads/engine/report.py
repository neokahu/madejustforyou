"""Render decisions into a Markdown call sheet."""
from __future__ import annotations

from economics import Economics
from rules import (Decision, Metrics, KILL, KEEP, SCALE, WATCH, INSUFFICIENT, UNMAPPED)

EMOJI = {SCALE: "🟢", KILL: "🔴", KEEP: "🟡", WATCH: "⚪", INSUFFICIENT: "⏳", UNMAPPED: "❓"}
ORDER = {SCALE: 0, KILL: 1, KEEP: 2, WATCH: 3, INSUFFICIENT: 4, UNMAPPED: 5}


def _metrics_line(m: Metrics) -> str:
    bits = [f"spend ${m.spend:.0f}", f"{m.impressions:,.0f} impr"]
    if m.link_clicks:
        bits.append(f"{m.link_clicks:,.0f} link clicks")
    bits.append(f"{m.atc:.0f} ATC")
    bits.append(f"{m.purchases:.0f} purch")
    if m.revenue:
        bits.append(f"${m.revenue:,.0f} rev")
    if m.age_days is not None:
        bits.append(f"{m.age_days}d old")
    if m.effective_status:
        bits.append(m.effective_status)
    return " · ".join(bits)


def render(items: list[tuple[Metrics, Decision, str | None, Economics | None]],
           account: dict, window_days: int, generated: str, sample: bool) -> str:
    counts: dict[str, int] = {}
    for _, d, _, _ in items:
        counts[d.verdict] = counts.get(d.verdict, 0) + 1

    L = [f"# MJ4U Ads — Decision Call Sheet"]
    mode = "SAMPLE DATA (synthetic)" if sample else "LIVE"
    acct = f"{account.get('name','?')} ({account.get('id','?')})"
    L.append(f"_Generated {generated} · account {acct} · window last {window_days}d · **{mode}** · "
             f"READ-ONLY (no ad changes were made)_\n")

    summary = " · ".join(f"{EMOJI.get(v,'')} {v}: {counts[v]}" for v in
                         sorted(counts, key=lambda v: ORDER.get(v, 9)))
    L.append("## Summary")
    L.append(summary if summary else "_no ads in window_")
    L.append("")

    # group by product code (None -> Unmapped bucket)
    groups: dict[str | None, list] = {}
    econ_by_code: dict[str | None, Economics | None] = {}
    for m, d, code, econ in items:
        groups.setdefault(code, []).append((m, d))
        econ_by_code[code] = econ

    for code in sorted(groups, key=lambda c: (c is None, c or "")):
        econ = econ_by_code[code]
        if econ is not None:
            L.append(f"## {code} — {econ.name}")
            L.append(f"_break-even CPA ${econ.break_even_cpa:.2f} · break-even ROAS "
                     f"{econ.break_even_roas:.2f}× · revenue/order ${econ.revenue_per_order:.2f}_\n")
        else:
            L.append(f"## {code or 'Unmapped (no product code)'}")
            L.append("_no economics — decisions can't be computed until a product code + economics exist_\n")

        rows = sorted(groups[code], key=lambda md: ORDER.get(md[1].verdict, 9))
        for m, d in rows:
            em = EMOJI.get(d.verdict, "")
            label = m.ad_name or m.ad_id or "(unnamed ad)"
            adset = f"  ·  adset: {m.adset_name}" if m.adset_name else ""
            L.append(f"### {em} {d.verdict} — {label}{adset}")
            L.append(f"**{d.headline}**")
            for r in d.reasons:
                L.append(f"- {r}")
            if d.leading:
                L.append(f"- _Leading:_ {' · '.join(d.leading)}")
            if d.flags:
                L.append(f"- ⚠️ {' · '.join(d.flags)}")
            L.append(f"- _metrics:_ {_metrics_line(m)}")
            L.append("")

    L.append("---")
    L.append("_Methodology: sop-docs Facebook-Testing-Scaling-Research.md. Thresholds in "
             "`engine/config/thresholds.json`, economics in `engine/config/products.json`. "
             "This is a recommendation sheet — a human (for now) executes the changes._")
    return "\n".join(L)
