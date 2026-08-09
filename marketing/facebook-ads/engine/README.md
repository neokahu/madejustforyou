# MJ4U FB Ads — Decision Engine (Phase 2, read-only)

Pulls ad Insights from the Meta Marketing API, maps each campaign to a product
via its **`MJ4U-NNN` code in the campaign name**, applies the kill/keep/scale
methodology, and writes a Markdown **call sheet** of recommendations.

**It is strictly read-only** — it never creates, edits, pauses, or deletes
anything. Execution stays human (you read the sheet and click) until Phase 4.

## Run
```bash
cd marketing/facebook-ads/engine
python3 run.py --sample        # synthetic data — see every verdict, no account needed
python3 run.py                 # live, last 7 days (reads ../.env)
python3 run.py --days 14       # live, custom window
python3 run.py --out /tmp/x.md # custom output path
```
Output → `marketing/facebook-ads/reports/` (gitignored). Zero pip installs (stdlib only). Python 3.10+.

## Campaign naming = the mapping contract
The engine reads the product from the campaign name. **Name campaigns so they contain the product code**, e.g.:
```
MJ4U-111 | Garden Film | Linear entry
MJ4U-052 | Snowman lightbox | UGC
```
Any campaign without an `MJ4U-NNN` code → listed as **UNMAPPED** (no break-even, no verdict). Regex: `\bMJ4U-\d{3}\b`.

## How a verdict is reached (per ad)
All thresholds are **relative to that product's break-even** (from `config/products.json`). In priority order:
0. **KILL (early / clearly-dead)** — *before* 1× CPA: enough impressions **AND** hook < 20% **AND** link-CTR < 0.8% **AND** 0 ATC. Fast-kills obvious duds so budget isn't wasted to a full CPA (methodology Part 2 leading indicators). CPM/CPC are context, never standalone triggers.
1. **INSUFFICIENT** — spend < 1× break-even CPA (and not early-dead) → too early to judge.
2. **KILL** — 0 add-to-cart after ≥1× break-even CPA (dead creative).
3. **KILL** — ATC but 0 purchases by ≥2.5× CPA (offer/checkout/price weak).
4. Has purchases → judge on ROAS vs break-even:
   - **SCALE** — ROAS ≥ 1.4× break-even **and** **profitable ≥3 *consecutive* days** (Part 6 — guards against a one-lucky-day aggregate).
   - **KEEP** — strong ROAS but <3 days old / not yet ≥3 consecutive profitable days, or profitable but below the scale bar (accumulate).
   - **KILL** — ROAS below break-even past 2× CPA spend & ≥3 days.
   - **WATCH** — below break-even but not yet at the kill bar.
5. **WATCH** — ATC, no purchase yet, under the 2.5× kill bar.
Plus an advisory **fatigue flag** — fires on the Part-7 combination: frequency high **AND** CPM rising **AND** CTR falling (from the daily series) → refresh creative. Frequency-high-alone shows a lighter "watch" note.

Scale actions also respect `execution.json → no_scale_after` (a fulfillment/seasonal cut-off date; Part 8).

Leading indicators (hook rate, link CTR, CPC, cost/ATC) are shown for every ad as context, tagged weak/ok/healthy.

## Files
| File | Role |
|---|---|
| `run.py` | CLI entrypoint: pull → map → decide → render |
| `meta.py` | **read-only** Marketing API client (Insights + ad age/status) |
| `economics.py` | break-even CPA/ROAS from unit economics |
| `rules.py` | the decision methodology + insights-row parser |
| `report.py` | Markdown call-sheet renderer |
| `floor_spec.py` | generates the Phase-3 native-rule safety-floor numbers per product |
| `execute.py` | **Phase-4 guardrailed write executor** (dry-run default; `--live` writes) |
| `meta_write.py` | the ONLY module the executor mutates through (pause ad / set ad-set budget) |
| `upload_draft.py` | **standardized ad-draft uploader** — reads a product's `ad-content.json`, enforces the copy-format standard, builds campaign→ad set→video→creatives→ads (all PAUSED). `--validate-only` lints + previews without writing. |
| `config/products.json` | per-product unit economics (**edit to add products**) |
| `config/thresholds.json` | methodology thresholds (recalibrate to your account over time) |
| `config/floor_thresholds.json` | native safety-floor multipliers (Phase 3) |
| `config/execution.json` | write-execution guardrails (Phase 4: ceilings, cooldown, kill-switch) |
| `sample_data.json` | synthetic insights + ad-set budgets for `--sample` |

## Known notes / TODO for later phases
- **Hook rate (live):** v26 removed the `video_3_sec_watched_actions` field, so live pulls use `video_play_actions` (video plays) as the numerator — a directional hook proxy, not literally 3-second views. Revisit if a truer 3-sec metric is needed.
- **Attribution:** ROAS/purchases come from Meta's own numbers (post-iOS14.5 undercount). The methodology already leans on leading indicators + accumulated spend for this reason; a server-side/first-party ROAS feed could be layered in later.
- **Add products:** copy the `MJ4U-111` block in `config/products.json` and fill real economics per product.
- **Phase 3/4:** native-rule safety floor, then guardrailed write execution (dry-run → live).
