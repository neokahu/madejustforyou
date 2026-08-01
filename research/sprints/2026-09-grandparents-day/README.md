# Sprint Report — Grandparents Day 2026

- **Occasion:** Grandparents Day — **Sun Sep 13, 2026**
- **Start-selling by:** 2026-07-13 · **Hard last-order:** 2026-08-30 (mfg + 14-day ship)
- **Run date:** 2026-07-10 · **Stages:** Discover (search + marketplace + social) → Score
- **Data pulled live (all 3 signals):**
  - **Search** — Ahrefs Keywords Explorer (US)
  - **Marketplace** — Apify `yumitori/etsy-listings-scraper` (in-cart velocity, US)
  - **Social** — Apify `automation-lab/pinterest-scraper` (saves + theme volume) + `clockworks/tiktok-scraper` (plays/saves/shares)

Scored rows live in [`../templates/idea-database.csv`](../../templates/idea-database.csv) (`occasion = grandparents day`); regenerate idempotently with [`score_gpd.py`](../../scripts/score_gpd.py).

---

## Headline findings

1. **Grandma demand ≈ 2.4× grandpa.** "gifts for grandma" **12,000/mo** vs "gifts for grandpa" **4,900/mo** (US). Weight the catalog toward grandma.
2. **SEO competition is negligible** — keyword difficulty **0–3** across virtually every term. The fight is on ads/marketplace/social, not SEO.
3. **Personalization is where the money is** — "personalized gifts for grandma" (1,100, *transactional*); **jewelry carries the highest buyer intent** (CPC $1.20–1.70).
4. **Etsy carts** are led by two themes: 🌸 **birth flower / "a flower per grandchild"** (top item **752 in cart**) and 🍢 **grandpa = grilling** (top item **793 in cart**). The **"new grandparent" milestone** ("Promoted to Grandma", "First Dad Now Grandpa" — 178 in cart) is a distinct hot buyer.

### Social signal (this is the important addition)

5. **Pinterest = "Grandma's Garden" birth-flower, overwhelmingly.** It is *the* dominant grandma-gift concept on Pinterest by pin volume. Confirms the birth-flower theme (GPD02/04/13) as a top social bet.
6. **TikTok grandma content skews to DIY / sentimental keepsakes — and those are what go viral:**
   - Kids' hand-painted gift for grandma — **920K plays, 15.6K saves**
   - "Cousins' I-love-you notes" keepsake — **284K plays, 9.6K saves**
   - **Grandma's recipe cards framed — 193K plays, 5.8K saves** → *new angle*
   - Memorial photo collage ("best gma") — **85K plays** → *new angle*
   - Product-listing-style videos (e.g. competitor **wanderprints**) flop at **~110 plays**.
   → **Implication for our organic strategy:** shoot content that feels *handmade/sentimental* ("I cried making this"), not catalog-style. Same product, emotional framing.
