# Topic — FB-ads automation + MJ4U-111 (Grandma's Garden candle warmer)

**Status:** engine built; MJ4U-111 ads-live since 2026-08-09 with 0 purchases; problem = cart→checkout cliff.

## Automation (marketing/facebook-ads/)
- Own Business app `870397309486973`, system-user non-expiring token; ad account `act_725748819027455`; pixel `1565119432072485`.
- Engine: `engine/run.py` (read-only call sheet), `execute.py` (guardrailed writes, dry-run default), `sensitivity.py` (funnel tracker), `rules.py` + `config/thresholds.json` (incl. efficiency-kill), `upload_draft.py` (enforces line-break copy).
- Native floor rules A/B/C live. Secrets in gitignored `.env`; IDs in `reports/mj4u-111-live-ids.txt`, `reports/mj4u-111-split-ids.json`.

## MJ4U-111 state
- Split into 2 ad sets: `dr-benefit` $30/day + `emo-thesis` $20/day; `count-us-all` retired.
- GA4: ~100% mobile, 83–100% bounce <10s, 1 ATC/33 sessions, 0 checkouts.
- Economics: pixel reports $49.94 (excl. $9.99 ship); break-even CPA ≈ $38.13; Meta-basis BE ROAS ≈ 1.31×.

## Decisions
- **Page speed is NOT the bottleneck** (Macorner 29/100, Wander Prints 33, us 33).
- Creative direction reversed to competitors' **product-reveal** format (memory `ad-style-thai-emotional-film`).
- Meta in-day metrics inflate then settle down — act only on settled days.
- Stay on lowest-cost bidding until ≥50–100 conversions.

## Open items
- Build product-reveal creative (static + 6-slide carousel); compare-at price + reviews/social proof; freelancer pixel fix (order total incl. shipping → 59.93).

## Detail
- `marketing/facebook-ads/HOW-TO-USE.md` · `README.md` · `products/MJ4U-111-grandmas-garden-candle-warmer/{mobile-cro-brief.md,theme-handoff-01-mobile-speed.md,report/}`
- MJ4U-111 report: https://mj4u111-report.pages.dev · GA4 property 546131581 (memory `ga4-mcp-setup`)
- Sessions: [2026-08-09](../../sessions/2026-08-09-fb-ads-automation-and-mj4u111-launch.md) · [2026-08-14](../../sessions/2026-08-14-cro-diagnosis-speed-ruled-out-efficiency-kill.md) · [2026-08-06](../../sessions/2026-08-06-video-ad-pipeline-and-repo-restructure.md)
