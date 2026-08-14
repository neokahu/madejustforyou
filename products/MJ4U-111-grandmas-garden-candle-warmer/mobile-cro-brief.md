# Mobile CRO Brief — MJ4U-111 Grandma's Garden Candle Warmer

**Page:** https://madejustforyou.net/products/grandmas-garden-love-grows-here-personalized-candle-warmer-49
**Owner of implementation:** theme freelancer (theme lives in the separate `shopify-theme-1` repo; merging to its `main` auto-publishes to the live store).
**Created:** 2026-08-13 · Source: GA4 funnel + live-DOM audit + competitor teardown.

## Why this exists (the problem, in numbers)
- **FB ad traffic is ~100% mobile** (30 mobile + 3 tablet, 0 desktop over Aug 9–12). The desktop page is irrelevant — optimize the **mobile** experience only.
- FB visitors **bounce 83–100% in <10 seconds**, view **~1.09 pages** (land on this page, leave — no browsing), **1 add-to-cart in 33 sessions, 0 checkouts, 0 purchases.**
- Store-wide over the ad window: **58 sessions → 2 ATC → 3 checkouts → 0 purchases → $0.**
- Per the funnel sensitivity model (`marketing/facebook-ads/engine/sensitivity.py`), at our achievable CPM (~$25–40) this product only breaks even if **CVR climbs from ~0% toward ~4%.** These changes target that.
- **Confirm with Microsoft Clarity mobile recordings** which first-screen issue (slow load vs. layout friction) hits first.

Economics: price $49.95 (+$9.99 ship = $59.93 revenue), break-even CPA ~$38.13.

---

## PRIORITY 1 — first-screen fixes (attack the <10-second bounce)

### ① Mobile page speed  ← MEASURED, this is the biggest problem
**Lighthouse MOBILE baseline (2026-08-13, Browserless):** Performance **30/100**. The page is catastrophically slow:

| Metric | Measured | Target | Verdict |
|---|--:|--:|---|
| **Largest Contentful Paint** | **17.1 s** | < 2.5s | 🔴 ~7× over — main content not painted for 17s |
| **Time to Interactive** | **25.8 s** | < 5s | 🔴 page frozen ~26s |
| **Total Blocking Time** | **4,470 ms** | < 200ms | 🔴 main thread blocked 4.5s |
| Speed Index | 9.0 s | < 3.4s | 🔴 |
| First Contentful Paint | 3.0 s | < 1.8s | 🟠 |
| Cumulative Layout Shift | 0.077 | < 0.1 | 🟢 (only bright spot) |
| Total page weight | **4,475 KiB (~4.4 MB)** | < 1.5MB | 🔴 |
| Main-thread work | 24.9 s | — | 🔴 |
| JS bootup time | 10.8 s | — | 🔴 |
| Server response (TTFB) | **10 ms** | — | 🟢 server is fine — problem is 100% front-end |

**LCP 17.1s alone explains most of the <10s bounce — half the visitors leave before the page even paints.**

