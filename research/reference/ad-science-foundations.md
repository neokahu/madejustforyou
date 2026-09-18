# Ad Science Foundations — psychology, marketing science, and a power-aware testing system

> 📄 **Google Doc mirror:** https://docs.google.com/document/d/14ox0fF4Cb6rOA6gejRIi8EmXYhMSPMXnVnJN4bAEh8Q/edit
> *(the Markdown file in this repo is the source of truth; re-import after edits)*

Research 2026-09-18. **Why this exists:** decomposing Macorner/Wander Prints tells us what *they* landed on.
That is a **local optimum and a ceiling** — copy it and we can at best tie. This doc is the first-principles
layer: peer-reviewed psychology of attention, self-relevance and **gift-giving**, the marketing-science
evidence base, and — most importantly — **what our budget can and cannot statistically learn.**
Competitor teardowns become *priors and reference*, not the source of truth.

**[PRIMARY]** = peer-reviewed/primary · **[EVIDENCE-BASE]** = large industry meta-analysis · **[OPINION]**.

> **The single most important finding:** at our planned budget a **conversion-rate comparison between two
> creatives costs ~$1,315** to run with 80% power. Our entire Phase-1 tournament is **$360**. But a
> **hook-rate comparison costs ~$21.** Statistics, not preference, therefore dictates where we run
> experiments and where we may only apply guardrails. See §5 — it inverts our current framework.

---

## 1. Attention — what actually captures and holds it

**① Motion ONSET beats motion. This corrects my own earlier advice.** Retinal ganglion cells produce an
*alert response* to motion onset; "motion onset is very effective at capturing attention and is **more
salient than smooth motion**" `[PRIMARY: pmcid:PMC3711149]`. A saliency model for dynamic scenes reproduces
the same **motion-saliency asymmetry**, where sudden-onset movement dominates `[PRIMARY: pmid:23314730]`.
- **Implication:** the goal is *not* "more motion." Continuous smooth drift — exactly what our clips do — is
  the **least** salient kind of movement. The arresting unit is a **stillness → sudden movement transition**.
- **This changes `motion_qa.py`:** mean motion is the wrong statistic. We need **onset events** (the
  derivative — how often motion jumps from near-zero to high), not the level. See §6.

**② Novelty and salience are distinct and compete** `[PRIMARY: pmid:32088400]`. A "salient" frame is not
automatically a *novel* one. In a feed of aspirational gift creative, the novel move may be the
*un*-polished frame — consistent with the pattern-interrupt literature, and it gives that practitioner
advice a mechanism rather than a vibe.

**③ Stimulus-driven capture is not unconditional.** Capture is modulated by task demands, display
probability and available resources `[PRIMARY: pmid:20377287, pmcid:PMC2668614, pmcid:PMC4099520]`.
Capture also involves an **evaluative stage** that decides behavioural significance `[PMC4099520]` — so an
interrupt that grabs the eye but signals "irrelevant ad" is spent for nothing. **Interrupt + immediate
relevance, or the capture is wasted.**

**④ The attention–memory threshold: ~2.5 seconds.** You need ~2.5s of *actual attention* before there is a
chance of influencing memory, and **~85% of digital ads never get there** `[EVIDENCE-BASE: Nelson-Field /
System1]`. Related: **less than a quarter of "viewable" time is actual attention**, and platforms have an
**attention elasticity** — a structural cap that limits attention *regardless of creative quality*.
- **Implication:** our real target is not "watched" — it is **≥2.5s of attention**. It also means part of
  our outcome is set by the platform and is not ours to win, which argues for judging creative *relatively*
  within a platform, never against cross-platform benchmarks.

---

## 2. Self-relevance and personalization — why it works, and its real limits

Personalization is our whole product, so its mechanism matters — and the literature is more restrictive
than the marketing folklore.

**What holds:** a person's own name elicits a large **N250 ERP component, indexing attentional capture**
`[PRIMARY: pmid:21256923]`. People **overestimate the duration** of their own name — self-relevant stimuli
get more processing time `[PRIMARY: pmid:31707077]`. Self-referential encoding produces a robust memory
advantage `[PRIMARY: pmid:38963906]`.

**What does NOT hold — three disconfirmations we must respect:**
- Own-name attention effects are **temporary and conditional**, appearing only when enough resources are
  available `[PRIMARY: pmid:18413272]`; self-face advantages are **not** driven by automatic capture
  `[PRIMARY: pmcid:PMC4206440]`.
- The advantage requires **conscious awareness** of the self-relevant cue `[PRIMARY: pmid:30218945]`.
- **Decisive:** "**Merely presenting one's own name along with target items is insufficient** to produce a
  memory advantage… critical role of **relational processing**" `[PRIMARY: pmcid:PMC6368470]`.

