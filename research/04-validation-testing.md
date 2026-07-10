# Stage 5 — Validation & Testing

Prove demand with the **cheapest test that can kill the idea**, escalating spend only as an
idea survives. Every test gets an [`experiment-card.md`](templates/experiment-card.md) with
**kill/scale thresholds declared before launch**.

> Benchmarks below are **starting heuristics** — replace them with *your own* numbers after the
> first ~10 tests. Calibrate against your AOV, margins, and audience. Never treat them as fixed.

---

## The test ladder

| Tier | Question it answers | Cost | Signal | Speed |
|------|--------------------|------|--------|-------|
| **0 — Desk check** | Does demand/competition even justify a test? | ~free | Scores from Stage 3 | minutes |
| **1 — Organic** | Do people *react* to the concept? | time only | Saves, CTR, comments, shares | 2–3 days |
| **2 — Paid signal** | Will people *click and intend to buy*? | $20–50/idea | CTR, CPC, ATC, cost-per-ATC | 3–5 days |
| **3 — Pre-order / live** | Will people *actually pay*? | ad spend + listing | Conversions, revenue, CPA vs margin | 1–2 weeks |

Climb one rung at a time. Most ideas should die at Tier 1 or 2 — that's the system working.

---

## Tier 1 — Organic reaction test

**Setup:** post a mockup (image-gen or quick designer render) natively to TikTok / Instagram
Reels / Pinterest with a hook caption. No spend. One concept per post.
**Measure over 48–72h:** save rate (Pinterest/IG), view-through & watch time (TikTok),
comments asking "where can I buy / do you make X for Y?", shares.
**Starting thresholds:**
- **Scale →** clearly outperforms your account's median post (e.g. ≥2× saves/engagement), or
  organic comments explicitly asking to buy.
- **Kill →** flatlines at/below median with no buy-intent signals.
**Why first:** near-zero cost, and the *comments* often hand you the exact angle/wording.

## Tier 2 — Paid signal test

**Setup:** $20–50 per idea on Meta and/or TikTok, single concept, broad-ish gift audience,
driving to a real product page (or a "notify me" landing page if not built yet). Objective:
traffic/engagement or ATC.
**Measure:**
| Metric | Starting benchmark* |
|--------|--------------------|
| Ad CTR (cold) | ≥ ~1.5% = interest; < ~0.7% = weak creative or weak idea |
| Cost per outbound click | at/below account average |
| Landing/product-page CVR to ATC | ≥ ~3–5% add-to-cart |
| **Cost per ATC** | **≤ ~⅓ of your product margin** (leaves room for real CPA) |

\*Calibrate to your data. Separate a **creative** problem (low CTR) from a **demand** problem
(good CTR, no ATC) — fix creative and re-test before killing the idea itself.
**Decision:** Scale if cost-per-ATC clears the bar; iterate the hook/creative once if CTR is
good but ATC weak; kill if both are poor.

## Tier 3 — Pre-order / live validation

**Setup:** list it live (real checkout) or run a pre-order/waitlist, with modest ad spend.
**Measure:** actual **conversion rate**, **revenue**, and **CPA vs contribution margin** — the
only test that proves people pay.
**Decision:**
- **Scale →** CPA < contribution margin with room to spend more → push budget, then expand the
  angle across more products/recipients (Stage 6).
- **Iterate →** profitable-ish but thin → try higher-AOV product, bundle, or new creative.
- **Kill →** can't acquire below margin after a fair creative iteration.

---

## Metrics glossary

- **CTR** — clicks ÷ impressions. Interest in the *hook/creative*.
- **ATC** — add-to-cart. Purchase *intent*.
- **CVR** — conversion rate (orders ÷ sessions). Willingness to *pay*.
- **CPA** — cost per acquisition (ad spend ÷ orders).
- **Contribution margin** — retail − (product base + shipping + fees). Your room for CPA.
- **AOV** — average order value. Raise it with bundles/premium tiers to widen CPA headroom.

---

## Design vs product — two variables, tested in order (don't blob them)

One design ports to many products (mug / shirt / blanket / rug / tote) — that's the leverage from
the Roster mechanic ([`05-idea-crafting.md`](05-idea-crafting.md)). But **don't test the design on
many products at once** — you'd confound *"is the concept good?"* with *"is the product good?"*,
split your traffic thin, and multiply SKUs before anything is proven. Run two single-variable
experiments in sequence:

| Phase | Question | Hold constant | Vary | Product used |
|-------|----------|---------------|------|--------------|
| **1 · Validate the design** | Does the concept/hook/metaphor resonate? | **product** (one cheap substrate) | the **design** | mug or shirt — low cost, low ship |
| **2 · Find the money product** | Which product sells the winning design best? | **design** (the Phase-1 winner) | the **product** | 2–3 tiers: mug $ · shirt $$ · blanket/rug $$$ |
| **3 · Scale + collection** | — | both winners | budget | roll winner; *then* offer the design across all products for AOV |

- **Phase 1 first, always.** Test `Garden vs Birds vs Night Sky` all on the **same sweatshirt** —
  so the winner is the *metaphor*, not the item. (Testing Garden-on-mug vs Birds-on-blanket tells
  you nothing clean.)
- **Product still matters — but later.** Same design earns very differently on a $19 mug vs a $60
  blanket; and some mechanics fit some products (recipe→tea towel, birth-flower→apparel/wall art,
  photo→mug/canvas). Phase 2 finds that fit *with the design already proven*.
- **Collection = merchandising, not a test.** Once a design wins, listing it across products (and
  bundling) lifts AOV and lets the buyer self-select — do it after validation, not to validate.

> Rule of thumb: **prove the design on one cheap product; expand the winner across products.**

## Decision discipline

1. **Thresholds are set before launch** and written on the experiment card. No post-hoc moving.
2. **One variable per test** where possible (idea vs creative vs audience) so you know what won.
3. **Fair-iteration rule:** an idea gets *one* creative iteration before a kill — many "dead"
   ideas are just bad first creatives.
4. **Everything gets logged** in the Idea Database with verdict + learnings, win or lose
   (Stage 6). The compounding value is in the losses you won't repeat and the wins you expand.
