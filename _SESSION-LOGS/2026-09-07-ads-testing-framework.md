# Handoff — Ads Testing Framework (2026-09-07)

## Where we are
Building a scientific ad-testing framework (factor matrix + multi-stage elimination funnel + research-backed thresholds) for MadeJustForYou.

## ✅ DONE (2026-09-07 rebuild) — design-unit correction applied end-to-end
The matrix was corrected to **DESIGN as the test unit** and this is now LIVE everywhere:
1. ✅ **Part A** of `TESTING-MATRIX-FRAMEWORK.md` rewritten: Matrix 1 (Design Profile, fixed/log) +
   Matrix 2 (test axes M/AUD/A/O/R/D/F). Material=new axis; buyer≠recipient; price only in Offer;
   stage/event = funnel dimension not an axis.
2. ✅ **Part B.1 / Part D / Part E** patched to the new codes (P3/P4→AUD; material held in Stage 1,
   tested Stage 2–3; planner table uses M/AUD columns).
3. ✅ **Google Doc** re-exported in place (id `1zND10THgf_VohvNRgRl4hGhsOwPaXVt15eNhNaOdh-I`), title now
   English: "Ad-Testing Framework — Design-Unit Matrix + Staged Funnel".
4. ✅ **Google Sheet** rebuilt in place (id `1ZNZijKm5PJRkOj91A4DUGhAb-orvDOidyMNP627-k1w`), 6 tabs:
   Design Profile · Factor Matrix · Campaign Planner · Results Log · Thresholds · Stage Scope; title now
   English. Builder script: `scratchpad/build_matrix_sheet.py` (openpyxl).

## ⭐ NEXT ACTION (next session)
Method is documented + live. Next is to **USE it**: pick the first DESIGN (D-001 Grandma's Garden),
fill the Campaign Planner Stage-1 rows (creative × buyer, material held = shirt), launch on LPV, and log
into Results Log. Optional deferred: interactive DB + dashboard (Supabase + Cloudflare) once combos scale.

## Files (source of truth — all in repo, English)
- `marketing/facebook-ads/MATRIX-CORRECTION-design-unit.md` — the corrected model (apply this)
- `marketing/facebook-ads/TESTING-MATRIX-FRAMEWORK.md` — framework (Part A needs the correction)
- `marketing/facebook-ads/FB-ADS-PLAYBOOK.md` — general kill/scale/structure rules + sources
- `marketing/facebook-ads/AD-KILL-RULES.md` — kill/keep decision guide
- `marketing/facebook-ads/engine/build_fb_report_page.py`, `pull_atc_perf.py` — data pulls
- `products/MJ4U-111-grandmas-garden-candle-warmer/report/` — the MJ4U-111 mgmt report (deployed)

## Live artifacts (Drive / Cloudflare)
- Framework Doc: https://docs.google.com/document/d/1zND10THgf_VohvNRgRl4hGhsOwPaXVt15eNhNaOdh-I/edit
- Matrix Sheet: https://docs.google.com/spreadsheets/d/1ZNZijKm5PJRkOj91A4DUGhAb-orvDOidyMNP627-k1w/edit
- Playbook Doc: https://docs.google.com/document/d/1_5MddywFb-MM5KLrpmMoMSKXh6Qzx_RDdKHOZjCmuxw/edit
- MJ4U-111 report (Cloudflare): https://mj4u111-report.pages.dev

## Research already done (cited, in the framework)
- Caption design (Doc/skill built). Funnel benchmarks per stage (hook/CTR/ATC/CPA/ROAS) — folded into Part D thresholds.

## Key benchmark thresholds (Part D, already in doc)
Stage 1: hook <18% kill / >28% advance; link CTR >4% (Gifts). Stage 2: Shopify ATC <2% kill / >7.5% advance.
Stage 3: click→purchase <0.65% kill / >3.2% advance; ROAS vs break-even=1÷margin. $5–20 reads Stage 1 only.

## Open decisions for user
- Interactive DB + dashboard (Supabase + Cloudflare) when combos scale — deferred until method proven on Sheet.
- Rename Doc/Sheet titles to English (currently VN display names, English content).