**The inference that changes our creative — and it is not obvious.** In our ads the scroller is the
**giver**; the name on the product belongs to the **recipient**. So *self*-reference does not apply to the
viewer at all. Flashing a stranger's name ("MARGARET") buys us nothing — and even for the recipient, a
name alone is insufficient without relational processing. What we can engage is **close-other relational
processing**: the ad must make the viewer *relate the artefact to their own specific person.*
- **Therefore: name the RELATIONSHIP, not the name.** "Your grandma's name on it" / "for the grandma who
  says don't get me anything" does relational work that a displayed name does not.
- This predicts a **testable** creative contrast: *displayed-name reveal* vs *relationship-cued reveal*.
  A hook-rate test between them costs ~$21 (§5). **This is our highest-value first experiment.**

---

## 3. Gift-giving psychology — the most specific and most neglected layer

This is a real literature, it is about exactly our transaction, and nothing in our repo uses it.

**① The smile-seeking hypothesis — reframes the reaction shot entirely.** Givers "often do not choose what
their recipients most want"; they are motivated and rewarded by the recipient's **immediate affective
reaction** (the smile at the moment of opening) as distinct from the recipient's overall satisfaction
`[PRIMARY: pmid:29920154]`.
- **Implication:** the reaction shot is **not "social proof."** The anticipated smile **is the product the
  giver is buying.** Our own decomposition ranks "recipient's genuine reaction" as proof #1 for the right
  outcome but the wrong reason — it is not evidence, it is the **benefit**. That means the reaction belongs
  in the **hook**, not in a proof beat at second 20.

**② Giver–receiver asymmetry is systematic.** Givers prefer exclusive-but-smaller items; receivers prefer
less luxurious, more **useful** ones `[PRIMARY: pmid:15901395]`. Givers **underestimate** how thoughtful
receivers find more-desirable partial gifts `[PRIMARY: pmid:28914152]`. Surrogates import their own
preferences when choosing for others `[PRIMARY: pmid:36048054]`.
- **Implication:** we sell to the **giver**, so we must sell the giver's decision criteria — thoughtfulness,
  uniqueness, "proof you paid attention" — **not** the recipient's utility. This validates our
  "feel truly seen" angle mechanistically, and warns against usefulness/quality-led messaging on cold traffic.

**③ "It's the thought that counts" is conditional.** Givers' thoughts increase receivers' appreciation
**only when the receiver is cued to consider the giver's thought** `[PRIMARY: pmid:22774790]`.
- **Implication:** a personalized keepsake is a **thought made physically visible and un-ignorable** — it
  supplies the cue the literature says is required. That is the strongest scientific case for the category
  itself, and it is an argument to show the *act of specifying* (choosing the names), not just the result.

**④ Closeness is the deliverable.** Feasible (vs desirable) gifts make recipients feel **psychologically
closer** to the giver `[PRIMARY: pmid:30027819]`. Gifts have social meaning whose reward value depends on
giver and gift type `[PRIMARY: pmcid:PMC4547715]`.

**⑤ A segmentation signal.** Recipient-centric gifts — explicitly including **"customized with a
recipient's name"** — are less about the giver and **less likely to foster social closeness** for
narcissistic givers, who avoid them `[PRIMARY: pmid:39425564]`.
- **Implication:** our buyer skews **relationship-focused, low-narcissism**. Status/flex framings
  ("be the favourite child") may actively select the wrong buyer. That contradicts one of our own hooks and
  is testable.

---

## 4. Marketing science — what generalizes beyond one niche

- **Growth comes from penetration, not loyalty; light buyers matter most** `[EVIDENCE-BASE: Ehrenberg-Bass]`.
  For us: broad reach over narrow retargeting-heavy plans — consistent with the broad-default we already run.
- **Mental availability = breadth/depth of memory links, built on Category Entry Points (CEPs)** — the cues
  (mood, event, need, time) that make someone think of the category `[EVIDENCE-BASE]`.
  **This reframes our 12-angle library:** for a gift store the CEPs *are* **occasion × relationship ×
  life-event** ("Mother's Day", "grandma's 80th", "my dog just died"). Angles should be written as CEPs so
  each one is a retrieval cue we own, not just a pitch.
- **Distinctive Brand Assets** are memory structures that **decay without reinforcement** `[EVIDENCE-BASE]`.
  We currently have essentially one (a logo end card) — and §0 of the director research shows it plays as
  3 seconds of frozen zero-motion. Worse than nothing.
- **Fluent devices** (a consistent recurring character/device) **overperform** on market-share and profit
  gain `[EVIDENCE-BASE: System1/WARC]`. A recurring character across our films is a real, cheap lever we
  are not using.
