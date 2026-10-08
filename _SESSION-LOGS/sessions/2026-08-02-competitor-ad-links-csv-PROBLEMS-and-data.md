# Session Handoff — 2026-08-02 · Competitor ad links CSV + the DATA + all problems

**Read this fully before touching `research/sprints/2026-07-competitor-ad-scoring/clone-shortlist-links.csv`.**
This session ended at **92% context** with a **likely-corrupted CSV** and an **unresolved counting flaw**.
Everything you need to rebuild/fix is here, including the raw pulled data (so nothing is lost).

---

## 0. TL;DR of where things stand
- Built a CSV of the **Tier-1 (12) + Tier-2 (13) = 25** competitor clone-concepts with, per row:
  `tier, concept, brand, score_pct, longest_creative_days, active_creatives_US, target_countries,
   product_link, eu_reach_PROXY, eu_spend_PROXY_usd, top_ad_started, brand_ad_library_US,
   per_product_ad_library_US, price, note`.
- **All 25 now have a verified product_link** (pulled live via WinningHunter `searchkeyword=landingurl`).
- **TWO UNRESOLVED PROBLEMS (fix next session):**
  1. **`active_creatives_US` column is WRONG** — it still holds the OLD July scored value (a paginated
     floor), NOT a clean per-landing-URL census. User (correctly) called this out. See §2.
  2. **The CSV file may be MALFORMED** — an earlier Python did an accidental double-`open()` write,
     and the final patch threw `IndexError` mid-write but a commit ran anyway. **Verify row integrity
     first** (`python3 -c "import csv;[print(len(r)) for r in csv.reader(open('clone-shortlist-links.csv'))]"`
     — every row must have 15 fields). If broken, **rebuild from §4 data below.**

---

## 1. PROBLEM: WinningHunter MCP responses are ~60 KB each → they blow up context
- Every `search_facebook_ads` call echoes a giant `allowed_apps`/`allowed_niches`/`filter_reference`
  catalog (~15k tokens) **regardless of result size**. ~4 calls = context warning; ~10 = near-exhaustion.
- Several calls **overflowed** and auto-saved to `…/tool-results/*.txt` — recover those with `jq`, e.g.
  `jq -r '.data[0]|"\(.product_url)|\(.countries|join(","))|\(.total_eu_views)|\(.total_eu_adspend)|\(.started)"' <file>`.
- **Mitigation for next time:** do these pulls in **small batches (≤3)**, and **persist extracted fields
  to disk immediately** after each batch (don't hold them in context). Or write a helper that runs the
  WH REST call outside the MCP layer. Consider running as a background task.

## 2. PROBLEM (the important one): how "active creatives" must be counted
User's exact complaint (valid): *"It should be based on same product links. If you count based on
keywords it makes no fucking sense."*
- **Good news:** the WH searches DO use `searchkeyword=landingurl` → they match the **product landing
  URL**, not ad text/keyword. So the *basis* is per-product. countActive is per-ad-record.
- **The flaw:** the CSV's `active_creatives_US` number was copied from the **old `concept-scores-full.tsv`**
  (a paginated floor from the July scrape) — it was NOT recomputed from these fresh per-landing-URL pulls.
  So the column is inconsistent with the correct method.
- **CORRECT method (from `research/method/new-ad-potential-scorecard.md` §PART 0):** for a product, group
  the landing-URL search results and split into TWO numbers:
  - **A4/B2 scaling = Σ `countActive`** for ads on the **same exact landing URL AND same
    `shopify_shopifydomain`** (the lead seller). This is "how hard the lead seller is scaling it."
  - **A2 validation = count of DISTINCT `shopify_shopifydomain`** running that product (copycat sellers).
- **Gotcha:** a `landingurl` substring search also returns (a) product **variants** (e.g. couple-sketch:
  `…-tumbler-cup-ma794l1gn` vs `…-wine-tumbler-ma4u9rq0x`) and (b) **copycat sellers** (macorner +
  heartmelting + bakven + geckocustom + nanyshop + cigreds + suzitee + bakven). Do NOT lump these into
  one "active" number — split lead-seller-scaling vs distinct-sellers.
- **Fix next session:** recompute `active_creatives_US` per row = Σ countActive for the lead seller's
  exact product URL, and ADD a new column `distinct_sellers` (A2). Raw per-row data is in §4.

## 3. PROBLEM: US spend / reach / demographics DON'T EXIST publicly (not a tool limit)
Asked repeatedly ("why only EU", "can we get age/gender/targeting"). The truth, confirmed empirically:
- Meta discloses **spend + reach + audience breakdown ONLY for (a) political/social-issue ads
  everywhere, and (b) ALL ads delivered in the EU** (EU DSA law, 2023). For **US commercial ads** Meta
  publishes **nothing quantitative** — no spend, no impressions, no reach, no age/gender. **No spy tool
  can get it** because Meta never releases it.
- So WH's `total_eu_adspend`/`total_eu_views` are **EU-only, used as a directional proxy** (same creative
  runs US+EU). The CSV labels them `_PROXY` on purpose.
