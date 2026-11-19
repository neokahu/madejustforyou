# Impact ranking: what moves paid short-form video ad performance, and what to test first

Research date: 2026-11-19. This replaces the first pass of the same day, which read only 3 internal docs, ran
3 searches and cited Teixeira 2010/2012 from memory.

**Question.** Which creative factors most affect Meta Reels/Feed video ads? The ads are purchase-optimized,
mostly watched muted, 15–25s, mostly AI-generated and captions-led. Test the big factors first. Fix the small
ones as house standards.

**Scope.** MadeJustForYou: print-on-demand personalized gifts for US buyers. Budget is about $965 max per
product at a $25 CPM (range $20–30), one ad per ad set with equal budgets, across 5 products.

**Grades.**
- **[STRONG]**: peer-reviewed, controlled, or large and validated, with the effect size published.
- **[MODERATE]**: a large observational vendor dataset, or a first-party platform claim. It may measure a
  proxy (recall, attention) rather than sales, or come from another platform.
- **[WEAK]**: a blog, an anecdote, a third-hand number, or an undisclosed method.

Every number below is quoted from a source that was opened or read. Where a commonly repeated number could
**not** be verified, the row says so. No number is invented.

---

## 0. Sources read

### Internal (read in full: 20 files)

Each was read in full by this session or by its reading agents, and line counts were checked against `wc -l`.

**`research/reference/` (8 files)**
- `ad-science-foundations.md` (250 lines)
- `video-ad-decomposition-2026.md` (275)
- `script-method.md` (176)
- `ad-video-director-research.md` (322)
- `feed-video-best-practice.md` (76)
- `short-form-caption-design.md` (67)
- `RESEARCH-REPORT-2026-10-ad-production.md` (255)
- `ai-emotional-video-ad-playbook.md` (111)

**`research/reference/video-team/` (8 files)**
- `README.md` (235)
- `hook-framework.md` (233)
- `concept-framework.md` (429)
- `role-research/01-03-hooks.md` (231)
- `role-research/04-script.md` (244)
- `role-research/05-visual-director.md` (311)
- `role-research/06-07-edit-qa.md` (272)
- the previous `impact-ranking.md` (166)

**`marketing/facebook-ads/` (4 files)**
- `TESTING-MATRIX-FRAMEWORK.md` (537)
- `FB-ADS-PLAYBOOK.md` (106, in Vietnamese)
- `AD-KILL-RULES.md` (99)
- `_ledgers/codebook.csv` (138)

### External (24 searches; 21 primary pages opened and extracted; more seen only as snippets)

