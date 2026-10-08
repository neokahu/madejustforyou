# Topic — Competitor research & ad scoring

**Status:** clone-shortlist (110 rows) and product tracker built; scorecard thresholds partly calibrated.

## Current decisions
- Count **active creatives per landing URL**, never by keyword. Validate on **longevity**, not seller count (`distinct_sellers` removed).
- Scorecard: Evergreen (~70%) + Trending (~30%) tracks; margin + differentiation beat raw competitor count.
- WinningHunter responses ~60KB → pull in batches ≤3, persist to disk, delegate to subagents; confirm exact page/entity before pulls.
- US spend/reach/demographics don't exist publicly.
- Page speed is not a competitive factor (Lighthouse 29–33 for winners).

## Key artifacts
- `research/method/new-ad-potential-scorecard.md`
- `research/sprints/2026-07-competitor-ad-scoring/` (`clone-shortlist-links.csv`, `concept-scores-full.tsv`, `wanderprints-deep-crawl.md`, `_recount/`)
- `research/sprints/2026-08-competitor-creative-teardown/`
- `products/_registry/product-tracker.csv` + Google Sheet `1BBO5WRBeBVQLkJI8l6zVBe2Ud1qzl7QOL7g5VS8ZoTE` (Claude sole writer; update both)

## Open items
- Margin ≥3× gate + cut-scores still uncalibrated against real sales.
- Pick new Phase-1 products from Tier-1 backlog (MJ4U-001…005 top-scored).

## Sessions
[2026-07-28](../../sessions/2026-07-28-winninghunter-ad-scoring-handoff.md) · [2026-07-31](../../sessions/2026-07-31-research-competitor-ad-scoring-gpd.md) · [2026-08-02](../../sessions/2026-08-02-competitor-ad-links-csv-PROBLEMS-and-data.md) · [2026-08-06](../../sessions/2026-08-06-video-ad-pipeline-and-repo-restructure.md) · [2026-08-14](../../sessions/2026-08-14-cro-diagnosis-speed-ruled-out-efficiency-kill.md)
