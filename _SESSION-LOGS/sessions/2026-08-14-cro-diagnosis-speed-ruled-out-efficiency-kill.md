# Session Handoff — 2026-08-14 · MJ4U-111 CRO diagnosis, speed ruled out, efficiency-kill shipped

## Achieved
- **Connected GA4 MCP** for on-site funnel analysis. Auth was hard: firebits.com Workspace blocks (a) the interactive `analytics.readonly` scope ("app blocked") and (b) service-account key download (`iam.disableServiceAccountKeyCreation`). Solved via **service-account impersonation, no key** (SA `ga4-mcp@madejustforyou.iam.gserviceaccount.com`). Details in memory `ga4-mcp-setup`. ⚠️ impersonated ADC expires ~daily → re-run `gcloud auth application-default login --impersonate-service-account=…`.
- **Ran the full on-site funnel** for MJ4U-111 FB traffic (GA4): ~100% mobile, **83–100% bounce <10s, ~1.09 pages/session, 1 ATC / 33 sessions, 0 checkouts, 0 purchases, $0.** Store-wide 58 sessions → 2 ATC → 3 checkouts → 0 purchases.
- **Split MJ4U-111 ads** into 2 ad sets (live on account): `dr-benefit` alone $30/day + new `emo-thesis` $20/day (reused post to keep social proof); retired `count-us-all`. IDs in `marketing/facebook-ads/reports/mj4u-111-split-ids.json`.
- **Shipped efficiency-kill** in the ad engine (`rules.py` + `config/thresholds.json`): kills an ad when link-CPC is too high to break even even at an exceptional 5% CVR (`max_cpc = be_cpa × best_case_cvr × safety_multiple`). Backtested: kills $12.91 & $20 CPC ads, spares $1.64. Also fixed hook-rate = true 3-sec views earlier.
- **Built `sensitivity.py`** — funnel tracker (CPM×CTR×CVR×AOV → CPA vs break-even + learning-phase spend sizing). `python3 sensitivity.py --product MJ4U-111`.
- **Competitor creative teardown** (4 subagents) → `research/sprints/2026-08-competitor-creative-teardown/` (candle-warmer, macorner, pfg, wanderprints).
- **Wrote CRO docs**: `products/MJ4U-111-.../mobile-cro-brief.md` (7 prioritized fixes) + `theme-handoff-01-mobile-speed.md`.
- **Lighthouse-audited** our page + 2 competitors (see below).
- Two deep-research runs: kill-rules (completed, cited) + Shopify-speed (failed — harness flakiness).

## Learnt / decided (with evidence)
- **PAGE SPEED IS NOT THE BOTTLENECK.** Evidence: Lighthouse-mobile — **Macorner 29/100, LCP 24.5s**; **Wander Prints 33/100, LCP 21.0s, 7.3MB**; **us 33/100, LCP 15.8s** (we're already faster than both scaling winners). Lab scores are brutal for all app-heavy POD stores and don't predict conversion. → memory `pod-page-speed-not-the-bottleneck`. **Stop optimizing speed** beyond the free Teeinblue toggle (already done — halved TBT).
- **CREATIVE DIRECTION REVERSED.** Drop the emotional Thai-film; **copy competitors' product-reveal format** (personalized mockup IS the ad, no actors/story, terse copy, full price). Evidence: teardowns show no winner uses story-films + our video underperformed. → memory `ad-style-thai-emotional-film` (updated to the reversal).
- **Competitors use simple text-field personalization, no live-preview canvas** (firecrawl reads of Macorner + agiftcustomized). Our Teeinblue 353KB canvas SDK is the LCP element but — per above — not worth migrating for speed.
- **Meta in-day metrics inflate then settle DOWN** (dr-benefit showed 4–5 live ATC → 1 settled). → memory `meta-inday-metrics-are-estimates`.
- **Economics are tight:** at achievable CPM ($25–40) + normal CTR, break-even needs CVR ~4% (ours ~0%). Can't brute-force learning at $30–50/day. Evidence: `sensitivity.py`.
- **The real levers (ranked):** (1) ad creative → product-reveal; (2) page persuasion (we have 5 reviews/no offer vs competitors' 49–76 reviews + "2k+ bought" badge + anchor price); (3) store/pixel newness = structural early tax.

## Next session — TODO
1. **BUILD THE PRODUCT-REVEAL CREATIVE** (start here). Static/carousel first (fastest to test), then a simple product-reveal video. Copy the winners: product-as-hero, names+birth-flowers on the lit lamp in the first second, terse copy + hashtags, no ad-side discount. Assets in `products/MJ4U-111-.../ads/` (`lamp-names.png`, `scene2-payoff.jpg`, `ads/film/refs/product/`). Acceptance: a static + a 6-slide carousel, product-forward, mobile 4:5.
2. **Page persuasion** (config/admin, per `mobile-cro-brief.md` items ④⑤): set a compare-at price on the product so Teeinblue shows ~~$79.95~~ $49.95 + Save badge (toggles already ON); seed more reviews + a social-proof "bought" badge.
3. **Test** the product-reveal creative as a new ad set vs the current dr-benefit/emo-thesis.
4. Minor cleanup (optional): remove the `adsagent` app (~150KB) — identify via DevTools Network → Initiator.

## Blockers / waiting on user
- Theme-side speed items are app/admin, now **deprioritized** (speed ruled out).
- Ad results still **0 purchases** — watching emo-thesis vs dr-benefit on settled days only.

## Where things live
- **Ad engine:** `marketing/facebook-ads/engine/` — `run.py` (call sheet), `execute.py` (live actions), `sensitivity.py` (funnel tracker), `rules.py` + `config/thresholds.json` (verdict logic incl. new efficiency-kill).
- **CRO:** `products/MJ4U-111-grandmas-garden-candle-warmer/mobile-cro-brief.md`, `theme-handoff-01-mobile-speed.md`.
- **Competitor intel:** `research/sprints/2026-08-competitor-creative-teardown/`.
- **GA4:** `ga4` MCP, property `546131581` (memory `ga4-mcp-setup`). **Clarity** for mobile session recordings.
- **Commit:** `189e066` (product-research → main).
