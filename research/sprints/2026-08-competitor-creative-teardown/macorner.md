# Macorner — Winning Creative Teardown

**Source:** WinningHunter MCP (Meta Ad Library index), US, page_type=products. Pulled 2026-08-13.
**Method:** search_facebook_ads (free reads) validated on LONGEVITY (days running) + creatives-per-landing-URL; scan_ad on the #1 longest-runner. get_ad_transcript attempted on top video but WinningHunter's video downloader returned `download_failed` (video not retrievable) — no verbatim VO/script captured. Visual hooks inferred from product name + copy + format, not from watching frames (FB preview CDN tokens were expired).

---

## 0. Brand / page confirmation (did NOT burn effort on wrong brand)

Landing-URL search `macorner.co` → **3,874 total indexed ads** (huge advertiser). Domains: `46338f-fd.myshopify.com` (primary) + `macorner.myshopify.com`. Pages seen in results, matching the brief's 5-page cluster:

| Page | Role (observed) |
|---|---|
| Macorner Home Decor | ornaments, suncatchers, apparel — biggest volume |
| Macorner | apparel, jewelry dish, sweatpants, blankets |
| Macorner Decor | ornaments, couple lamps, engraved belts/glass |
| Macorner Pet Lover Gifts | pet-loss suncatchers, dog mugs |
| MA Commerce Inc | overflow page for apparel (legend shirt) |

Confirmed the CONCENTRATE thesis: 3,874 ads is not broad SKU spraying — it's many creatives stacked on a small hero set, spread across multiple pages per hero (legend shirt alone runs across 3 Macorner pages).

---

## 1. Longevity-validated winners (min_days_running=200 → 771 ads qualify)

Sorted longest-running. "dup" = countActive (times WH saw the same creative). Days running derived from `started` → still live per `lastSeen`.

