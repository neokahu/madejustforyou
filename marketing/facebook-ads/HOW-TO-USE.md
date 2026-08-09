# How to Use the MJ4U FB-Ads Agent

The operator's manual — how to run the automation day to day. For **one-time setup** (API token, native rules), see `setup/`. This doc assumes setup is done.

---

## 1. What it is (mental model)

Three layers, each with a clear job:

| Layer | File | Job | Acts on the account? |
|---|---|---|---|
| **Decision engine** | `engine/run.py` | reads metrics, applies the kill/keep/scale methodology, writes a **call sheet** | ❌ read-only |
| **Executor** | `engine/execute.py` | turns the engine's verdicts into actions (pause / scale) | ✅ only with `--live` |
| **Safety floor** | Ads Manager rules (Phase 3) | 24/7 emergency backstop, independent of the above | ✅ (native, in Meta) |

**The contract that makes it all work:** every campaign name must contain its product code, e.g.
`MJ4U-111 | Garden Film | Linear entry`. No code → the engine can't map it to break-even economics and marks it **UNMAPPED** (untouched).

---

## 2. Commands (cheat sheet)

Run from `marketing/facebook-ads/engine/`:

```bash
python3 run.py                # LIVE read-only → call sheet of kill/keep/scale recommendations
python3 run.py --days 14      # same, 14-day window (default 7)
python3 run.py --sample       # demo on synthetic data (no account needed)

python3 execute.py            # DRY-RUN on live account: prints what it WOULD pause/scale, changes nothing
python3 execute.py --live     # LIVE: actually pauses losers / scales winners (guardrailed)
python3 execute.py --sample   # demo the executor on synthetic data

python3 floor_spec.py         # print the Ads-Manager safety-floor numbers for each product
```

Outputs land in `marketing/facebook-ads/reports/` (git-ignored): dated call sheets + the append-only `action-log.jsonl`.

---

## 3. The everyday workflow

**Daily (once campaigns are running):**
1. `python3 run.py` → open the newest `reports/call-sheet-*.md`. This is the engine's read on every ad.
2. `python3 execute.py` (dry-run) → read the **"WOULD DO"** list. This is exactly what it would pause/scale.
3. Either do those clicks yourself, **or** (once you trust it) let the scheduled `--live` run do them (see §7).

**Weekly:** skim `reports/action-log.jsonl` and recent call sheets for patterns the rules don't reason about — which *angles* win, creative fatigue trends, products to retire. That's your strategic layer.

---

## 4. Reading the call sheet

Each ad gets one verdict:

| Verdict | Meaning | What the executor does |
|---|---|---|
| 🟢 **SCALE** | winner — ROAS ≥ 1.4× break-even **and profitable ≥3 consecutive days** (not a one-day fluke) | +20% to its ad set's daily budget (skipped past `no_scale_after` cut-off) |
| 🟡 **KEEP** | profitable but not yet a scale candidate (or too young) | nothing — let it accumulate |
| ⚪ **WATCH** | below break-even but not yet at the kill bar | nothing — watch closely |
| 🔴 **KILL** | dead creative — **clearly-dead-early** (bad hook + bad link-CTR + 0 ATC, *before* 1× CPA), or 0 ATC after 1× CPA, or ATC-no-sale by 2.5×, or unprofitable past the bar | pauses the ad |
| ⏳ **INSUFFICIENT_DATA** | spent < 1× break-even CPA — too early to judge | nothing |
| ❓ **UNMAPPED** | no `MJ4U-NNN` code in the campaign name | nothing (can't compute break-even) |

Every ad also shows a **Leading** line (hook %, link CTR, CPC, cost/ATC tagged weak/ok/healthy) and its raw metrics. All thresholds are relative to **that product's** break-even.

---

## 5. Reading the executor output

```
WOULD DO (3):
  • pause ad 'Flash-forward hook'  (0 add-to-cart after $46 …)
  • pause ad 'Static testimonial'  (34 ATC but 0 purchases by $100 …)
  • scale ad set 'US | Broad 25-65'  $60.00 → $72.00  (winner(s): Linear-entry v1)

SKIPPED by guardrail (1):
  • scale ad set '…'  $X → $Y  →  would exceed global daily ceiling $500.00
```

- **WOULD DO** (dry-run) / **EXECUTED** (`--live`) = the actions.
- **SKIPPED by guardrail** = a safety rule blocked it, with the reason (ceiling, cap, cooldown, CBO, max-actions).
- The `reports/action-log.jsonl` records every line permanently (timestamp, reason, from→to budget) for audit and undo.

---

## 5b. Uploading a new product's ad draft (standardized)

Don't hand-build ads. Author the content once, in the standard format, and let the uploader build the PAUSED draft identically every time.

1. Create `products/<id>/ads/ad-content.json` (copy MJ4U-111's as a template). The key rule: **`primary_text` is an array of lines**, not a paragraph — this is what keeps copy scannable in-feed. Empty string `""` = blank line; use emoji/✔️ bullets for lists.
2. Lint + preview it (no writes):
   ```bash
   cd marketing/facebook-ads/engine
   python3 upload_draft.py ../../../products/<id>/ads/ad-content.json --validate-only
   ```
   It rejects a wall-of-text `primary_text` and warns on over-long lines.
3. Build the PAUSED draft (campaign → ad set → video upload → creatives → ads):
   ```bash
   python3 upload_draft.py ../../../products/<id>/ads/ad-content.json
   ```
   It prints an Ads Manager review link + saves IDs to `reports/<id>-draft-ids.json`. Everything is PAUSED — you review and activate.

> **Copy-format standard (enforced):** short lines, a blank line between beats, emoji/✔️ bullets for lists, CTA on its own line. Never one dense paragraph. The uploader will refuse copy that isn't structured as lines.

> **Structure standard (enforced, methodology Parts 3/4/5/8):** set `stage` (`validate` or `iterate`) and `test_variable` in `ad-content.json`. The uploader checks the build against the doc: **ABO** budget (CBO = hard error on a test), **lowest-cost** bid, budget in the stage's range (validate $20–30, iterate $30–50), creative count in range (validate 2–3, iterate 3–5), **broad** audience (warns on interests/LAL), and that you've declared the one variable you're isolating. Run `--validate-only` to see the conformance line + any warnings before building.

## 6. Common changes

**Add a new product** (so its campaigns get managed):
1. Edit `engine/config/products.json` — copy the `MJ4U-111` block, set the new code + real economics (`revenue_per_order`, `cogs_all_in`, `fee_pct`).
2. Name that product's campaigns with the code: `MJ4U-123 | …`.
3. `python3 floor_spec.py` → set the new product's native floor rules in Ads Manager.
That's it — the engine and executor pick it up automatically.

**Tune the methodology** (kill/scale sensitivity): `engine/config/thresholds.json`. The doc's US-ecom benchmarks are defaults — recalibrate to your account after a few weeks.

**Tune the guardrails** (spend limits): `engine/config/execution.json` — `global_daily_budget_ceiling_usd`, `max_adset_daily_budget_usd`, `scale_cooldown_hours`, `scale_increase_pct`, `max_actions_per_run`.

**Tune the safety floor**: `engine/config/floor_thresholds.json`, then re-run `floor_spec.py` and update the Ads Manager rules.

---

## 7. Going unattended (full auto)

Only after a **3–4 day dry-run soak** where `execute.py`'s "WOULD DO" matches your judgement (full go-live sequence in `setup/03-unattended-execution.md`). Then schedule it — `crontab -e`, daily 9am:

```cron
0 9 * * * cd /Users/neovh34/Desktop/projects/worktree/madejustforyou/product-research/marketing/facebook-ads/engine && /usr/bin/python3 run.py >> ../reports/cron.log 2>&1 && /usr/bin/python3 execute.py --live >> ../reports/cron.log 2>&1
```

Daily is the right cadence for a $30–100/day account; the 48h scale cooldown prevents over-scaling. No Claude needed in the loop — the methodology is fully in the code.

---

## 8. Emergency stop 🛑

Any one of these makes the next run write **nothing** (dry-run still shows what it wanted to do):
- `export FB_ENGINE_KILL_SWITCH=1` (in your shell / the cron environment), **or**
- set `"kill_switch": true` in `engine/config/execution.json`, **or**
- remove the cron line entirely.

The **native floor rules stay active regardless** — they're in Meta, not in this code, so they keep protecting you even if you stop the engine.

**Undo a specific action:** find it in `reports/action-log.jsonl` (it has the from→to budget) and reverse it in Ads Manager.

---

## 9. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Ad shows **UNMAPPED** | campaign name has no `MJ4U-NNN` code | rename the campaign to include the code |
| Ad shows **UNMAPPED** with "code but no economics" | product missing from `products.json` | add it (§6) |
| Everything **INSUFFICIENT_DATA** | campaigns too new / too little spend | wait until spend ≥ 1× break-even CPA |
| Scale **SKIPPED: CBO** | ad set uses campaign budget (CBO) | scale at the campaign level manually, or switch to ABO for testing |
| Scale **SKIPPED: ceiling/cooldown/cap** | a guardrail did its job | expected; raise the limit in `execution.json` only if intended |
| `execute.py --live` writes nothing | kill-switch on | unset `FB_ENGINE_KILL_SWITCH` / `kill_switch` |
| `Meta API 190 / token` error | token expired or rotated | regenerate the system-user token, update `.env` |
| `(#274)` on write | system user lost the ad-account role | re-check §3 of `setup/01-meta-api-setup.md` |

---

## 10. Safety guarantees (why this is safe to run)

- **Read and write are separate modules.** `run.py` literally cannot write; only `execute.py --live` (via `meta_write.py`) can.
- **Dry-run is the default** everywhere — you always see actions before they happen.
- **Five guardrails** cap spend, pace scaling, and bound blast radius.
- **Everything is logged** append-only.
- **An independent native floor** protects the account even if this whole system is off.
