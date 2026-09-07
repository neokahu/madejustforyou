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

Each factor has several **levels** to test. Codes: `P` product/audience, `A` ads, `R` retail,
`D` delivery, `O` offer, `F` follow-up.

### Group 1 — Product / Audience (P)
| Code | Factor | Levels to test |
|---|---|---|
| P1 | Product / variant | product variants; different hero features |
| P2 | Core need / emotion | emotional gift · utility · novelty/gag · collectible |
| P3 | Recipient (persona) | spouse · parent · grandparent · best friend · pet |
| P4 | Audience interest angle | by hobby · by occasion · by job · by gift-buying behavior |
| P5 | Occasion / timing | everyday · holiday (Xmas, Mother's/Father's Day) · birthday |
| P6 | Market / geo | US · EU · AU · other |
| P7 | Price tier | low · mid · high |

### Group 2 — Ads (A)
| Code | Factor | Levels to test |
|---|---|---|
| A1 | Text angle | pain-point · benefit · emotional · humor · social-proof · scarcity |
| A2 | Media format | product-reveal · UGC · static · carousel · slideshow |
| A3 | 3-sec hook type | question · before/after · POV · surprise reveal · number |
| A4 | Music / mood | happy · emotional · trending · none |
| A5 | Imagery / color tone | warm · bright · minimal · messy-fun |
| A6 | On-screen caption | yes/no · bold-box style · keyword highlight |
| A7 | Length | ≤10s · 15–20s · 30s+ |
| A8 | Audience targeting | broad · narrow interest · lookalike · retarget |
| A9 | Optimization event | LPV/Traffic · ViewContent · Add to Cart · Purchase |
| A10 | CTA | Shop Now · Learn More · Get Offer |

### Group 3 — Retail / On-site (R)
| Code | Factor | Levels to test |
|---|---|---|
| R1 | Landing UI/UX | layout A/B · static gallery vs personalizer-first |
| R2 | Price & anchoring | flat · strikethrough anchor · % off |
| R3 | Reviews / social proof | few vs many · "X sold" badge · customer photos |
| R4 | Shipping/delivery message | free-ship threshold · clear delivery date |
| R5 | Sales-lift note | urgency/scarcity · warranty · "perfect gift for…" |
| R6 | Offer / bundle | single · combo · gift-with-purchase |
| R7 | Trust | payment badges · prominent return policy |

### Group 4 — Delivery / Media-buying (D) — *how you run it, not the content*
| Code | Factor | Levels to test |
|---|---|---|
| D1 | Placement | Feed · Reels · Stories · Advantage+ (auto) |
| D2 | Bid strategy | lowest-cost · cost-cap · bid-cap |
| D3 | Budget per ad set | low · mid · high (affects delivery) |
| D4 | Attribution window | 1-day click · 7-day click |
| D5 | Dayparting | hour/day scheduling |

### Group 5 — Offer (O) — *strongest conversion lever; separate from Retail*
| Code | Factor | Levels to test |
|---|---|---|
| O1 | Price point | low · mid · high |
| O2 | Discount depth | none · light · deep |
| O3 | Bundle / gift | single · combo · gift-with-purchase |
| O4 | Free-ship threshold | none · with threshold |
| O5 | Deadline urgency | none · flash-sale/deadline |
| O6 | Payment method | card · COD · installment |

### Group 6 — Follow-up / Retention (F) — *recovers Stage-3 orders*
| Code | Factor | Levels to test |
|---|---|---|
| F1 | Abandoned-cart recovery | email · SMS · both |
| F2 | Retargeting sequence | none · yes (sequence) |
| F3 | Upsell / cross-sell | none · yes |

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
| **1 Engagement** | Traffic / LPV | **A1–A7** (angle, media, hook, music, imagery, caption, length) + audience **P3/P4/A8** | all **R, O, F**; one **D** baseline | hook ≥ 28% **AND** link CTR ≥ 4% (kill < 18% / < 1.7%) | the winning **creative(s)** |
| **2 Intent** | Add to Cart | **R1 page UI/UX · R2/O2 price+anchor/discount · R3 reviews · O3 bundle · O4 free-ship · R5 note** | winning **creative + audience** fixed | ATC rate ≥ 7.5% (session) **or** cost/ATC ≤ baseline (kill < 2%) | winning **creative × page/offer** |
| **3 Purchase** | Purchase | **R4 delivery msg · R7 trust · O5 urgency · O6 payment · F1 cart-recovery · F2 retargeting · F3 upsell** | winning **creative × page/offer** fixed | CPA ≤ break-even **&** ROAS ≥ target-by-margin (click→purchase > ~1.5–3.2%) | winning **full combo → SCALE** |

**How to build combos each phase (concrete):**
- **Phase 1 — creative only.** Fix 1 baseline product/audience/offer/page. Build **N creative variants**
  that differ by **one creative axis at a time** (e.g., 8 ads: same everything, differ in hook × media ×
  music). Run ~$5 each on **LPV**. → keep the 3–4 clearing the Stage-1 threshold. *(Landing/offer/checkout
  are irrelevant here — do NOT vary them.)*
- **Phase 2 — page/offer on the winning creative.** Take the winning creative(s); build **on-site/offer
  variants** (e.g., 4 versions: price-anchor on/off × reviews few/many). Run on **ATC** with real budget.
  → keep the best page/offer.
- **Phase 3 — checkout/trust/follow-up on the winning creative × page/offer.** Build **variants** (e.g.,
  urgency on/off × cart-recovery email vs SMS). Run on **Purchase**. → the winner **scales**.

**Why layered, not all-at-once:** if Stage 1 also varied page/offer, you'd burn budget on changes that
cannot move hook/CTR **and** you couldn't attribute a creative win cleanly. Each stage isolates the one
factor group that actually moves *that* stage's metric — which is exactly what makes the induction clean.

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
- **Stage 1** ⟵ **creative / 3-sec hook** (dominant). Fails Stage 1 → change media/hook (Group A).
- **Stage 2** ⟵ **offer, price, reviews/social-proof, landing/product-page quality** (Groups O, R). ATC < 2% → page/price/trust problem.
- **Stage 3** ⟵ **checkout friction (~76% abandon), price/margin, trust** (Groups O, R). Delivery (Group D) affects all stages.
- **Audience:** retargeting inflates hook (30–45%) vs cold (18–28%) → judge **cold vs cold**.

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

Before launch, draw the tree: **Campaign → k media → n ads → each ad = one matrix combo code.**

Planning table (each row = 1 ad = 1 combo):

| Ad ID | Combo code | Media (A2) | Hook (A3) | Music (A4) | Text angle (A1) | Audience (A8) | Event (A9) | Retail set (R) | Stage | Budget | Pass threshold |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1-01 | P3spouse·A2reveal·A3POV·A4happy | reveal | POV | happy | emotional | broad | LPV | R-base | 1 | $5 | CTR≥4%; hook≥28% |
| C1-02 | (change EXACTLY 1 axis vs 01) | reveal | before/after | happy | emotional | broad | LPV | R-base | 1 | $5 | … |

→ The table shows how many media, how many ads, which combo each ad tests, and that you **change exactly
1 axis between rows** so induction stays clean.

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
