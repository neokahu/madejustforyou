# Session Handoff — 2026-08-09 · FB-Ads Automation built + MJ4U-111 launched

## Achieved
1. **Built the full FB-ads test→scale automation system** in `marketing/facebook-ads/` (Phases 1–4):
   - **P1 — Meta API access** (`setup/01-meta-api-setup.md`): own Business app `870397309486973` (created in a trusted 2nd BM, shared into the ads BM), system user "Lisa Donovan Five", **non-expiring token** (scopes `ads_read/ads_management/business_management/pages_manage_ads/pages_read_engagement`). Read **and** write validated on the rented+shared ad account `act_725748819027455` — the `#274` "Full Access/App Review" wall is cleared.
   - **P2 — read-only decision engine** (`engine/`: `run.py` `meta.py` `economics.py` `rules.py` `report.py` + `config/products.json`,`thresholds.json`). Encodes the methodology; `--sample` proves every verdict; live read validated.
   - **P3 — native safety-floor rules** created via API (`adrules_library`): **A** runaway-kill (0 sales @ $115), **B** ROAS emergency, **C** fatigue notify. `floor_spec.py` generates the per-product numbers.
   - **P4 — guardrailed write executor** (`execute.py` + write-only `meta_write.py`): KILL→pause ad, SCALE→+20% ad-set budget. Dry-run default; kill-switch; ceiling/cap/cooldown/max-actions guardrails (all tested on sample); append-only `reports/action-log.jsonl`.
   - **Standardized uploader** (`upload_draft.py` + `products/<id>/ads/ad-content.json`): builds the PAUSED draft and **enforces** the copy line-break format + doc-aligned structure.
2. **Audited engine + structure against the methodology doc and fixed the gaps** (user pushed to re-check): early leading-kill (before 1× CPA), **sustained-profit scale** (≥3 *consecutive* profitable days, not an aggregate fluke), **fatigue = combination** (freq + CPM↑ + CTR↓), `no_scale_after` fulfillment cutoff, **ABO/structure enforcement** (CBO on a test = hard error). Added a daily insights pull (`ad_insights_daily`).
3. **Renamed product prefix `MJP` → `MJ4U`** everywhere: tracker CSV (111 codes) + product folder + all active docs + session-log contents + memory + the Google Sheet. **MJ4U = "Made Just 4 U"** (resolves the old open abbreviation question). `design-system.html` base64 font left untouched (was a false positive).
4. **Built + LAUNCHED the real MJ4U-111 draft — scheduled 8:00 AM PDT today:**
   - Campaign `120251785507510556` (OUTCOME_SALES) → ad set **`120251797792690556`** ($30/day, US 25–65, Advantage+ audience, Purchase-optimized on pixel `1565119432072485`) → **3 line-break copy-angle ads** (emo-thesis / count-us-all / dr-benefit) → hero video `1370081524468622`. All ACTIVE; ad-set `start_time=2026-08-09T08:00:00-0700`.
   - Native floor rules A/B/C **live**. Pixel Purchase event **verified** firing (Pixel Helper: value 49.94, USD).
5. **Tracker + Sheet updated:** MJ4U-111 → `stage: ads-live`, `ad_status: active`, `ad_launch_date: 2026-08-09`.

