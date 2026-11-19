# Impact ranking — what moves paid short-form video ad performance, ranked by evidence

Research 2026-11-19. **Question:** which creative factors have the biggest effect on Meta Reels/Feed video ads
(purchase-optimized, mostly watched muted)? Test those first and fix the small ones as house standards.
**Scope:** MadeJustForYou, POD personalized gifts, US buyers, 15–25s mostly AI-generated captions-led video,
~$965 max per product × 5 products.

**Grades.** **[STRONG]** = large controlled or meta-analytic study, first-party or peer-reviewed, effect size published.
**[MODERATE]** = large dataset or first-party claim, but observational, old, or not on our format.
**[WEAK]** = vendor or practitioner claim, small sample, secondhand, or method not shown.
Numbers are quoted from the source. None are invented. Where the source was not re-opened in this session, the row says so.

---

## 0. The headline finding

1. **Creative is the biggest controllable driver of sales lift, much bigger than targeting.**
   NCSolutions meta-study of ~450 CPG campaigns (2023): creative = **49%** of incremental sales, brand 21%,
   targeting 11%, recency 5% ([Circana/NCS](https://www.circana.com/post/brand-loyalty-impact-on-sales)).
   The 2017 version, ~500 campaigns: creative 47%, reach 22%, brand 15%, targeting 9%, recency 5%, context 2%
   ([Nielsen 2017](https://www.nielsen.com/insights/2017/when-it-comes-to-advertising-effectiveness-what-is-key)).
   Marketers estimate creative at only ~19–20% ([Westwood One](https://www.westwoodone.com/blog/2024/04/22/marketers-vastly-understate-the-sales-effect-of-creative-and-significantly-overestimate-the-impact-of-targeting)).
   **[STRONG]**, with one caveat: these are CPG brands on TV and digital, not DTC gifts on Reels.
   **"Creative" in these studies means the whole ad (idea plus execution), not caption styling.**
2. **Within creative, the idea (concept/angle) and the first 3 seconds carry the variance.** Small craft details
   (caption length, caption timing, music choice) have no published effect sizes anywhere near this.
   They are hygiene: get them right once, then hold them fixed.
3. **What our budget can measure decides how we test** (internal `ad-science-foundations.md` §5b, power math):
   at 80% power, a hook-rate gap of 22%→28% needs ~814 impressions per arm. A 25%→28% gap needs ~1,700–3,400.
   Link CTR 1.2%→2.5% needs ~1,683. A conversion-rate comparison needs ~1,315 *clicks* per arm, which is
   unaffordable. **So we rank big factors on hook rate, hold rate and coarse CTR, and use purchases only as a
   break-even check, never to pick between creatives.**

---

## 1. Ranked factor table

Codes are from `marketing/facebook-ads/_ledgers/codebook.csv`.
Verdicts: **TEST-FIRST** = large or uncertain effect, cheap to measure. **TEST-LATER** = real but smaller, or only
measurable on CVR. **FIX** = house standard, not tested.

| # | Factor | Evidence of effect size (grade · source) | Metric it moves | Codes | Verdict / fixed value |
|---|---|---|---|---|---|
| 1 | **Concept / angle** (who is buying, for whom, why, what story) | Creative = 47–49% of sales lift **[STRONG, NCS]**. Weak creative means lift comes "primarily from media". Strong creative lifts sales and depends less on media **[STRONG, Nielsen 2017]**. ~5% of ads become winners across 550k+ Meta ads / ~$1.3B spend, so you need several real shots **[MODERATE, Motion via internal 01-03-hooks.md]**. Andromeda groups near-duplicate ads into one, so only *distinct* concepts get separate delivery **[MODERATE, practitioner reading of Meta's engineering post: runneth.com, admanage.ai]** | All: hook, hold, CTR, CVR | AN, BY, RC×OC, ST, PV | **TEST-FIRST** (R0) |
| 2 | **Hook / first 3 seconds** (opening visual + first caption) | Meta/Nielsen: up to **47%** of a video campaign's value is delivered in the first 3s **[MODERATE, Meta first-party, old]**. Same body with 3 hooks gave **18% → 38%** hook rate **[WEAK, AdLibrary anecdote]**. Ads still running at day 21 launched at 30%+ hook rate; ads dead by day 7 launched at 15–20% **[WEAK, AdLibrary]**. Median Meta hook rate is 28%, top 10% is 45% **[MODERATE, Benly 12k ads](https://www.adbeacon.com/2026-creative-benchmarks-are-out)** | Hook rate, then everything downstream | F, T, M, SU, ON | **TEST-FIRST** (R1) |
| 3 | **Frame-1 subject: people and visible relationship vs product alone** | Google/Kantar ABCD: ads that follow Attention, Branding, Connection ("humanize with people") and Direction give **+30% short-term sales likelihood** and **+17% long-term brand contribution** on average **[STRONG for the bundle, Google/Kantar 2021](https://support.google.com/google-ads/answer/14783551)**. No published split for faces alone. Internal rule: the giftee shown alone reads as lonely **[internal, untested]** | Hook rate, hold | SU, PC | **TEST-FIRST** (one axis in R1) |
| 4 | **When the product and personalization appear** (early vs pulsed) | ABCD: brand early and often **[STRONG bundle]**. Teixeira, Wedel & Pieters (*Marketing Science* 2010, "Moment-to-moment optimal branding"): a prominent early brand *raises* zapping, and short pulsed brand moments work better **[STRONG, peer-reviewed eye-tracking; not re-opened this session]**. **The two sources conflict**, so this is worth testing | Hook rate vs CTR (trade-off) | RV, VS | **TEST-FIRST** within R1. **FIX the floor:** product present (VS1+) from 0s |
| 5 | **Emotional register** | Teixeira, Wedel & Pieters (*JMR* 2012): **joy and surprise** keep viewers watching (less zapping), and the *velocity* of emotion matters **[STRONG, peer-reviewed; not re-opened]**. Ads work more through feeling than persuasion **[MODERATE, Binet & Field / IPA, internal]**. Gift givers are buying the recipient's smile **[STRONG lab, pmid:29920154, internal]** | Hold, hook | EM, T4/T5 | **TEST-LATER** as its own axis. It rides inside concepts in R0. Default EM1/EM2 |
| 6 | **Reason to buy / proof** (personalization legible, recipient reaction, reviews) | Gift psychology: givers buy thoughtfulness ("proof you paid attention"), not usefulness **[STRONG lab, internal §3]**. No ad-level effect size published for our category. Mainly moves CVR, which we cannot power **[internal power table]** | CTR, CVR | PF, AN | **TEST-LATER** (R2, read on CTR + ATC as weak signal) |
| 7 | **Production format** (cinematic mini-film vs creator-style vs hands/demo) | "Creator-led ads drive 70% higher CTR" **[WEAK, vendor blog, method not shown]**. Andromeda practitioners list format as the first diversity lever **[WEAK]**. Obvious AI ads can trigger a negative brand reaction **[WEAK, NielsenIQ via vendor]** | Hook, CTR | PX | **TEST-LATER**, or as a deliberate concept difference in R0. Do not run a separate format grid |
| 8 | **Body / storyline / pacing** (hold) | Of people who watch 3s, 65% reach 10s and 45% reach 30s **[MODERATE, Meta, old]**. A good hold rate is ~40–50% **[WEAK–MODERATE, vendors]**. No published ranking of story structures for DTC | Hold, CTR | ST, beat script | **TEST-LATER**. Fix the body only when hook is high and hold is low (Hook × Hold 2×2) |
| 9 | **Length** | Best Meta length band 15–30s **[MODERATE, Benly 12k ads]**. Meta guidance: ≤15s and message in the first 3s **[MODERATE, first-party]** | Hold, cost per result | — | **FIX** 15–25s, plus a ≤15s cut from the same edit |
| 10 | **Captions / on-screen text** | 92% of mobile users watch with sound off **[MODERATE, Verizon/Publicis 2019, n=5,616]**. FB video views up to 85% silent **[MODERATE, Digiday 2016]**. Captioned video ads gave +12% view time **[WEAK–MODERATE, Meta 2016, refuted as a precise number in our caption doc]**. **No source gives an effect size for caption length or timing.** | Hook, hold (only whether captions exist, not their length) | CT, LB, TM | **FIX:** captions always present. First caption by ≤0.5s (TM1/TM2). 1–7 words per card (LB1–LB2). Safe-zone layout. Caption *wording* is part of the hook, so it is tested only there |
| 11 | **Sound / music / VO** | Most plays are muted, so audio cannot carry meaning **[MODERATE]**. "Video ads *with* audio have 15% lower CPA" **[WEAK, analyst quoting Meta]**. ABCD: audio brand mentions help **[STRONG bundle, mostly YouTube with sound on]** | Small, for the muted majority | AU | **FIX:** a music bed (AU0) and a sync hit on the onset (AU1). No VO dependency. Do not test |
| 12 | **CTA / end card** | ABCD "Direction": a clear CTA is part of the +30% bundle **[STRONG bundle]**. No standalone effect size | CTR (small) | — | **FIX:** a spoken-style text CTA plus branded end card ≤2s, kept moving, not frozen |
| 13 | **Aspect ratio / placement** | No published data on 4:5 vs 9:16 performance; "+7% CTR"-type claims are anecdotes **[WEAK, internal feed-video doc]** | CPM, reach | — | **FIX:** 9:16 master plus 4:5 reframe; Advantage+ placements |
| 14 | **Offer / price** | Not a creative variable in the NCS split (price falls under "brand factors"). No video-level effect size found | CVR | — | **FIX** one store-wide offer during creative tests, so the offer does not confound the creative read |

**How to read the ranking.** Ranks 1–2 are where the published variance sits. Ranks 3–4 are cheap hook-rate
axes with a real evidence base. Ranks 5–8 are real but either bundled into concepts or only readable on
CVR/hold. Ranks 9–14 are hygiene: no source shows a large effect from *varying* them once they meet the
standard, so testing them spends budget on effects we cannot detect.

---

## 2. Recommended per-product plan (~$965 max)

**Assumptions.** $25 CPM (range $20–30). One ad per ad set, equal budgets, same schedule. ~800 impressions
per ad = **$20** (enough for large gaps such as 22%→28% hook). ~1,700 impressions = **$42.50** (enough for
3-point gaps or coarse CTR gaps). At $30 CPM every figure is about 20% higher, so the R3 reserve absorbs it.

### R0 · Concept discovery (5 concepts × 2 hooks) · 10 ads × 800 impr · **$200**
- **Purpose:** find which *idea* stops and pulls clicks. Concept is the #1 lever (§1 row 1).
- **Why 5 concepts × 2 hooks, not 2 concepts × 5 hooks:** the base rate of winners is ~5%, and Andromeda
  dedups look-alike ads. So the scarce thing is *distinct* ideas, not hook variants. Two hooks per concept
  stop one bad hook from killing a good concept (hook spread is wide, 18%→38%). Pooling the two hooks gives
  ~1,600 impressions per concept, enough for a ~6-point hook gap and a coarse CTR gap
  (1.2% vs 2.5% needs ~1,683).
- **Concludes:** concept ranking on pooled hook rate (primary) and link CTR (secondary). Hook-pair spread
  shows whether a concept is "hook-sensitive".
- **Decision:** keep the top 1–2 concepts. Drop any concept below 20% pooled hook or in the bottom CTR tier.
  If all concepts are below 20%, rebuild concepts. Do not run hook rounds on a dead idea.

### R1 · Hook grid on the winning concept · 2×2×2 factorial, 8 ads × 850 impr · **$170**
- **Axes (evidence-ranked):** (a) frame-1 subject, people with visible relationship (SU2/PC2) vs product or
  hands (SU1/SU4). (b) Personalization reveal, in the hook (RV1) vs pulsed by ~3s (RV2). This is the
  ABCD vs Teixeira conflict. (c) Format/trigger: the best two F×T families from R0.
  Onset (ON2/ON4) is **fixed** for every cell, since the motion-onset evidence is strong.
- **Why factorial:** each main effect pools 4 cells = ~3,400 impressions per level, enough for a 3-point
  hook gap.
- **Concludes:** which opening wins on hook rate and whether it holds on CTR.
- **Decision:** lock the opening recipe. Carry the top 2 cells forward.

### R2 · Reason to buy / proof · 4 ads × 1,700 impr · **$170**
- **Purpose:** on the winning concept and opening, vary what the body proves: legible personalization (PF1)
  vs recipient reaction (PF2) vs thought made visible (ST6/M10) vs reviews (PF5).
- **Concludes:** CTR (Tier A) plus ATC rate as a *directional* signal only (Tier B).
- **Decision:** pick the body. If hold is <30% on every arm, rewrite the body before scaling.

### R3 · Validation and break-even check · top 2–3 ads, consolidated ad set · **~$425**
- **Purpose:** buy enough purchases to check the absolute economics: ROAS vs break-even, and CPA vs margin.
  **Not** a creative comparison, because CVR is unpowered.
- **Optional:** if the R0 runner-up concept was close (within ~3 points of hook rate), spend ~$85 of this on
  its best hook to keep a second idea alive. This protects against fatigue.
- **Decision:** scale, iterate, or kill the product.

**Total ≈ $965.** Order = impact: concept → opening → reason → economics.

---

## 3. The current plan vs the evidence

Current plan: R0 5 concepts × 2 hooks; R1 hook grid (format / trigger / frame-1 subject / onset);
R2 reason to buy; R3 storyline grid. Fixed: sound, captions, length, VO, CTA, end card.

**Right:**
- **Concepts first, with 2 hooks each.** This matches the NCS/Nielsen ranking and the low winner base rate,
  and it protects against a hook confound. Keep it.
- **Sound, captions, length, VO, CTA and end card are fixed.** No published effect sizes justify testing them.
  This answers the earlier frustration correctly.
- **One ad per ad set, equal budgets.** This avoids the delivery-selection confound (Lewis & Rao,
  Gordon et al. 2019).
- **Hook rate and CTR as the decision metrics.** This matches what the budget can power.

**Wrong or weak:**
- **The R1 grid has 4 axes.** Format, trigger, frame-1 subject and onset at ~$965 per product spreads the
  impressions too thin for 3-point gaps. Onset has strong mechanism evidence, so fix it (ON2/ON4) rather
  than test it. Format and trigger are largely set by the R0 concept. Swap in **reveal timing (RV)**: it has
  a genuine, published conflict (ABCD vs Teixeira) and is cheap to resolve.
- **R3 storyline grid.** Body/storyline effects only show up on hold and CVR. Hold is cheap to read, but
  the evidence ranks the body below concept and opening, and CVR is unpowered. Make it conditional: run it
  only when hook is high and hold is low (the Hook × Hold 2×2). Use the budget for a break-even
  validation round instead, which the plan currently lacks.
- **Emotional register is not explicit.** It is bundled in concepts. That is fine for now, but log EM per
  concept so it can be read across products later.
- **Missing: a fixed offer during tests.** Without one, an offer change confounds the creative read.

---

## 4. Gaps (what no source answers)

1. **No published effect size for any single factor on DTC gift video on Reels.** The NCS and ABCD
   numbers are CPG / YouTube bundles. Transfer is assumed, not shown.
2. **No public hook-rate breakdown by hook or format type.** Motion, Foreplay, Varos and Benly publish
   medians and winner rates, not causal splits (internal hook-framework.md gap #1 confirmed).
3. **Andromeda's "diversity" reward is inferred** from Meta's engineering post and practitioner reports.
   There is no controlled study.
4. **Faces, UGC vs polished, and AI-look penalties:** only vendor claims (WEAK). Our own ledger will be the
   first on-niche data. Log every cell, nulls included.
5. **Teixeira et al. (2010, 2012) and Binet & Field are cited from memory and internal docs.** They were
   not re-opened this session. Read the full texts before R1 depends on the reveal-timing hypothesis.
6. **Purchase outcomes per creative stay unknowable at ~$965 per product.** Pooling across 5 products and
   quarters (same codes) is the only route to CVR-level learning.

## Sources
NCS/Circana 2023 https://www.circana.com/post/brand-loyalty-impact-on-sales ·
Nielsen 2017 https://www.nielsen.com/insights/2017/when-it-comes-to-advertising-effectiveness-what-is-key ·
Westwood One 2024 (above) · Google/Kantar ABCD https://support.google.com/google-ads/answer/14783551 and
https://business.google.com/us/think/future-of-marketing/youtube-video-ad-creative ·
Benly via AdBeacon https://www.adbeacon.com/2026-creative-benchmarks-are-out ·
Andromeda practitioners https://runneth.com/blog/andromeda-impact-on-bfcm, https://admanage.ai/blog/meta-andromeda ·
Teixeira, Wedel & Pieters, *Marketing Science* 29(5) 2010; *JMR* 49(2) 2012 ·
Lewis & Rao, *QJE* 2015 · Gordon et al., *Marketing Science* 2019 ·
Internal: `research/reference/ad-science-foundations.md` (§1, §3, §5), `video-ad-decomposition-2026.md`,
`feed-video-best-practice.md`, `short-form-caption-design.md`, `video-team/role-research/01-03-hooks.md`,
`video-team/hook-framework.md`, `marketing/facebook-ads/TESTING-MATRIX-FRAMEWORK.md`.
