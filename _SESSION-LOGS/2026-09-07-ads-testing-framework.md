# Handoff — Ads Testing Framework (2026-09-07)

## Where we are
Building a scientific ad-testing framework (factor matrix + multi-stage elimination funnel + research-backed thresholds) for MadeJustForYou.

## ⭐ NEXT ACTION (do this first next session)
**Rebuild the framework Doc + Sheet from `marketing/facebook-ads/MATRIX-CORRECTION-design-unit.md`.**
The matrix was corrected: **the test unit is the DESIGN, not the product.** One design → many materials
(shirt/mug/rug/sweatshirt). See that file for the full corrected model (2 matrices, material as a new
test axis, buyer≠recipient, price consolidated into Offer, event=stage not axis).

Steps:
1. Rewrite **Part A** of `marketing/facebook-ads/TESTING-MATRIX-FRAMEWORK.md` per the correction file.
2. Fix Part B.1 factor-code references (P3/P4 → buyer/AUD; material added).
3. Re-export to the Google Doc **in place** (id `1zND10THgf_VohvNRgRl4hGhsOwPaXVt15eNhNaOdh-I`) via
   `update_drive_file` (stage md into `~/.workspace-mcp/attachments/` first — paths are sandboxed).
4. Rebuild the Google Sheet (id `1ZNZijKm5PJRkOj91A4DUGhAb-orvDOidyMNP627-k1w`): tabs = Design Profile /
   Factor Matrix (test axes) / Campaign Planner / Results Log / Thresholds / Stage-scope. Build xlsx with
   openpyxl (installed --user), stage in attachments, `update_drive_file` in place.

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