- **Advertising works more through association and feeling than persuasion** `[EVIDENCE-BASE: Binet & Field;
  Feldwick & Heath, "60 Years of Using the Wrong Advertising Model"]` — the evidential backing for our
  emotion-arc-over-PAS decision, which until now rested on a LAST-RESORT citation.

---

## 5. ⭐ The testing system — power-aware, because the economics of measurement are brutal

### 5a. The hard external evidence
Lewis & Rao, **QJE 2015**, 25 large field experiments, $2.8M spend, most reaching millions `[PRIMARY]`:
- **Median confidence interval on ROI is over 100 percentage points wide.**
- Individual-level sales are wildly volatile — **coefficient of variation ≈ 10** is common.
- Informative experiments "can easily require **more than 10 million person-weeks**."
- Only **3 of 25** experiments were powered to distinguish a *blockbuster* 50% ROI from 0%; the median would
  need to be **9× larger**. "Reliably distinguishing a 50% from 0% ROI is typically **not possible with a
  $100,000 experiment involving millions of individuals.**"
- **Selection bias from targeted delivery is "a crippling concern" for observational methods** — corroborated
  by Gordon, Zettelmeyer, Bhargava & Chapsky (*Marketing Science* 2019) on Facebook field experiments.

### 5b. What that means at OUR budget — computed, not asserted
Two-proportion tests, α=0.05 two-sided, **80% power**, at our own D.1 PAR assumptions (CPM $13, CPC $0.50):

| Comparison | n per arm | unit | **Cost, both arms** | Verdict |
|---|---|---|---|---|
| Hold rate 12% → 30% | 76 | impressions | **$2** | ✅ trivial |
| Hook rate 22% → 28% | 814 | impressions | **$21** | ✅ **run these** |
| Link CTR 1.2% → 2.5% | 1,683 | impressions | **$44** | ✅ affordable |
| Hook rate 25% → 28% (3pt) | 3,393 | impressions | **$88** | ✅ affordable |
| Link CTR 2.0% → 2.5% | 13,806 | impressions | **$359** | ⚠️ = our whole budget |
| ATC rate 4.6% → 7.5% | 1,057 | clicks | **$1,057** | ❌ unaffordable |
| **CVR 1.4% → 3.0%** | 1,315 | clicks | **$1,315** | ❌ **3.7× total budget** |
| CVR 2.0% → 2.5% | 13,806 | clicks | **$13,806** | ❌ out of the question |

### 5c. The consequence — this INVERTS our framework
`TESTING-MATRIX-FRAMEWORK.md` Part B.1 says Stage 1 is "a **weak filter** for gifts… the real decisions live
at **Stage 2–3**." **The statistics say the opposite.** Stage 1 is the *only* stage where we can afford a
properly powered experiment; Stage 2–3 comparisons are 3–40× our budget. So:

| Tier | Metrics | Status at our budget | How to treat it |
|---|---|---|---|
| **A — Experiment** | hook rate, hold rate, coarse link CTR | **Powered for $2–$90** | Real A/B science. Pre-register, one hypothesis, report effect + CI. **This is where we learn.** |
| **B — Weak signal** | fine CTR distinctions, ATC rate | $350–$1,100 — one per quarter at most | Directional only. Never a kill on one read. |
| **C — Guardrail, NOT a test** | CPA, ROAS, click→purchase CVR | $1,300–$13,800 per comparison | **Never compare creatives here.** Use only as an absolute economic red line vs break-even (§ the tournament doc's per-product ROAS lines). A "winner" on ROAS at $66 spend is noise. |

**Our 5-tier grading of CPA/ROAS at $47–66 of spend is statistically meaningless as a comparison.** It is
still a legitimate *guardrail* (am I above break-even? stop). The doc must say which of the two it is doing.

### 5d. Internal validity — the confound inside our own method
Meta's delivery optimisation **assigns different audiences to different ads**. So multiple ads in one ad set
is **not a randomized experiment** — it is precisely the targeted-delivery selection bias Lewis & Rao call
crippling. Our framework's "consolidate a few per ad set and let delivery sort" is good *media buying* and
**invalid inference**: you cannot then attribute the difference to the creative.
- **Fix, in order of rigour:** (1) Meta's built-in **A/B Test** tool (randomized user split) for any Tier-A
  claim; (2) one creative per ad set with equal budgets and matched schedules; (3) conversion-lift / holdout
  for anything Tier C — accepting that at our spend it will be underpowered and should be run for
  *direction over quarters*, not per-test decisions.
- **Keep the consolidated ad set for scaling. Never read a causal claim off it.**

### 5e. Experimental discipline (cheap, and it is what makes this science)
1. **Pre-register** before launch: hypothesis, mechanism from §1–§4, manipulation, primary metric,
   min-sample gate, decision rule. No post-hoc metric switching.
2. **One manipulation per Tier-A test.** Diverse-concept batches are *discovery* (hypothesis generation);
   they are not tests and must not be reported as such.
3. **No peeking.** Sequential looks at accumulating data inflate false positives. Fix the sample in advance;
   if you must monitor, use the T0 red lines — which are *safety* stops, not significance tests.
4. **Count your comparisons.** 18 ads pairwise = 153 comparisons; at α=0.05 ~8 "winners" are pure chance.
   Compare against a **pre-named control**, not all-vs-all.
5. **Report effect size + CI, never a bare winner.** Given Lewis & Rao, the CI is the finding.
6. **Log every result — including nulls.** Our accumulating internal database is the only source that will
   ever be *exactly* on-niche; the published literature never will be.

---

## 6. Concrete revisions this forces on existing docs
| Doc | Revision |
|---|---|
| `research/scripts/motion_qa.py` | Add a **motion-onset** metric (derivative/jump events), not just mean level — §1①. Mean motion over-credits smooth drift, the least salient motion there is. |
| `ad-video-director-research.md` | Hook target becomes **≥2.5s of attention** and an **onset event in frame 1**, not "high mean motion". Add the reaction shot to the **hook** (§3①). |
| `video-ad-decomposition-2026.md` | Proof ranking: recipient's reaction is **the benefit, not proof** (§3①). Angle library → rewrite as **CEPs** (§4). Personalization hook → **relationship-cued, not name-displayed** (§2). |
| `TESTING-MATRIX-FRAMEWORK.md` | Add the **power ladder** (§5b–c): Stage 1 = experiment, Stage 2 = weak signal, Stage 3 = guardrail. Label the CPA/ROAS tiers explicitly as guardrails, not comparisons. Add the **delivery-selection confound** (§5d) and require Meta's A/B tool for causal claims. |
| `PHASE1-TOURNAMENT-3-products.md` | The "tournament" can legitimately rank on **hook/hold/CTR** (Tier A). It **cannot** rank products on ROAS at $47–66. Reframe the product decision as economics + Tier-A creative signal, not a conversion test. |

## 7. Honesty and limits
- **Transfer risk is the main threat.** §1–§3 are lab findings (ERP, eye-tracking, gift-choice vignettes).
  None were run on Meta feed video for personalized gifts. They generate **strong, mechanism-backed
  hypotheses**, not guarantees. Every one must go through §5's Tier-A ladder.
- **§4 is industry meta-analysis, not peer review** — large-sample and replicated, but largely
  proprietary datasets (IPA, System1, Ehrenberg-Bass) that we cannot audit.
- **Lewis & Rao is about ROI measurement at scale.** Our Tier-A engagement metrics are far cheaper to
  measure than sales precisely because they are high-frequency and low-variance. Their pessimism applies to
  **Tier C**; it does **not** mean we can learn nothing.
- **The power table assumes** CPM $13, CPC $0.50, independent observations, and no delivery confound.
  Real ad delivery is clustered and non-random, so treat every figure as a **lower bound** on the true
  sample requirement.
- **Two abstracts cut against a naive read of our own plan** (§2 relational processing; §3⑤ narcissism /
  recipient-centric gifts). Both are single findings read from abstracts, not full texts. Flagged rather
  than acted on — worth reading in full before they change creative.

## Sources
**Primary (PubMed/PMC):** pmid:15901395 · pmid:28914152 · **pmid:29920154 (smile-seeking)** · pmid:22774790 ·
pmid:30027819 · pmid:36048054 · pmid:39425564 · pmcid:PMC9005789 · pmcid:PMC4547715 · pmid:32799734 ·
pmid:38963906 · pmid:21256923 · pmid:31707077 · pmid:18413272 · pmid:30218945 · **pmcid:PMC6368470
(relational processing)** · pmcid:PMC4206440 · pmid:23263878 · **pmcid:PMC3711149 (motion onset)** ·
pmid:23314730 · pmid:32088400 · pmcid:PMC4099520 · pmcid:PMC2668614 · pmid:20377287 · pmcid:PMC3838954
**Economics / measurement:** Lewis & Rao, *QJE* 130(4):1941–1973 (2015) · Gordon, Zettelmeyer, Bhargava &
Chapsky, *Marketing Science* 38(2):193–225 (2019) · Johnson, Lewis & Nubbemeyer, *JMR* 54(6) (Ghost Ads) ·
Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments*
**Evidence base:** Ehrenberg-Bass (Sharp, Romaniuk, Dawes) · Binet & Field (IPA) · Feldwick & Heath,
"60 Years of Using the Wrong Advertising Model" · Nelson-Field, *The Attention Economy* · System1/WARC
*Anatomy of Effectiveness*
**Internal:** [[ad-video-director-research]] · [[video-ad-decomposition-2026]] · [[ai-film-studio]]
