# Scientific Ad-Testing Framework — Factor Matrix + Multi-Stage Funnel

Goal: turn ad testing into a real **inductive experiment** — not just find the winning combo,
but understand **WHY** it wins, so each round moves closer to the "truth."

Three pillars:
1. **Factor matrix** = the *independent variables* (what we deliberately change).
2. **Per-stage funnel metrics** = the *dependent variables* (what we measure).
3. **Experiment design + thresholds** = how we isolate variables for correct causal induction.

Loop: **Hypothesis → design variants (coded combos) → run by stage with pass-thresholds →
analyze → find common traits of winners → refine matrix + thresholds → repeat.**

---

## PART A — Factor Matrix

> **The unit of test is the DESIGN, not the product.**
> A **DESIGN** = the creative concept / artwork + who it is for (e.g. "Grandma's Garden with the
> grandkids' names → for grandma"). **One design → many materials** (shirt · sweatshirt · mug · rug ·
> candle-warmer…). The recipient is fixed by the **design**, not by the material. So there are two
> matrices: what is **fixed** per design (log it, never A/B it) and what the funnel **varies** per design.

### Matrix 1 — DESIGN PROFILE (fixed per design — LOG, do NOT test)

Chosen once at design-selection. You never A/B these *inside* one design's test — a "Grandma's Garden"
design is for grandma; you can't retest it as a spouse gift. (To test a different recipient, that's a
**different design**, logged as its own row.)

| Field | Example | Note |
|---|---|---|
| Design concept / artwork | "Grandma's Garden, grandkids' names on flowers" | the creative idea itself |
| Recipient | grandma | fixed by the design |
| Core need / emotion | sentimental family-legacy gift | why it lands emotionally |

### Matrix 2 — PER-DESIGN TEST AXES (what the staged funnel varies)

Codes: `M` material, `AUD` audience/buyer, `A` creative, `O` offer, `R` on-site, `PZ` personalizer, `D` delivery, `F` follow-up.

#### Group M — Material / product *(NEW axis: same design, different physical product)*
| Code | Factor | Levels to test |
|---|---|---|
| M1 | Material / product | shirt · sweatshirt · hoodie · mug · rug · canvas · candle-warmer · ornament… |
> Same design, which material converts + sells best. Material drives price, perceived value & margin,
> so it is a **real test axis** — but it can't move hook/CTR, so hold it constant in Stage 1 (see B.1).

#### Group AUD — Audience / BUYER *(who you target to BUY the gift — NOT the recipient)*
| Code | Factor | Levels to test |
|---|---|---|
| AUD1 | Buyer / gifter segment | grandchild · adult-child · spouse · friend (who purchases the gift) |
| AUD2 | Targeting type | broad · interest · lookalike · retarget |
| AUD3 | Occasion / timing | everyday · Christmas · Mother's/Father's Day · birthday |
| AUD4 | Market / geo | US · EU · AU · other |
> The recipient (grandma) is fixed by the design; the **buyer** (e.g. the grandchild who buys it for her)
> is the audience you test. Buyer ≠ recipient.

#### Group A — Creative execution *(how the design is shown in the ad)*
| Code | Factor | Levels to test |
|---|---|---|
| A1 | Text angle | pain-point · benefit · emotional · humor · social-proof · scarcity |
| A2 | Media format | product-reveal · UGC · static · carousel · slideshow |
| A3 | 3-sec hook type | question · before/after · POV · surprise reveal · number |
| A4 | Music / mood | happy · emotional · trending · none |
| A5 | Imagery / color tone | warm · bright · minimal · messy-fun |
| A6 | On-screen caption | none · bold-box · keyword-highlight |
| A7 | Length | ≤10s · 15–20s · 30s+ |
| A8 | CTA | Shop Now · Learn More · Get Offer |

#### Group O — Offer *(the ONLY place price lives)*
| Code | Factor | Levels to test |
|---|---|---|
| O1 | Price point | low · mid · high |
| O2 | Discount depth | none · light · deep |
| O3 | Bundle / gift | single · combo · gift-with-purchase |
| O4 | Free-ship threshold | none · with threshold |
| O5 | Deadline urgency | none · flash-sale/deadline |
> Price used to appear 3× (old P7 tier, R2 anchor, O1 point) — **consolidated here**. Price-on-page
> presentation (strikethrough/anchor) is an on-site execution of the O price, logged under R.

