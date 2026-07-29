# Ad/Product Replication Methodology & Scorecard (personalized-gift POD)

**Evidence-based system to decide whether a competitor's ad/product concept is worth replicating**, across two tracks — **Evergreen** (durable, proven demand) and **Trending** (perishable, caught early). Inputs come from an ad-intelligence tool (WinningHunter); the *interpretation* of those inputs is grounded in the research cited below.

> **Confidence tags:** claims are cited. Thresholds are either cited or marked **[CALIBRATE]** with the method to derive them from your own data. High = multiple independent sources agree; Med = agree directionally, numbers vary; Low = weak/contested. **Overall framework confidence: Medium→High — the *logic* is well-triangulated, and as of 2026-07-29 the observable-signal thresholds (A1/A4/A7/B1/B2) are CALIBRATED to real niche data (see PART 0). Still un-validated: the margin GATE and the Decision-band cut-scores, which need your own win/loss outcomes + supplier costs.**

---

## PART 0 — DATA CALIBRATION (signal thresholds)  ·  *added 2026-07-29*

**What this is:** the observable-signal thresholds (A1, A4, A7, B1, B2) are now set from real niche data, not judgment. **Still pending your sales data:** the margin/3× GATE and the Decision-band cut-scores (PART 2) — those need your win/loss outcomes and supplier costs; unchanged here.

**Method:** count-based percentile calibration. Queried WinningHunter `search_facebook_ads` for the exact active-ad population in your competitive set and read the `total` count at each threshold. No sampling — these are full-population counts.

**Sample frame (held constant across all buckets):** niche = `GS` (Gift — the tag WinningHunter puts on tracked brand *Personalized Family Gifts*) · country = US · store tech = Shopify · language = English. **Base population = 414,776 active ads** (as of 2026-07-29).

**① Longevity survival curve** (drives A1 / B1):
| Days running | Ads reaching it | Share of base | Percentile |
|---|---|---|---|
| any (base) | 414,776 | 100% | — |
| ≥30d | 111,138 | 26.7% | top 27% |
| ≥60d | 63,788 | 15.3% | top 15% |
| ≥90d | 40,276 | 9.7% | **top 10%** |
| ≥180d | 17,319 | 4.1% | top 4% |
| ≥365d | 4,511 | 1.0% | top 1% |

→ **73% of gift ads die before 30 days.** 90 days = top-decile survivor → the strongest revealed-ROI cut. A1 score-3 set at ≥90d; B1 (trending, inverts) rewards <30d.

**② Price / AOV distribution** (drives A7), USD:
| Price | Ads ≥ it | Share | Read |
|---|---|---|---|
| ≥$25 | 273,924 | 66% | ~34% priced under $25 |
| ≥$40 | 186,631 | 45% | median ≈ **$38** |
| ≥$60 | 55,129 | 13% | premium tier = top 13% |

→ A7 score-3 at ≥$60 (premium AOV), 2 at $35–60 (around/above median), 0 at <$25 (thin-margin impulse tier). **Note:** our own brand's ads run **$18.99–$27.99 → at/below niche median**, competing in the low-AOV tier.

**③ Active-ads growth, 1-month** (spend-scaling proxy; drives A4 / B2):
| Growth ≥ | Ads | Share | Percentile |
|---|---|---|---|
| +25%/mo | 81,078 | 19.5% | top 20% |
| +50%/mo | 53,418 | 12.8% | top 13% |
| +100%/mo | 28,261 | 6.8% | top 7% |

→ "sharp scaling" = +50–100%/mo (top 13→7%). B2 score-3 at ≥+100%; A4 (evergreen, just needs *sustained*) score-3 at ≥+25%.

**Caveats:** (1) `GS` is WinningHunter's broad Gift tag — includes generic gifts, not only *personalized*; treat as the addressable competitive set, slightly wider than exact-template. (2) Counts are a point-in-time snapshot (2026-07-29); survival curve is cross-sectional (age of currently-live ads), a good proxy for true longevity but not a cohort-tracked one. (3) Growth % is a proxy for spend, not a spend measurement (PART 3 gap #2 stands).

