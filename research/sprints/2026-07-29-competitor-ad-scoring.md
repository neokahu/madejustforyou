# Competitor Ad Scrape + Scoring — 2026-07-29

**Tool:** WinningHunter MCP (`search_facebook_ads`). **Scored against** `research/new-ad-potential-scorecard.md` (PART 0 thresholds calibrated same day). **Reads only — 1000 credits untouched.** Days-running as of 2026-07-29.

**Crawl depth:** deep-paginated 3 competitors by top ad-rank and deduped to concept (product URL): **PFG 80 ads → 45 concepts · Macorner 80 ads → 78 concepts · Wander Prints (domain crawl) 18 ads.** Full auto-scored table: `2026-07-29-concept-scores-full.tsv` (133 concepts). Scorer: `research/tools/score_concepts.py`.

> **How scored.** Objective criteria auto-scored from real signals against calibrated thresholds — **A1** longevity (max days-running), **A7** price band, **A4/B2** active-ads growth. Judgment criteria (**A5** occasion durability, **A6/B7** differentiation) use transparent keyword heuristics — *first pass, human-review before spend.* **A3/B3 (Google Trends shape) NOT pulled** → track is a proxy (long-runner/mature-format = Evergreen; young + novel mechanic = Trending). Evergreen % is out of 60 (A1×3,A2×3,A5×2,A6×3,A4×2,A7×2; A2 fixed=3 = multi-seller template; A3 excluded).
>
> ⚠️ **Growth is seasonally inflated** (late-July Q4 ornament ramp) → A4/B2 read high across the board; treat as suggestive, not measured. **PFG price ≈ $24** assumed (WH captured only 2/20; matches known $18.99–27.99 tier). Macorner prices are real.

## Brand-level signals
| Brand | Domain | Active ads | Growth 1m | Longest runner | Concepts found |
|---|---|---|---|---|---|
| Personalized Family Gifts | trendingcustom.com | 1,621 | +1,846% | **468d** (best-dad baseball figure) | ~45 |
| Macorner | (macorner) | 519 | +159% | 329d (dog-memorial suncatcher) | ~78 |
| Wander Prints Unique Gift | wanderprints.com | 1,304 | +1,033% | 13d (top ad) | squishy + ready-made lines |

---

## TIER 1 — REPLICATE shortlist (Evergreen, score ≥85%, proven long-runners)

Every one is a **top-decile survivor** (well past the 90d cut) on a multi-seller template. Ranked.

| # | Concept (template) | Brand | Score | Max days | Price | Why it wins / mechanic |
|---|---|---|---|---|---|---|
| 1 | **Custom pet-portrait → phone case / mug / tote** (watercolor/sketch) | Macorner | 91% | 126 | $27–30 | Photo→art, **year-round, no occasion window**; runs across 8+ formats = deep template |
| 2 | **"Legend: Husband·Dad·Grandpa" custom family-name** (shirt/Hawaiian) | Macorner | 91% | 309 | $30–33 | Multi-name family; Father's Day + birthday recurring |
| 3 | **Pet memorial suncatcher / "always with you"** | Macorner | 91% | 314 | $27 | Memorial = year-round, high emotion, low competition on suncatcher format |
| 4 | **"Once a brother, always a brother" distance tumbler** | Macorner | 91% | 228 | $30 | Sibling bond, year-round; name personalization |
| 5 | **Custom bestie-photo trinket / jewelry dish** | Macorner | 91% | 224 | $30 | Photo + friendship; giftable, demoable |
| 6 | **Family-camping "making memories" doormat** | Macorner | 91% | 107 | $30 | Multi-name family, hobby niche, year-round |
| 7 | **Y2K couple heart-with-names LED light box** | PFG | 87% | **410** | ~$24 | **Most-proven concept in the set**; couple/anniversary year-round |
| 8 | **"Always with you sky" family-members memorial** (grandma/dad/kids/pets) | PFG | 87% | 286 | ~$24 | Multi-character family — **our exact Teeinblue conditional-logic/clipart strength** |
| 9 | **Daddy's-team baseball family-sitting poster** | PFG | 87% | 236 | ~$24 | Add each kid; sports-family evergreen |
| 10 | **Dog/cat memorial wooden car-visor clip** | Macorner | 87% | 329 | $25 | Memorial, year-round, cheap to build |
| 11 | **"Proud hero" couple nation-flag 2-layer wood plaque** (nurse/police/army) | PFG | 87% | 118 | ~$24 | Occupation + couple; strong niche pride angle |
| 12 | **Sibling/sisters-forever acrylic ornament** | Macorner | 87% | 300 | $17 | ⚠ low AOV, but 300d proven |

## TIER 2 — TEST-SMALL / watchlist (Evergreen 78–84%)