#### Group R — On-site / landing page *(the page that converts the click)*
| Code | Factor | Levels to test |
|---|---|---|
| R1 | **Landing page TYPE** | **generic product-info page** (default; used Stage 2 for every design) → **dedicated sales/advertorial page** (Stage 3 only, unlocked for designs that already cleared the Stage-2 ATC threshold) |
| R2 | Reviews / social proof | few vs many · "X sold" badge · customer photos |
| R3 | Shipping/delivery message | free-ship threshold shown · clear delivery date · **order-by-date for holiday delivery** |
| R4 | Sales-lift note | urgency/scarcity · **remake-free guarantee** (personalized = non-returnable) · "perfect gift for…" |
| R5 | Trust | payment badges · prominent return policy |
| R6 | Price presentation | flat · strikethrough anchor · % off *(displays the O price)* |
> **R1 rule:** page type is *stage-gated, not blindly A/B'd.* A product must **sell itself on the cheap generic
> page (Stage 2)** before it earns the effort of a dedicated sales page (Stage 3) — the sales page is a
> **scaling reward for proven designs**, not an early test axis. (Do NOT test page speed — competitors win at
> 29–33 Lighthouse; speed is not the bottleneck.)

#### Group PZ — Personalizer conversion toggles (Teeinblue) *(tested one-at-a-time at Stage 2–3 on a WINNING design)*
All four **verified verbatim** in Teeinblue → Store Settings → **Product Page Settings** (Help Center, fetched 2026-09-07).
| Code | Factor | Teeinblue setting | Levels to test |
|---|---|---|---|
| PZ1 | ATC confirmation checkbox | *"Show 'Confirmation checkbox'"* | on · off *(friction vs wrong-personalization safety)* |
| PZ2 | Mobile sticky ATC + "Personalize" scroll button | *"Show 'Personalize' button on mobile"* + *"Show sticky buttons"* | on · off *(**highest leverage** — below-fold discovery on ~90% mobile)* |
| PZ3 | ATC/Buy-Now inside the Preview popup | *"Show ATC/Buy now button on Preview popup"* | on · off *(capture the buy at the emotional preview peak)* |
| PZ4 | Live-preview gallery load | *"Load gallery immediately"* | on page load · on-interaction *(show value-prop instantly vs faster first paint)* |
> Teeinblue is **not** a CRO-configurable personalizer — the customization *steps* are fixed and there is **no
> "add-to-cart-first, personalize-later" mode** (always personalize-before-ATC). Only these ~4 toggles are real
> conversion axes; everything else it exposes is cosmetic/operational. Test them **sparingly, one at a time** on a
> design that already cleared Stage 2 — never fan all of them out at once.
> **Availability caveat:** some settings are Campaign-by-Product-Base vs Campaign-by-Shopify specific — confirm in-app.
> **Dropped — "Buy Now" (express checkout):** the toggle exists but only skips the *cart page*, not personalization,
> and Shopify's dynamic checkout is unreliable with required line-item properties (personalization) — it's a risk,
> not a lever. *Source: `research/reference/teeinblue.md` → "Conversion-relevant settings".*
> Secondary toggles to try only if the above plateau: block-preview-until-fields-complete · ATC redirect-to-cart
> vs on-page message · preview watermark on/off · save-badge/compare-at price framing (lives in Offer).

