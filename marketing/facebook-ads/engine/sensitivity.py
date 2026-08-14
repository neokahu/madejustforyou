#!/usr/bin/env python3
"""Funnel sensitivity tracker — is a product survivable BEFORE you spend a dollar?

Chains the only four levers that decide paid-prospecting viability:

    CPC = CPM / (CTR x 1000)                    # cost to buy a click
    CPA = CPC / CVR = CPM / (CTR x 1000 x CVR)   # cost to buy a sale
    survivable  <=>  CPA <= break-even CPA (contribution margin/order)
    max-viable CPC = break-even CPA x CVR

Break-even CPA comes from the product's own economics (economics.py / products.json),
so "survivable" is always relative to THAT product's margin — same basis the kill
engine uses. Also sizes the spend to clear Meta's ~50-sales/week learning-phase exit.

Usage:
  python3 sensitivity.py                         # default product (first in products.json)
  python3 sensitivity.py --product MJ4U-111
  python3 sensitivity.py --product MJ4U-111 --cvr 0.02
  python3 sensitivity.py --aov 59.93 --cogs 20 --fee 0.03   # ad-hoc product, no config
  python3 sensitivity.py --op-cpm 30 --op-ctr 0.02          # set the "realistic" operating point

All benchmark defaults are labelled at the bottom with their source. Nothing here is
scraped live — it's arithmetic on inputs you choose.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import economics

HERE = Path(__file__).resolve().parent
PRODUCTS = HERE / "config" / "products.json"

# --- default sweep ranges (override on CLI) ---
CPM_ROWS = [14, 20, 25, 30, 40, 50, 60]        # $ per 1000 impressions
CTR_COLS = [0.010, 0.015, 0.020, 0.025, 0.030, 0.040, 0.050]  # link CTR
CVR_SWEEP = [0.008, 0.012, 0.016, 0.020, 0.025, 0.030]        # click->purchase


def cpc(cpm: float, ctr: float) -> float:
    return cpm / (1000.0 * ctr) if ctr else float("inf")


def cpa(cpm: float, ctr: float, cvr: float) -> float:
    return cpc(cpm, ctr) / cvr if cvr else float("inf")


def weekly_spend(target_sales: int, cvr: float, ctr: float, cpm: float) -> dict:
    clicks = target_sales / cvr
    impressions = clicks / ctr
    spend = impressions / 1000.0 * cpm
    return {
        "clicks": clicks, "impressions": impressions,
        "spend_wk": spend, "spend_day": spend / 7.0,
        "cpa": spend / target_sales, "cpc": spend / clicks,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--product", help="product code in products.json (default: first)")
    ap.add_argument("--aov", type=float, help="revenue/order (ad-hoc, overrides --product)")
    ap.add_argument("--cogs", type=float, help="all-in COGS/order (with --aov)")
    ap.add_argument("--fee", type=float, default=0.03, help="payment fee fraction (with --aov)")
    ap.add_argument("--cvr", type=float, default=0.016, help="click->purchase rate for the matrix (default 1.6%%)")
    ap.add_argument("--target-sales", type=int, default=50, help="weekly sales to size (default 50 = learning-exit)")
    ap.add_argument("--op-cpm", type=float, default=30.0, help="'realistic' operating CPM")
    ap.add_argument("--op-ctr", type=float, default=0.020, help="'realistic' operating CTR")
    args = ap.parse_args()

    # --- resolve economics ---
    if args.aov is not None:
        if args.cogs is None:
            ap.error("--aov requires --cogs")
        econ = economics.Economics("adhoc", "ad-hoc product", args.aov, args.cogs, args.fee)
    else:
        prods = economics.load_products(PRODUCTS)
        code = args.product or next(iter(prods))
        if code not in prods:
            ap.error(f"{code} not in products.json (have: {', '.join(prods)})")
        econ = prods[code]

    be = econ.break_even_cpa
    cvr = args.cvr

    print(f"\n{'='*72}")
    print(f" FUNNEL SENSITIVITY — {econ.name}")
    print(f"{'='*72}")
    print(f" revenue/order ${econ.revenue_per_order:.2f} · COGS ${econ.cogs_all_in:.2f} · "
          f"fee ${econ.fee:.2f}  ->  contribution = break-even CPA ${be:.2f}")
    print(f" matrix CVR = {cvr*100:.1f}%   ·   max-viable CPC = ${be*cvr:.2f}  (= break-even CPA x CVR)")
    print(f" survivable cell = CPA <= ${be:.2f}  (marked +).  '-' = loses money per sale.\n")

    # --- MATRIX: CPA for CPM (rows) x CTR (cols) at fixed CVR ---
    hdr = "  CPM \\ CTR |" + "".join(f"{c*100:>8.1f}%" for c in CTR_COLS)
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    for cpm in CPM_ROWS:
        cells = []
        for ctr in CTR_COLS:
            a = cpa(cpm, ctr, cvr)
            mark = "+" if a <= be else "-"
            cells.append(f"{'$'+format(a,'.0f'):>7}{mark}")
        print(f"  ${cpm:>4.0f}     |" + "".join(cells))
    print(f"\n  (+ = CPA within break-even ${be:.0f} at {cvr*100:.1f}% CVR;  - = above it)")

    # --- required CTR to reach break-even, per CPM ---
    print(f"\n  Link CTR you'd need just to hit break-even CPC (${be*cvr:.2f}) at {cvr*100:.1f}% CVR:")
    for cpm in CPM_ROWS:
        req = cpm / (1000.0 * be * cvr)
        flag = "" if req <= 0.03 else ("  (>3% — hard cold)" if req <= 0.06 else "  (>6% — ~impossible cold)")
        print(f"    CPM ${cpm:>4.0f}  ->  {req*100:>5.2f}% CTR{flag}")

    # --- CVR sensitivity at the realistic operating point ---
    print(f"\n  At operating point CPM ${args.op_cpm:.0f} + CTR {args.op_ctr*100:.1f}% (CPC ${cpc(args.op_cpm,args.op_ctr):.2f}), "
          f"CPA by CVR:")
    for c in CVR_SWEEP:
        a = cpa(args.op_cpm, args.op_ctr, c)
        mark = "+ survivable" if a <= be else "- loses money"
        print(f"    CVR {c*100:>4.1f}%  ->  CPA ${a:>6.0f}   {mark}")
    breakeven_cvr = cpc(args.op_cpm, args.op_ctr) / be
    print(f"    -> break-even needs CVR >= {breakeven_cvr*100:.1f}% at this CPM/CTR")

    # --- AOV / margin lever ---
    print(f"\n  Margin lever — raise contribution, widen the CPC ceiling (at {cvr*100:.1f}% CVR):")
    for mult, label in [(1.0, "current"), (1.25, "+25%"), (1.5, "+50%"), (2.0, "x2")]:
        c = be * mult
        opa = cpa(args.op_cpm, args.op_ctr, cvr)
        surv = "+ op-point survives" if opa <= c else "- op-point still loses"
        print(f"    contribution ${c:>6.2f} ({label:>7})  ->  break-even CPA ${c:>6.2f} · "
              f"max-viable CPC ${c*cvr:.2f}   {surv}")

    # --- learning-phase sizing ---
    op = weekly_spend(args.target_sales, cvr, args.op_ctr, args.op_cpm)
    print(f"\n  To clear Meta's ~{args.target_sales}-sales/week learning exit "
          f"@ CPM ${args.op_cpm:.0f}/CTR {args.op_ctr*100:.1f}%/CVR {cvr*100:.1f}%:")
    print(f"    {op['impressions']:>9,.0f} impr  ->  {op['clicks']:>6,.0f} clicks (@ ${op['cpc']:.2f})  ->  "
          f"{args.target_sales} sales")
    print(f"    spend ${op['spend_wk']:,.0f}/wk (${op['spend_day']:,.0f}/day)  ·  "
          f"CPA ${op['cpa']:.0f} vs break-even ${be:.0f}  "
          f"({'PROFITABLE' if op['cpa']<=be else f'{op['cpa']/be:.1f}x OVER'})")

    print(f"\n  Benchmarks (defaults): CVR 1.6%%, CTR 2.19%%, CPM $14 = Triple Whale FY2025 (blended, "
          f"optimistic for cold);\n  CPC $0.70 = WordStream 2025 traffic. Op-point CPM $30/CTR 2%% = "
          f"realistic cold-prospecting (this account's post-learning range).\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
