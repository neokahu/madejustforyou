# Phase-1 Tournament — 3 new products (suncatcher · blanket · magnet)

> 📄 **Google Doc mirror:** https://docs.google.com/document/d/1AI5wciotbRFLsUSBTmwUfT7Zn61_7YXfA41OX60WH8E/edit
> *(the Markdown file in this repo is the source of truth; re-import after edits)*
>
> 🇻🇳 **Bản tiếng Việt:** https://docs.google.com/document/d/1cO05lrK4zm2xnITi_Kmak82m-DNRAyPqHdetUr1X5_8/edit

**Status:** planned, not launched. **Written 2026-09-18.**
**Provenance:** decisions and economics were settled in the session of 2026-09-17, which was lost to a power
outage before anything was written to disk. Recovered from the session transcript and **re-verified** (every
figure below recomputed from source prices/costs, not transcribed).

**Scope:** the three products below only. **MJ4U-111 is excluded** — it is already ads-live with a separate
cart→checkout diagnosis running; do not fold it into this tournament.

Method source of truth: `TESTING-MATRIX-FRAMEWORK.md` (Part B.1 stage scope, Part D tiers/T0/min-samples,
D.6 budgets) + `research/reference/video-ad-decomposition-2026.md` (components, format fit, brief template).

## The three products

| | **Dog memorial suncatcher** | **Granddaughter blanket** | **Grandma-hug magnet** |
|---|---|---|---|
| Buyer | grieving owner (self-buy) **or** sympathy-giver | grandma, 60+ (buys to give) | adult child / grandkid |
| Emotion | grief-comfort | reassurance / legacy letter | warmth, togetherness |
| Occasion | **none** — year-round, no deadline | graduation / birthday / Christmas | Mother's Day / Christmas |
| Personalization | breed silhouette + name — **visually strong** | 2 names + avatar — **visually weak; the TEXT is the product** | N grandkids + names — strong, **variable count** (Teeinblue conditional) |
| AOV | mid | high | low |

**Three consequences that shape the plan:**
- **The suncatcher has no deadline**, so our #1-ranked gift offer (order-by-date urgency) is unavailable to
  it. Its offer test must be the memorial-specific stack instead.
- **The blanket cannot do a personalization reveal** — the HIGH-fit format for the other two. The product is
  a wall of text that is illegible on a phone, and the personalization is just two names. Its concepts must
  be **VO-led** (grandma reads the letter aloud) or **reaction-led** (granddaughter reads it and breaks).
  Buyer is 60+, so fast-cut pacing may actively hurt → brief ~5s/cut, real human VO, never synthetic.
- **The magnet's low AOV is a structural risk** → bundle / multi-recipient is its **#1 Stage-2 offer**, not
  an optional one.

## Locked decisions

1. **Tournament, not three parallel campaigns.** Run all three through Stage 1 simultaneously (Stage 1 is
   cheap and, for gifts, a deliberately weak filter). Then let the **product** compete and push only the
   **top 1–2** into Stage 2–3 with real budget. Rationale: the framework warns that Stage 3 must be
   concentrated (≥3× CPA just to judge, ~5× CPA/day to escape learning) — spreading Stage 2–3 across three
   products is exactly the failure mode it warns against.