#### Group D — Delivery / media-buying *(how you run it — hold constant, test sparingly)*
| Code | Factor | Levels to test |
|---|---|---|
| D1 | Placement | Feed · Reels · Stories · Advantage+ (auto) |
| D2 | Bid strategy | **lowest-cost/highest-volume (DEFAULT, Stages 1–3)** → cost-cap / bid-cap **only when SCALING a proven winner** |
| D3 | Budget per ad set | low · mid · high (affects delivery) |
| D4 | Attribution window | 1-day click · 7-day click |
| D5 | Dayparting | hour/day scheduling |
> **D2 rule — do NOT set a bid cap during testing/cold-start.** Caps (cost-cap, bid-cap, ROAS-goal) *constrain*
> delivery and only work once Meta has conversion signal. On a new pixel or in learning phase a cap starves
> delivery → you never hit ~50 events/week to exit learning. Stay on **Highest Volume / Lowest Cost** through
> Stages 1–2 (and cold start). Graduate to a **cost cap** only when ALL are true: out of learning · ~50+
> conversions of history · you know your real CPA + break-even · you're pushing budget up and CPA starts to
> creep. Its job is holding CPA steady *while you scale* — not an early-test axis. (Note: even "auto"/Advantage+
> campaigns run lowest-cost by default — the point is you don't touch a cap until scale.)

#### Group F — Follow-up / retention *(recovers Stage-3 orders)*
| Code | Factor | Levels to test |
|---|---|---|
| F1 | Abandoned-cart recovery | email · SMS · both |
| F2 | Retargeting sequence | none · yes (sequence) |
| F3 | Upsell / cross-sell | none · yes |

### Not an axis — the funnel dimension
- **Stage / optimization event** (LPV → ViewContent → ATC → Purchase) is the **funnel dimension you move
  UP as the pixel matures**, *not* a factor you A/B. (It was wrongly listed as an axis before.)

### Interaction factor
- **Message match (ad ↔ landing):** does the ad's promise match the landing page? A mismatch kills
  conversion even when ad + page are each good on their own. Always check when Stage 2 fails.

### Covariates to LOG (do NOT test, but record)
For clean causal induction, log these noise variables; ignoring them **silently distorts** conclusions:
| Covariate | Why log it |
|---|---|
| Seasonality / holidays | traffic & CVR swing seasonally → cross-time comparisons mislead |
| Frequency / ad fatigue | high freq → metrics decay over time, NOT a bad creative |
| Market CPM / competition | auction prices shift with season & competitors |
| Tracking (pixel/CAPI) | if tracking is wrong ALL data lies → **guardrail** check each round |
| iOS / privacy | attribution gaps → adjust expectations |

> This list is **OPEN** — add factors as discovered; each new factor = a new test axis.
> **Anti-combinatorial-explosion:** each round vary only **2–3 high-leverage axes**, hold the rest
> fixed (control), and **LOG the covariates**.

---

## PART B — Multi-stage funnel within one budget (elimination funnel)

One campaign = **one max budget**, split by funnel stage. **Only combos that pass the prior stage's
threshold get budget to advance** (prune → concentrate on strong candidates).

| Stage | Measures | Optimize event | Deciding metrics | Role |
|---|---|---|---|---|
| **1 — Engagement** | Is the ad compelling? | Traffic / LPV | hook/ThruPlay, CTR, CPC | cheap filter; kill weak media/hook fast |
| **2 — Intent** | Drives ATC/checkout? | Add to Cart | ATC-rate, cost/ATC | filter combos with buying pull |
| **3 — Purchase** | Profitable orders? | Purchase | CPA vs break-even, ROAS | true winner conclusion |

**Example budget split ($100):** Stage 1 **~$40** across many cheap variants ($5 × 8) → keep top 3–4;
Stage 2 **~$35** for survivors (more budget for ATC sample); Stage 3 **~$25** for the 1–2 strongest
to read orders/ROAS.

> Run **many campaigns in parallel**, each with many matrix combos. After stats, compare winners to
> find **common traits** (e.g., many winners use happy-music + POV hook → signal).

---

## PART B.1 — What each stage tests (factor scope per stage) ⭐

**Key principle: a stage's metric is only influenced by certain factor groups — vary THOSE, hold the
rest constant.** This is why Stage 1 ignores landing-page/offer factors (they cannot affect hook/CTR),
and why each stage **layers new factors on top of the previous stage's winner** instead of testing
everything at once.

| Stage | Optimize event | VARY (test axes this stage) | HOLD constant (baseline) | Advance threshold | Carry to next |
|---|---|---|---|---|---|
| **1 Engagement** | Traffic / LPV | **A1–A8** (angle, media, hook, music, imagery, caption, length, CTA) + **AUD1 buyer / AUD2 targeting** | **1 baseline material (M)**; all **R, O, F**; one **D** baseline | hook ≥ 28% **AND** link CTR ≥ 4% (kill < 18% / < 1.7%) | the winning **creative × buyer** |
| **2 Intent** | Add to Cart | **M1 material** (shirt vs mug vs rug) · **O1/O2 price+discount · O3 bundle · O4 free-ship · R1 page type (generic) · R2 reviews · R4 note · R6 price presentation · PZ personalizer toggles** | winning **creative × buyer** fixed | ATC rate ≥ 7.5% (session) **or** cost/ATC ≤ baseline (kill < 2%) | winning **creative × buyer × material × page/offer** |
| **3 Purchase** | Purchase | **R1 dedicated sales page (unlock for winners) · R3 delivery msg · R5 trust · O5 urgency · PZ ATC-gate toggles · F1 cart-recovery · F2 retargeting · F3 upsell** | winning **creative × buyer × material × page/offer** fixed | CPA ≤ break-even **&** ROAS ≥ target-by-margin (click→purchase > ~1.5–3.2%) | winning **full combo → SCALE** |

**How to build combos each phase (concrete):**
- **Phase 1 — creative × buyer only.** Fix **1 baseline material** + 1 baseline offer/page. Build **N
  creative variants** that differ by **one creative axis at a time** (e.g., 8 ads: same everything, differ
  in hook × media × music), optionally crossed with 1–2 buyer segments. Run ~$5 each on **LPV**. → keep the
  3–4 clearing the Stage-1 threshold. *(Material/landing/offer/checkout can't move hook/CTR — do NOT vary
  them here; material is held at ONE baseline product.)*
- **Phase 2 — material × page/offer on the winning creative.** Take the winning creative × buyer; now
  **introduce material as an axis** (same design on shirt vs mug vs rug) crossed with **on-site/offer
  variants** (e.g., price-anchor on/off × reviews few/many). Run on **ATC** with real budget. → keep the
  material + page/offer that converts with the best economics (price/margin).
- **Phase 3 — checkout/trust/follow-up on the winning creative × buyer × material × page/offer.** Build
  **variants** (e.g., urgency on/off × cart-recovery email vs SMS). Run on **Purchase**. → the winner **scales**.

**Why layered, not all-at-once:** if Stage 1 also varied material/page/offer, you'd burn budget on changes
that cannot move hook/CTR **and** you couldn't attribute a creative win cleanly. Material earns its place as
an axis in Stage 2–3, where it actually moves conversion + economics. Each stage isolates the one factor
group that actually moves *that* stage's metric — which is exactly what makes the induction clean.

---

## PART C — Experiment design to enable INDUCTION (most important)

If an ad changes *many* factors at once and wins, you **can't tell which factor caused it** → no
induction. Principles for clean causality:

1. **Fixed baseline (control).** Every variant differs from baseline only on the axis under test.
2. **Each batch varies only 1 axis** (OFAT — one factor at a time). Easy causality, costs more variants.
   - Advanced: **fractional factorial** — systematic multi-axis to cut variant count, but needs a design
     table so each factor's effect is still separable (do this once you're comfortable).
