# Session Handoff — 2026-07-31 · Research: competitor ad scoring + Grandparents Day

Inherits from `2026-07-28-winninghunter-ad-scoring-handoff.md`. **This log = the research/concept/design thread only** (theme work is in a separate log same date).

## Achieved
- **Resumed the interrupted WinningHunter scrape+score.** Scored **133 competitor concepts** across PFG (trendingcustom), Macorner, Wander Prints → tiered Replicate/Test/Trending shortlist. Files: `research/sprints/2026-07-29-competitor-ad-scoring.md`, `…-concept-scores-full.tsv`, `…-competitor-links.md` (product + Meta Ad Library + TikTok links), tools `research/tools/score_ads.jq` + `score_concepts.py`.
- **FIXED the scorecard's scaling signal (A4/B2).** Was using brand-level `total_active_ads_on_page(_growth)` — product-blind & useless. Now **per-product active-creative count** (`sum(countActive)` over a product's `landingurl`). Recalibrated PART 0 (134 products: median 1, p90 4, max 18). See `research/new-ad-potential-scorecard.md`.
- **A2 seller count = distinct Shopify BACKEND DOMAIN, not page name** (one seller runs many pages: Macorner ran 5, PFG 2). Same-seller multi-page = *profitability* signal (A4/B2); distinct sellers = *validation* (A2).
- **Exact per-product census** on Tier-1 finalists (query each by `landingurl`): e.g. PFG "always-with-you memorial" = 18 creatives, "our-moon night light" = 21, Macorner Legend family-name = 18 across 4 real sellers.
- **Grandparents Day competitor spy** → `research/sprints/2026-09-grandparents-day-competitor-spy.md` (live FB winners, TikTok Shop trending, Personal Chic day-0 baseline). Folded refs into `2026-09-grandparents-day-concepts.md`.
- **Grandma's Little Birds layout spec** (1–10 birds, customer-picked clipart, count-scaling layout) → `research/sprints/2026-09-grandmas-little-birds-layout-spec.md`. Decisions locked: center-balanced, full 1–10, fixed grandma-bird anchor, names on.
- **Occasion sizing:** added an NRF spend-ranked tier list to `research/occasions-calendar.md` (Christmas ~$1T, Mother's $38B, Valentine's $29.1B, Father's $28B…).

## Learnt / decided (with evidence)
- **Grandparents Day is a MINOR gifting occasion** — NRF publishes no GPD spending survey; competitor winners ride Christmas/Mother's/Father's Day/Halloween; only 1 (Italian Charms) merchandised GPD by name; TikTok grandparent gifts peak at Mother's Day then cool. → Treat GPD as a **cheap September on-ramp**; grandparent demand is **evergreen**, monetizes hardest at **Christmas + Mother's Day**.
- **Lead GPD picks** (both scaling + validation fire, roster mechanic = our Teeinblue core): **"Always with you" family memorial** (PFG's hardest-pushed), **Legend Husband·Dad·Grandpa family-name** (Macorner 18 creatives/4 sellers), **Grammy/Nana roster sweatshirt** (triple-confirmed: FB + TikTok +46% + Etsy). Memorial "in heaven/always with you" = strongest emotional angle across all channels.
- **WinningHunter isn't broken** — its data is complete when queried by `landingurl`; only the track-by-domain resolver mis-picks sibling pages. Confirm exact page/entity before pulls. TikTok open-video search + Exploding Topics are dead ends for this niche (use TikTok Shop products; Pinterest via Apify).
- **"Little Birds" design has abundant refs** (Etsy "birds grandkids", roseinside plaque) but is **under-advertised on FB** — an opening.

## Tracked / tools
- **Personal Chic - Family Gifts** now in WinningHunter Brand Tracker (page_id `119529914438788`, personalchic.com) — grandparent-gift scaler to watch through GPD. (Custom Chic UK was a mistaken add; different brand.)

## Next
1. Pull Google Trends (5yr+90d) on Tier-1 mechanics + "grandparents day gifts" to firm the evergreen/trending split (A3/B3 still un-pulled).
2. Bird-library asset brief (8 birds, 520×520 feet-anchor) + Nano-Banana prompts; then spec the 2A "Grandma's Garden" side for the A/B.
3. Calibrate the margin ≥3× GATE + decision-band cut-scores from real supplier costs + sales (still un-validated).

## Where things live
- Scorecard: `research/new-ad-potential-scorecard.md` · Scored data: `research/sprints/2026-07-29-*`
- GPD: `research/sprints/2026-09-grandparents-day-*` + `2026-09-grandmas-little-birds-layout-spec.md`
- Occasions: `research/occasions-calendar.md`
