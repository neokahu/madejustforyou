"""Per-product break-even economics.

Break-even CPA  = contribution margin per order
Break-even ROAS = revenue_per_order / contribution
Every kill/keep/scale threshold is drawn RELATIVE to these, per the methodology
(Facebook-Testing-Scaling-Research.md, Part 1).
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Economics:
    product_id: str
    name: str
    revenue_per_order: float                       # TRUE revenue you collect (product + shipping)
    cogs_all_in: float
    fee_pct: float
    reported_value_per_order: float | None = None  # what the PIXEL sends to Meta (may exclude shipping);
                                                   # defaults to revenue_per_order when they match

    @property
    def fee(self) -> float:
        return self.revenue_per_order * self.fee_pct

    @property
    def contribution(self) -> float:
        # profit margin per order, on TRUE revenue -> drives break-even CPA
        return self.revenue_per_order - self.cogs_all_in - self.fee

    @property
    def reported_value(self) -> float:
        return self.reported_value_per_order if self.reported_value_per_order is not None else self.revenue_per_order

    @property
    def break_even_cpa(self) -> float:
        return self.contribution

    @property
    def break_even_roas(self) -> float:
        # ROAS is measured against what META SEES (reported pixel value), not true revenue,
        # so this stays consistent with the ROAS the engine reads from Insights.
        return self.reported_value / self.contribution if self.contribution > 0 else float("inf")


def load_products(path: str | Path) -> dict[str, Economics]:
    raw = json.loads(Path(path).read_text())
    out: dict[str, Economics] = {}
    for pid, p in raw.get("products", {}).items():
        rv = p.get("reported_value_per_order")
        out[pid] = Economics(
            product_id=pid,
            name=p.get("name", pid),
            revenue_per_order=float(p["revenue_per_order"]),
            cogs_all_in=float(p["cogs_all_in"]),
            fee_pct=float(p.get("fee_pct", 0.0)),
            reported_value_per_order=float(rv) if rv is not None else None,
        )
    return out