3. **Code every combo** (P2=emotional, A4=happy, A3=POV → "combo #12"). Log winners by code.
4. **Find common traits of winners:** when ≥2 independent winners share the same *level* of a factor →
   that factor has real signal; keep it and test another axis.
5. **Don't over-conclude:** if two winners differ in 5 things, no conclusion yet.

---

## PART D — Thresholds & induction (leading indicators)

Deductive chain: *campaign wins ⟹ ad is compelling ⟹ engagement is good ⟹ at $5 visit-web the metrics
beat threshold X.* Reverse it to act (**induction**): **set $5, if it beats threshold X → candidate
"good-engagement ad" → advance.**

### Advance-threshold cheat-sheet — starting point (general e-com benchmarks, then calibrate)

> These are **general e-com benchmarks** (sources listed) as a starting point. No niche personalized-POD
> data yet → judge against these, then **calibrate with your own data**.

**STAGE 1 — Engagement (readable on a $5–$20 micro-budget):**
| Metric | KILL | Average | ADVANCE | Source / confidence |
|---|---|---|---|---|
| Hook rate (3s / impr, cold feed) | < 18% | ~22–23% | > 28% | AdSights/SuperScale — practitioner, **medium** (judge cold-vs-cold; Reels 24–36%, retarget 30–45%) |
| Link CTR | < 1.7% (all-industry floor) | ~2% | **> 4%** (Gifts-category bar) | WordStream 2025; Shopping/Gifts = **4.13% CTR / $0.34 CPC** — near-niche proxy, **high** |
| CPM (reference) | — | ~$13–15 | cheaper = better | Top Growth $13.52 · Triple Whale $15.06 |

*Note: "all-clicks CTR" (~2.4–2.7%) ≠ "link CTR" (~1–1.7%). Grade on **link CTR**.*

**STAGE 2 — Intent (needs more spend; not readable at $5):**
| Metric | KILL | Average | ADVANCE | Source / confidence |
|---|---|---|---|---|
| ATC rate (session, Shopify) | < 2% | ~4.6% | > 7.5% (top 20%), strong > 9.6% (top 10%) | Littledata, 2,800 Shopify sites 2023, **high** (not POD-validated) |
| LPV → ATC | < 2% = page/price/trust problem | | | Braze/ClickPost |
| Cost/ATC | > ~3–4× your good level | — | ≤ your baseline | price-dependent → use **your own baseline** |

**STAGE 3 — Purchase (needs the most spend):**
| Metric | KILL | Average | ADVANCE | Source / confidence |
|---|---|---|---|---|
| Click → Purchase (paid Meta) | < 0.65% | ~1.24–1.53% | > 3.2% | Managed-DTC + Triple Whale, **high** (most portable) |
| Session → purchase (reference) | | ~2.9% | | Dynamic Yield 2024 |
| Checkout completion | < 20% (abandon > 80%) | ~24% (abandon ~76%) | | Dynamic Yield 2024 |
| CPA | AOV-dependent → judge vs break-even | industry median $38.99 | ≤ break-even | Triple Whale 2026 |
| ROAS | < break-even | industry median ~1.9–2.2× | ≥ target by margin | Varos / Triple Whale |

