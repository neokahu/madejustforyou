# Matrix correction — the test unit is the DESIGN (not the product)

Supersedes Part A of `TESTING-MATRIX-FRAMEWORK.md`. Apply this on next rebuild of the Doc + Sheet.

## The unit
A **DESIGN** = the creative concept / artwork + who it is for (e.g. "Grandma's Garden with grandkids'
names → for grandma"). **One design → many materials** (shirt · pant · mug · rug · sweatshirt · candle
warmer…). The recipient is fixed by the **design**, not by the material.

## Matrix 1 — DESIGN PROFILE (fixed per design — LOG, do NOT test)
- Design concept / artwork
- Recipient (fixed by design, e.g. grandma)
- Core need / emotion
> These are chosen at design-selection. You never A/B them inside one design's test.

## Matrix 2 — PER-DESIGN TEST AXES (what the staged funnel varies)
| Axis group | Factors | Notes |
|---|---|---|
| **Material / product** | shirt · pant · mug · rug · sweatshirt · candle-warmer … | NEW axis: same design, which material converts/sells best. Affects price & perceived value. |
| **Audience (BUYER, not recipient)** | buyer/gifter segment (grandchild · adult-child · spouse) · targeting type (broad/interest/LAL/retarget) · occasion/timing · geo | who you target to BUY the gift |
| **Creative execution (A)** | text angle · media format · hook · music · imagery · caption · length · CTA | how the design is shown in the ad |
| **Offer (O)** | price · discount depth · bundle/gift · free-ship threshold · urgency · payment | **price lives here only** (removed old P7 & R price duplicates) |
| **On-site page (R)** | UI/UX · reviews/social-proof · shipping/delivery message · trust · sales-note | |
| **Delivery / media-buying (D)** | placement · bid strategy · budget · attribution window · dayparting | usually held constant; test sparingly |
| **Follow-up (F)** | cart-recovery (email/SMS) · retargeting · upsell | Stage-3 recovery |

- **Stage / optimization event** (LPV → ViewContent → ATC → Purchase) = the **funnel dimension**, NOT a test axis (removed old A9 as an axis).
- **Covariates — LOG only, never test:** season/holiday · ad-fatigue & frequency · market CPM/competition · tracking (pixel/CAPI) · iOS/privacy.

## How MATERIAL fits the staged funnel
- **Stage 1 (engagement):** hold material constant (one baseline product) — creative + audience only, since material can't move hook/CTR.
- **Stage 2–3 (intent/purchase):** material becomes a test axis — same winning design/creative across shirt vs mug vs rug to see which converts + which economics (price/margin) win.

## Errors this corrects (from the old matrix)
1. Recipient/need/product were treated as per-item test axes → they're **design-fixed** (log).
2. "Audience" was recipient → must be the **buyer/gifter**.
3. Price appeared 3× (P7, R2, O1) → **consolidated into Offer**.
4. Optimization event was an axis → it's the **stage dimension**.
5. **Material/product added as a real test axis** (one design, many materials) — was missing entirely.