---

## PART 1 — METHODOLOGY (principles)

**P1 · Unit of competition = the TEMPLATE (concept/angle/personalization mechanic), not the SKU.** In custom gifts, exact overlap is rare; competitors re-skin winning *concepts*. Judge saturation, demand, differentiation at the template level. Same-template competition is scored *differently per track* (validated demand for Evergreen; late/saturated for Trending); the escape hatch in both is a **better mechanic + design + offer**. Conf: Med. ([flashship](https://flashship.net/en/news/market-and-trends/the-personalized-gift-trend-why-it-continues-to-grow-stronger))

**P2 · Ad run-time is a real but imperfect profit proxy — the most-cited one.** Rational advertisers only keep paying while profitable, so long-lived ads reveal positive ROI ([adintime](https://adintime.com/en/blog/facebook-ads-library-the-ultimate-guide-to-winning-campaigns-n299), [Marpipe](https://www.marpipe.com/blog/mastering-the-facebook-ad-library)). Caveats (Conf Med–High): big brands subsidize losers for LTV; "active" ≠ "spending"; a *single creative* fatigues in ~1–8 weeks ([adlibrary](https://adlibrary.com/posts/facebook-ad-creative-refresh-frequency), [inBeat](https://inbeat.agency/blog/facebook-creative-fatigue)), so 90d+ longevity is really a **concept/template kept alive across refreshes** → template-level longevity > single-creative age. **Rule: runtime is necessary-not-sufficient; require a scaling co-signal before acting.**

**P3 · A scaling/winning ad shows via SPEND-PROXY GROWTH, not one metric.** Operators scale by raising budget on and duplicating winners ([Digital Darts](https://www.digitaldarts.com.au/scale-facebook-ads-shopify), [admetrics](https://www.admetrics.io/en/post/how-to-scale-facebook-ads)). We can't see budgets → **rising active-ads count + creative-variant count over 1w/1m are the spend-growth proxies.** Conf: Med.

**P4 · Saturation is real but MARGIN + DIFFERENTIATION dominate raw competitor count.** Across a 228-product dataset, competition level had ~zero correlation with margin (r=0.08) — high margins *attract* competitors; judge via a **margin × competition** lens + a **wow-factor shield**, not headcount ([productlair](https://productlair.com/blog/dropshipping-product-saturation)); differentiation beats saturation ([Circana](https://www.circana.com/post/how-do-you-make-your-brand-and-products-stand-out-in-saturated-markets)). Conf: Med–High. **Corollary:** for personalized gifts the mechanic *is* the differentiation, so a crowded-but-proven template is enter-able with a superior mechanic/design/offer.

**P5 · Evergreen vs Trending is diagnosed from the SHAPE of the Google Trends curve.** Use **5-yr view for seasonality/durability + 90-day for momentum** ([mydesigns](https://mydesigns.io/blog/google-trends-for-print-on-demand/)); seasonality is inferred from repeated YoY peaks ([Exploding Topics](https://explodingtopics.com/blog/google-trends-ecommerce)); rising/breakout = act before saturation ([Shopify](https://www.shopify.com/blog/how-to-use-google-trends-to-start-and-run-a-retail-business)). Conf: High.

| Trends shape | Track | Meaning |
|---|---|---|
| Flat/growing baseline + repeating annual peaks | **Evergreen** | durable; low risk |
| Steep recent rise, no multi-yr history (breakout) | **Trending** | perishable upside; enter early |
| Rise plateaued/rolling over | late | likely saturated; skip unless differentiated |
| Single spike, no repeat | fad | opportunistic only |

**P6 · Recurring "winning product" criteria = the base gate.** Cross-source checklist ([Dropified](https://www.dropified.com/blog/how-to-find-winning-dropshipping-products-in-2026-the-ultimate-niche-product-research-guide/), r/dropship): emotion/desire (**replaces "problem-solving" for gifts** — buying "a story, a memory" ([flashship](https://flashship.net/en/news/market-and-trends/the-personalized-gift-trend-why-it-continues-to-grow-stronger))), wow-factor, **margin ≥3× markup** [CALIBRATE to your costs], broad/passionate audience, giftable + visually demoable. Niche levers (Conf High): **occasion timing — start 4–6 wks pre-holiday** ([merchOne](https://merchone.com/blog/mothers-day-marketing/)); AOV bands — mug/apparel impulse tier vs jewelry 2–3× ([mydesigns](https://mydesigns.io/blog/mothers-day-print-on-demand/)) [CALIBRATE].

**Decision logic:** (1) pass the GATE → (2) classify track via Trends shape → (3) score on the track's card → (4) saturation judged at template level via margin×differentiation → (5) runtime needs a scaling co-signal → (6) differentiation plan mandatory to enter a crowded template.

---

## PART 2 — SCORECARDS  (each criterion 0–3 × weight)

### GATE — must pass before scoring
| Check | Signal | Pass | Basis |
|---|---|---|---|
| Emotion/wow | hook/transcript | clear emotional/scroll-stopping angle | flashship, Dropified |
| Margin ≥3× | your cost vs price | ≥3× markup **[CALIBRATE]** | Dropified |
| Giftable + demoable | product/creative | personalization visually demonstrable | merchOne, mydesigns |
| Buildable mechanic | Teeinblue | you can build ≥ parity | P1/P4 |

### SCORECARD A — EVERGREEN  *(long runtime & many competitors = GOOD)*
| # | Criterion | Signal | Score-3 | Wt | Basis |
|---|---|---|---|---|---|
| A1 | Ad longevity (proven ROI) | days-running of best ads | **≥90d=3** · 60–89=2 · 30–59=1 · <30=0 | 3 | **CALIBRATED (PART 0)** · adintime, Marpipe |
| A2 | Template persistence across sellers | store-discovery count | multiple stores, months = 3 | 3 | productlair (Med) |
| A3 | Evergreen Trends shape | 5-yr Trends | flat/growing + annual peaks = 3 | 3 | mydesigns (High) |
| A4 | Sustained spend proxy | active-ads growth 1m | **≥+25%/mo=3** · 0–25%=2 · declining=1 | 2 | **CALIBRATED (PART 0)** · admetrics |
| A5 | Occasion durability | angle → recurring occasions | multi year-round occasions = 3 | 2 | flashship (High) |
| A6 | Differentiation headroom | your mechanic/design/offer vs incumbents | clearly superior = 3 | 3 | productlair, Circana (Med–High) |
| A7 | Margin/AOV band | price vs niche median (~$38) | **≥$60=3** · $35–60=2 · $25–35=1 · <$25=0 | 2 | **CALIBRATED (PART 0)** · mydesigns, Dropified |

Red flags (downgrade): only ONE store runs it (A2=0); Trends rolling over (A3=0); no differentiation on a crowded template (A6=0).

### SCORECARD B — TRENDING  *(long runtime & many competitors = BAD/late; inverts A)*
| # | Criterion | Signal | Score-3 | Wt | Basis |
|---|---|---|---|---|---|
| B1 | Earliness/recency (are we early?) | days-running | **<30d=3** · 30–59=2 · 60–89=1 · ≥90=0 *(inverts A1)* | 3 | **CALIBRATED (PART 0)** · Marpipe, adlibrary |
| B2 | Scaling momentum | active-ads growth 1m | **≥+100%/mo=3** · 50–100%=2 · 25–50%=1 · <25%=0 | 3 | **CALIBRATED (PART 0)** · Digital Darts, admetrics |
| B3 | Breakout Trends | 90d Trends + Exploding-Topics | steep 90d rise / breakout = 3 | 3 | Shopify, Exploding Topics (High) |
| B4 | Not-yet-crowded | store-discovery count | **few** stores=3 · many=1 *(inverts A2)* | 2 | Shopify (Med) |
| B5 | Creative validation | lead advertiser's variant count + hook | iterating variants (committing budget) = 3 | 2 | causalfunnel (Med) |
| B6 | Occasion timing fit | days to occasion | 4–6 wks runway=3 · past window=0 | 2 | merchOne (High) |
| B7 | Emotion/wow + differentiation | hook + your mechanic | strong hook you can match/beat = 3 | 2 | flashship, productlair (Med–High) |

Red flags (auto-skip): old ads + many competitors (late); Trends plateauing (B3=0); occasion window passed (B6=0).

### Decision bands — **[CALIBRATE] (no source gives validated cut-scores)**
Method: score your **last ~20–30 launched concepts** retrospectively, tag each win/breakeven/loss from your own sales data, then set the "Replicate" cut at the score that best separated historical winners (start: winner-precision-maximizing cut; better: logistic regression to re-weight criteria). Until then, provisional:
- **Replicate now:** top tertile **and** zero auto-flags.
- **Test small / watchlist:** middle tertile, or high score with one soft flag.
- **Skip:** bottom tertile or any auto-skip flag.

**Highest-value calibrations:** (1) real margin/3× gate from supplier costs; (2) runtime thresholds A1/B1 — 60–90d is cited but Meta-wide; measure your niche's real longevity curve from concepts observed start-to-finish in WinningHunter.

---

## PART 3 — BIGGEST EVIDENCE GAPS (be honest)
1. No independent quantification that "still running after N months = profitable" — it's a repeated *revealed-preference* inference (vendors have incentive to promote Ad-Library use). Direction: High; specific day-count: Low → **calibrate A1/B1 from your own data.**
2. Active-ads count → spend is a **proxy, not a measurement** (WH shows counts, not budgets) → treat B2/A4 as suggestive.
3. The r=0.08 saturation finding is one vendor's 228-product sample → trust direction (margin > count), not the coefficient.
4. Thresholds un-validated for this bespoke rubric → **back-testing against your last 20–30 concepts is the #1 upgrade** (turns "evidence-informed" into "evidence-calibrated").
5. Niche AOV/margin figures are illustrative POD-blog numbers → replace with real supplier costs + store AOV.

## PART 4 — SOURCES (used)
Longevity/fatigue: adintime, [Marpipe](https://www.marpipe.com/blog/mastering-the-facebook-ad-library), [adlibrary](https://adlibrary.com/posts/facebook-ad-creative-refresh-frequency), [inBeat](https://inbeat.agency/blog/facebook-creative-fatigue), Meta Business Help. Scaling: [Digital Darts](https://www.digitaldarts.com.au/scale-facebook-ads-shopify), [admetrics](https://www.admetrics.io/en/post/how-to-scale-facebook-ads), causalfunnel. Saturation: [productlair](https://productlair.com/blog/dropshipping-product-saturation) *(best single source — real 228-product data)*, [Circana](https://www.circana.com/post/how-do-you-make-your-brand-and-products-stand-out-in-saturated-markets). Trends: [Exploding Topics](https://explodingtopics.com/blog/google-trends), [Shopify](https://www.shopify.com/blog/how-to-use-google-trends-to-start-and-run-a-retail-business), Glimpse, [mydesigns](https://mydesigns.io/blog/google-trends-for-print-on-demand/) *(most on-point for POD)*. Winning-product criteria: [Dropified](https://www.dropified.com/blog/how-to-find-winning-dropshipping-products-in-2026-the-ultimate-niche-product-research-guide/). Niche: [flashship](https://flashship.net/en/news/market-and-trends/the-personalized-gift-trend-why-it-continues-to-grow-stronger), [merchOne](https://merchone.com/blog/mothers-day-marketing/), [mydesigns Mother's Day](https://mydesigns.io/blog/mothers-day-print-on-demand/).

> WinningHunter = the tool that supplies the signals (days-running, active-ads growth, variants, store discovery, exploding topics, hooks). Run pulls with native `mcp__winninghunter__*` after a session restart. Ties to `research/tools/winninghunter-*`.