**Opened and extracted**
1. NCSolutions press release, Aug 2023: https://www.prnewswire.com/news-releases/in-advertising-the-balance-is-shifting-301897320.html
2. Nielsen 2017: https://www.nielsen.com/insights/2017/when-it-comes-to-advertising-effectiveness-what-is-key
3. Meta, Instagram video ad best practices: https://www.facebook.com/business/help/188534925073536
4. Meta, Reels ads (the 15 split tests): https://www.facebook.com/business/ads/facebook-instagram-reels-ads
5. Meta, Demystifying creative diversification: https://www.facebook.com/business/news/demystifying-creative-diversification
6. Google, ABCD creative best practices: https://www.thinkwithgoogle.com/future-of-marketing/creativity/creative-best-practices-youtube-ads
7. Google, *Creating YouTube ads that break through in a skippable world*: https://www.thinkwithgoogle.com/_qs/documents/953/creating-youtube-ads-that-break-through-in-a-skippable-world.pdf
8. TikTok, top-performing ads: https://ads.tiktok.com/business/en-US/blog/creative-best-practices-top-performing-ads
9. TikTok, resonance and ad effectiveness: https://ads.tiktok.com/business/en-US/blog/resonance-key-factor-ad-effectiveness
10. TikTok's own *5 Keys to Successful TikTok Creator Ads* PDF (Lumen/MetrixLab data): https://s3.amazonaws.com/media.mediapost.com/uploads/5_Keys_to_Successful_TikTok_Creator_Ads.pdf
11. System1 × TikTok, *The Long and the Short (form) of It*: https://system1group.com/creative-effectiveness-tiktok
12. Teixeira, Wedel & Pieters 2012, *JMR* 49(2), "Emotion-induced engagement": http://www.economicsofattention.com/site/assets/files/1054/emotion-induced_engagement-_teixeira_et_al-_jmr.pdf
13. Teixeira, Wedel & Pieters 2010, *Marketing Science* 29(5), "Moment-to-moment optimal branding": http://www.economicsofattention.com/site/assets/files/1083/teixeira-_et_al-_m2m_optimal_branding.pdf
14. Billo H1 2026 hook-rate benchmarks: https://billo.app/creative-insider/data-insights/hook-rate-benchmarks-h1-2026
15. Binet & Field, *The Long and the Short of It* (IPA; reproduced PDF): maynardpaton.com/…/SYS1-long-and-short-of-it.pdf
16. DataAlly UGC benchmarks: https://dataally.ai/blog/ugc-ad-benchmarks
17. Confect Black Friday 2026 Meta study: https://confect.io/tactics/black-friday-2026-meta-ads-study
18. Biddyco Meta video length: https://biddyco.com/blog-posts/meta-video-ad-length
19. Social Media Today on Meta, AppsFlyer and Dentsu (via Yahoo): https://finance.yahoo.com/news/meta-shares-ad-tips-based-193858384.html
20. Sepia Lab summary of Motion 2026 benchmarks: https://sepia-lab.com/en/blog/ad-creative-volume-benchmarks
21. Motion metrics help page: https://help.motionapp.com/en/articles/8991407-motion-metrics-for-meta-and-tiktok

**Seen only as snippets or fragments (not fully opened)**
- Pieters & Wedel 2004 (Tilburg PDF fragment)
- Meta "updated features for video ads" and the Andromeda "creative advantage" post
- Meta Al-Futtaim case
- System1 creator playbook
- Kantar "role of attention"
- datadrew hook-rate blog
- Marpipe blog
- the Yahoo analyst note quoting Meta reps

**Could not open**
- Motion's own 2026 Creative Benchmarks report: motionapp.com now redirects to Runneth.
- Varos, Foreplay, Segwise, AdManage and Benly published no factor-level splits that could be found. The Benly
  numbers below come from internal docs.

---

## 1. Ranked factor table

Codes are from `marketing/facebook-ads/_ledgers/codebook.csv`.

**Verdicts**
- **TEST-FIRST**: large or uncertain effect, cheap to read on hook rate, hold or CTR.
- **TEST-LATER**: real but smaller, bundled inside concepts, or only readable on CVR.
- **FIX**: a house standard, held constant and never tested.