7. **Grandpa's viral lane is novelty apparel.** Competitor **macorner's Hawaiian grandpa shirt did 4.2M plays / 4.4K shares / 2.3K saves.** Funny/novelty grandpa apparel is the TikTok winner (supports GPD08/09).
8. **Two new angles the social pull surfaced** (now scored): **GPD15 recipe keepsake** (grandma's handwriting) and **GPD16 memorial photo collage**.

---

## Ranked shortlist (composite score) — 16 ideas, 4 greenlit

| # | Score | Status | Idea (hook) | Product | Signal highlight |
|---|:-----:|--------|-------------|---------|-----|
| 1 | **4.24** | 🟢 greenlit | Grandma + grandkids' names / "Promoted to Grandma" | mug | Highest blended demand; cheap POD |
| 2 | **4.15** | 🟢 greenlit | Grandma's Garden — a birth flower per grandchild | sweatshirt | #1 Etsy theme + Pinterest-dominant |
| 3 | **4.06** | 🟢 greenlit | Grandma's Recipe — in her handwriting | tea towel/mug | TikTok viral (193K/5.8K saves) |
| 4 | **4.03** | 🟢 greenlit | First Dad, Now Grandpa | mug | Top grandpa cart-velocity (178) |
| 5 | 3.99 | backlog | A birthstone for every grandchild | necklace | Highest buyer-intent CPC |
| 6 | 3.97 | backlog | Nana's Garden tumbler | tumbler | Birth-flower on higher-AOV item |
| 7 | 3.90 | backlog | Grandma's woven family blanket | blanket | Premium AOV; heavier ship |
| 8 | 3.84 | backlog | Grandpa's Grilling Crew + kids' names | apron | Grilling #1 grandpa theme (793) |
| 9 | 3.82 | backlog | Grandma's Garden — where love grows | pillow | Birth-flower home decor |
| 10 | 3.72 | backlog | Grandmas should live forever (memorial) | canvas/blanket | TikTok memorial viral (85K) |
| 11 | 3.69 | backlog | Best Papa Ever + photo | t-shirt | Photo novelty, 290 cart |
| 12 | 3.69 | backlog | Grandpa Est. 2026 | cap/hat | New-grandpa milestone |
| 13 | 3.58 | backlog | "In a world full of grandmas, be a Mimi" | t-shirt | High demand but **saturated** |
| 14 | 3.55 | backlog | Grandkids make life grand | wood sign/canvas | Photo keepsake |
| 15 | 3.40 | backlog | Life is better at Gigi & Poppy's | doormat | Proven cat, bulky ship |
| 16 | 3.15 | backlog | "You're not my grandkids" (funny) | t-shirt | Grandma social skews sentimental, not funny |

> Note #13: the "Mimi" tee has the 2nd-highest raw *demand* (4.1) but drops to #13 on composite — **saturated** niche, thin margin. The rubric routes budget away from the crowded trade and toward #1–4. This is the discipline pure competitor-spying lacks.

---

## Recommended action — this week

**Brief these four greenlit ideas now** ([`../templates/design-brief.md`](../../templates/design-brief.md)):

1. **GPD01 — "Grandma's Crew" mug** (grandkids' names; Grandma/Gigi/Nana/Mimi variants). Cheapest test, biggest demand.
2. **GPD02 — "Grandma's Garden" sweatshirt** (one birth flower per grandchild + names). Ride the Pinterest-dominant birth-flower theme; highest AOV of the four.
3. **GPD15 — "Grandma's Recipe" keepsake** (her handwriting on a tea towel/mug). TikTok-proven emotional angle; cheap POD substrate.
4. **GPD07 — "First Dad, Now Grandpa" mug** (grandkids' names + est. year). Covers the grandpa side with the proven milestone angle.

**Content/validation notes baked in from the social pull:**
- **Tier 1 (now):** organic Pinterest (birth-flower pins) + TikTok. **Shoot TikTok as sentimental/handmade storytelling, NOT product shots** — that's what gets 100K+ vs ~110. Watch saves/comments 48–72h.
- **Tier 2 (~Jul 20):** $20–50 Meta/TikTok per concept → product page; gate on cost-per-ATC vs margin.
- Winners must be production-ready before the **Aug 30** last-order date.

## Competitor intel (from this run)
Superseded by a **targeted** pull → see [`competitor-intel-2026-07.md`](../2026-07-competitor-ad-scoring/competitor-intel.md). Corrected headline:
- Both competitors' engines are **sentimental relationship gifts** (couple / mom / siblings / **memorial** / "to the moon" on suncatchers & ornaments), not grandparent lines. macorner's 4.2M grandpa Hawaiian shirt was a keyhole view — their real top posts are 20–54M and mostly non-grandpa.
- **Active paid ads (running now):** both fund **memorial** heavily (validates GPD16); macorner actively pushes **grandpa novelty apparel + caps**. Neither actively advertises a **grandma names-mug or recipe keepsake** → those are **white space** for us.

> **Want to see what's selling?** Reference links to the actual top Etsy listings and viral posts,
> grouped by concept, are in [`concepts.md` → Reference examples](concepts.md#-reference-examples--see-what-the-researched-designs-look-like).

## Suggested next pulls
- **Etsy review-growth re-pull in ~1 week** to separate *accelerating* items from already-peaked.
- **Competitor `/new` + `/best-sellers` diff** (macorner / wanderprints / wrappiness / almagems) for their live grandparent SKUs and any active paid ads.
- **Concept mockups** for the 4 greenlit ideas (image-gen) so Tier-1 tests can launch immediately.
