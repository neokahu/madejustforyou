# Step 4 — Unattended Execution (dry-run → live)

**Goal:** let the engine *act* — pause losers and scale winners — on a schedule, with no human in the loop, behind hard guardrails. This is the "full unattended execution" endpoint.

**Command:** `engine/execute.py`. It runs the decision engine, turns verdicts into Meta actions, and writes them — or, by default, only *proposes* them.

```
KILL ad   → pause the ad
SCALE ad  → increase its ad set's daily budget by scale_increase_pct (20%)
KEEP / WATCH / INSUFFICIENT / UNMAPPED → no action
```

Everything else (decisions, break-even, naming contract) is unchanged from Phases 2–3.

---

## Safety model (read this before `--live`)

- **Dry-run is the default.** `python3 execute.py` proposes + logs, changes **nothing**. Only `--live` writes.
- **Writes are physically isolated.** All mutations go through `meta_write.py`, which is only constructed on a real `--live` run. In dry-run it doesn't exist in memory — no write can happen.
- **Kill-switch.** Set `"kill_switch": true` in `config/execution.json` **or** `export FB_ENGINE_KILL_SWITCH=1`. Either one makes even `--live` refuse to write. Your emergency stop.
- **Full audit log.** Every action — executed, dry, or skipped — appends to `reports/action-log.jsonl` with timestamp, reason, and from/to budget.

### Guardrails (`config/execution.json`)
| Guardrail | Default | What it prevents |
|---|---|---|
| `scale_increase_pct` | 20 | keeps each scale under Meta's learning-reset threshold |
| `max_adset_daily_budget_usd` | 300 | a single ad set running away; scales cap here |
| `global_daily_budget_ceiling_usd` | 500 | total account spend blowing past a hard ceiling; scales that would exceed it are skipped |
| `scale_cooldown_hours` | 48 | re-scaling the same ad set too soon (respects the ~20%/2–3-day rule + Meta's ≤4 budget edits/hr/ad-set) |
| `max_actions_per_run` | 25 | a bad data pull triggering a flood of changes |

All four are proven to bite (see the sample tests). Tune them to your risk tolerance before going live.

**Not covered / by design:**
- **CBO ad sets are never scaled** — if an ad set has no own budget (campaign-budget/CBO), the executor skips it and says so; scale CBO at the campaign level yourself.
- **Attribution:** scale/kill read Meta's own numbers (undercounted post-iOS14.5). The methodology leans on leading indicators + accumulated spend for this reason; the native floor (Phase 3) is the independent backstop.

---

## Go-live sequence (don't skip the dry-run soak)

1. **Rotate** the system-user token + app secret (they were briefly exposed in setup). Update `.env`.
2. **Set the native floor rules** (Phase 3) — the independent seatbelt.
3. **Launch one small test campaign**, named with the product code: `MJ4U-111 | Garden Film | Linear entry`. Give it a couple of ad sets / a few creatives.
4. **Soak in dry-run for 3–4 days.** Once a day run:
   ```bash
   cd marketing/facebook-ads/engine
   python3 run.py            # the call sheet (what the engine thinks)
   python3 execute.py        # dry-run: what it WOULD pause/scale
   ```
   Eyeball the "WOULD DO" list against your own judgement. If it consistently matches, the logic is trustworthy on *your* account.
5. **Flip to live on a schedule.** Only after the soak looks right.

---

## Make it unattended (cron)

Because the methodology is fully encoded in the engine, unattended = just schedule the script. No Claude in the loop, no ongoing token cost. Example `crontab -e` (daily 09:00 local):

```cron
0 9 * * * cd /Users/neovh34/Desktop/projects/worktree/madejustforyou/product-research/marketing/facebook-ads/engine && /usr/bin/python3 run.py >> ../reports/cron.log 2>&1 && /usr/bin/python3 execute.py --live >> ../reports/cron.log 2>&1
```

- Daily is the right cadence for a $30–100/day account (matches the 3–4-day judgement window; the cooldown stops over-scaling).
- Keep `run.py` in the line so a dated call sheet is saved alongside each execution.
- **To pause everything:** `export FB_ENGINE_KILL_SWITCH=1` in the cron environment, or set `kill_switch: true` — the next run writes nothing.

> Optional higher-judgement layer: schedule a weekly Claude review of `reports/` (call sheets + action log) to catch strategy-level issues (fatigue trends, angle winners, products to retire) the deterministic rules don't reason about. That's a supplement, not required for unattended operation.

---

## Rollback / stop
- **Immediate:** kill-switch (env var or config) → next run is a no-op.
- **Full stop:** remove the cron line.
- **Undo a bad action:** the action log has every change with from/to budgets — reverse by hand in Ads Manager or restore the prior budget.

---

## Checklist to go live
- [ ] Token + app secret rotated; `.env` updated
- [ ] Native floor rules (Phase 3) active
- [ ] Test campaign live, named `MJ4U-NNN | …`
- [ ] 3–4 day dry-run soak; "WOULD DO" matches your judgement
- [ ] Guardrail numbers in `execution.json` reviewed for your budget
- [ ] cron scheduled with `--live`; `cron.log` + `action-log.jsonl` being written
- [ ] Kill-switch procedure known and tested
