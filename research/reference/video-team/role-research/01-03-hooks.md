# Video team · roles 01–03: Hook Ideator, Hook Critic, Hook Selector

> Research 2026-11-18. Scope: the hook stage of the video-team methodology for MadeJustForYou paid Meta video ads (15–25s, 9:16 + 4:5, mostly AI-generated, captions-led, often emotional story with the product as payoff, tested as concepts × hooks).
> **Tool-agnostic by rule.** Nothing here names a generator, LLM, stock library or editor. "Judge" means any rater (a model run or a person); "generator" means whatever produced the hook.
> Grades: **[STRONG]** peer-reviewed or platform first-party · **[MODERATE]** large practitioner dataset or preprint · **[WEAK]** opinion, lore, single anecdote. Internal evidence is cited by repo file.
> Builds on, does not repeat: `research/reference/ad-science-foundations.md` (§1–§5), `video-ad-decomposition-2026.md` (hook library, tactic tiers), `script-method.md` §1a (R1–R6), `marketing/facebook-ads/suncatcher-phase1/HOOKS-shared.md` §3 + §7, plan page §06–§08.

---

## 0. What we already know, and where it is thin

**Already solid internally**
- Hook = frame 1 + on-screen text, 0.5–3s; the gift must be identifiable muted within 3s (plan §06/§09; `HOOKS-shared.md` §7). Product on screen by 1s is STRONG in our own ad audits (`script-method.md` R1).
- Name the **relationship**, not the name, because the viewer is the giver (relational processing, `ad-science-foundations.md` §2). This is already the live H1-vs-H2 test.
- The recipient's reaction is the **benefit the giver buys**, not proof (smile-seeking, §3①).
- Motion **onset** beats smooth drift (§1①); interrupt without relevance is wasted (§1③).
- A hook-rate comparison is affordable (~$21 for 22%→28%); conversion comparisons are not (§5b). So hooks are the one place we can run real experiments.
- Meta Personal Attributes: describe the character, never the viewer (`script-method.md` R6, HARD).
- The plan locks **2 hook arms** (H1 name shown = control, H2 relationship = challenger), the same hook clips across all concepts, and parks POV / social proof / curiosity for the velocity round.

**Thin or missing (what this doc adds)**
1. No written procedure for *generating* hooks: the H1/H2 lines were hand-written; no candidate pool, no cliché filter, no record of what was rejected.
2. No rubric: §7's 3-second check is one binary gate. Nothing scores stop power, relevance, or "the body pays the promise".
3. No guard against model-judge bias (self-preference, position, verbosity) or against rewordings posing as variants.
4. No answer to "how good is any pre-launch judgment?" (answer: barely better than chance unaided; see §1d).
5. No account of how Meta's similar-ad grouping changes what counts as a *distinct* hook.
6. The library has tactic names but no mechanism definitions with worked frame-1 + caption pairs per product.

---

## 1. Evidence summary

