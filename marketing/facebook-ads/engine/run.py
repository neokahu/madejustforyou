#!/usr/bin/env python3
"""MJ4U FB Ads — read-only decision engine (Phase 2).

Pulls ad Insights, maps each campaign to a product via its MJ4U-NNN code,
applies the kill/keep/scale methodology, and writes a Markdown call sheet.
It NEVER changes anything in the ad account.

Usage:
  python3 run.py --sample            # run on synthetic data (no account needed)
  python3 run.py                     # live: pull last 7d from the account in ../.env
  python3 run.py --days 14           # live, 14-day window
  python3 run.py --out path.md       # custom output path
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import economics
import report
import rules
from meta import MetaReadClient, age_days

HERE = Path(__file__).resolve().parent
ENV_PATH = HERE.parent / ".env"
CFG = HERE / "config"


def load_env(path: Path) -> dict:
    env: dict[str, str] = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


def build_items(rows, products):
    """rows: list of raw insight dicts -> list of (Metrics, Decision, code, econ)."""
    thr = rules.load_thresholds(CFG / "thresholds.json")
    items = []
    for row in rows:
        m = rules.normalize_row(row)
        code = rules.product_code(m.campaign_name)
        econ = products.get(code) if code else None
        d = rules.decide(m, econ, thr)
        items.append((m, d, code, econ))
    return items


def main() -> int:
    ap = argparse.ArgumentParser(description="MJ4U FB Ads read-only decision engine")
    ap.add_argument("--sample", action="store_true", help="run on engine/sample_data.json instead of the live account")
    ap.add_argument("--days", type=int, default=7, help="insights window in days (default 7)")
    ap.add_argument("--out", type=str, default=None, help="output markdown path")
    args = ap.parse_args()

    products = economics.load_products(CFG / "products.json")
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

    if args.sample:
        raw = json.loads((HERE / "sample_data.json").read_text())
        rows = raw["insights"]
        account = raw.get("account", {"name": "SAMPLE", "id": "act_SAMPLE"})
    else:
        env = load_env(ENV_PATH)
        token = env.get("META_SYSTEM_USER_TOKEN")
        acct_id = env.get("META_AD_ACCOUNT_ID")
        version = env.get("META_API_VERSION", "v26.0")
        if not token or not acct_id:
            print(f"ERROR: META_SYSTEM_USER_TOKEN / META_AD_ACCOUNT_ID missing in {ENV_PATH}", file=sys.stderr)
            return 2
        client = MetaReadClient(token, acct_id, version)
        account = client.account()
        rows = client.ad_insights(days=args.days)
        meta = client.ads_meta()
        daily = client.ad_insights_daily(days=args.days)
        for r in rows:  # enrich with age + status + daily series
            am = meta.get(str(r.get("ad_id", "")))
            if am:
                r["_age_days"] = age_days(am.get("created_time"))
                r["effective_status"] = am.get("effective_status", "")
            roas, cpm, ctr = rules.daily_series(daily.get(str(r.get("ad_id", "")), []))
            r["_daily"] = {"roas": roas, "cpm": cpm, "ctr": ctr}

    items = build_items(rows, products)
    md = report.render(items, account, args.days, now, sample=args.sample)

    out = Path(args.out) if args.out else (HERE.parent / "reports" /
          f"call-sheet-{'sample-' if args.sample else ''}{dt.datetime.now().strftime('%Y%m%d-%H%M')}.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md)

    # stdout summary
    counts: dict[str, int] = {}
    for _, d, _, _ in items:
        counts[d.verdict] = counts.get(d.verdict, 0) + 1
    if not items:
        print("No ads in the selected window.")
    else:
        print("Verdicts: " + " · ".join(f"{v}={counts[v]}" for v in sorted(counts)))
    print(f"Call sheet → {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