**ROAS judged vs BREAK-EVEN = 1 ÷ gross margin, NOT vs industry average:**
| Gross margin | Break-even ROAS | Profitable target |
|---|---|---|
| 60% | 1.7× | ≥ 2.5× |
| 50% | 2.0× | ≥ 3.0× |
| 30% | 3.3× | ≥ 4.5× |
| 20% | 5.0× | ≥ 6.5× |

### Which factors drive each stage (so you know what to change when it fails)
- **Stage 1** ⟵ **creative / 3-sec hook** (dominant) + **buyer** targeting. Fails Stage 1 → change media/hook (Group A) or buyer (AUD). *Material can't move hook — held at baseline.*
- **Stage 2** ⟵ **material, offer, price, reviews/social-proof, landing/product-page quality** (Groups M, O, R). ATC < 2% → material/page/price/trust problem. This is where shirt-vs-mug-vs-rug is decided.
- **Stage 3** ⟵ **checkout friction (~76% abandon), price/margin, trust** (Groups O, R, F). Delivery (Group D) affects all stages.
- **Buyer audience:** retargeting inflates hook (30–45%) vs cold (18–28%) → judge **cold vs cold**.

- **Thresholds are HYPOTHESES, not truth.** After each round, calibrate: look back at real winners'
  Stage-1 metrics → update thresholds for your niche. That IS "getting closer to the truth."

### ⚠️ Statistical limits (don't fool yourself)
- A **$5–$20 micro-budget reliably reads only Stage-1 metrics** (hook/CTR/CPM — impression-level, accrue
  fast); it **cannot** read ATC/purchase (rare events need far more spend). This validates the staged
  design: filter cheap on engagement, spend up only on survivors.
- **"0 orders" only means something after ~2–3× break-even CPA** of spend. Below that = insufficient sample.
- In-day numbers are estimates → decide on **closed days** only.
- Good top-funnel but no orders is usually an **on-site (R/O)** problem → fix retail, don't kill a good ad.
- (Foundations: see `FB-ADS-PLAYBOOK.md`.)

---

## PART E — Pre-launch plan template

Before launch, name the DESIGN (Matrix 1, fixed) then draw the tree:
**Design → Campaign → k media → n ads → each ad = one Matrix-2 combo code.**

Design header (fixed, log once): `Design = Grandma's Garden · Recipient = grandma · Emotion = family-legacy`.

Planning table (each row = 1 ad = 1 combo). Stage 1 holds material at ONE baseline:

| Ad ID | Combo code | Material (M) | Media (A2) | Hook (A3) | Music (A4) | Text angle (A1) | Buyer (AUD1) | Stage/event | Offer (O) | On-site (R) | Budget | Pass threshold |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1-01 | AUD1grandchild·A2reveal·A3POV·A4happy | shirt (base) | reveal | POV | happy | emotional | grandchild | 1 / LPV | O-base | R-base | $5 | CTR≥4%; hook≥28% |
| C1-02 | (change EXACTLY 1 axis vs 01) | shirt (base) | reveal | before/after | happy | emotional | grandchild | 1 / LPV | O-base | R-base | $5 | … |

→ In Stage 1 the **Material column stays fixed** (one baseline product) and you **change exactly 1 axis
between rows** so induction stays clean. Material becomes a varying column only from Stage 2 onward.

---

## PART F — Logging & convergence to "truth"

1. **Log every combo + result** (one Google Sheet: 1 row/ad, columns = matrix factors + per-stage metrics).
2. Each round: **filter winners → find shared factor levels** → update "beliefs" about which levels win.
3. **Refine the matrix** (drop losing levels, add new axes) **+ thresholds** (calibrate to real winners).
4. Even when you drift from the truth, understand **why** (which variable is noise, sample too small) → fix the method.
5. Tighter method + more rounds → **converges**. This is "scientizing" ad testing.

---

## One-line summary
**Matrix (variables) × multi-stage funnel (measure, prune by threshold) × isolate one axis at a time
(to induce) → repeat and calibrate thresholds → converge on the winning combo AND the reason it wins.**

*Foundations: `FB-ADS-PLAYBOOK.md`. Cold-start mechanics: `research/reference/new-pixel-coldstart-methodology.md`.*