| # | Product (hero) | Fmt | Started | Last seen | ~Days | Page | Angle |
|---|---|---|---|---|---|---|---|
| 1 | **A Hug From Heaven, I'm Always With You — photo pillow** ($27.95) | video | 2023-11-10 | 2026-08-11 | **~1005** | Home Decor | Memorial / grief |
| 2 | Congrats On Being My Husband You Lucky Bastard — engraved leather belt | video | 2025-10-14 | 2026-08-10 | ~300 | Decor | Couple / humor |
| 3 | Mother's Day Gift For Mom — window suncatcher ornament | video | 2024-04-08 | 2026-07-28 | ~840 | Home Decor | Mom / love |
| 4 | Forever In My Heart — acrylic ornament (pet memorial) | video | 2024-08-17 | 2026-07-26 | ~710 | Decor | Pet loss |
| 5 | Pet Loss custom photo — ceramic ornament | video | 2024-09-15 | 2026-08-12 | ~700 | Pet Lover | Pet loss |
| 6 | Our First Christmas Married as Mr & Mrs — acrylic ornament | video | 2024-09-13 | 2026-08-04 | ~700 | Decor | Couple / occasion |
| 7 | A True Friendship Is A Journey — jewelry dish | video | 2025-10-29 | 2026-08-07 | ~290 | Macorner | Friendship |
| 8 | Photo Inserted I Am Always With You — acrylic ornament | video | 2024-09-25 | 2026-07-31 | ~690 | Macorner | Memorial |
| 9 | Video-game controller custom name — sweatpants | video | 2025-10-17 | 2026-08-12 | ~300 | Macorner | Novelty / personal-name |
| 10 | Basketball custom name/number — hooded blanket | video | 2024-11-15 | 2026-08-11 | ~640 | Macorner | Hobby / name |
| 11 | We're Yours No Returns Or Refunds — shirt (grandma/kids) | video | 2025-03-17 | 2026-06-24 | ~460 | Home Decor | Family / humor |
| 12 | Congrats On Being My Husband — engraved whiskey glass | video | 2024-08-14 | 2025-11-19 | ~460 | Decor | Couple / humor |
| 13 | I Licked It So It's Mine — engraved leather belt | video | 2026-01-05 | 2026-08-12 | ~220 | Decor | Couple / humor |
| 14 | Fuck Valentine's Day I Love You Everyday — bottle lamp | image | 2026-01-08 | 2026-08-01 | ~220 | Decor | Couple / edgy-humor |
| 15 | A Girl & Her Dogs Unbreakable Bond — mug (rank #11!) | image | 2025-10-24 | 2026-08-12 | ~300 | Pet Lover | Pet love |

**Format split:** ~85% VIDEO, remainder single IMAGE. No carousels among the longevity winners. Video is the default for Macorner scaling.

**The #1 asset (scan_ad on ad 3634209046813156):**
- `days_running: 1005`, `verdict: likely_scaling`, page fb_like_count **170,322**, performing_factor 40,442.
- Price $27.95. Single video. This memorial photo-pillow is the single most durable creative in the account — ~3 years live and still scaling.

---

## 2. Flagged heroes from prior intel — re-validated (corrections)

### 2a. "Legend Husband·Dad·Grandpa" family-name shirt — CONFIRMED hero, but category-wide
Product-name search returned **119 ads across MANY brands** (The Pawfect House, Best Family Ever, Godmerch, Newsvips, Thesunnyzone…). This is a **proven cross-market POD winner**, not Macorner-exclusive.
Macorner's own footprint on it: run across **Macorner Home Decor + Macorner + MA Commerce Inc**, ~10+ video creatives, started 2025-09-23, still live 2026-08-13. Video-led, dup counts up to 4 per creative.
Copy (verbatim, short + hashtag stack):
- "Not multitasking—just multi-legendary! 🔄🏆  #macorner #shirt #vintagevibes #grandpa #papa"
- "Wearing the legacy of the family he built 🤍  #macorner #familyfirst #dadlife #grandpalove #giftideas"

### 2b. "Mother & Daughter On The Moon" suncatcher — MISATTRIBUTED
Landing-URL search shows this specific moon suncatcher is run heavily by **Newsvips (13 creatives, 2024→2025)**, NOT Macorner. Macorner ran only **1** old creative (2024-03-20, ended 2024-10-07, on the legacy `macorner.myshopify.com` domain).
→ The 53.8M-organic-plays / "to the moon" engine belongs to Newsvips, not Macorner. Do not build the Macorner brief around it.
Newsvips copy pattern (direct-response, link in text): "Capture the love between mother and daughter with our Personalized Window Hanging Suncatcher Ornament! 🌙👩‍👧 Customize yours now: newsvips.com/H0325-02"

### 2c. Suncatchers ARE a Macorner engine — just different SKUs
Landing-URL `suncatcher` → 1,296 ads market-wide; Macorner owns a large slice. Macorner's live suncatcher winners are **memorial / pet-loss / mom**, not couple-moon:
- Loss Of Pet — suncatcher (5 dup, video, 2026-05-29)
- Mother's Day Gift For Mom — suncatcher (~840 days, #3 overall)
- "My Favorite Hello And My Hardest Goodbye" — dog-loss suncatcher (Pet Lover page)
- Girl & Her Dogs / Dog Mom & Her Dogs — suncatchers (2026 launches)

### 2d. Grandpa novelty apparel + high-rank mug — CONFIRMED
- "A Girl & Her Dogs Has Unbreakable Bond" mug — **within-brand ad_rank #11** (one of Macorner's strongest-ranked creatives), image, ~300 days, still live. Companion "A Man & His Dogs" mug also live.
- Engraved leather belts ("Lucky Bastard", "I Licked It So It's Mine"), whiskey glass, bottle lamps = a whole **edgy-humor couple/husband gifting line** that scales on both video and image.

---

## 3. Creative anatomy (what the ads actually are)

**Format:** short vertical VIDEO is the workhorse (product beauty-roll / hand-holding the personalized item / photo reveal). Single IMAGE used for humor/novelty SKUs (belts, mugs, lamps) where the joke text on the product IS the hook.

**On-image text = the product's own engraved/printed text.** Macorner doesn't overlay marketing headlines; the personalization line printed on the product does the selling ("Legend Husband Dad & Grandpa", "I Licked It So It's Mine", "A Hug From Heaven"). The visual hook = the product close-up showing that line + a real photo/name inserted.

**Caption/description fields:** almost always `none`. All copy lives in the primary text (`copy`).

**Primary-text copy formula (verbatim structure):**
1. Line 1 = either the product's phrase as a title-case headline ("Congrats On Being My Husband You Lucky Bastard - Personalized Gift For Husband, Boyfriend") OR a one-line benefit/emotion hook with 1–2 emojis ("Who needs Valentine's Day when love is 365 days strong? 💘☕").
2. Blank line.
3. Dense hashtag stack, always led by **#macorner** + product-type + recipient + occasion (#giftforhusband #anniversarygift #valentinesday #grandpa #petloss …).

No price, no discount code, no urgency/countdown, no "50% off" in the primary text of the durable winners. Offer/urgency is carried on the landing page, not the ad. (One DR variant with an explicit link in copy exists but is the Newsvips style, not Macorner's durable format.)

**Emotional angles + mechanics (ranked by durability):**
1. **Memorial / grief** ("A Hug From Heaven", "Forever In My Heart", "I Am Always With You", pet-loss) — the #1 and several of the longest runners. Mechanic: photo/name insert → "the person/pet is still with you." Highest emotional payload, longest life.
2. **Family legacy / pride** (Legend Husband·Dad·Grandpa; "Wearing the legacy of the family he built") — names of all kids/grandkids printed → identity + status gift.
3. **Mom love** (Mother's Day suncatcher, "Mom We Love You" shadow box).
4. **Couple — edgy humor** ("Lucky Bastard", "I Licked It So It's Mine", "Fuck Valentine's Day") — printed joke IS the creative; scales on cheap image ads.
5. **Pet love** (girl & her dogs mug/suncatcher) — high within-brand rank (#11 mug).
6. **Hobby / name novelty** (basketball blanket, game-controller sweatpants) — custom name+number on a wearable.

---

## 4. Offer structure

- Ad-level: **no discount / urgency in copy.** Ads sell emotion + personalization; conversion mechanics deferred to LP.
- Price points on hero SKUs are low-mid: pillow $27.95; ornaments/suncatchers similar $20–35 band → impulse gift price.
- Distribution offer = **multi-page saturation**: same hero runs simultaneously across 3–5 Macorner FB pages (each page a different "brand face": Home Decor / Pet Lover / Decor), multiplying active-ad count and audience pools without new creative.

---

## 5. Data caveats
- `countActive` (dup) is WH's sighting count of one creative, NOT total ad-set size; treat as a coarse "how saturated" signal.
- Video transcripts could not be generated (WH downloader failed); VO/spoken-hook wording is not verbatim here.
- Days-running is derived from `started`→today; some creatives refresh (re-upload) so a single physical asset may span multiple entries.
- The prior intel's "Mother & Daughter On The Moon" hero belongs to **Newsvips**, not Macorner — corrected above.