## Learnt / decided (with the source behind each)
- **Account structure makes first-party automation legit:** BM is his, only the ad account is rented + shared into his BM with admin → own app + system-user token works. *Source: the §6 API write test succeeded (created+deleted a paused campaign).*
- **Pixel-value gotcha (affects every product's ROAS):** Shopify's standard pixel reports the **product subtotal only ($49.94)**, excluding the always-$9.99 shipping. True revenue = **$59.93**; all-in cost **$20** (confirmed by user). => break-even **CPA ≈ $38.13** (CPA logic + purchase-count rules UNAFFECTED), but break-even **ROAS on Meta's basis = 49.94/38.13 ≈ 1.31×** (not 1.57× true). The understatement cancels because thresholds are on the same basis → **no false kills**. `economics.py` splits `revenue_per_order` (true) vs `reported_value_per_order` (pixel). *Source: Pixel Helper test showed value 49.94; user confirmed shipping + cost.* **Fix later:** freelancer sends order total via a Shopify custom pixel → set `reported_value_per_order=59.93`, ROAS reverts to ~1.57×.
- **App must be LIVE to create ad creatives** (page posts); dev mode blocks it (subcode 1885183). Everything else (campaign/adset/insights/pause/budget) works in dev mode. *Source: API error during build.*
- **v26 API quirks:** campaigns need `is_adset_budget_sharing_enabled`; `video_3_sec_watched_actions` field removed → use `video_play_actions`; automated-rule purchases field = `result`, `spent` in cents; can't set `start_time` on an already-started ad set (1487057) → recreate the ad set to schedule. *Source: API errors.*
- **Bidding:** stay on **lowest-cost (auto)** until ≥50–100 conversions + stable 7–14d CPA + ~5 conv/day + moving to scale; cost cap **backfires on learning-limited** accounts; bid cap ≈ never for a $30–100/day operator. *Source: research agent — Meta-official learning phase + strong consensus.*
- **Methodology is two-speed:** leading indicators kill fast (before 1× CPA) on the **combination** hook<20% + link-CTR<0.8% + 0 ATC; CPM is context (not standalone), CPC a symptom; the **3–4 day wait is for judging winners/ROAS, not obvious duds.** *Source: doc Part 2/3.*
- **Ad copy must be line-break scannable, never a paragraph** — enforced in the uploader. *Source: user feedback.*
- **`/schedule` routines run REMOTE (cloud)** → can't reach the local `.env` token or unpushed engine → chose **on-demand** performance pulls (user pings "check MJ4U"). *Source: schedule-skill docs.*

## Next session — TODO
1. **First real read: tomorrow afternoon (~2–3pm GMT+7).** User says "check MJ4U" → run `engine/run.py` (read-only) and summarize. **Don't judge before 3–4 days** (learning noise); fast-kill handles obvious duds.
2. **User manual to-dos (non-blocking):** (a) point floor-rule **notifications to own account** (currently the system user); (b) eyeball the 2 pause rules show **$114/$115** not $11,500 (cents-units check); (c) **rotate token + app secret** (briefly in chat) before long-term unattended use.
3. **Recommended:** freelancer fixes the pixel to send **order total incl. shipping** → then flip `reported_value_per_order` to 59.93 (ROAS → 1.57×).
4. **Hands-off later:** after a 3–4-day dry-run soak, cron `run.py` daily + `execute.py --live`; leading-kill speed = run cadence (run more often for within-hours).
5. **Not-yet-built structural builders (documented gaps):** Stage-1 multi-audience variant (3–5 ad sets); CBO/Advantage+ **scale-campaign** builder (horizontal scale is manual for now).
6. **Optional:** wire the AI Film Studio's ad-copy step to emit `ad-content.json` directly, so new products flow into the uploader with zero reformatting.

## Where things live
- **Domain:** `marketing/facebook-ads/` — `README.md` (architecture) · **`HOW-TO-USE.md` (operator manual — start here)** · `setup/01-03` guides · `engine/`
- **Engine:** `engine/{run,execute,floor_spec,upload_draft,meta,meta_write,economics,rules,report}.py` + `config/{products,thresholds,floor_thresholds,execution}.json`
- **Secrets (gitignored):** `marketing/facebook-ads/.env` (token + IDs); live campaign IDs in `reports/mj4u-111-live-ids.txt`
- **Methodology source:** sop-docs `Internal-Guidelines/Kien-thuc-chuyen-mon/Marketing/Facebook-Testing-Scaling-Research.md`
- **Memory:** `fb-ads-automation.md`, `ad-copy-linebreak-format.md`, `product-tracker-and-sheet-sync.md`

## Commit
- `c23667d` on `product-research` (pushed to `origin` = github.com/neokahu/madejustforyou). Single repo — sop-docs methodology doc was only read, not modified.