- **US-valid signals you CAN rank on (all global):** `longest_creative_days` (longevity — the #1 proxy),
  per-landing-URL active-creative count (scaling), `distinct_sellers` (validation), target `countries`,
  and the actual live creatives via the per-product Meta Ad-Library **keyword search** link.
- **Apify engagement test (done, ~$0.002):** ran `constructive_calm/facebook-ad-library-pro` with
  `scrapeAdDetails=true`. Result: Ad-Library scrapers return creative/copy/CTA/dates/`page_like_count`
  but **NO reactions/comments/shares and NO age/gender** for commercial ads. Also its **keyword search
  is noisy** (a memorial query returned "Pocket FM" audiobook ads) — worse than WH's landingurl search.
  → Engagement is only obtainable via AdSpy/BigSpy's proprietary post-matching, still no US spend/demo.
- **AdSpy verdict: DON'T BUY.** ~$149/mo, no free trial; the one thing it adds (engagement) is
  gettable free-ish and doesn't break the US wall. If ever adding a 2nd tool, prefer **Minea (~€49,
  multi-platform incl TikTok)** or **BigSpy (cheap)** — and only once running weekly paid tests. The
  real bottleneck is EXECUTION (133-concept backlog, 1 built), not more spy data.

## 4. THE DATA — verified product links + per-landing-URL facts (USE THIS TO REBUILD CSV)
Format: `# | concept | brand | score | longest_creative_days | product_url | target_countries |
eu_reach_PROXY | eu_spend_PROXY | top_ad_started | notes(variants/copycats)`
Ad-library links are constructed: brand page = `…?view_all_page_id=<id>` (Macorner `102971998671051`,
PFG/trendingcustom `1562252470694113`); per-product = `…&q=<product words>&search_type=keyword_unordered`.