**Named culprits (heaviest / most-unused resources):**
- **Teeinblue personalizer** `sdk.teeinblue.com/…/app-v1.js` — **353 KB (212 KB unused)** + heavy preview images (121/82/80 KB). Biggest single script, loads eagerly.
- **Tracking bloat — THREE Google tag containers** loading eagerly: `G-FY63Q735GJ` (GA4, 165KB), `AW-18336945415` (Google Ads, 153KB), `GT-MK5QW83V` (144KB) = **~460 KB, ~170 KB unused.**
- **"adsagent" app** `adsagentclientafd-*.azurefd.net` — 114KB + chunks (~150KB unused). Identify & remove if not needed.
- **Facebook pixel** `fbevents.js` 104 KB.
- Shopify checkout-web hydrate 198KB + hooks 91KB (Shopify's own).

**Change (in impact order):**
1. **Lazy-load Teeinblue** — don't load the SDK + preview images until the user taps "Personalize" (dovetails with item ③, which moves the personalizer down anyway). Single biggest win: ~470KB + main-thread work off the critical path.
2. **Consolidate/defer tracking** — 3 Google containers is excessive; consolidate to one GTM container and fire non-essential tags on a delayed/interaction trigger (or move to Shopify Customer Events / server-side). Defer FB pixel. Remove the "adsagent" app if unused.
3. **Images** — serve mobile-width hero (not 3840px), `preload` the LCP image, lazy-load everything below the fold.
4. **Reduce unused JS/CSS** (theme + apps).

**Acceptance:** re-run Lighthouse mobile → **LCP < 2.5s, TBT < 500ms, total weight < 1.8MB.**

### ② Emotional hero + benefit headline (message-match to the ad)
**Why:** first image is a generic mockup; H1 is the SKU-style product name — a cold, transactional jump from an emotional video ad → "wrong place, leave."
**Change:**
- First gallery image = **the lit lamp showing personalized names/flowers** (finished product, glowing amber), not a blank mockup.
- Add a one-line emotional benefit at/above the title.
**Copy (headline):** `One glowing bloom for every grandchild 🌸 — her garden, lit every night.`
**Acceptance:** within the first mobile screen (no scroll), visitor sees the finished personalized product + the emotional line, before any form field.

### ③ Remove upfront personalizer friction
**Why:** above the fold on mobile the visitor hits **required** `Choose Titles*` + `Number of Flowers* (1–10)` AND the warning *"You are responsible for supplying correct personalization information before hitting Buy Now"* — homework + a liability threat in the first 10 seconds.
**Change:**
- **Pre-select sensible defaults** (Title = Grandma, Flowers = 3) so it is never a blank required form.
- **Move the full personalizer below** images/benefit/price/reviews, behind a friendly button: `🎨 Personalize yours`.
- **Relocate/soften** the "you are responsible…" warning to the cart/checkout step, not the hero.
**Acceptance:** a visitor can see product + price + social proof without being forced to fill anything.

---

## PRIORITY 2 — perceived value + trust (convert those who survive the first screen)

### ④ Real offer / anchor price
**Why:** page shows "Sale price $49.95 / **Regular price $49.95**" — labeled "Sale" with **zero** discount = credibility gap. Anchor framing costs no margin.
**Change:** show a struck-through anchor + discount + soft urgency. E.g. `~~$79.95~~ $49.95 — 38% off, limited time.` (Competitor teardown: winners sell on emotion in the ad, put the discount/urgency on the page.)
**Acceptance:** a visible anchor price + savings near the buy button on mobile.

### ⑤ Trust above the fold
**Why:** only 5 generic reviews on a new store asking $50.
**Change:** push ★5.0 rating + 30-day guarantee + secure-checkout + payment badges up near the price; add more/UGC-photo reviews over time.
**Acceptance:** rating + guarantee visible within the first 1–2 mobile screens.

### ⑥ Sticky mobile Add-to-Cart bar
**Why:** on mobile the CTA scrolls out of reach.
**Change:** persistent bottom bar with price + "Add to Cart", always one tap away.
**Acceptance:** ATC bar stays pinned on scroll on mobile.

---

## PRIORITY 3 — nice-to-have

### ⑦ Delivery reassurance widget
**Why:** cosmetic; delivery time itself is standard for POD and is far down the page.
**Change:** replace the plain Order/Ship/Deliver text with a visual "Order today, get it by [date range]" + a progress bar (🖐 → 🚚 → 🎁), like competitor examples.
**Acceptance:** visual timeline present; low priority.

---

## Working order & status
Tackling **one at a time**, first-screen first: ① speed → ② hero/headline → ③ personalizer → ④ offer → ⑤ trust → ⑥ sticky CTA → ⑦ delivery.

| # | Item | Status |
|---|------|--------|
| ① | Mobile page speed | in progress |
| ② | Emotional hero + headline | todo |
| ③ | Personalizer friction | todo |
| ④ | Offer / anchor price | todo |
| ⑤ | Trust above the fold | todo |
| ⑥ | Sticky mobile ATC | todo |
| ⑦ | Delivery widget | todo |
