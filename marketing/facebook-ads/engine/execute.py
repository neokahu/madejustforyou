#!/usr/bin/env python3
"""Phase 4 — guardrailed write executor.

Turns the engine's verdicts into Meta actions:
  KILL ad   -> pause the ad
  SCALE ad  -> increase its ad set's daily budget by scale_increase_pct

DRY-RUN BY DEFAULT (proposes + logs, changes nothing). --live actually writes,
and additionally requires the kill-switch to be off. Every action — executed,
dry, or skipped-by-guardrail — is appended to reports/action-log.jsonl and shown
in a run digest.

Guardrails: global daily-budget ceiling, per-ad-set max budget, per-ad-set scale
cooldown, max actions/run, kill-switch, CBO detection. Writes go through the
separate meta_write module, which is only constructed for a real --live run.

Usage:
  python3 execute.py --sample     # dry-run on synthetic data (prove the path)
  python3 execute.py              # dry-run on the live account (default)
  python3 execute.py --live       # LIVE writes (guardrailed)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

import economics
import rules
from meta import MetaReadClient, age_days
from run import load_env  # reuse the tiny .env loader

HERE = Path(__file__).resolve().parent
ENV_PATH = HERE.parent / ".env"
CFG = HERE / "config"
LOG = HERE.parent / "reports" / "action-log.jsonl"


def _money(cents: float) -> str:
    return f"${cents/100:,.2f}"


def load_data(sample: bool, days: int):
    """Return (account, insight_rows, adsets{ id: {name, daily_budget_cents|None} })."""
    if sample:
        raw = json.loads((HERE / "sample_data.json").read_text())
        adsets = {aid: {"name": a.get("name", aid),
                        "daily_budget": int(a["daily_budget"]) if a.get("daily_budget") else None}
                  for aid, a in raw.get("adsets", {}).items()}
        return raw.get("account", {"name": "SAMPLE", "id": "act_SAMPLE"}), raw["insights"], adsets

    env = load_env(ENV_PATH)
    token, acct_id = env.get("META_SYSTEM_USER_TOKEN"), env.get("META_AD_ACCOUNT_ID")
    if not token or not acct_id:
        sys.exit(f"ERROR: token/account missing in {ENV_PATH}")
    client = MetaReadClient(token, acct_id, env.get("META_API_VERSION", "v26.0"))
    account = client.account()
    rows = client.ad_insights(days=days)
    ads_meta = client.ads_meta()
    daily = client.ad_insights_daily(days=days)
    for r in rows:
        am = ads_meta.get(str(r.get("ad_id", "")))
        if am:
            r["_age_days"] = age_days(am.get("created_time"))
            r["effective_status"] = am.get("effective_status", "")
        droas, dcpm, dctr = rules.daily_series(daily.get(str(r.get("ad_id", "")), []))
        r["_daily"] = {"roas": droas, "cpm": dcpm, "ctr": dctr}
    adsets = {aid: {"name": a.get("name", aid),
                    "daily_budget": int(a["daily_budget"]) if a.get("daily_budget") else None}
              for aid, a in client.adsets_meta().items()}
    return account, rows, adsets


def last_executed_scale(adset_id: str) -> dt.datetime | None:
    """Most recent LIVE-executed scale of this ad set, from the action log (for cooldown)."""
    if not LOG.exists():
        return None
    latest = None
    for line in LOG.read_text().splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("action") == "scale_adset" and e.get("adset_id") == adset_id and e.get("status") == "executed":
            ts = dt.datetime.fromisoformat(e["ts"])
            if latest is None or ts > latest:
                latest = ts
    return latest


def append_log(entries: list[dict]):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        for e in entries:
            f.write(json.dumps(e) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description="MJ4U FB Ads — guardrailed write executor")
    ap.add_argument("--sample", action="store_true", help="run on synthetic data")
    ap.add_argument("--live", action="store_true", help="ACTUALLY write (default is dry-run)")
    ap.add_argument("--days", type=int, default=7)
    args = ap.parse_args()

    cfg = json.loads((CFG / "execution.json").read_text())
    kill_switch = bool(cfg.get("kill_switch")) or os.environ.get("FB_ENGINE_KILL_SWITCH") == "1"
    pct = cfg["scale_increase_pct"]
    max_cents = int(cfg["max_adset_daily_budget_usd"] * 100)
    ceiling_cents = int(cfg["global_daily_budget_ceiling_usd"] * 100)
    cooldown = dt.timedelta(hours=cfg["scale_cooldown_hours"])
    max_actions = cfg["max_actions_per_run"]

    # effective mode: live writes only if --live AND kill-switch off
    live = args.live and not kill_switch
    now = dt.datetime.now()

    products = economics.load_products(CFG / "products.json")
    account, rows, adsets = load_data(args.sample, args.days)
    items = []  # (Metrics, Decision)
    for row in rows:
        m = rules.normalize_row(row)
        code = rules.product_code(m.campaign_name)
        econ = products.get(code) if code else None
        items.append((m, rules.decide(m, econ, json.loads((CFG / "thresholds.json").read_text()))))

    # -- build proposed actions ---------------------------------------------
    proposals: list[dict] = []  # each: dict with action, ids, reason, and mutable status
    for m, d in items:
        if d.verdict == rules.KILL and m.ad_id and (m.effective_status in ("", "ACTIVE")):
            proposals.append({"action": "pause_ad", "ad_id": m.ad_id, "ad_name": m.ad_name,
                              "campaign": m.campaign_name, "reason": d.headline})

    scale_by_adset: dict[str, list[str]] = {}
    for m, d in items:
        if d.verdict == rules.SCALE and m.adset_id:
            scale_by_adset.setdefault(m.adset_id, []).append(m.ad_name)

    # projected total daily budget (for the global ceiling)
    projected_total = sum(a["daily_budget"] for a in adsets.values() if a.get("daily_budget"))

    no_scale_after = cfg.get("no_scale_after")
    cutoff_passed = bool(no_scale_after) and now.date() > dt.date.fromisoformat(no_scale_after)

    for adset_id, winners in scale_by_adset.items():
        a = adsets.get(adset_id, {})
        cur = a.get("daily_budget")
        name = a.get("name", adset_id)
        base = {"action": "scale_adset", "adset_id": adset_id, "adset_name": name,
                "reason": f"winner(s): {', '.join(winners)}"}
        if cutoff_passed:
            proposals.append({**base, "skip": f"past scale cut-off {no_scale_after} (fulfillment deadline)"})
            continue
        if cur is None:
            proposals.append({**base, "skip": "CBO/campaign-budget ad set — scale at campaign level (unsupported)"})
            continue
        if cur >= max_cents:
            proposals.append({**base, "from": cur, "skip": f"already at/above max cap {_money(max_cents)}"})
            continue
        new = int(round(cur * (1 + pct / 100)))
        capped = new > max_cents
        if capped:
            new = max_cents
        last = last_executed_scale(adset_id)
        if last and (now - last) < cooldown:
            hrs = (now - last).total_seconds() / 3600
            proposals.append({**base, "from": cur, "to": new, "skip": f"cooldown ({hrs:.0f}h < {cfg['scale_cooldown_hours']}h since last scale)"})
            continue
        if projected_total - cur + new > ceiling_cents:
            proposals.append({**base, "from": cur, "to": new, "skip": f"would exceed global daily ceiling {_money(ceiling_cents)}"})
            continue
        projected_total += (new - cur)
        proposals.append({**base, "from": cur, "to": new, "capped": capped})

    # -- max actions per run -------------------------------------------------
    actionable = [p for p in proposals if "skip" not in p]
    if len(actionable) > max_actions:
        for p in actionable[max_actions:]:
            p["skip"] = f"exceeds max_actions_per_run ({max_actions})"

    # -- execute / log -------------------------------------------------------
    writer = None
    if live:
        from meta_write import MetaWriteClient
        env = load_env(ENV_PATH)
        writer = MetaWriteClient(env["META_SYSTEM_USER_TOKEN"], env.get("META_API_VERSION", "v26.0"))

    log_entries, done, skipped = [], [], []
    for p in proposals:
        entry = {"ts": now.isoformat(timespec="seconds"), "mode": "live" if live else "dry",
                 "account": account.get("id", "?"), **{k: v for k, v in p.items() if k != "skip"}}
        if "skip" in p:
            entry["status"] = "skipped"
            entry["detail"] = p["skip"]
            skipped.append(p)
        elif not live:
            entry["status"] = "dry"
            done.append(p)
        else:
            try:
                if p["action"] == "pause_ad":
                    writer.pause_ad(p["ad_id"])
                elif p["action"] == "scale_adset":
                    writer.set_adset_daily_budget(p["adset_id"], p["to"])
                entry["status"] = "executed"
                done.append(p)
            except Exception as ex:  # noqa: BLE001 — log and continue, never crash mid-run
                entry["status"] = "error"
                entry["detail"] = str(ex)
                skipped.append(p)
        log_entries.append(entry)
    append_log(log_entries)

    # -- digest --------------------------------------------------------------
    mode = "LIVE (writes applied)" if live else (
        "DRY-RUN (kill-switch ON — no writes)" if (args.live and kill_switch) else "DRY-RUN (no writes)")
    print(f"\nMJ4U executor — {mode} · account {account.get('name','?')} ({account.get('id','?')})")
    if kill_switch and args.live:
        print("⛔ KILL SWITCH ENGAGED — refused to write. Unset config.kill_switch / FB_ENGINE_KILL_SWITCH to enable.")

    def _fmt(p):
        if p["action"] == "pause_ad":
            return f"pause ad '{p['ad_name']}'  ({p['reason']})"
        if "from" in p and "to" in p:
            cap = " [capped at max]" if p.get("capped") else ""
            return f"scale ad set '{p['adset_name']}'  {_money(p['from'])} → {_money(p['to'])}{cap}  ({p['reason']})"
        return f"scale ad set '{p['adset_name']}'  ({p['reason']})"

    verb = "EXECUTED" if live else "WOULD DO"
    print(f"\n{verb} ({len(done)}):")
    for p in done:
        print(f"  • {_fmt(p)}")
    if skipped:
        print(f"\nSKIPPED by guardrail ({len(skipped)}):")
        for p in skipped:
            print(f"  • {_fmt(p)}  →  {p['skip']}" if "skip" in p else f"  • {_fmt(p)}  →  error")
    if not done and not skipped:
        print("\nNo KILL/SCALE actions this run.")
    print(f"\nProjected total daily budget after run: {_money(projected_total)} "
          f"(ceiling {_money(ceiling_cents)})")
    print(f"Action log → {LOG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