2. **Three test axes only** — the decomposition was deliberately cut down:
   - **Test:** **Concept/Angle** (Phase 1, the big swing) · **Hook** (Phase 1, OFAT, same body) · **Offer** (Phase 2).
   - **Hold constant:** *Format* — folded into the concept, since each concept is already an angle+format
     pairing; testing it separately doubles the matrix for nothing. *Body* — **not an axis**, it is a
     **repair** triggered by the hook×hold 2×2 (high hook / low hold → fix the body, don't kill). *CTA* —
     baseline gift CTA; becomes a test only if Phase 1 shows good hook+hold but dead CTR. *Craft*
     (9:16, captions, sound-off) — baseline spec, never an A/B.
   - **Group M (material) is not an axis here.** Each design is welded to its physical product, so Stage 2
     becomes **offer × page**, not material × offer. One exception: the blanket design could port to a
     pillow (pillow clones exist in the tracker) — optional, that product only.
3. **6 ads per product = 3 concepts × 2 hooks.** The research recommends 9–12 for a single-product account;
   at three products in parallel, 18 ads is already the ceiling. The hook test stays cheap regardless:
   it is **3 bodies + 6 openers** per product, not 6 full films.
4. **D.1 tiers are authoritative; B.1 was corrected to match** (done 2026-09-18 — B.1's link-CTR gate came
   from an *all-clicks* figure; see the ᴬ footnote in `TESTING-MATRIX-FRAMEWORK.md` Part B.1).

## Unit economics — product price vs base cost only

Shipping excluded on **both** sides; we charge above cost, so that upside is real but uncounted. These are
therefore **conservative**. Shopify fees also excluded — see the caveat below the table.

| Product | Variant | Price | Base cost | **Gross profit** | Margin | **BE CPA** | **BE ROAS** | Target CPA | CVR needed @ $0.50 CPC |
|---|---|---|---|---|---|---|---|---|---|
| **Blanket** | S 40×30 | $39.95 | $18.75 | **$21.20** | 53.1% | $21.20 | **1.88×** | $14.84 | 2.36% |
| | M 60×50 | $55.95 | $30.99 | **$24.96** | 44.6% | $24.96 | **2.24×** | $17.47 | 2.00% |
| | **L 80×60** ⭐ | $69.95 | $39.59 | **$30.36** | 43.4% | $30.36 | **2.30×** | $21.25 | 1.65% |
| **Suncatcher** | 4 IN | $23.95 | $4.25 | **$19.70** | 82.3% | $19.70 | **1.22×** | $13.79 | 2.54% |
| | **6 IN** ⭐ | $26.95 | $4.61 | **$22.34** | 82.9% | $22.34 | **1.21×** | $15.64 | 2.24% |
| | 8 IN | $34.95 | $6.28 | **$28.67** | 82.0% | $28.67 | **1.22×** | $20.07 | 1.74% |
| **Magnet** | 3.54 IN | $21.95 | $6.20 | **$15.75** | 71.8% | $15.75 | **1.39×** | $11.02 | 3.17% |
| | 4.5 IN | $24.95 | $6.45 | **$18.50** | 74.1% | $18.50 | **1.35×** | $12.95 | 2.70% |
| | 5.5 IN | $26.95 | $6.60 | **$20.35** | 75.5% | $20.35 | **1.32×** | $14.24 | 2.46% |
| | **10 IN** ⭐ | $39.95 | $8.50 | **$31.45** | 78.7% | $31.45 | **1.27×** | $22.02 | 1.59% |

⭐ = **hero variant** — the size the ad promises. Chosen for headroom. Bigger sizes convert worse, and that
price/size trade is exactly what Stage 2 exists to settle; switch the hero to 4 IN / S / 4.5 IN if we'd
rather lead cheap and upsell. *Target CPA = 70% of gross profit. BE ROAS = price ÷ gross profit.*

> **Caveat:** these exclude Shopify payment fees (2.9% + $0.30). Including them lowers gross profit by
> roughly $1.46 (suncatcher 6 IN) to $2.33 (blanket L) per order and raises BE ROAS by ~0.06–0.10×. The
> ranking and every conclusion below are unaffected.

### Three findings that drive the plan

**① The suncatcher is roughly twice as forgiving as the blanket.** It breaks even at **1.21× ROAS**; the
blanket needs **2.24–2.30×**. Identical ad performance makes one profitable and the other underwater. In a
tournament that is a structural head start — worth knowing *before* we read any creative result, so we
don't mistake economics for creative quality. **Stage 3 gets a per-product ROAS line, never a shared one.**

**② For ad math, contribution dollars beat margin %.** Ad budget is paid in dollars, not percentages. The
**10 IN magnet has the highest headroom of all ten variants at $31.45** — more than the "premium" L blanket.
So the hero variant materially changes what CPA we can afford: leading on 4.5 IN ($18.50) vs 10 IN ($31.45)
is a **70% difference in allowable CPA**.

**③ The uncomfortable one — at median performance, all three lose money.** Break-even needs a click→purchase
CVR of **1.6–3.2%**. Our D.1 tiers put PAR at 1.24–1.53% and STRONG at ~3%.

| | CVR 1.4% (PAR) | CVR 3.0% (STRONG) | CVR 4.5% (ELITE) |
|---|---|---|---|
| CPC $0.34 (gifts ELITE) | $24.29 | $11.33 | $7.56 |
| **CPC $0.50 (gifts PAR)** | **$35.71** | **$16.67** | $11.11 |
| CPC $0.70 | $50.00 | $23.33 | $15.56 |

At **par CPC and par CVR the CPA is ~$35.71** — above break-even for every variant, including the 10 IN
magnet. This is not a reason not to run. It is the reason **Stage 2 must be an AOV/offer test, not a
decoration**: bundles, size upsell and multi-recipient ordering are the economic requirement.

## Gates and budgets

**Stage 1 (per ad)** — impression-priced, not CPA-priced:
- **Hook rate:** kill < 18% · advance ≥ 28% · **T0 red-line < 21%** on ~2k **settled** impressions.
- **Link CTR:** kill < 1.0% · advance ≥ 2.5% · **T0 < 0.5%.**
- **Hold rate:** **diagnostic, not a kill** — routes the hook×hold 2×2 (high hook / low hold → rebuild the
  body; low hook / high hold → rebuild only the first ~1.5s).
- ⚠️ Impressions + **settled delivery**, never the calendar — in-day Meta metrics are estimates that settle
  *down*.

**Stage 2–3 (per product, at the hero variant):**

| Product | Hero | Target CPA | **T0 kill** (0 ATC / 0 purchase at 3× target CPA) | Stage 2 (5–8×) | Stage 3 to judge (3×) | Stage 3 to optimize (~5×/day) |
|---|---|---|---|---|---|---|
| Suncatcher | 6 IN | $15.64 | **$47** | $78–125 | $47 | ~$78/day |
| Blanket | L 80×60 | $21.25 | **$64** | $106–170 | $64 | ~$106/day |
| Magnet | 10 IN | $22.02 | **$66** | $110–176 | $66 | ~$110/day |

**Total to a real answer:** Stage 1 ≈ $20/ad × 6 ads = **~$120/product → ~$360 for all three**, then
**$80–175** on the one or two survivors, then **$50–65** for a first purchase read ≈ **$500–700**.

## The 9 test cases

Each gets a full 12-field brief (see the brief template in `video-ad-decomposition-2026.md`) before it is shot.

> ⚠️ **Hooks below are superseded for Phase 1.** This section gives each concept its own hook pair;
> the approved plan locks **one** pair shared by all three concepts, because per-concept hooks would
> confound concept with hook. Build from `PHASE1-SUNCATCHER-video-build-plan.md` and the plan page.
> The unused lines here are material for **Vòng Hook**, after a winner exists.

### A · Dog memorial suncatcher
No deadline; breed + name is the visual hook; buyer is either the grieving owner or a sympathy-giver.
- **A1 "The light still comes in"** — memorial keepsake reveal; sun hits the glass at 4pm and the room fills
  with colour, his name visible.
  *H1:* "The sun hits it at 4pm and the whole room turns into him." *H2:* "We still leave the window open for him."
- **A2 "Say his name"** — hyper-personalization flex; split-screen generic dog vs *their* breed silhouette +
  name. **Shoot with the adopted Compare recipe** (split screen, parallel cutting, zoom on the differentiator).
  *H1:* "That's not a generic dog. That's his actual breed — and his name." *H2:* "Anyone can hang a rainbow. This one has his name on it."
- **A3 "I didn't know what to send"** — sympathy-giver POV. **This is the buyer-swap concept** — identical
  product, different persona — testing whether the giver market beats the self-buyer market.
  *H1:* "Her dog died on Tuesday. I didn't know what to send." *H2:* "Flowers wilt in a week. This catches the light every morning."

> ⚠️ **Meta Personal Attributes policy:** all six hooks are deliberately **first/third-person**. Ads implying
> knowledge of the viewer's hardship get rejected — *"Did you lose your dog?"* is a rejection risk,
> *"When we lost Coop…"* is not. Keep every grief hook in this form.

### B · Granddaughter blanket
The product is a letter → every concept is VO- or reaction-led, **never a reveal**. Slow cuts, real human VO.
- **B1 "The letter she'll keep"** — sentiment build (Skeleton B); grandma's voice reads it over the
  granddaughter's life beats, blanket as late payoff.
  *H1:* "I'm 74. I wrote her a letter she can wrap herself in." *H2:* "She won't read my texts. She'll read this."
- **B2 "This old girl has your back"** — gift-reaction; she gets three lines in and stops talking. Leans on
  the product's own best line.
  *H1:* "'This old girl will always have your back' — watch her get to that line." *H2:* "She opened it, got three lines in, and stopped talking."
- **B3 "800 miles away"** — long-distance grandma; the blanket as a hug by proxy.
  *H1:* "I live 800 miles from her. This is the closest I get to a hug." *H2:* "I can't be there when life knocks her down. This can."

### C · Grandma-hug magnet
Variable grandkid count is the feature; everyday visibility is the benefit.
- **C1 "Every grandkid, on her fridge"** — reveal built on the Teeinblue conditional count.
  *H1:* "Four grandkids. All four names. One magnet." *H2:* "Add a kid. Add another. It grows with the family."
- **C2 "She opens that fridge 20 times a day"** — gift-reaction + the real benefit (a card goes in a drawer;
  this doesn't).
  *H1:* "Grandma opens that fridge 20 times a day. Now she sees this every time." *H2:* "She didn't say anything. She just kept looking at it."
- **C3 "Don't get me anything"** — relationship callout + occasion deadline. **Carries the bundle into
  Phase 2**, which is the magnet's AOV fix.
  *H1:* "For the grandma who says 'don't get me anything.'" *H2:* "Mother's Day is in 9 days and this is made-to-order."

## Open decisions (blocking nothing, but decide before shooting)
1. **Hero variant** — keep the headroom picks (6 IN / L / 10 IN), or lead cheap (4 IN / S / 4.5 IN) and upsell?
2. **Blanket → pillow port** — run M as an optional axis for the blanket only, or leave it out?
3. **Sequencing** — all three Stage-1 at once (~$360), or stagger?

## ⭐ Next action
Pick the hero variants, then build the 6 briefs per product (12 fields each) and shoot. Stage 1 launches on
**LPV**, broad, Advantage+ placements, signal verified first (EMQ 8+) — Fixed Setup in the framework.