**TIER 1**
1 | Custom pet-portrait phone case | Macorner | 91 | 126 | https://macorner.co/products/custom-pet-portrait-personalized-leather-phone-case-ma4ddrzzh | US+CA/AU/NZ+EU | 1123460 | 12358 | 2026-03-25 | lead ~5 US creatives; copycat: cigreds.com
2 | "Legend Husband·Dad·Grandpa" family-name shirt | Macorner | 91 | 309 | https://macorner.co/products/legend-husband-dad-and-grandpa-custom-family-name-personalized-shirt-grd200504dohn | US+CA/AU/NZ | — | — | 2025-09-23 | variants: hawaiian -mauftaf9o, hoodie -grd221101nahn ($54.95); ~10 creatives across Macorner Home Decor/MA Commerce/Macorner Decor
3 | Pet memorial suncatcher "in loving memory" | Macorner | 91 | 314 | https://macorner.co/products/loss-of-dog-in-loving-memory-personalized-window-hanging-suncatcher-ornament-dog280502hutl | US | — | — | 2025-09-18 | 2 creatives; slug needs "suncatcher" (earlier 0-result was wrong slug)
4 | "Once a brother" distance tumbler | Macorner | 91 | 228 | https://macorner.co/products/once-a-brother-always-a-brother-no-matter-the-distance-personalized-tumbler-cup-sib081202dghn | US+EU | 67148 | 738 | 2025-12-24 | variants: pocket-hug -mai4qpprb, coin -maz50bgmo
5 | Custom bestie-photo jewelry dish | Macorner | 91 | 224 | https://macorner.co/products/custom-bestie-photo-trinket-tray-for-best-friend-friendship-thank-you-gifts-personalized-jewelry-dish-fri021205huhn | US+EU | — | 2826 | 2025-12-17 | copycats: geckocustom.com, nanyshop.com; variant: stemless-wine-glass -fri280101huhn
6 | Family-camping "making memories" doormat | Macorner | 91 | 107 | https://macorner.co/products/making-memories-one-campsite-at-a-time-family-camping-personalized-doormat-cam150401vuhn | US+CA+GB+NZ | 72948 | 802 | 2026-04-13 | copycat: cigreds.com
7 | Y2K couple heart LED light box | PFG | 87 | 410 | https://trendingcustom.com/products/y2k-couple-heart-shape-with-names-psnl-light-box-anniversary-gift-valentines-day-gift-for-him-for-her-12203492 | US+EU | 18935 | 208 | 2025-06-14 | most-proven in set
8 | "Always with you sky" family memorial | PFG | 87 | 286 | https://trendingcustom.com/products/always-with-you-sky-family-members-grandma-grandpa-dad-mom-kids-dogs-cats-memorial-personalized-acrylic-keychain-1311141 | US+EU(~33 ctry) | 99671 | 1096 | 2025-10-16 | lead ad countActive=18 (our Teeinblue strength)
9 | Daddy's-team baseball family poster | PFG | 87 | 236 | https://trendingcustom.com/products/daddys-team-baseball-family-sitting-psnl-poster-2201056 | US+CA+EU | 214748 | 2362 | 2024-05-30 | sold by "Perfect Gifts For Loved Ones" + PFG pages
10 | Dog/cat memorial car-visor clip | Macorner | 87 | 329 | https://macorner.co/products/dog-memorial-cat-memorial-personalized-wooden-car-visor-clip-pet180702laht | US+CA/AU/NO/BR/NZ | 1119 | 12 | 2025-09-03 | 2 creatives
11 | "Proud hero" couple nation-flag plaque | PFG | 87 | 118 | https://trendingcustom.com/products/proud-hero-couple-nation-flag-psnl-2layered-wooden-plaque-valentines-day-gift-for-couple-for-him-for-her-nurse-police-firefighter-army-01155141 | US+EU(~33) | 12420 | 137 | 2026-04-02 | nurse/police/firefighter/army angle
12 | Sisters/siblings-forever acrylic ornament | Macorner | 87 | 300 | https://macorner.co/products/sisters-siblings-forever-personalized-acrylic-ornament-xma021001vupg | US+NO+EU | 35286 | 388 | 2025-10-02 | ~6 creatives; variant: up-to-12 -xma091003vupg

