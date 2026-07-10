# Stage 1 — Signal Sources (Demand Sensing)

Where ideas come *from*. The goal is to blend **leading** signals (predict demand) with
**lagging** signals (confirm demand) so you're early but not guessing. Each source lists what
it reveals, how often to check it, and the exact tool/query to pull it once automated.

Signal-to-idea flow: a signal becomes one or more rows in
[`templates/idea-database.csv`](templates/idea-database.csv) (status = `backlog`).

---

## Source scorecard

| # | Source | Lead vs Lag | Reveals | Cadence | Tool to automate |
|---|--------|-------------|---------|---------|------------------|
| 1 | Search demand | Lag→Lead | Real query volume, trend slope, related questions, difficulty | Weekly | Ahrefs Keywords Explorer; Semrush |
| 2 | Seasonal curves | Lead | When demand spikes → lead-time planning | Monthly | Ahrefs volume history; Google Trends |
| 3 | Marketplace velocity | Lag | What's *selling now* + how fast (review growth) | Weekly | Apify Etsy / Amazon actors |
| 4 | Social ideation | Lead | Emerging phrases, aesthetics, formats before search catches up | Weekly | Apify TikTok / Pinterest / Instagram actors |
| 5 | Competitor new-arrivals & ads | Lag | What rivals just bet on + what they're paying to push | Weekly | Firecrawl/Tavily; Meta & TikTok ad libraries |
| 6 | Voice-of-customer (reviews) | Lag | Unmet needs, gifting context, exact customer phrasing | Monthly | Apify review scrapers; own reviews |
| 7 | Internal store data | Lag (highest signal) | Own search queries, ATC/wishlist, bestsellers, support asks | Weekly | Shopify Analytics; site-search app |

---

## 1. Search demand — Ahrefs / Semrush

**Reveals:** whether real people already search for a combination, how big it is, and whether
you can rank. The backbone of the demand sub-score.

**How to use:**
- Seed queries from the dimension libraries: `personalized [recipient] [product]`,
  `custom [occasion] gift for [recipient]`, `[recipient] [product] with [personalization]`.
- Pull: **volume**, **trend / volume history**, **matching terms** + **related terms** (idea
  expansion), **questions** (angle & copy ideas), and **KD** (SEO difficulty).
- Watch the **slope**, not just the level — a smaller term rising fast beats a big flat one.

**Automate:** Ahrefs `keywords-explorer-overview`, `-matching-terms`, `-related-terms`,
`-volume-history`, `-search-suggestions`; cross-check with Semrush. Feed volume + slope
straight into the Idea Database `demand_*` columns.

## 2. Seasonal curves — volume history / Google Trends

**Reveals:** the shape of the year for each occasion/recipient so you can back-time production.
**How to use:** pull 12–24 mo volume history for the head terms; mark the month demand starts
rising and set the "lock design by" date backward from it (see occasion table in
`01-dimension-libraries.md`).
**Automate:** Ahrefs `keywords-explorer-volume-history` / `site-explorer-*-history`.

## 3. Marketplace velocity — Etsy & Amazon (Apify)

**Reveals:** what is *actually selling* (not just searched), and momentum. Etsy is the closest
analog to this business; Amazon shows mass-market pull.
**How to use:**
- Scrape category bestsellers + "new & rising"; capture **review count** and, on repeat pulls,
  **review growth week-over-week** as a sales-velocity proxy.
- Note listing age vs review count — young listing with fast reviews = a rising winner worth
  moving on quickly.
- Record the *angle and hook*, not just the product.
**Automate:** Apify Etsy scraper + Amazon Best Sellers / product scraper actors; diff pulls
over time to compute velocity.

## 4. Social ideation — TikTok / Pinterest / Instagram (Apify)

**Reveals:** the *earliest* signal — phrases, aesthetics and formats trend socially before
they show up in search or sales. Pinterest especially: high purchase intent + long seasonal
lead (people plan gifts/holidays there months out).
**How to use:** track gift hashtags/keywords, saves/engagement, and recurring visual motifs
and captions. A phrase that keeps appearing in captions/comments is a hook candidate.
**Automate:** Apify TikTok, Pinterest, Instagram scraper actors; rank by save/engagement rate.

## 5. Competitor new-arrivals & ads — Firecrawl / Tavily + ad libraries

**Reveals:** what rivals just committed to (their `/new` collection) and what they're paying to
scale (ad libraries = they've likely validated it). This is the *disciplined* version of
"spying" — a tracked weekly diff, not aimless browsing.
**How to use:**
- Scrape each competitor's **New Arrivals** and **Best Sellers** collections; diff vs last week
  to get only *what changed*.
- Check **Meta Ad Library** and **TikTok Creative Center / Ad Library** for their active ads —
  creatives running for weeks/months are validated winners; reverse-engineer the angle, not the art.
  **Active ads = present-tense spend**, so this is the one competitor signal with no recency gap.
- **Target profiles directly** for their real top content — a keyword search only shows what ranks
  for *your* query (keyhole bias); scrape the profile to see their actual best.
- Competitors: macorner.co, wanderprints.com, wrappiness.co, almagems.com.
**Automate (proven 2026-07):** Meta ads → Apify `curious_coder/facebook-ads-library-scraper`
(Ad Library keyword/page URLs); top organic → `clockworks/tiktok-scraper` with `profiles:[…]`,
sort=popular; storefront diffs → Firecrawl/Tavily on collection URLs. Store every creative/listing URL.

## 6. Voice-of-customer — reviews

**Reveals:** unmet needs and the *exact language* buyers use ("bought this for my mom who lost
her dog") — gold for angles and ad copy.
**How to use:** mine your own + competitor + Etsy/Amazon reviews for recurring gifting
contexts, complaints (= product/angle gaps), and phrasing. Feed phrasing into hooks & briefs.
**Automate:** Apify review scrapers; tag by recipient/occasion/angle.

## 7. Internal store data — your highest-signal, free source

**Reveals:** demand from people already on *your* site — the least noisy signal you have.
**How to use:** review **on-site search queries** (esp. zero-result searches = unmet demand),
add-to-cart/wishlist patterns, bestsellers, and repeated **support/CS requests** ("do you make
X for Y?"). These often beat any external signal.
**Automate:** Shopify Analytics exports + a site-search app (e.g. searchspring/searchanise);
pipe zero-result queries into the backlog automatically.

---

## From signal → backlog

For every notable signal, create an Idea Database row capturing: the dimensions it implies,
the **hook**, the **source — including the direct URL(s)** (a *required* field, not optional —
see principle #7), and any raw numbers (search volume, review velocity, saves).
Don't score yet — Stage 3 does that. The job here is volume and coverage: cast wide, cheaply.

**Reference-linking is a standard step at every stage:** when a listing, pin, video, or ad
informs an idea or concept, capture its URL then. Sprint concept docs must end with a
**"Reference examples"** section grouped by concept so anyone can open the real designs.