### a) Hook mechanisms: what is evidenced for ads, what is lore
| Mechanism | Evidence | Grade | Read for gift ads |
|---|---|---|---|
| Information-gap curiosity | Curiosity arises from a perceived gap that seems closable (Loewenstein 1994, *Psych Bull* 116:75, doi:10.1037/0033-2909.116.1.75). Field data on ~9,000 Upworthy A/B tests: an **inverted U**: too vague or too concrete both lose clicks; most headlines would lose clicks by becoming *more* concrete (https://pmc.ncbi.nlm.nih.gov/articles/PMC11704130). Lab studies of forward-reference/question headlines show no gain or a negative effect (Scacco & Muddiman 2019; https://pike.psu.edu/publications/chi21.pdf). | STRONG (text headlines, not video) | Curiosity works only with a concrete anchor ("what is on that wall?"), never as pure withholding. Plan §09 already notes curiosity that hides what is sold produces unfiltered clicks. |
| Pattern interrupt / motion onset | Motion onset is more salient than smooth motion (PMC3711149); novelty ≠ salience (pmid:32088400). Google: tight framing, 2+ shots in first 5s, open with people (https://www.thinkwithgoogle.com/_qs/documents/8472/ABCD_Complete_V7b_HR_1.pdf). Meta: "start bold… more motion, scenes and speed" (https://www.facebook.com/business/news/mobile-first-creative). | STRONG (lab + first-party) | The arresting unit is still→sudden change in frame 1 (sun hits glass, hands lift lid), not constant drift. |
| Self-relevance (own name) | Own-name capture is real but conditional; a name alone is insufficient without relational processing (PMC6368470). | STRONG | The viewer is the giver: a stranger's name is not self-relevant. Use relationship cues; the name is proof of personalization, not the stop. |
| Emotion / faces | Joy and surprise, measured moment to moment, raise engagement and reduce zapping in internet video ads, partly by concentrating attention (Teixeira, Wedel & Pieters, *JMR* 2012, https://www.hbs.edu/faculty/Pages/item.aspx?num=40850). Faces/people early raise engagement (Google ABCD, first-party). Animals get category-specific attention priority (New, Cosmides & Tooby, *PNAS* 2007, doi:10.1073/pnas.0703913104). | STRONG | A face mid-emotion or a clearly readable dog are legitimate frame-1 subjects. Caution: emotion without context reads as "drama", which MJ4U-111 showed buys views, not buyers. |
| Negativity / loss | Each negative word raised CTR ~2.3% across 105k Upworthy headline tests (Robertson et al., *Nat Hum Behav* 2023, https://www.nature.com/articles/s41562-023-01538-4). But gain vs loss **framing** barely differs in persuasion (O'Keefe & Jensen meta-analysis, r≈.03, https://pubmed.ncbi.nlm.nih.gov/17934940). | STRONG (news/health, transfer risk) | Grief and absence words can stop the scroll; "loss aversion" framing as persuasion is mostly lore. A "warning" hook that addresses the viewer's loss breaks R6. |
| Social proof | No ad-hook-specific evidence found; it is a general persuasion principle. Our decomposition ranks it Tier 2 for cold traffic. | WEAK for hooks | Keep for the velocity round, not discovery. |
| Specificity / contrast | Concreteness sweet spot (above). "Specific stat" and "contrarian" are practitioner tactics only. | MODERATE→WEAK | Specific *detail* (his breed, her 4 grandkids) is useful; contrarian claims fight the emotion arc (Tier 3). |
| Gift-category specifics | Smile-seeking giver (pmid:29920154); thought counts only when cued (pmid:22774790); givers buy on thoughtfulness and uniqueness (pmid:15901395, 28914152). **No A/B data isolating any hook mechanism inside personalized gifts was found.** | STRONG mechanisms, no category test | Gift hooks should show the person and the relationship and make the thought visible; every mechanism here is a hypothesis to test. |

### b) Visual vs text vs audio in the first 1–3s; hook-rate definitions
- **Platform first-party.** Meta: get the main message across in the first 3s; ≤15s (https://www.facebook.com/business/news/mobile-first-creative). Meta/Nielsen: up to 47% of a video campaign's value lands in the first 3s, 74% in the first 10s (2016, via https://finance.yahoo.com/news/facebook-wants-advertisers-lot-better-160805371.html). TikTok: introduce the proposition in the first 3s; the hook can sit within the first 6s; text overlays carry context (https://ads.tiktok.com/resources/help/article/creative-best-practices). Google ABCD: tight framing, people early, product/brand in first 5s; claimed +30% short-term sales likelihood (Google/Kantar, self-reported). **[STRONG, but first-party and partly self-reported]**
- **Sound.** Most feed plays are sound-off, so the visual and caption carry the hook. Meta reports video ads *with* audio at 15% lower CPA (analyst note quoting Meta: https://finance.yahoo.com/news/meta-meta-stock-outlook-brightens-213455790.html) **[MODERATE, second-hand]**. Rule: the audio cue reinforces the hook and is never required to understand it.
- **Which channel wins?** No first-party or peer-reviewed study isolates visual vs caption vs audio hooks in feed video. Evidence missing. Practitioner datasets claim "payoff in frame 1", "motion by 0.5s" and "text by 0.5s" each add points (`video-ad-decomposition-2026.md`) **[MODERATE, vendor]**. Working rule: the frame does the stopping, the caption does the relevance and the filtering.
- **Definitions.** Hook rate = thumbstop = 3-second video plays ÷ impressions × 100; Meta lists "Hook rate" as a metric in development with that formula (https://admanage.ai/blog/what-is-a-good-hook-rate-for-facebook-ads). Hold rate = ThruPlays (or 15s plays) ÷ 3s plays. Tools differ in threshold and denominator, so check before comparing. **[MODERATE]**
- **Benchmarks.** Median Meta hook rate ~28% Feed / ~31% Reels, top 10% ~43–50% (Benly 12k-ad analysis, https://adliftr.com/blog/ad-creative-testing-statistics-2026); 25–35% healthy, <20% rebuild (multiple vendors). Our plan gates: kill <18%, red <21%, advance ≥28%. **[MODERATE: vendor datasets, inconsistent denominators]**

### c) Meta retrieval and similar-ad grouping (2025–26)
- **First-party:** "Our ads system… groups together ads that share key visual and thematic attributes. When multiple ads look or feel alike, these are seen as variations of the same creative, meaning learnings and delivery optimizations are shared at the creative level." Meta's own example of *iteration* (not diversification): "two ads with identical visuals, but different text CTAs" (https://www.facebook.com/business/news/demystifying-creative-diversification). Meta: the focus shifted "from niche targeting to creative diversification" (same source; also https://business-auth.facebook.com/business/news/the-creative-advantage-unlocking-the-power-of-diversification-with-meta-andromeda). **[STRONG]**
- "Entity ID", similarity scores and thresholds are practitioner vocabulary; Meta has published no threshold (https://lemonado.io/blog/meta-andromeda). Claims of "100 ads = 10 entities" are illustrative. **[WEAK]**
- **Implications for hooks.** (1) Two hooks that differ only in caption over the same frame are, by Meta's own definition, iteration and will likely share delivery. (2) Hook arms must differ in **frame-1 visual and mechanism**, not wording. (3) Our H1/H2 design swaps 0–2s of picture over an identical 18s body. That suits a hook experiment, but the two ads may be treated as related creative, so causal reads need a randomized split or separate ad sets (`ad-science-foundations.md` §5d). (4) Diversity for reach comes from concepts; hooks are the experimental knob.

### d) AI judges and the validity of pre-testing at all
- **Pre-testing accuracy is low.** On 96 matched ad pairs, unaided expert judgment picked the more effective ad **55.4%** of the time, novices 54.1%, commercial copy testing 57.0%. A **checklist of evidence-based principles, rated by 5 people and averaged, reached 74.5%** (Armstrong, Du, Green & Graefe, *Eur J Mark* 2016, https://faculty.wharton.upenn.edu/wp-content/uploads/2016/03/Predictive-Validity-R328-R_3.pdf). Print ads and recall, not feed video, but it is the best head-to-head evidence. **[STRONG]** Lesson: decompose into specific checks, use several raters, aggregate.
- **Model predictions of A/B outcomes are biased, not just noisy.** Raw model CTR predictions on thousands of Upworthy headline tests recovered only **39%** of the true treatment effect; calibration against human data helped only under unverifiable assumptions, "least justified precisely when it offers the most benefit" (novel treatments) (https://engineering.atspotify.com/2026/8/when-can-llms-replace-humans-in-a-b-tests). **[MODERATE]** Vendor claims of "90% accuracy" from creative-scoring tools come without independent validation. **[WEAK]**
- **Base rate.** Across 550k+ Meta ads (~$1.3B spend), ~5% become winners and about half get almost no spend. Motion's own conclusion: "creative strategy is not prediction" (https://sepia-lab.com/en/blog/ad-creative-volume-benchmarks). **[MODERATE]**
- **Judge biases.** Strong model judges agree with humans ~80% on pairwise preferences, about human–human agreement, and show position, verbosity and self-enhancement biases (Zheng et al., NeurIPS 2023, https://arxiv.org/abs/2306.05685) **[STRONG]**. Models recognise and favour their own generations, and self-recognition causally drives self-preference (Panickssery, Bowman & Feng, NeurIPS 2024, https://arxiv.org/abs/2404.13076) **[STRONG]**. Even rubric-based pointwise scoring shows order effects that flip the top-1 pick on 16–39% of prompts (https://arxiv.org/html/2602.02219v2) **[MODERATE, preprint]**. A panel of diverse smaller judges beat a single large judge and reduced intra-model bias (Verga et al., https://arxiv.org/abs/2404.18796) **[MODERATE, preprint]**.
- **Formats.** Pairwise needs both orders, with a flip counted as a tie. Pointwise has no candidate order but needs anchored levels. Mixing them can produce contradictory rankings (A>B>C>A). Binary, evidence-required checks are the most reliable for defect detection (practitioner consensus, e.g. https://befailproof.ai/learn/llm-judge-bias) **[MODERATE]**.
- **Net.** A critic can reliably catch **defects** (illegible frame 1, gift not identifiable, policy breach, unpaid promise, cliché). It cannot reliably pick **the winner**. Design the critic as a filter and leave winner-finding to the market.

### e) Selection under a low-budget test
- "Pick exactly 1" fits organic posting, where the creator publishes one video and the platform is the test. In paid testing the market is the selector, pre-launch judgment is ~55–75% accurate, and a hook-rate test costs ~$21–88. So **pick the best execution per pre-registered arm, and carry 2 arms per concept** (3 only if budget covers ≥~3,400 impressions per arm for a 3-point difference, `ad-science-foundations.md` §5b).
- Arms must be **mechanism contrasts** (a hypothesis such as name-shown vs relationship), not wording variants. One manipulation per test; compare against a pre-named control (§5e).
- More arms split the budget until none reaches its sample gate (plan §06). Velocity mode (10–20 swaps on a proven body) comes only after a body wins. **[MODERATE practitioner + STRONG statistics]**
- Diversity choice: maximise distance between arms on mechanism and frame-1 composition; within an arm, maximise expected quality.

### f) The "50 Psychology-Based Hook Templates" list: fit assessment
Creator/educational lines spoken to camera in the first person. No performance evidence is attached. **[WEAK]**
| Template | Fit | Adaptation |
|---|---|---|
| "This looks like [simple thing]. It's actually [deeper thing]" | **High** | "This looks like a suncatcher. At 4pm, it's Alex again." Contrast plus a concrete gap. |
| "Imagine [scene]. That starts with [vehicle]" | **High** as a structure | Drop "imagine"; *show* the scene as frame 1 and let the caption name the vehicle. |
| "Nobody talks about the [small thing]…" | **Medium** | Recognition of a private ritual, third person only: "Nobody tells you what to do with the leash." Check R6. |
| "This is what [outcome] looks like before it looks impressive" | Medium | Making-of / personalization act: "This is what 'I thought of you' looks like before it's wrapped." |
| "I used to X, now Y" | Medium–low | Only as a character's caption ("We used to leave the window open for him. We still do."). Not a creator confession. |
| "Most people think X, the real reason is Y" · "I tested A vs B" · "N mistakes" · "It took me X to learn Y" · "Before you X, check Y" | **Low** | Rational/authority (System-2, Tier 3); they fight the emotion arc. |
| "Save this before you…" | **Reject** | Organic engagement bait; meaningless in a paid ad. |
**What it lacks:** visual-first hooks (it is all spoken lines), reaction cold-open, personalization reveal, relationship callout, occasion/CEP, giver POV, motion-onset events, and any rule against addressing the viewer's personal attributes. Use it as a phrasing source for the caption layer only, never as the mechanism list.

---

## 2. Role specs

### Shared object: the **Hook Card** (one row per hook, used by all three roles)
| Field | Content |
|---|---|
| `id` | `<concept>-<arm>-h<nn>`, e.g. `C1-H2-h07` |
| `arm` | Pre-registered test arm this hook executes (e.g. H1 name shown / H2 relationship) |
| `mechanism` | One code from §4 (M1–M11). Exactly one primary. |
| `cep` | Relationship × occasion/life-event cue (e.g. "dog died this year", "grandma's 80th") |
| `frame1_visual` | What is in the pixels at 0.0s: subject, framing, product visible? (yes, where, % of frame width) |
| `onset_0_5s` | What changes or moves by 0.5s (a still→move event, not drift) |
| `caption` | On-screen line(s), ≤10 words, readable by 0.5s; line-break plan |
| `audio_cue` | Sound at frame 1; must not be needed to understand the hook |
| `promise` | The question or expectation the hook opens, in one sentence |
| `paid_by` | Body beat and second where the promise is answered (≤ 3s after the hook ends) |
| `asset_source` | Real product still / approved plate / new generation needed; product never model-drawn |
| `policy` | R6 viewer-attributes check, casting-matches-caption check |
| `rationale` | Ideator's reasoning. **Hidden from the Critic.** |

### 01 · HOOK IDEATOR
**Mission:** produce a wide, mechanism-diverse pool of producible hook cards for each test arm of one concept.

**Inputs (exact):** concept 12-field brief; test plan (arms, controls, shared-hook rule); body beat sheet with seconds (what is on screen 2–6s and at the reveal); product truth sheet (what the real product can show, sizes, personalization fields); cast sheet; recipient × buyer pair; CEP list; past-hook ledger (all prior hooks + measured hook/hold rate); banned list (clichés §2.01 rule 4 + every hook already run).

**Output:** `<test-folder>/hooks/01-candidates.md`, a Hook Card table with ≥15 rows, plus a "self-rejected" table (id, line, reason).

**Procedure**
1. Restate each arm's hypothesis in one line. If the plan fixes the arm (H1 name shown), every hook in that arm must express that contrast.
2. List what the body can pay. Any promise outside this list is invalid.
3. Generate ≥15 cards across **≥6 mechanisms** from §4, ≥2 per arm-compatible mechanism. Write the **frame first**, then the caption. A caption with no frame is not a card.
4. Self-reject: clichés ("wait for it", "you won't believe", "the perfect gift for…", "stop scrolling", "gone but never forgotten", "forever in my heart", "this made me cry"); any line addressing the viewer's attributes; any frame where the product is not identifiable by 3s muted; promises the body cannot pay; near-duplicates (same frame and same mechanism as another card; keep one).
5. Keep **8–10** cards, at least 2 per arm and ≥5 mechanisms overall.
6. For each kept card, fill `paid_by` with a second, not a beat name.

**Hard rules:** never reuse a ledger hook verbatim as "new"; never write "you/your" plus a sensitive attribute (loss, age, health, relationship status); the product comes from real artwork; caption pronouns match casting (`casting-matches-caption`); for grandparent products the grandparent is alive and present (R18).

**Failure modes + guards:** *caption-only variety* (guard: the near-duplicate test is on frame + mechanism, not words); *clever but unpayable* (guard: `paid_by` second is mandatory); *drift to creator-style first-person confessions* (guard: mechanism list §4, not template lists); *same-model monoculture* (guard: if a model ideates, run ≥2 independent passes with different seeds or instructions, merge, then dedupe).

**Handoff:** the 8–10 kept cards to the Critic **without** `rationale`, author, or generation order.

### 02 · HOOK CRITIC
**Mission:** remove defective hooks and score the rest on an anchored rubric. Filter, not fortune-teller.

**Inputs:** Hook Cards minus `rationale`; frame-1 still for each (a mock or sketch frame if the asset does not exist yet, labelled MOCK); body beat sheet; product truth sheet; policy rules; calibration set (4 past hooks with known hook rates, 2 high, 2 low, shuffled in blind).

**Output:** `<test-folder>/hooks/02-scores.md`: per card, gate results (pass/fail + one-line evidence), criterion scores with a quoted reason, judge-level scores, median total, flags. Plus a calibration line (did the panel rank the 2 known winners above the 2 known losers?).

**Judge protocol (independence is the point)**
1. The Critic is **never the Ideator** (not the same person, and not the same model session; preferably a different model family).
2. Use **3 independent judges** (e.g. 2 different model families + 1 human, or 3 runs with shuffled card order if only one model is available, *declared as weaker*). Aggregate by **median**; flag any criterion where judges differ by ≥2 points.
3. Each judge sees cards in a fresh random order, scores **one card at a time** (pointwise), and must quote the evidence (caption words / frame description) **before** giving a score.
4. All cards use the identical card format and length (verbosity guard). Any field over its limit is truncated and the overrun recorded as a defect.

**Stage A: binary gates (any FAIL = cut, no score)**
| Gate | Pass condition |
|---|---|
| G1 Muted identity | From frame 1 + caption alone, sound off, a cold reader can say *what kind of gift* and *for whom* within 3s (plan §06/§09; `HOOKS-shared.md` §7). |
| G2 Policy | No assertion or implication of the viewer's personal attributes (R6); no prohibited claims. |
| G3 Payable | `paid_by` names a real beat in the body that answers the promise ≤3s after the hook ends. |
| G4 Producible | Frame 1 can be made from the real product art or an approved plate; no model-drawn product or text. |
| G5 Casting | Caption pronouns and relationships match who is on screen. |
| G6 Arm fit | The card actually expresses its arm's manipulation (an H1 card shows the name; an H2 card names the relationship and not the name). |

**Stage B: anchored scoring (each criterion 1–5; points = weight × score/5; total /100)**
| Criterion (weight) | 1 | 3 | 5 |
|---|---|---|---|
| **S1 Stop power, frame 1 muted (25)** | Static or logo or empty room; subject unreadable at phone size | Clear subject, but smooth drift only; nothing new for the feed | A still→sudden change or a face/animal/name in tight framing by 0.5s; reads at ~360px wide |
| **S2 Right-buyer relevance (20)** | Generic ("a nice gift") or about a stranger's name | A recognisable relationship *or* occasion, not both | A gift-giver with this relationship or life event recognises "my person" in ≤2s, and non-buyers self-select out |
| **S3 Open loop, concreteness sweet spot (15)** | Nothing unresolved, or pure withholding ("you won't believe…") | A question exists but is vague | One concrete detail plus one unanswered *what next*, closable by the body |
| **S4 Body pays it (25)** | Promise contradicts or outruns the body | Paid, but later than 3s after the hook, or partially | The very next beat answers the promise and escalates it; product on screen throughout |
| **S5 Cover/caption legibility (15)** | >12 words, or text fights the image, or falls outside safe zones | Readable but needs >2s, or breaks in 4:5 crop | ≤8 words, one line break, readable in ~1.5s, survives 9:16 and 4:5 crops and works as a thumbnail |

**Kill rules:** any gate FAIL; median total **<70**; any single criterion median = 1 (non-compensatory); S4 median ≤2. **Calibration rule:** if the panel fails to rank the 2 known-high calibration hooks above the 2 known-low ones, all scores in this batch become *advisory* and the Selector leans on gates plus the cold read.

**Hard rules / must-nots:** never see the author or rationale; never compare cards side by side in Stage B; never rewrite a hook (only flag what is wrong); never output a "winner".

**Failure modes + guards:** self-preference (separate judge, different family where possible, author hidden); position bias (per-judge shuffle); verbosity (fixed card format, length caps); halo from production polish (MOCK frames allowed and labelled, judged on content); leniency (gates first; the calibration set exposes a judge that passes everything); false precision (report the median and the spread, never decimals).

**Handoff:** all surviving cards (typically 3–6), with scores, spreads and flags, grouped by arm.

### 03 · HOOK SELECTOR (referee)
**Mission:** choose **one execution per pre-registered arm** (≥2 arms per concept), make the arms maximally distinct, and keep reserves.

**Inputs:** `02-scores.md`; frame-1 stills; test plan; the body's first 6 seconds as a cut or animatic if one exists; past-hook ledger.

**Output:** `<test-folder>/hooks/03-selection.md`: per arm: winner card, 1 reserve, the reason in two lines, and the pre-registration line (hypothesis, primary metric = hook rate, gate per plan §08, control named). Plus a "parked for velocity" list (cut-for-test, not cut-for-quality).

**Procedure**
1. **Within each arm, pairwise.** Compare the top 2–3 surviving cards head to head on one question: "which one more of the right buyers would stop for, and then stay?" Run each pair **in both orders**; a flip counts as a tie, and the tie breaks on higher S4 (payability).
2. **Outsider cold read (hard).** Show the chosen frame 1 + caption, muted, for 2 seconds at phone size to someone who has never seen the brief (a person, or a fresh judge context given *only* the image and the caption). They must answer: what is being sold, for whom, what happens next. A wrong "for whom" is a fail (cf. the H2 "dead husband" misread, `HOOKS-shared.md` §3). On a fail, take the reserve and repeat.
3. **Body-pays re-test.** Watch or read hook + seconds 2–6 together: is the promise answered immediately, and does the product stay in frame?
4. **Distinctness across arms.** The arm winners must differ in **mechanism and frame-1 composition** (subject, framing or event), not only caption. If two arms' frames would read as the same picture to a stranger, re-select. Caption-only differences are iteration by Meta's own definition (§1c).
5. **Shared-hook constraint.** If the plan requires one hook clip across all concepts, test it against every concept body (step 3 per body) before locking.
6. Write the pre-registration line and freeze it. No changes after launch except a gate failure found in QA.

**Hard rules:** exactly one winner per arm, ≥2 arms per concept for paid tests; never promote a card that failed a gate; never choose on "it's my favourite"; the reserve must be a different card, not a reworded winner.

**Failure modes + guards:** two winners that are rewordings (step 4); picking the most beautiful frame over the most payable (tie-break on S4); a selector who also wrote the hooks (the Selector must not be the Ideator); skipping the cold read because "it's obvious" (step 2 is mandatory and logged).

**Handoff:** to role 04 (script): the winners' frame-1 spec, onset event, caption, audio cue, promise and `paid_by` second, as fixed requirements for 0–6s. To the test log: the pre-registration lines. After results: hook rate and hold rate per hook appended to the past-hook ledger, which becomes the next calibration set.

---

## 3. Recommended changes vs the original 7-role pipeline
| Original | Ours | Why |
|---|---|---|
| Hooks are spoken/text lines | Hooks are **cards**: frame-1 visual + onset + caption + audio + promise | Sound-off feed; Meta/Google/TikTok first-party guidance centres the opening visual (§1b). |
| 15 → 6 → 3 revised → **1** | 15+ → 8–10 (self-cull) → 3–6 survive gates/≥70 → **1 per arm, ≥2 arms per concept, + 1 reserve each** | Paid testing: the market selects; pre-launch picks are ~55–75% accurate (§1d); a hook-rate test is cheap (~$21–88). |
| ≥5 mechanisms (recognition, warning, curiosity, contrast, promise) | ≥6 from the gift library §4; "warning" dropped or rewritten in the third person | Warnings that address the viewer's loss break R6; gift mechanisms (reaction, relationship, reveal, giver POV) are missing from the original. |
| Critic scores its own team's output | Critic is independent of the generator: different person/session, ideally a different model family; blind; 3 judges; median | Self-preference (NeurIPS 2024), position and verbosity bias (NeurIPS 2023); panels reduce intra-model bias (§1d). |
| 5 holistic criteria /100, <70 cut | **Binary gates first**, then 5 **anchored** criteria with weights; non-compensatory kills; calibration against known past hooks | Principle-checklist + multiple raters reached 74.5% vs 55% unaided (Armstrong 2016); binary checks catch defects reliably. |
| "Audience breadth" | "**Right-buyer relevance**": recognisable by the giver *and* filtering out non-buyers | Plan §09: broad curiosity that hides the product buys clicks, not buyers (MJ4U-111). |
| Selector re-tests and picks 1 | Selector picks pairwise **within** arm (both orders), enforces **distinctness across** arms, runs a muted outsider cold read, pre-registers | Meta groups visually similar ads (§1c); one manipulation per test (`ad-science` §5e). |
| Revision loop by the selector | Selector never rewrites; a failed cold read promotes the reserve | Keeps the scored object equal to the shipped object. |
| No learning loop | Every shipped hook's hook/hold rate goes into the ledger, which calibrates the Critic | The only on-niche evidence we will ever have is our own (`ad-science` §5e.6). |

---

## 4. Gift-ad hook mechanism library (frame-1 visual + caption)
Products: **Dog-memorial suncatcher** (stained-glass panel, breed silhouette + name, projects coloured light and the name onto the wall in sun). **Grandma gift** (e.g. blanket or magnet carrying all grandkids' names; grandma alive and present). Captions are third person (R6).

| # | Mechanism | Definition | Why it works | Suncatcher: frame 1 / caption | Grandma gift: frame 1 / caption |
|---|---|---|---|---|---|
| M1 | **Personalization reveal** | The name/breed appears on screen in the first second | Specific detail makes "the thought" visible; the thought counts only when cued (pmid:22774790). The name is proof, not the stop (PMC6368470) | ECU "Alex" in white script on the black German Shepherd, pulling back to the panel in a sunny window / "That's not a generic dog. That's his breed — and his name." | Blank magnet, 4 names typing on one by one / "All four of them. On one thing she'll see every day." |
| M2 | **Relationship callout** | Name the relationship or role, not the person's name | Relational processing drives the self-relevance effect (PMC6368470); CEPs are retrieval cues (`ad-science` §4) | Man at the open window, panel a third of the frame wide, dog unmistakable / "We still leave the window open for him." | Grandma in her armchair, blanket on her lap, kids' drawings on the fridge behind / "For the grandma who says 'don't get me anything.'" |
| M3 | **Reaction cold-open** | Start on a face mid-emotion before any context | The smile is the product the giver buys (pmid:29920154); joy/surprise reduce zapping (Teixeira 2012) | Owner's face as coloured light lands on it; the panel in soft focus in frame / "He didn't say anything for a long time." | Grandma's hands stop on the blanket; her face breaks into a smile / "She read the names twice. Then she called every one of them." |
| M4 | **Private-ritual recognition** | Show a small, specific habit that only people in this situation know | Recognition of a concrete, personal detail; concreteness sweet spot (PMC11704130) | Empty dog bed in a patch of morning sun, leash on the hook / "His bed still gets the morning sun." | Fridge door covered in grandkids' drawings, her hand adding one more / "Every drawing they ever gave her is still up." |
| M5 | **Light/transformation event (onset)** | A sudden visual change in frame 1: the sun hits, the room fills with colour | Motion onset > smooth motion (PMC3711149); interrupt plus immediate relevance (pmid:20377287) | Grey wall; sun breaks; a German Shepherd silhouette and "Alex" bloom across it / "Every afternoon at 4, he comes back." | Lights off, kids whisper "now"; a lamp clicks on and her name glows on the blanket / "Ready? … Now." |
| M6 | **Concrete curiosity gap** | One concrete detail plus one unanswered question the body closes in seconds | Information gap with an anchor (Loewenstein 1994); the inverted-U on concreteness | Coloured light patterns on a wall, origin unseen / "This light is shaped exactly like him." | Close-up of embroidery, half the letters out of frame / "She didn't notice the last line until Christmas night." |
| M7 | **Contrast: generic vs theirs** | Side by side or a cut from the generic to the specific | Givers value uniqueness and thoughtfulness (pmid:15901395, 28914152) | Split: generic paw-print suncatcher / his breed + name / "Any dog. Or *her* dog." | Store-bought "World's Best Grandma" mug vs the magnet with 4 names / "Anyone can buy 'Grandma'. Only they could make this." |
| M8 | **Giver POV / hand-off** | The gift in the giver's hands at the moment of giving | Smile-seeking giver; closeness is the deliverable (pmid:30027819) | Friend's hands holding the open box out toward the owner, panel glinting / "She didn't know what to say at the funeral. So she brought this." | Granddaughter's hands passing the wrapped blanket across a table to grandma's hands / "She's been planning this since spring." |
| M9 | **Occasion / CEP** | Anchor the hook to a dated moment or life event | Category Entry Points (Ehrenberg-Bass, `ad-science` §4) | Christmas tree, ornaments; the panel in the window behind, glowing / "First Christmas without him. Still in every photo." | Birthday cake with "80" candles, blanket folded beside it with names showing / "80 years. 4 grandkids. 1 blanket." |
| M10 | **Thought made visible (making-of)** | Show the act of specifying: choosing the breed, typing the name | The thought counts only when the receiver is cued to it (pmid:22774790); process vs result is an open test (`script-method` T5) | Hands sliding a photo of Alex beside the finished panel: silhouette matches / "We matched his ears from this photo." | Grandkids' handwriting on paper next to the same handwriting printed on the blanket / "That's their real handwriting." |
| M11 | **Quiet social proof** (velocity only) | Volume or community framed emotionally, not as a stat | General persuasion; no hook-level evidence (WEAK); for cold legitimacy | Wall of customer window photos, many breeds, each glowing / "12,000 windows like this one." *(only with a true number)* | Grid of grandmas holding their blankets / "The gift grandmas don't put away." |

**Not in the library (and why):** problem-callout, stat and contrarian (Tier 3, System-2); "warning" aimed at the viewer (R6); offer/discount-first (undercuts keepsake value, `video-ad-decomposition` offer ranking); organic engagement bait ("save this", "comment if…").

**Use with the current plan:** H1 = M1 and H2 = M2 are the live discovery contrast. M3 is barred at the hook layer in Phase 1 because it is concept 02's body (plan §06). M4–M10 are candidate arms for the next concept round. M11 waits for velocity mode on a proven body.

---

## 5. Limits
- No study tests any of these mechanisms *inside* personalized gifts on Meta. All are mechanism-backed hypotheses (same caveat as `video-ad-decomposition-2026.md`).
- Curiosity, negativity and pre-testing evidence comes from text headlines (Upworthy) and print ads (Armstrong). Transfer to video frame 1 is assumed, not shown.
- Hook-rate benchmarks are vendor datasets with inconsistent denominators. Use our own plan gates and our own ledger.
- The rubric weights are design choices, not fitted coefficients. Re-weight once the ledger holds ~20 measured hooks: check which criterion medians correlate with real hook rate.