**TIER 2**
13 | Day-of-the-Dead pet tumbler | Macorner | 89 | 299 | https://macorner.co/products/day-of-the-dead-dog-cat-hispanic-mexican-flowers-personalized-wine-tumbler-pet171001tvec | US | — | — | 2025-10-18 | variants: crewneck-cardigan -pet290804tvec, ugly-sweater -pet101003tvec, jewelry-dish -ma71y8p07; copycat: suzitee.com; ~9 creatives across variants
14 | "Adventure partners" solar mason-jar light | Macorner | 89 | 180 | https://macorner.co/products/adventure-partners-for-life-couple-gift-personalized-solar-mason-jar-light-cam291203ttnh | US+CA+EU | 184359 | 2028 | 2026-01-30 | (enamel variant is a different slug)
15 | Birth-flower book-lover blanket hoodie | Macorner | 89 | 298 | https://macorner.co/products/birth-flower-book-lovers-books-quotes-personalized-wearable-blanket-hoodie-boo280801paht | US+EU | 1114206 | 12256 | 2025-10-04 | huge EU proxy ($12k)
16 | "Gaming do-not-disturb" blanket hoodie | Macorner | 89 | 294 | https://macorner.co/products/im-gaming-do-not-disturb-personalized-wearable-blanket-hoodie-gam181101docy | US | — | — | 2025-10-08 | $59.95 top AOV
17 | "F*ck Valentine's" bottle lamp | Macorner | 89 | 202 | https://macorner.co/products/fuck-valentines-day-i-love-you-everyday-personalized-bottle-lamp-cou110102vupg | US+EU | 851289 | 9364 | 2026-01-08 | countActive 3; big EU proxy
18 | Buffalo-plaid family runner rug | Macorner | 87 | 280 | https://macorner.co/products/family-sitting-festive-plant-buffalo-plaid-personalized-runner-rug-xma200901tvec | (NOT re-pulled — from competitor-links.md) | — | — | — | re-pull to get countries/eu
19 | "Our moon" crystal-ball night light | PFG | 82 | 189 | https://trendingcustom.com/products/our-moon-the-night-we-got-married-psnl-crystal-ball-night-light-heartfelt-anniversary-gift-for-her-for-him-23106957 | US+EU | 65221 | 717 | 2026-02-13 |
20 | "Professional grandma of grandkids" shirt | PFG | 82 | 189 | https://trendingcustom.com/products/im-not-retired-im-a-professional-grandma-of-cute-grandkids-psnl-shirt-400520 | US+EU | 20345 | 224 | 2026-01-21 |
21 | Snowman grandkids LED light box | PFG | 82 | 295 | https://trendingcustom.com/products/snowman-grandma-and-grandkids-psnl-light-box-christmas-gift-for-grandma-91505378 | (NOT re-pulled — from competitor-links.md) | — | — | — | re-pull
22 | Custom gingerbread-letter family-name | Macorner | 82 | 284 | https://macorner.co/products/custom-gingerbread-letter-with-name-for-family-kids-personalized-family-wood-ornament-xma101001dghn | US+NO | 87 | 1 | 2025-10-18 |
23 | "We caught the best dad" baseball figure | PFG | 82 | 468 | https://trendingcustom.com/products/we-caught-the-best-dad-baseball-custom-figure-personalized-acrylic-block-plaque-fathers-day-gift-for-dads | US+EU | 8322 | 91 | 2025-04-17 | countActive 7; longest runner overall (468d)
24 | Grandma-grandkids hugging fridge magnet | PFG | 78 | 94 | https://trendingcustom.com/products/grandma-grandkids-hugging-psnl-acrylic-fridge-magnet-mothers-day-gift-for-grandma-mom-60405033 | US+EU | 56533 | 622 | 2026-04-26 | countActive 3
25 | Custom couple-photo sketch line-art tumbler | Macorner | 78 | 37 | https://macorner.co/products/custom-couple-photo-sketch-line-art-anniversary-gift-for-him-her-personalized-tumbler-cup-ma794l1gn | US+EU | 247255 | 2720 | 2026-06-22 | lead countActive 9; variant wine-tumbler -ma4u9rq0x; copycats: heartmelting.net, bakven.com

> `longest_creative_days` = per-product LONGEST single creative (max days-running), NOT account-level.
> Renamed this session from the confusing `days_running_US`. Account-level = `total_active_ads_on_page`
> (505–2886 for these brands) — do NOT use that for scoring (product-blind).

## 5. NEXT SESSION — exact steps
1. **Verify CSV integrity** (15 fields/row). If broken, rebuild from §4.
2. **Fix `active_creatives_US`**: recompute per row as Σ countActive for the lead seller's exact
   product URL; ADD `distinct_sellers` column (A2). Re-pull rows 18 & 21 (never re-pulled). Data source
   = WH `search_facebook_ads keyword=<slug> searchkeyword=landingurl country=US` (BATCH ≤3, persist each).
3. Commit the corrected CSV. (Repo = docs repo `madejustforyou`; merge product-research→main is safe,
   NOT a store deploy — that only applies to the separate theme repo.)
4. Then back to the real priority: **GPD02 build** (see `research/sprints/2026-09-grandparents-day/
   GPD02-garden-birds/STATUS.md`) — bird assets need bg-remove + anchor-place; flowers not generated;
   lamp legibility test pending.

## 6. Other things done this session (already committed, fine)
- `research/` folder **restructured** (method/ reference/ scripts/ calendar/ + per-sprint/per-concept
  folders); methodology renumbered 0–4; all cross-links fixed. See commit `a635edc`.
- **Bird library**: 10 assets generated + **prompts validated (v3)** — see
  `research/sprints/2026-09-grandparents-day/GPD02-garden-birds/2B-bird-library.md` §5a and `bird-gen/`.
  Raw PNGs are gitignored (Drive-synced). v3 prompt fixes: front-facing, no phantom perch, no paper
  border, tail tucked.
- **Lamp print spec** recorded in `…/GPD02-garden-birds/2A-flower-library.md` §0: continuous wrap
  31×5 cm → 3661×591 px @300 DPI, single-row garden border.

## 7. Meta process note (why sessions "forget")
Session memory does not persist automatically — **durable context lives in `_SESSION-LOGS/` (this file)
+ repo docs + `~/.claude/.../memory/`**. Always read the newest `_SESSION-LOGS/` file first. This handoff
is deliberately verbose so the next session has parity with this one.
