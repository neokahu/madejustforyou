# Sprint Report — Grandparents Day 2026

- **Occasion:** Grandparents Day — **Sun Sep 13, 2026**
- **Start-selling by:** 2026-07-13 · **Hard last-order:** 2026-08-30 (mfg + 14-day ship)
- **Run date:** 2026-07-10 · **Stages:** Discover (search + marketplace) → Score
- **Data pulled live:** Ahrefs Keywords Explorer (US) · Apify `yumitori/etsy-listings-scraper` (in-cart velocity, US)
- **Not pulled this round:** Pinterest/TikTok social signal → `social` sub-scores are *inferred* (flagged in every DB row). Recommend a follow-up social pull before finalizing creative.

Scored rows live in [`../templates/idea-database.csv`](../templates/idea-database.csv) (`occasion = grandparents day`); regenerate with [`score_gpd.py`](score_gpd.py).

---

## Headline findings

1. **Grandma demand ≈ 2.4× grandpa.** "gifts for grandma" **12,000/mo** vs "gifts for grandpa" **4,900/mo** (US). Weight the catalog toward grandma.
2. **SEO competition is negligible** — keyword difficulty **0–3** across virtually every term. Ranking is easy; the fight is on ads/marketplace, not SEO.
3. **Personalization is where the money is** — "personalized gifts for grandma" (1,100, *transactional*), and **jewelry carries the highest buyer intent** (CPC $1.20–1.70 on "personalized grandma jewelry / birthstone gifts for grandma").
4. **Two mega-themes dominate Etsy carts:**
   - 🌸 **Birth flower + "a flower/stone per grandchild"** — the #1 hot item overall was a personalized birth-flower piece (**752 in cart**). Shows up on suncatchers, sweatshirts, tumblers, pillows, garden stones.
   - 🍢 **Grandpa = grilling** — the #1 grandpa item was a personalized grilling board (**793 in cart**). Aprons/boards/plates with grandkids' names.
5. **The "new grandparent" milestone is a distinct, hot buyer** — "Promoted to Grandma", **"First Dad Now Grandpa" (178 in cart)**, "Grandpa Est. 2026", pregnancy-announcement framing. High emotion, clear trigger.
6. **Nicknames matter** — Gigi / Nana / Mimi / Grammy / Oma / Abuela and Papa / Poppy. Build these as variants, not separate designs.

---

## Ranked shortlist (composite score)

| # | Score | Status | Idea (hook) | Product | Why |
|---|:-----:|--------|-------------|---------|-----|
| 1 | **4.24** | 🟢 greenlit | Grandma + grandkids' names / "Promoted to Grandma" | mug | Highest blended demand; cheap POD; proven carts |
| 2 | **4.15** | 🟢 greenlit | Grandma's Garden — a birth flower per grandchild | sweatshirt | Rides the #1 Etsy theme + birth-flower Pinterest trend |
| 3 | **4.03** | 🟢 greenlit | First Dad, Now Grandpa | mug | Top grandpa cart-velocity; clear milestone trigger |
| 4 | 3.99 | backlog | A birthstone for every grandchild | necklace | Highest buyer-intent CPC; jewelry = higher margin, more POD complexity |
| 5 | 3.91 | backlog | Nana's Garden tumbler | tumbler | Birth-flower on higher-AOV durable item |
| 6 | 3.90 | backlog | Grandma's woven family blanket | blanket | Premium AOV, strong gift; heavier ship |
| 7 | 3.82 | backlog | Grandma's Garden — where love grows | pillow | Birth-flower home decor |
| 8 | 3.78 | backlog | Grandpa's Grilling Crew + kids' names | apron | Grilling is grandpa's top theme (793 cart) |
| 9 | 3.69 | backlog | Grandpa Est. 2026 | cap/hat | New-grandpa milestone |
| 10 | 3.64 | backlog | "In a world full of grandmas, be a Mimi" | t-shirt | High demand but **saturated** (compgap=2) |
| 11 | 3.63 | backlog | Best Papa Ever + photo | t-shirt | Photo personalization, 290 cart |
| 12 | 3.49 | backlog | Grandkids make life grand | wood sign/canvas | Photo + names decor |
| 13 | 3.40 | backlog | Life is better at Gigi & Poppy's | doormat | Proven category, bulky ship |
| 14 | 3.15 | backlog | "You're not my grandkids" (funny) | t-shirt | Shareable but generic; low giftability |

> Note #10: "Mimi" tee has the 2nd-highest *demand* (4.3) but drops on composite because the niche is **saturated** and margin is thin — exactly the kind of trap that pure competitor-spying walks into. The rubric routes budget to #1–3 instead.

---

## Recommended action — this week

**Brief these three greenlit ideas now** (fill [`../templates/design-brief.md`](../templates/design-brief.md)):

1. **GPD01 — "Grandma's Crew" mug**, grandkids' names, nickname variants (Grandma/Gigi/Nana/Mimi). Cheapest test, biggest demand.
2. **GPD02 — "Grandma's Garden" sweatshirt**, one birth flower per grandchild + names. Highest-AOV of the three; ride the birth-flower trend while it's hot.
3. **GPD07 — "First Dad, Now Grandpa" mug**, grandkids' names + est. year. Covers the grandpa side with the proven milestone angle.

**Then validate** with [`../templates/experiment-card.md`](../templates/experiment-card.md):
- **Tier 1 (now):** Pinterest + TikTok organic mockup posts for all three (also fills the missing social signal cheaply). Watch saves/comments 48–72h.
- **Tier 2 (by ~Jul 20):** $20–50 Meta/TikTok per concept → product page; gate on cost-per-ATC vs mug/sweatshirt margin.
- Winners must clear validation and be production-ready before the **Aug 30** last-order date.

## Suggested next pulls to tighten this
- **Pinterest/TikTok** velocity for "birth flower grandma" and "grandma sweatshirt" to replace the inferred social scores.
- **Competitor diff** (macorner / wanderprints / wrappiness / almagems) `/new` + `/best-sellers` for their grandparent SKUs and any active ads.
- Etsy **review-growth** re-pull in ~1 week to confirm which of these are *accelerating* vs already-peaked.