| Concept | Brand | Score | Days | Price | Note |
|---|---|---|---|---|---|
| Day-of-the-Dead pet (cardigan/wine tumbler) | Macorner | 89% | 299 | $37 | Seasonal (Oct) but premium AOV |
| "Adventure partners" couple **solar mason-jar light** | Macorner | 89% | 180 | $37 | Novel-ish light mechanic, couple, $37 |
| Birth-flower **book-lover wearable blanket hoodie** | Macorner | 89% | 298 | $50 | **Premium AOV**, hobby niche |
| "Gaming do-not-disturb" wearable blanket hoodie | Macorner | 89% | 294 | **$60** | Top AOV tier; gamer year-round |
| "F*ck Valentine's, love you everyday" **bottle lamp** | Macorner | 89% | 202 | $40 | Novel lamp mechanic, couple |
| Buffalo-plaid family runner rug | Macorner | 87% | 280 | $50 | Premium, Christmas-lean |
| Custom moon-phase **crystal-ball LED night light** ("our moon") | PFG | 82% | 189 | ~$24 | Novel mechanic; anniversary; low AOV as sold |
| "Professional grandma of grandkids" shirt / word-search | PFG | 82% | 189 | ~$24 | Multi-grandkid names = our strength |
| Snowman family/grandkids LED light box | PFG | 82% | 295 | $28 | Christmas; multi-name |
| Custom gingerbread-letter family-name (ornament/sweatpants) | Macorner | 82% | 284 | $27 | Christmas; multi-name |
| "We caught the best dad" baseball **custom action figure** acrylic | PFG | 82% | **468** | ~$24 | Longest runner overall; figure mechanic |
| Grandma-grandkids hugging **fridge magnet** | PFG | 78% | 94 | ~$24 | Multi-name; cheap build |
| Custom couple-photo **sketch line-art tumbler** | Macorner | 78% | 37 | $32 | Photo→lineart; newer |

## TIER 3 — TRENDING / novel-mechanic candidates (perishable upside — verify Trends first)

These are the *newer mechanics* worth an early test; most need a Google Trends / Exploding-Topics check (B3) and possibly a new supplier.

| Concept | Brand | Signal | Note |
|---|---|---|---|
| **Funny photo "squishy" keepsake** (dad-bod acrylic magnet, pet derp, visor clip) | Wander Prints | top ad 13d, brand +1,033%/mo | Novel photo→squishy mechanic + humor; **differentiated from our sentimental line** — flagship watchlist |
| **Kids'-names + birth-dates keepsake canvas** ("give them back to her, on the wall") | Cstm Canvas (trending pull) | $54.95, fresh | Same names-keepsake as our core but **~2× AOV** — pricing/AOV-lift test |
| Custom pet-portrait **jewelry dish** (trending variant) | Macorner | 20d, $32, +159% | Early format spin on the #1 evergreen (pet portrait) |
| DIY **book-nook kit** "my favorite place is next to you" | Macorner | 7d, $40 | Novel build; couple; unproven |
| "Our moon" moon-phase crystal-ball night light | PFG | novel mechanic | Also in Tier 2; trending if Trends confirms breakout |

---

## Concept-FAMILY view (angle × format — what to actually build)
The catalog collapses to a small **angle × format matrix**; replicate the *angle+mechanic*, re-skin across formats:

- **Angles that repeat & win:** grandma/grandkids (multi-name) · couple/anniversary · pet (portrait + memorial) · dad/grandpa "legend" · sibling/bestie · family-memorial ("always with you") · funny/naughty couple · hobby (gaming, books, guitar, camping).
- **Formats that repeat:** LED light box / night light · 2-layer wood plaque · acrylic ornament · photo→portrait product (case/mug/tote/dish) · doormat · car-visor clip · wearable blanket hoodie · poster · shirt/mug.
- **Highest-leverage for us (Teeinblue multi-name/photo core):** anything **multi-character family** (always-with-you, snowman grandkids, daddy's-team) and **photo→art** (pet portrait, couple sketch). These map 1:1 to Conditional Logic + Clipart.

## Decision gates still open (before spend)
1. **A3/B3 Google Trends** (5yr + 90d) on: personalized LED light box, custom pet portrait, memorial suncatcher, moon-phase night light, squishy keepsake. Confirms Evergreen durability vs Trending breakout.
2. **Margin ≥3× GATE** per concept — needs supplier costs (esp. LED lights, wearable-blanket hoodies, action figures, squishy — non-flat POD).
3. **AOV lever:** our tier is ~$24; Macorner sits $27–60 and PFG's premium concepts (blanket hoodie $60, canvas $55) prove the niche pays more — test higher-AOV formats.
4. Heuristic judgment scores (A5/A6) are first-pass — eyeball the Tier-1 list before committing.
