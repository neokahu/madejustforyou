#!/usr/bin/env python3
"""Generate the native-rule SAFETY-FLOOR spec per product from unit economics.

The floor rules are set by hand in Meta Ads Manager (Automated Rules) and run
24/7 under your own BM — a deterministic backstop, independent of the decision
engine. Thresholds are LOOSER than the engine on purpose: the engine acts first
(1x / 2.5x CPA); the floor only catches runaways or moments the engine didn't run.

This script just computes the exact numbers per product so they stay in sync with
config/products.json. Read-only, prints Markdown.

Usage: python3 floor_spec.py
"""
from __future__ import annotations

import json
from pathlib import Path

import economics

HERE = Path(__file__).resolve().parent
CFG = HERE / "config"


def main() -> int:
    products = economics.load_products(CFG / "products.json")
    thr = json.loads((CFG / "floor_thresholds.json").read_text())
    ek, nf, sc = thr["emergency_kill"], thr["notify"], thr["optional_interim_scale"]

    out = ["# Native-rule SAFETY-FLOOR spec (per product)", "",
           "_Set these in Ads Manager → Rules. Defensive backstop, looser than the engine. "
           "Guide: `setup/02-native-rules-safety-floor.md`._", ""]

    for pid, e in products.items():
        be_cpa, be_roas = e.break_even_cpa, e.break_even_roas
        no_purchase_spend = be_cpa * ek["no_purchase_spend_mult_of_be_cpa"]
        roas_floor = be_roas * ek["roas_floor_frac_of_be_roas"]
        roas_spend = be_cpa * ek["roas_floor_spend_mult_of_be_cpa"]
        scale_roas = be_roas * sc["roas_mult_of_be_roas"]
        out += [
            f"## {pid} — {e.name}",
            f"break-even CPA **${be_cpa:.2f}** · break-even ROAS **{be_roas:.2f}×**", "",
            "| Rule | Scope | Condition | Action | Frequency |",
            "|---|---|---|---|---|",
            f"| **A · Runaway kill (no sales)** | Ad set | Purchases = 0 **AND** Amount spent ≥ **${no_purchase_spend:.0f}** | Turn off ad set | Daily (or continuously) |",
            f"| **B · ROAS emergency** | Ad set | Purchase ROAS < **{roas_floor:.2f}** **AND** Amount spent ≥ **${roas_spend:.0f}** **AND** Time since created ≥ **{ek['min_age_days']}d** | Turn off ad set | Daily |",
            f"| **C · Fatigue notify** | Ad | Frequency > **{nf['frequency_high_above']:.0f}** (last 7d) | **Send notification only** | Daily |",
            f"| **D · (optional, interim) Scale** | Ad set / Campaign | Purchase ROAS > **{scale_roas:.2f}** (last {sc['min_days']}d) | Increase daily budget **{sc['increase_pct']}%** | Max once / **{sc['cooldown_hours']}h** |",
            "",
            f"> Rule D is an interim offense-rule for the window BEFORE the Phase-4 engine drives scaling. "
            f"**Disable it when the engine goes live** to avoid two systems changing budgets at once.", "",
        ]
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