**Rank 1. Concept / angle** (who buys, for whom, why, what story)
- Codes: AN, BY, RC×OC, ST, PV, EM
- Metric moved: everything (hook, hold, CTR, CVR)
- Verdict: **TEST-FIRST** (R0)
- Evidence:
  - Creative accounts for **49%** of incremental sales, against brand 21%, reach 14%, targeting 11% and
    recency 5%. Source: ~450 CPG campaigns, ML lift model (NCS 2023, #1). **[STRONG, but CPG on TV/digital]**
  - Nielsen 2017 (#2): weak creative gives weak lift, while "when the creative is strong, sales lift is higher
    and is affected less by media". Project Apollo 2006 put creative at 65% of lift. The popular "47%" split
    was **not on the primary page**, so cite it as "reported".
  - Binet & Field (#15): emotional campaigns are "more than twice as efficient" as rational ones.
    **[STRONG, long-term brand outcomes]**
  - Only ~5% of ads become winners (≥10× the account's median spend): 578,750 creatives, 6,015 brands,
    $1.29B spend (Motion via #20). **[MODERATE]**
  - Meta (#5): Andromeda favours creatives that are "truly different in look, feel, storyline, and message".
    **[MODERATE, no number]**
- **Missing:** no study splits concept variance from execution variance. Section 5 covers this.

**Rank 2. Hook: first 1–3 seconds** (frame-1 visual, onset, first caption)
- Codes: F, T, M, SU, ON, CT
- Metric moved: hook rate, then everything downstream
- Verdict: **TEST-FIRST** (R0 gives 2 hooks per concept; R1 is the factorial)
- Evidence:
  - TikTok Value-of-a-View meta-analysis (#9): **50%** of ad impact lands in the first 2s, and the first 6s
    carry **90%** of recall impact. **[MODERATE, measures recall]**
  - Meta/Nielsen 2016: "up to **47%** of value in the first 3s". **[MODERATE, old, secondary]**
  - Billo (#14), 88,329 Meta sales-objective ads, $122M spend: average hook rate **25.44%**, with a 7.47-point
    spread across industries. Gifting categories declined. **[STRONG for benchmarks]**
  - Same body cut 3 ways: 18%→38% hook rate (AdLibrary). **[WEAK]**
  - Vendor hook levers: payoff in frame 1 +5–12 points, text by 0.5s +4–9, motion in the first 0.5s +3–8.
    **[WEAK, self-reported]**

**Rank 3. Frame-1 human with a visible relationship** vs product or hands alone
- Codes: SU2/PC1–PC2 vs SU1/SU4
- Metric moved: hook rate; CPA (Meta)
- Verdict: **TEST-FIRST** (R1 axis A)
- Evidence:
  - TikTok Lumen/MetrixLab (#10): a person in the first 2s gives **+50% "hooking power"** and +32% ad
    recognition; direct address is 1.5× more likely to hook. **[MODERATE]**
  - Meta/AppsFlyer/Dentsu, 1.1M variations (#19): 9:16 + audio + emotional hook + human + text overlay gave
    **−16% CPA, +29% CVR**; a person plus expressive audio gave +8% conversions per dollar.
    **[MODERATE, app ads, bundled]**
  - DataAlly (#16): UGC hook rate 21.5% vs studio 15.0%, but hold was equal and CTR was −10%. **[MODERATE]**
  - Google (#7): a recognizable face or smiling characters in the first 5s raise viewing.
  - Counterpoint: our competitor corpus showed 0 of 3 faces in frame 1 (script-method NW). **[internal, n=3]**

**Rank 4. Product / personalization timing:** early and brief (pulsed) vs a sustained hero vs a late reveal
- Codes: VS, RV
- Metric moved: hook rate vs memory and CTR
- Verdict: **FIX** the floor at VS1+ from 0s, with no late reveal. **TEST-FIRST** RV1 vs RV2 (R1 axis B).
- Evidence:
  - Teixeira, Wedel & Pieters 2010 (#13), 31 TV ads, ~2,000 viewers, eye tracking: **pulsing** the brand
    (more often, shorter, same total exposure) cut avoidance by **~8% in simulation (range 2.0–19.1%) and
    ~10% in a lab experiment**. Long, central brand displays *raise* zapping. **[STRONG, confirmed in the PDF]**
  - System1 × TikTok (#11), 887 ads: strong branding in the first 2s gives **+88% memory lift** and +92%
    awareness lift, and "does not come at the cost of attention". **[MODERATE]**
  - TikTok (#8): product on screen gives **+65% brand affinity** and +25% recall. **[MODERATE]**
  - Google (#7): brand in the first 5s raises recall but also skips; logos floating off the product hurt.
    **[MODERATE]**
  - Competitor winners: 8 of 8 gift ads show the product by 1s; 0 of 19 use a story-film with a late reveal
    (script-method). **[internal corpus]**

**Rank 5. Emotional register and its shape** (joy rising, early surprise)
- Codes: EM, T4/T2
- Metric moved: hold, hook
- Verdict: **TEST-LATER** as its own axis; it rides inside concepts. Rule: open with surprise, end on rising
  joy (EM1/EM3).
- Evidence:
  - Teixeira, Wedel & Pieters 2012 (#12), 28 ads × 50 viewers, mean zapping 48%:
    - The *velocity* of joy cuts zapping most (coefficient −1.818, against −0.398 for the level of joy).
    - Joy beats surprise.
    - Surprise works early, by concentrating attention.
    - Rises in joy help more than falls hurt.
    - **[STRONG direction, small sample]**
    - The often-cited "emotion explains 72% / joy 58%" was **not found in the paper**. Do not cite it.
  - Binet & Field (#15). **[STRONG]**
  - System1 (snippet): "salesmanship" features cut emotion by 7–12%. **[MODERATE]**

**Rank 6. Reason to buy / proof** (personalization legible, reaction, reviews, process)
- Codes: PF, AN2
- Metric moved: CTR, then CVR
- Verdict: **TEST-LATER** (R2, read on CTR and hold)
- Evidence:
  - Givers buy the recipient's anticipated smile and "proof you paid attention" (pmid:29920154). **[STRONG lab]**
  - Etsy: 1–2% CVR under 10 reviews vs 10–15% at 500+. **[WEAK for ads]**
  - **No ad-level effect size exists for our category.**

**Rank 7. Production format** (mini-film, creator-style, hands/demo, product-hero)
- Codes: PX
- Metric moved: hook vs CTR (trade-off)
- Verdict: **TEST-LATER**. Vary it *between* R0 concepts; do not run a format grid.
- Evidence:
  - DataAlly (#16): UGC hook +44% but CTR −10%. Against static ads, the CTR gain is +16% within the same brand
    and CPA is +12%. **[MODERATE]**
  - Motion (#20): hit rate text-only 11.6%, image + text 8.75%, UGC 7.56%. **[MODERATE]**
  - System1 (#11): creator ads get +39% attention but about half the brand identification. **[MODERATE]**
  - Meta Al-Futtaim: 4× incremental conversions from UGC Reels. **[MODERATE, 1 case]**
  - NIQ 2024: obvious AI ads are rated more annoying and weaker on memory. **[MODERATE]**

**Rank 8. Body / storyline / pacing** (hold)
- Codes: ST, beat script
- Metric moved: hold, CTR
- Verdict: **TEST-LATER**, conditional on a high hook with low hold
- Evidence:
  - Narrative transportation meta-analysis (van Laer 2014): affect r = .57, identifiable character r = .20,
    imaginable plot r = .29. **[STRONG, persuasion rather than ads]**
  - Our failed film had 1 cut in 36.6s and ended on 3s of no motion, against a 333-day competitor winner at
    0.40 cuts/s. **[internal, n=1]**
  - No published ranking of story structures exists for direct-response.

**Rank 9. Length**
- Codes: none
- Metric moved: hold, CPM
- Verdict: **FIX** 15–25s plus a ≤15s cut
- Evidence:
  - Biddyco (#18), 421 videos, 21 brands, within-brand: **cost per result flat across lengths (0.94–1.03×)**;
    average watch is 3–5s at every length. **[MODERATE]**
  - Meta (#3): 6–15s "more effective". **[guidance]**
  - TikTok "21–34s +280%". **[UNVERIFIED]**

**Rank 10. Format / aspect ratio**
- Codes: none
- Metric moved: cost per result, delivery
- Verdict: **FIX** a 9:16 master with sound plus a 4:5 reframe; Advantage+ placements
- Evidence:
  - Meta (#4), 15 Reels split tests: 9:16 video with sound in safe zones gave **34.5% lower cost per result than
    image ads** (99.9% confidence), and 2× Reels delivery. **[STRONG for Meta; video vs image]**
  - 4:5 vs 9:16 claims are anecdotal. **[WEAK]**

**Rank 11. Captions / on-screen text**
- Codes: CT, LB, TM
- Metric moved: hook, hold (whether captions exist, not their length)
- Verdict: **FIX** captions always on; first card by ≤0.5s (TM1/TM2); LB1–LB2; boxed, in the safe zone.
  Caption *wording* is tested only as part of the hook.
- Evidence:
  - 92% of mobile viewers watch sound-off, n = 5,616 (Verizon/Publicis 2019). **[MODERATE]**
  - TikTok (#10): text overlay makes ads 1.4× more likely to hook. **[MODERATE]**
  - Meta 2016: "+12% view time". **[MODERATE as a direction; our caption doc refutes it as a precise number]**
  - **No source gives an effect for caption length, timing or animation.**

**Rank 12. Sound / music / VO**
- Codes: AU
- Metric moved: small for the muted majority
- Verdict: **FIX** music bed (AU0) plus a sync hit on the onset (AU1); the ad must not depend on VO
- Evidence:
  - Meta (#3): feed ads get 2.25× CTA CTR *when watched with sound on*, but "most people watch with sound
    off". **[MODERATE]**
  - Google (#7): music in the first 5s can hurt awareness. **[MODERATE]**
  - "Audio = 15% lower CPA" is **only in an analyst note**. **[WEAK]**

**Rank 13. CTA / end card**
- Codes: none
- Metric moved: recall, CTR (small)
- Verdict: **FIX** a create-verb CTA plus a moving branded end card ≤2s
- Evidence:
  - TikTok (#8): CTA cards give +45% recall and +19% likeability; this is not conversion. **[MODERATE]**
  - System1: hard CTAs reduce emotion. **[MODERATE]**

**Rank 14. Offer / price**
- Codes: none
- Metric moved: CVR, not CTR
- Verdict: **FIX** one store-wide offer for all test cells (see below)
- Evidence:
  - Confect (#17), 2.6B impressions, catalog ads in the Black Friday month:
    - voucher code: CTR +2%, **CVR +59%**
    - free shipping: CTR +12%, CVR +10%
    - price shown: CTR −6%, CVR +11%
    - "CVR predicts ROAS, CTR does not". **[MODERATE, correlational]**
  - No study of offers in video creative was found.

**How to read the ranking.**
- Ranks 1–4 are where measured variance and real disagreement sit, and all four read on hook rate or CTR,
  which our budget can power.
- Ranks 5–8 matter, but they ride inside concepts or only show on hold and CVR.
- Ranks 9–13 are hygiene. No source shows a large effect from *varying* them once they meet the standard, and
  for length the best within-brand data shows **no** effect on cost per result.
- **Offer (rank 14) is the exception.** It probably has a big effect, but on CVR, which we cannot power and
  which would confound every creative read. So it is fixed, not ignored.

**Why the offer is held fixed.** Confect shows offer elements move CVR by tens of percent while barely moving
CTR. Varying the offer between cells would swamp the creative signal on exactly the metric we cannot power.
- Pick one store-wide offer (e.g. free shipping, or one code) and show the *same* text in every cell's end
  card or primary text.
- Change the offer only between rounds, never within one, and log it per round.
- An offer test belongs on the site (A/B) after a creative winner exists, not in the ad grid.

---

## 2. Per-product round plan (about $965), ordered by impact

### Assumptions and what we can detect

**Delivery setup**
- One ad per ad set, equal daily budgets, same schedule.
- Advantage+ creative enhancements OFF on test cells.
- Read only settled days (in-day Meta metrics inflate).

**Detectable gaps at 80% power** (`ad-science-foundations.md` §5b)
- Hook rate 22%→28% needs ~814 impressions per arm.
- A 3-point hook gap needs ~3,400 impressions per arm.
- Coarse link CTR 1.2%→2.5% needs ~1,683 impressions per arm.
- CVR 1.4%→3.0% needs ~1,315 *clicks* per arm, which is unaffordable. **Purchases are a guardrail, never a
  selector.**

**Kill and advance gates** (TESTING-MATRIX D.1, reconciled)
- Hook rate: kill below 18%, red below 21%, advance at 28% or more. Billo's 25.44% is the market average.
- Link CTR: kill below 0.5%, weak below 1.0%, advance at 2.5% or more.
- Hold (15s ÷ 3s): below 10% means fix the body.

| Round | Ads × impressions | Impressions | $20 CPM | **$25 CPM** | $30 CPM |
|---|---|---|---|---|---|
| R0 Concept discovery | 10 × 800 | 8,000 | $160 | **$200** | $240 |
| R1 Opening factorial | 4 × 1,700 | 6,800 | $136 | **$170** | $204 |
| R2 Reason to buy | 4 × 1,700 | 6,800 | $136 | **$170** | $204 |
| R3 Break-even guardrail | top 2 ads, 17,000 total | 17,000 | $340 | **$425** | $317 (capped) |
| **Total** | | 38,600 | $772 | **$965** | $965 |

- At $20 CPM, the $193 left over funds the R0 runner-up concept's best hook inside R3. That gives a second
  live idea and protects against fatigue.
- At $30 CPM, R0–R2 keep their impression targets ($648) and R3 shrinks to $317, about 10,600 impressions.
  That is still enough for the guardrail logic below at ≥2.5% CTR. **Never cut R0 impressions to save money.**
  An under-powered R0 is the most expensive mistake, because every later round builds on its winner.

### R0: Concept discovery, 5 concepts × 2 hooks (10 ads × 800 impressions, $200)

**Purpose.** Find which idea stops people and pulls clicks. Concept is the largest lever (rank 1), and only
~5% of ads win, so the scarce resource is distinct ideas.

**Why concepts, not hooks, in discovery**
- **Base rate.** With ~5% winners, 5 distinct shots beat 5 variants of one idea.
- **Andromeda.** Meta clusters near-duplicate ads, so hook-only variants of one concept compete for the same
  delivery.
- **Insurance.** The 2 hooks per concept (different frame-1 mechanism, not just a caption swap) stop one bad
  hook from killing a good concept.
- **Power.** Pooling the 2 hooks gives 1,600 impressions per concept: enough for a ~6-point hook gap and,
  almost, a coarse CTR gap.
- **Diagnostics.** The spread between a concept's two hooks shows whether that concept is hook-sensitive.

**Held fixed:** offer, length band, captions spec, audio spec, CTA/end card, 9:16 + 4:5, product visible from
0s (VS1+).

**Varies:** concept, at least 3 distinct AN codes and at least 2 PX/EM values across the 5. Code and log
everything, nulls included.

**What it concludes.** A concept ranking on pooled hook rate (primary) and link CTR (secondary). A concept's
score is the mean of its ads, not its best ad.

**Decision**
- Keep the top concept, plus the runner-up if it is within ~3 hook points.
- Drop any concept below 18% pooled hook rate or below 1.0% CTR.
- If every concept is below 21%, rebuild the concepts. Do not polish hooks on a dead idea.

### R1: Opening factorial on the winning concept, 2×2 (4 ads × 1,700 impressions, $170)

Both axes have strong mechanism evidence, and their direction is genuinely uncertain for our format:
- **Axis A, frame-1 subject:** a human with a visible relationship (SU2 + PC2) vs product or hands (SU4, VS2).
  The TikTok and Meta human-on-screen lifts conflict with the face-free competitor corpus.
- **Axis B, personalization reveal:** in the hook, 0–1s (RV1), vs a brief early cue then a payoff by ~3s
  (RV2). This sets System1's early branding against Teixeira's pulsing.

**Held fixed:** onset ON2/ON4 (motion onset is strong evidence, and our static test crashed), caption timing
TM1/TM2.

**Why a factorial.** Each main effect pools 2 cells, giving 3,400 impressions per level. That is enough for a
~3-point hook gap, and a coarse CTR read comes for free.

**What it concludes and decides.** The opening recipe for this product. Lock the winning level on each axis
whenever the gap is at least 3 points. Otherwise keep the cheaper-to-produce level. Read the interaction
directionally only, because it is under-powered.

### R2: Reason to buy / proof on the winning concept and opening (4 ads × 1,700 impressions, $170)

**Arms (body varies, opening frozen and frame-identical):**
- PF1: personalization legible on the real product
- PF2: recipient reaction
- ST6/M10: thought made visible
- PF5: real reviews/photos, if the product has them; otherwise PF3

**What it concludes.** Which proof earns the click: CTR is primary, hold secondary. ATC rate is logged as
directional only.

**Decision.** Pick the body. If hold is below 10% on every arm, rewrite the body (beat script) before R3.

### R3: Break-even guardrail on the top 2 ads, consolidated (≈17,000 impressions, $425)

**Purpose.** Check absolute economics, not compare creatives.

**Break-even maths**
- Break-even ROAS = 1 ÷ gross margin.
- On the MJ4U-111 economics (~$45 AOV) the break-even CPA is ~$23–27.
- 17,000 impressions at 2% CTR gives ~340 clicks. At 2% CVR that is ~7 purchases: enough for a
  pass/fail on CPA, not a ranking.

**Rules**
- **Kill:** spend ≥ 3× break-even CPA (≈$75) with 0 purchases, on settled days.
- **Pass:** CPA ≤ break-even across ≥3 purchases. The product graduates to scaling and fresh-concept refresh.
- **Fix the site, not the ad:** CPA between 1× and 2× break-even with CTR ≥2.5% and many ATCs but few
  checkouts. This is MJ4U-111's pattern of 25 ATC and 0 purchases.

### Conditional, not default: storyline grid

Run a storyline grid only when R0–R2 produce a hook ≥28% with hold below 10% (the Hook × Hold 2×2). Fund it
from R3's reserve, and only if R3 passes.

---

## 3. Cross-product: when can we trust our own ranking?

**Rule for reading a code** (concept-framework): at least 4 ads per code, across at least 2 concepts or
products, with the code not aliased.

**Opening factors (R1 axes)**
- Each product gives one clean replicate of each main effect (3,400 impressions per level).
- **After 3 products**: ~10,000 impressions per level, enough for a ~2-point pooled gap, plus a sign-consistency
  check.
- **After 5 products**: confident on direction if the sign matches in 4 of 5.
- That makes **12–20 R1 ads** in total.

**Concept-level codes (AN, PX, EM, ST)**
- 5 concepts × 5 products = 25 concepts, about 50 R0 ads.
- With 8 AN codes, that is only ~3 concepts per AN code, so **only the 3–4 most-used angles become readable**,
  and only after all 5 products.
- PX and EM have fewer levels (6 and 5), so their main effects become readable at ~25 concepts if each level
  is used in at least 4 ads across at least 2 products. **Plan the R0 slates jointly across products to
  guarantee that coverage.**

**Proof (R2)**
- 4 arms × 5 products = 20 ads.
- That supports a pooled CTR ranking of the 4 proof types after ~4 products.

**CVR / CPA factors**
- **Not confirmable within 5 products.** About 1,315 clicks per arm would mean ~$1,300+ per arm at our CPC.
- Purchases only become informative when pooled across products and quarters under the same codes.

**Bottom line.** About **70–90 ads across 5 products** (10 R0 + 4 R1 + 4 R2 + 2 R3 per product) confirm the
opening axes and the main proof types on our own data. The concept ranking stays partial and directional, and
so does the CVR ranking.

---

## 4. The current deck plan against the evidence

The deck plan:
- R0: 5 concepts × 2 hooks
- R1: hook grid (format, trigger, frame-1 subject, onset)
- R2: reason to buy
- R3: storyline grid
- Fixed: sound, captions, length, VO, CTA, end card

**What it gets right**
- **Concepts first, 2 hooks each.** Matches NCS/Nielsen (creative and idea dominate), the ~5% winner base rate
  and Andromeda's demand for distinct creatives.
- **Fixing sound, captions, length, VO, CTA and end card.** Supported by the evidence:
  - length has no within-brand effect on cost per result (Biddyco)
  - audio does not reach a 92% sound-off audience
  - no source measures caption length or timing effects

  The user's intuition that these are minor is consistent with every source found.
- **One ad per ad set, equal budgets, deciding on hook rate and CTR.** This is the only design our budget can
  power, and it avoids the delivery-selection confound (Lewis & Rao 2015; Gordon et al. 2019).
- **Reason to buy as its own round.** Proof is the strongest lab-backed purchase driver for gifts.

**What it gets wrong or leaves weak**
1. **The R1 grid has 4 axes.** At ~$965, a 4-axis grid leaves too few impressions per level for 3-point gaps.
   - Fix onset (ON2/ON4): the evidence and our own static-open failure already decided it.
   - Format and trigger are mostly set by the concept and get tested across concepts in R0.
   - Keep frame-1 subject and add **reveal timing (RV)**, the axis with a genuine published conflict.
2. **R3 storyline grid by default.** Body effects show on hold and CVR. The evidence ranks them below concept,
   opening and proof, and CVR is unpowered. Make it conditional (Hook × Hold) and replace the default R3 with
   a **break-even guardrail**, which the plan lacks. Without one, a product can "win" every creative round and
   still lose money.
3. **The offer is not in the fixed list.** Offer elements move CVR by tens of percent (Confect). Add "one
   store-wide offer, identical in every cell" to the fixed factors.
4. **The late-reveal house style** (film-studio Rule 8, product at ~60%) conflicts with:
   - rank 4: product visible from 0s, pulsed
   - the 0 of 19 competitor story-films with a late reveal

   Keep the film as one R0 concept if wanted, but with VS1+ from frame 1.
5. **Emotion is implicit.** Log EM on every concept and write the arc as "surprise early, joy rising to the
   end", the shape Teixeira 2012 found keeps viewers.

---

## 5. Gaps and conflicts between sources

**Gaps (no source answers these)**
1. **Concept vs execution variance.** No study splits concept variance from execution variance. The ranking of
   concept above hook rests on the NCS "creative" share (idea plus execution), the winner base rate and
   Meta's diversity guidance, not on a direct decomposition. **[inference]**
2. **No hook-rate split by hook type, format or people-on-screen.** Billo publishes only averages. Motion's
   hook-tactic hit rates could not be opened (the site redirects). Varos, Foreplay, Segwise, AdManage and Benly
   publish no factor splits that could be found. Marpipe's "image drives most variance" is unverified.
3. **Mostly proxy outcomes, little purchase data.** TikTok, System1, Google and Kantar mostly measure recall,
   awareness or attention, and NCS measures CPG sales. Purchase-level evidence on Meta comes only from:
   - Meta's 15 Reels split tests (video vs image)
   - Meta/AppsFlyer/Dentsu (app ads, bundled, "up to")
   - Confect (catalog, correlational)
4. **Not verified, so not cited as fact:**
   - Nielsen "47%"
   - Kantar "brand in first 5s"
   - Teixeira "72% / 58%"
   - Meta "5–10 themes +24% ROAS"
   - "audio −15% CPA"
   - TikTok "21–34s +280%"
   - Motion hook-tactic hit rates
5. **Formats not covered.** No source studies AI-generated gift ads, muted Reels specifically, or caption
   length or timing.

**Conflicts**
1. **Early brand:** System1 says it is free (+88% memory) and Google says it raises skips. Teixeira resolves
   much of this: *sustained, central* branding drives avoidance, while *brief, repeated* cues help. A short
   product cue at 0s, pulsed again, satisfies both. R1 axis B tests the remaining question.
2. **People in frame 1:** platform data (+50% hooking, −16% CPA bundle) conflicts with the face-free
   competitor winners (0/3) and with DataAlly (UGC hook up but CTR −10%). Tested in R1 axis A.
3. **UGC:** higher hook rate (DataAlly) but lower hit rate (Motion: UGC 7.56% vs text 11.6%), and lower CTR
   and higher CPA within brand. A higher hook rate is not a higher purchase rate.
4. **Length:** Meta says 6–15s; internal docs say 15–25s (competitor median 21.2s); one playbook says under
   45s; Biddyco finds no cost-per-result effect. Resolved by fixing 15–25s plus a ≤15s cut.
5. **Captions +12%:** cited as Meta first-party, refuted as a precise number by our caption doc. Captions stay
   fixed either way.
6. **Hook and hold thresholds differ across internal docs:**
   - hook kill <15%, <18%, <20% or <21%
   - hold "40–50%" vs "12–25%", from different denominators

   This doc uses TESTING-MATRIX D.1 (hook kill <18%, red <21%, advance ≥28%; hold = 15s ÷ 3s, PAR 12–25%).
   The other docs should be reconciled to it.
7. **One ad per ad set:** FB-ADS-PLAYBOOK §6 and TESTING-MATRIX call it legacy, while concept-framework §4c
   requires it for causal reads. For *tests* it stays. Consolidation is for scaling (R3) only.
8. **Advantage+ creative:** TESTING-MATRIX says ON (+22% ROAS, a figure that Meta's page ties to targeting, not
   creative). README and QA require OFF in test cells. Keep it OFF in tests.
