# Role 04 · SCRIPT: research + spec (video-team methodology)

> Written 2026-11-18. Defines the script role for MadeJustForYou's Meta video ads (15–25s, 9:16 + 4:5, usually AI-generated, often emotional story with the product as payoff, captions on, often no VO, music bed, tested as concepts × hooks).
> **Tool-agnostic.** This role names no generator, LLM, voice engine or editor. It specifies decisions, inputs/outputs, budgets, rubrics and gates.
> Grades: **[STRONG]** = 2+ independent good sources or a platform primary source on its own platform · **[MODERATE]** = one solid source, or several weak ones agreeing · **[WEAK]** = vendor blog, n≤2, practitioner opinion. **[HARD]** = policy/production correctness (not a performance claim).
> Internal authority is still `research/reference/script-method.md` (R1–R24, T1–T7). This file adapts the role; it does not overrule that doc. Conflicts are listed in §4, not resolved.

---

## 0. What we already know internally vs gaps

| Known (internal) | Where |
|---|---|
| Product identifiable at 0–1s (R1, STRONG); personalization is the hero visual (R2); opening moves (R4); feeling-line hook allowed for memorial if product still by 1s (R5) | script-method §1a |
| Character-described copy, never viewer-described (R6, HARD); captions carry the story muted (R7); create/customize CTA (R8); Phase-1 locked CTA "Make one that's only theirs" | script-method §1b, decomposition §CTA |
| 15–25s default (R10); varied 2–5s shots, hard cuts (R11); music + captions, no VO default (R13); letter products → giver-voice VO (R14); emotional pivot ~55–60% (R15, WEAK) | script-method §1c |
| Show connection, never a lonely giftee (R17 + memory); living grandma buyer present (R18); casting names every trait to match printed figures and caption pronouns (R19 + memory `casting-matches-caption`) | script-method §1d |
| Gift buyer = the giver; the recipient's anticipated smile *is* the benefit; personalization makes the giver's thought visible | ad-science-foundations §3 |
| 12-field brief; emotion arc (anticipation → escalation → reveal + reaction), not PAS; proof ranking (reaction > personalization detail > volume > photo-UGC > craft) | decomposition §Body, §brief |
| Worked caption spec: ≤2.5 words/s, ≥2.0s per card, ≤2 lines, hard on/off, one fixed band, numbers = 1 word | suncatcher-phase1/CAPTION-SHEET.md |
| Process: plan page is test authority; scripts written by the agent from research, council per case, council may not restructure; compile all criteria before any build | memory `follow-plan-page-scripts-via-agent` |
| Primary text = line-broken array, never a paragraph | memory `ad-copy-linebreak-format` |

**Gaps:** no in-category A/B on story-vs-product-hero (T1), VO-vs-none (T4), or late reveal; no 55+ reading-speed data for vertical video; no evidence on max words per caption card for ads specifically (subtitle standards are for dialogue transcription, not ad supers); no data on how much a hook/body mismatch costs in *our* niche; no verified story-film winner (script-method §0).

---

## 1. External evidence summary (a–g)

### (a) Structure and emotional vs rational
- **Emotional campaigns win long-term; rational campaigns win short-term direct effects.** Binet & Field (IPA Databank, ~1,000 cases): emotional campaigns more profitable over time, but "rational campaigns outperform others in short-term direct effects"; emotional priming *amplifies* activation messages ("brand response effect"); best results when both work together. **[STRONG]** — https://maynardpaton.com/wp-content/uploads/2019/12/SYS1-long-and-short-of-it.pdf · https://thetomroach.com/wp-content/uploads/2020/06/the_greatest_hits_of_binet_and_field.pdf · https://www.youtube.com/watch?v=i0OKdtaJ8g0 (Binet: "in more emotional categories we tend to get bigger brand effects"). Caveat: measured on mostly TV/multi-year campaigns, not Meta prospecting.
- **Short-form: entertainment/emotion also drives conversion lift.** System1 × TikTok: 887 short-form ads, 92k viewers, matched to 350+ brand/conversion lift studies; "challenges [the] binary" that emotion builds brand while DR sells. **[MODERATE]** (TikTok, not Meta; vendor-commissioned) — https://system1group.com/blog/how-to-make-entertaining-short-form-ads-for-tiktok-social
- **Story structure raises liking.** 108 Super Bowl ads: more complete dramatic acts (exposition → rising action → climax → falling action → denouement) correlated with higher consumer ratings. **[MODERATE]** (30–60s TV, likability not sales) — https://hub.jhu.edu/2014/01/31/super-bowl-ads
- **Thai "sadvertising"** is a documented genre (Thai Life Insurance etc.), built for virality and goodwill over minutes-long films; no performance data for 15–25s paid placements. **[WEAK]** for our format — https://www.worldfinance.com/wealth-management/how-thai-life-insurance-is-successfully-pioneering-the-use-of-sadvertising · https://digiday.com/marketing/7-thai-commercials-will-make-bawl-like-baby
- **Joy dynamics retain viewers.** Teixeira, Wedel & Pieters (JMR 2012): *rising* joy (velocity) reduces zapping most; early surprise concentrates attention and reduces zapping more than late surprise. **[STRONG]** (peer-reviewed, lab) — https://www.hbs.edu/faculty/Pages/item.aspx?num=40850 · summary https://darwiniq.com/research/academic/emotion-video-engagement
- PAS / hook-story-offer: practitioner frames only; no controlled evidence for 15–25s gift ads found. **[WEAK]**

### (b) Hook→body continuity and brand/product timing
- **High hook + low hold = the hook over-promised.** Practitioner consensus: "mismatched expectations are the number one hold rate killer"; fix the 3–15s body without touching the opener. **[WEAK→MODERATE]** (several vendors agree, no controlled study) — https://adlibrary.com/posts/hook-rate · https://www.glued.me/blog/hook-rate-vs-hold-rate-guide · https://hawky.ai/blog/hook-rate
- **The sharpest drop is 3–6s; a second reason to stay is needed by ~6s.** **[WEAK]** — https://increditors.com/video-ad-hook-hold-benchmarks
- **Value is front-loaded.** Nielsen for Facebook: up to 47% of campaign value delivered in the first 3s, 74% in the first 10s. **[MODERATE]** (2016, platform-commissioned) — https://www.businessinsider.com/facebook-releases-automated-captioning-and-new-metrics-for-video-ads-2016-2
- **Brand/product early does not cost attention when natural.** Google ABCD "brand early, often, richly… introduce your brand or product in the first 5 seconds"; Kantar validation: +30% short-term sales likelihood. **[STRONG]** on YouTube, directional on Meta — https://support.google.com/google-ads/answer/14783551 · https://www.kantar.com/de/case-studies/validating-googles-abcd-framework-with-the-power-of-artificial-intelligence. System1/TikTok: highest early brand recognition → +88% memory lift; "a logo isn't a hook, but other distinctive assets are." **[MODERATE]** — system1 link above.
- **But how the brand appears matters.** Teixeira et al. (Marketing Science 2010, 31 ads, ~2,000 viewers, eye-tracking + zapping): *centered* brand placement increases avoidance (size does not); **pulsing** brand presence (short, frequent) at constant total exposure cut avoidance ~8–10%. **[STRONG]** — https://ideas.repec.org/a/inm/ormksc/v29y2010i5p783-804.html
- Implication for us: "product early" is supported; "logo/brand card early" is not the same thing. Product-in-world, pulsed across beats, is the evidence-consistent reading of R1 + late *payoff*.

### (c) Sound-off, captions, reading speed
- **Feed is largely sound-off; Reels defaults sound-on.** Meta: "Reels default to Sound On"; Reels ads in 9:16 *with audio* and safe-zone elements had 34.5% lower cost per result than image ads on Reels (confounded: video vs image). **[STRONG]** that both modes matter — https://www.facebook.com/business/ads/facebook-instagram-reels-ads. Meta 2016: ~40–41% of video ads "don't communicate… unless sound is on"; captions +12% view time (internal, old). **[MODERATE]** — BI link above. Our caption doc: 92% mobile sound-off (Verizon/Publicis 2019, n=5,616). **[MODERATE]**
- **Reading-speed standards (for subtitles):** BBC 160–180 wpm = 0.33–0.375 s/word, min ≈0.3 s/word on screen; max 2 lines. **[STRONG]** — https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles. Netflix English (USA): ≤20 cps adult, 42 chars/line, 2 lines, 5/6 s–7 s per event (the generic template page says 17 cps — the two Netflix pages disagree). **[STRONG]** — https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977 · https://partnerhelp.netflixstudios.com/hc/en-us/articles/219375728. DCMP (educational/special-interest): 130–160 wpm, ≥2 s. **[MODERATE]** — https://www.captioncraft.studio/guides/subtitle-guidelines
- **No published standard for words per ad caption card.** Subtitle standards assume viewers already chose to watch; ad captions compete with a scroll and with picture. Our 2.5 w/s (=150 wpm), ≥2.0 s, ≤2 lines is *more conservative* than BBC/Netflix and sits inside DCMP — reasonable for a 55+ buyer. **[WEAK]** as an optimum; house choice.

### (d) VO vs no VO vs dialogue; synthetic voice
- Reels sound-on default + Meta "build with audio" argues audio matters; it does not say *voice* specifically. **[MODERATE]** (Meta link above).
- **Synthetic voice:** WPP Media study — listeners prefer voices they *believe* are human (more relatable/emotional), but synthetic VO matched human VO on brand engagement and purchase intent; <50% could identify generic AI voices. **[MODERATE]** (audio ads, vendor research) — https://www.wppmedia.com/thought-leadership/research-business-intelligence/ai-voices-audio-ads-research. Adobe survey (n=850): 58% say they'd trust a brand less if it used AI voices (stated, not behavioural). **[WEAK]** — https://www.adobe.com/express/learn/blog/ai-audio-consumer-trust
- **AI-made ads overall:** NIQ (n≈2,000; EEG n≈150): viewers spotted most AI-generated ads, rated them more "annoying/boring/confusing", weaker memory activation even when "high quality". **[MODERATE]** — https://nielseniq.com/global/en/news-center/2024/niq-research-uncovers-hidden-consumer-attitudes-toward-ai-generated-ads
- VO word budgets (practitioner timing): ~2.5 words/s natural read; TV-style 15s ≈ 30–35 words, 30s ≈ 60–70; write under the ceiling to leave pauses. **[MODERATE]** (convergent practitioner rules, "not standards") — https://www.thevoiceoverco.com.au/voice-over-script-length-guide.php · https://www.granary.digital/voiceover-script-timing-words-per-minute.html
- No source isolates VO vs captions-only for emotional short ads. **Gap** → stays T4.

### (e) Policy constraints on script copy
- **Meta Personal Attributes:** ads "must not contain content that asserts or implies personal attributes" — race, ethnicity, religion, beliefs, age, sexual orientation, gender identity, disability, physical or mental health, vulnerable financial status, etc. ✅ describing the product; ✅ "you" without a personal attribute; ❌ "you/your" referencing a personal attribute. **[HARD/STRONG]** — https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes
- Reported 2026 tightening on *indirect* implication (conditional "If you've…", empathy "We understand your pain"), enforced in headline + primary text. **[WEAK]** (one vendor blog, unverified figures) — https://www.1clickreport.com/blog/meta-ad-policy-changes-2026-compliance-guide. Treat as a risk to guard, not a confirmed rule.
- **Grief:** not named as an attribute, but grief → mental-health implication is the obvious enforcement path ("Did you lose your dog?" ≈ "are you grieving?"). Character-described framing avoids it. **[MODERATE]** inference.
- **FTC (US buyers):** final rule (effective 2024-10-21) bans fake/AI-generated reviews or testimonials and testimonials misrepresenting experience; AI avatars giving testimonials can be deceptive. **[HARD/STRONG]** — https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials · https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers. → A scripted "customer" line, reaction, or order count must be clearly dramatized or real. Claims need substantiation.
- **How to check:** a 5-question pass — specific unverified result? implied transformation? assumed viewer trait? urgency tied to a real condition? comparison you could prove? **[WEAK]** but cheap — https://adsify.app/blog/ad-policy-traps-claims-before-after-personal-attributes

### (f) Script QA methods
- **Read-aloud / table read at target pace** to catch timing and awkward phrasing before production. **[MODERATE]** (universal practitioner rule) — https://voicebros.com/en/blog/voice-over-script-writing
- **Budget words per beat from a words-per-second rate** (VO ~2.5 w/s; captions per §1c). **[MODERATE]**
- **Muted test** — "watch the finished ad with sound off; if you can't follow it, neither can a buyer." **[MODERATE]** (Meta-aligned guidance) — https://rhythmads.com/learn/video-ad-captions
- **One-message test** (state the single takeaway in one sentence) — practitioner/copywriting convention; no controlled evidence found. **[WEAK]**
- Netflix reading-speed edits: "deletion, reformulation, re-timing, re-segmentation, merging, contractions" — the toolkit for cutting to time. **[STRONG]** as craft method (Netflix template link).

### (g) AI-written scripts: failure modes and guards
- **Homogeneity:** LLM creative outputs resemble other LLMs' far more than humans resemble each other, across models. **[STRONG]** — https://pmc.ncbi.nlm.nih.gov/articles/PMC13010328 · https://scale.stanford.edu/ai/repository/homogenizing-effect-large-language-models-llms-creative-diversity-empirical
- **Higher average quality but lower novelty/diversity**; mitigations that work: pooling across models, injecting heterogeneous personas/constraints, chain-of-thought exploration. **[MODERATE]** (preprint) — https://arxiv.org/abs/2607.27553
- **Ungrounded generation invents facts;** grounding to supplied data + rule-based accept/reject checks is the production pattern (Amazon: LLM-judge + rule checks; most common reject = "not relevant"). **[MODERATE]** — https://assets.amazon.science/50/cd/89210b7449df8dc810b79369da1b/llms-for-customized-marketing-content-generation-and-evaluation-at-scale.pdf
- Guards therefore: closed fact list, traceability per line, banned-phrase list, forced diversity across variants, rule-based gates before any human/council review.

---

## 2. Role 04 spec

### Mission
Turn ONE plan cell (concept × hook) into a timed, word-budgeted beat script that (1) pays off the hook's promise, (2) keeps the personalized product present from frame 1 and lands its emotional payoff mid-to-late, (3) tells the whole story muted, and (4) hands the visual director and ad-copy uploader everything they need without them inventing words, people or facts.

### Inputs (all required; missing input = stop and ask, never fill from imagination)
| # | Input | Source | Used for |
|---|---|---|---|
| I1 | Plan section for this cell (concept, locked hook text/clip, length, beat boundaries, CTA, offer rule) | test plan page | structure authority; never restructure |
| I2 | 12-field brief (fields 1–12) | decomposition §brief | body skeleton, proof beat, voice, length |
| I3 | Chosen hooks (verbatim) + hook type | role 01–03 output | kept **word for word** |
| I4 | **Product fact sheet** (closed list, IDs F1…Fn): what it is, size, material, what is personalized, what it physically does (e.g. projects the name), real names/breed on the sample | product page + sample QA | every factual line must cite an F-ID |
| I5 | Cast sheet: every person/animal with role (buyer/giver/recipient), gender, age, skin tone, hair texture/colour/style, matched to the printed figures | casting/art | pronoun and trait checks |
| I6 | Policy pack: R6, Meta personal-attributes list, FTC testimonial rule, banned-phrase list | this doc §2 rules | gates |
| I7 | Reused assets list (shared hook clips, shared beats, approved music) | build list | don't rewrite locked beats |

### Outputs
**O1 · Beat table** (one row per beat; the deliverable the visual director builds from):

| Col | Content |
|---|---|
| Beat # / purpose | from §3 structure (HOOK / STAKES / TURN / PROOF / CONNECTION / CTA) |
| Timecode | start–end in seconds (picture); caption on/off listed separately if offset |
| Duration | seconds; no two consecutive shots equal |
| Visual intent | what the viewer must *understand* from the picture (not a prompt): subject, action, product position + legibility, emotional state, which cast member. One camera idea max. |
| Product presence | `hero` / `in frame` / `light/effect of product` / `absent (justify)` |
| Caption (on-screen story text) | exact words, line break marked `/` |
| Dialogue / VO | exact words + speaker (cast ID) or `—` |
| Other on-screen text | printed/composited text that must be legible (names on product, tag), flagged for real-artwork compositing |
| Sound | music cue (start/lift/resolve), SFX, VO bed |
| Words vs budget | `n words / budget` and `w/s` for caption and VO separately |
| Traces to | brief field #, fact F-ID, rule R#, hook ID |

**O2 · Header block:** cell ID, one-message sentence (≤15 words), emotional thesis (what the ending makes the viewer feel), hook promise (what the hook implies will be shown) and **"promise paid at Xs by beat #"**, total caption words, total VO words.

**O3 · Ad copy block** (same thesis as the film): primary text as a line array (≥2 lines, blank line between beats, bullets for features, CTA own line, offer only if plan says so); headline in the locked format; description; button preset. Every factual bullet cites an F-ID.

**O4 · Check report:** the §2 rubric with pass/fail per item, plus flagged conflicts (plan vs research) for the user — never silently resolved.

### Procedure
1. **Load and freeze.** Read I1–I7. Copy the hook verbatim. Write the hook promise in one line ("viewer expects to see the dog's actual breed and name").
2. **One message, one thesis.** Write O2's one-message sentence and thesis before any beat. If it needs "and", it's two ads.
3. **Lay the skeleton** from §3 using the plan's beat boundaries (plan wins over §3 defaults). Fill *visual intent* first, words second — the picture must carry each beat muted.
4. **Budget words** per beat (§3 tables). Write captions to budget, then cut 10%.
5. **Pay the promise early.** The hook's specific promise is visibly delivered by the PROOF beat (≤12s in a 20s ad, ≤9s in 15s).
6. **Ground every claim** to an F-ID. No numbers, stats, order counts, reviews, testimonials or delivery claims unless in I4 and true.
7. **Cast/pronoun pass:** for every caption pronoun, name the on-screen person/animal it refers to; check against I5 traits and gender (memory `casting-matches-caption`). Hands-only shots name whose hands.
8. **Policy pass:** each caption, VO line, headline and primary-text line through the R6 / personal-attributes / FTC checks (§2 hard rules).
9. **Read-aloud timing:** read captions at 2.5 w/s with a stopwatch against the timecodes; read VO at a natural pace; anything over budget is cut (delete → reformulate → re-time → re-segment, in that order).
10. **Muted test on paper:** read only the visual-intent column + captions. Can a stranger say what is sold and why it matters by 3s, and retell the story at the end?
11. **Write O3** from the same thesis; line-broken.
12. **Variants:** when asked for alternates, produce them from *different* angles/constraints (not rewordings) and from at least two independent drafting passes; reject near-duplicates.
13. **Self-check rubric**, then hand to council review (craft only; structure changes go to the user).

### Hard rules / must-nots
- **H1** Hook text and hook clip are verbatim from I3. The script may not "improve" them.
- **H2** Product identifiable within 1s and in frame (or its light/effect) in every beat, max one beat absent (R1). No logo-card opening; logo small, over moving picture, at the end (R12; Teixeira centered-brand finding).
- **H3** Never describe the viewer. No "you/your" tied to age, health (incl. grief), family status, finances, or loss. Describe characters: "Her dog died on Tuesday." (R6 HARD)
- **H4** No invented facts, statistics, counts, reviews, testimonials, shipping/delivery or quality claims. Dramatized characters are not presented as real customers (FTC).
- **H5** Names, breeds and text on screen = the real product sample (I4). Text beats on rigid products flagged "real artwork / still" for the visual director (R21–R22).
- **H6** No lonely giftee; the relationship is visible or carried by a relationship prop (R17). Grandparent buyer is alive and present unless the cell is explicitly memorial (R18).
- **H7** Every caption ≤2 lines, ≤2.5 w/s, ≥2.0s on screen; numbers count as one word.
- **H8** Story readable with sound off. VO/dialogue, if present, is duplicated in captions (may be condensed, never contradicted).
- **H9** Length per plan (default 20s; 15s cutdown from the same master).
- **H10** No tool names, model names or generation prompts in the script; the visual director owns prompts.
- **H11** Banned phrases (generic AI/gift clichés): "more than just a", "cherish forever", "timeless", "perfect gift for any occasion", "will melt your heart", "speechless", "a gift they'll never forget", "made with love" (unless I4), "unique" as the only claim, "heartwarming", "Imagine…", "Did you know…", rhetorical questions to the viewer, stacked em-dashes, triads used as filler. Extend from council notes.

### Pass/fail self-check rubric (all must pass; any FAIL blocks handoff)
| # | Check | Pass when |
|---|---|---|
| Q1 | Hook verbatim | character-for-character match with I3 |
| Q2 | 3-second muted check | visual intent + caption at 0–3s names *what gift* is sold |
| Q3 | Promise paid | O2 states the second/beat; ≤12s (20s) / ≤9s (15s) |
| Q4 | One message | O2 sentence ≤15 words, no "and" joining two ideas |
| Q5 | Product presence | every beat tagged; ≤1 absent beat with reason |
| Q6 | Budgets | every caption ≤2.5 w/s, ≥2.0s, ≤2 lines; VO ≤2.5 w/s; totals within §3 |
| Q7 | Grounding | every factual word cites an F-ID; zero numbers without one |
| Q8 | Policy | zero viewer-attribute lines across captions, VO, headline, primary text, description |
| Q9 | Cast/pronouns | every pronoun resolved to a cast ID; traits match I5; no gender/role mismatch |
| Q10 | Connection | relationship visible in ≥1 beat after the turn |
| Q11 | Clichés | zero banned phrases; no line that would fit any other product unchanged ("swap test") |
| Q12 | Shot rhythm | no two consecutive equal durations; hard cuts unless plan specifies a dissolve |
| Q13 | CTA | plan's locked line on screen as text; button preset named |
| Q14 | Copy alignment | primary text/headline share the thesis and name; line-broken array |
| Q15 | Trace | every row cites brief field / rule / hook; plan-vs-research conflicts listed in O4 |

### Failure modes → guards
| Failure | Guard |
|---|---|
| Generic copy that fits any gift | Q11 swap test + banned list; require ≥1 concrete, product-specific noun per caption (name, breed, tag, window light) |
| Invented stat/review/"10,000 grandmas" | closed fact list I4 + Q7; FTC rule in H4 |
| Drift from brief/plan (writer restructures) | beat boundaries copied from I1; "Traces to" column; council may not restructure |
| Hook→body bait-and-switch | O2 promise line + Q3 |
| Over-length captions (writing for readers who aren't there) | per-beat budgets, stopwatch read, cut 10% |
| Second-person grief/age copy | H3 + Q8 on every text surface incl. headline |
| Picture and words disagree (her/him, wrong hands) | Q9 cast pass; visual intent names cast ID |
| Lonely recipient | H6 + Q10 |
| Homogeneous variants | variants from different angles + ≥2 independent passes; reject near-duplicates |
| Late reveal starving the first 3s | H2; payoff ≠ first appearance |
| VO-dependent story | H8 muted test |

### Handoff to role 05 (visual director)
Deliver O1–O4. Visual director receives per beat: visual intent, product presence tag, cast IDs + traits, legible-text list (with "real artwork/still" flags), duration, sound cue, caption band constraints (what must not be covered: face, name, payoff). Visual director may change *how* a beat is shown; any change to *what* the beat shows, its duration, or words comes back to role 04. Ad copy (O3) goes to the upload step unchanged.

---

## 3. Recommended beat structure (adapting the creator's 6 blocks)

Why adapt: the source pipeline is a 60s first-person *argument* (HOOK → PROBLEM → REFRAME → PROOF → RESULT → CTA). Ours is a 15–25s *story* sold to a giver. Evidence: emotion arc over PAS for gift buys (decomposition; Binet & Field [STRONG] for brand, mixed for short-term), product early (R1, ABCD), rising joy retains (Teixeira 2012), story completeness raises liking (Quesenberry).

| Creator block | Ours | Adaptation |
|---|---|---|
| 1 HOOK | **HOOK** | Kept verbatim (H1). Product in frame 1. Third-person/character line. |
| 2 PROBLEM (pain viewer recognizes) | **STAKES** | The *character's* situation, shown not asserted about the viewer (R6). Absence, ritual, occasion — the CEP (occasion × relationship). |
| 3 REFRAME | **TURN** | The gift enters the story / its effect appears. Rising joy starts here (joy velocity). |
| 4 PROOF (2–3 real data points) | **PROOF = personalization made visible** | No statistics. Proof is the name/breed/photo legible on the real product (proof rank #2) — this pays the hook's promise. |
| 5 RESULT | **CONNECTION** | Emotional payoff through the relationship (giver↔receiver, photo, family) — the smile the giver is buying (ad-science §3①). Pivot line ~55–65%. |
| 6 CTA (keyword) | **CTA** | Locked create-verb line over moving product; small logo; button preset. |
| "Pay off hook in first 15s" | **Promise paid by 12s (20s) / 9s (15s)** | Same principle, scaled to length (~60%). |

### 20s default (matches Phase-1 suncatcher boundaries)
| Beat | Picture | Caption on–off | Caption budget (≤2.5 w/s, ≥2.0s) | VO budget if used | Product |
|---|---|---|---|---|---|
| 1 HOOK | 0.0–2.0 | 0.0–3.2 | ≤8 w | ≤5 w | hero, frame 1 |
| 2 STAKES | 2.0–6.0 | 3.2–6.0 | ≤7 w | ≤8 w | in frame |
| 3 TURN | 6.0–8.8 | 6.0–8.8 | ≤7 w | ≤6 w | product/effect |
| 4 PROOF (promise paid) | 8.8–12.0 | 8.8–12.0 | ≤8 w | ≤7 w | hero, personalization legible |
| — gap | 12.0–12.5 | none | — | — | — |
| 5 CONNECTION (pivot ~12.5–13) | 12.0–17.0 | 12.5–17.0 | ≤9 w (aim 7) | ≤10 w | in frame / effect |
| — gap | 17.0–17.5 | none | — | — | — |
| 6 CTA | 17.0–20.0 | 17.5–20.0 | ≤6 w | ≤4 w (or none) | hero, moving; small logo |
| **Total** | 20.0 | | **≤45 w (aim 35–40)** | **≤40 w (aim 30–35)** | |

### 15s variant (cut from the same master, not re-scripted)
| Beat | Picture | Caption | Budget | Note |
|---|---|---|---|---|
| 1 HOOK | 0.0–2.0 | 0.0–3.0 | ≤7 w | identical hook |
| 2 STAKES | 2.0–4.8 | 3.0–5.0 | ≤5 w | shortest stakes that still reads |
| 3+4 TURN→PROOF | 4.8–9.0 | 5.0–9.0 | ≤9 w (two cards) | promise paid by 9s |
| 5 CONNECTION | 9.0–12.5 | 9.3–12.5 | ≤7 w | pivot ~9–10s (60–65%) |
| 6 CTA | 12.5–15.0 | 12.7–15.0 | ≤5 w | locked line |
| **Total** | 15.0 | | **≤33 w (aim 26–30)** | VO ≤30 w |

Adaptation notes: the 15s variant merges TURN and PROOF because a separate turn costs ~3s the payoff can't spare; if the concept has no turn (product-hero), the slot becomes a second personalization angle. Letter/poem products: VO carries the text in the giver's voice (R14), captions show the one pivot line only; VO budget then replaces caption budget in beats 2–5.

---

## 4. Conflicts: external evidence vs script-method.md / internal docs (flagged, not resolved)

| # | Conflict | External | Internal | Status |
|---|---|---|---|---|
| X1 | **Emotion vs short-term sales** | Binet & Field: rational wins short-term direct effects; emotion's edge is long-term [STRONG]. System1/TikTok: emotion/entertainment also drives conversion lift [MODERATE]. | decomposition + ad-science §4 cite B&F as backing for emotion-arc-over-PAS on cold Meta prospecting | Partial mismatch: B&F supports emotion for *brand*, not for a 7-day-attributed test. Keep emotion arc (category is emotional, Binet's own caveat) but the "combined emotional + rational" finding argues for a concrete product-fact line inside the story. Test, don't argue. |
| X2 | **Late reveal vs product early** | ABCD brand/product in first 5s [STRONG]; System1 early brand recognition → higher memory [MODERATE]; Teixeira: centered brand raises zapping, pulsing helps [STRONG] | R1 product by 1s (STRONG); memory `ad-style-thai-emotional-film` overruled; old screenwriter agent says product ≈60% | Evidence agrees with R1. This spec keeps "payoff late, product early". Old agent's 60% rule must be dropped. T1 remains the only place a true late reveal is tested. |
| X3 | **Logo end card** | Teixeira: brand pulsing > one long brand block; ABCD "early and often" | R12 small logo over moving shot (WEAK, n=1); old agent "brand end card" | External supports R12 direction and adds: pulse product/brand across beats. |
| X4 | **No-VO default** | Reels sound-on default; Meta "with audio" result (confounded); WPP: synthetic VO performs ≈ human | R13 music + captions, no VO (MODERATE); decomposition: "sentiment-build = real human VO, never synthetic" [OPINION] | Unresolved. Music is required either way. Synthetic-voice ban is opinion vs one MODERATE study saying parity (but NIQ says AI-made ads draw negative halo). Keep in T4; don't hard-code either way. |
| X5 | **Caption reading speed** | BBC 160–180 wpm (≈2.7–3 w/s); Netflix 17 vs 20 cps (Netflix pages disagree); DCMP 130–160 wpm | CAPTION-SHEET ≤2.5 w/s, ≥2.0s | Ours is stricter than broadcast and inside DCMP. Justified for 55+ and ad context, but it's a house choice, not evidence of an optimum. |
| X6 | **"Your granddaughter…" hook (R3)** | Meta bans "you/your" referencing a personal attribute; reported 2026 crackdown on indirect implication [WEAK] | R3 MODERATE; R6 lists it as allowed | "Your granddaughter" implies the viewer is a grandparent (age/family). Family status is not on Meta's listed attributes; age is. Risk is real but unconfirmed. Flag for policy check; prefer character-described variants in tests until verified. |
| X7 | **2nd-person copy** | Meta policy above | old `film-screenwriter.md` rule "2nd-person" | Direct conflict with R6 (HARD). Drop from the agent. |
| X8 | **Uniform 4–5s scenes** | Meta Stories guidance: short, concise scenes beat long slow ones [MODERATE] | old agent "duration 4–5s from the beat"; R11 varied 2–5s | External agrees with R11. Drop the old agent rule. |
| X9 | **Hook→body "within 15s" rule** | creator pipeline (60s format) | our 20s plan pays name at ~9–12s | Scaled to ~60% of runtime here; no external evidence for the exact number. |
| X10 | **Reaction as proof vs benefit** | Teixeira: joy velocity retains | decomposition ranks reaction as "proof #1"; ad-science §3 reframes it as the benefit, belonging early | Internal docs disagree with each other; this spec puts proof = personalization (pays the hook) and reaction = CONNECTION beat; a reaction cold-open is a hook test, not a script decision. |

### What to keep / drop from `.claude/agents/film-screenwriter.md`
**Keep:** one emotional thesis feeding both film and ad copy; full per-beat script (visual/dialogue/VO/sound/on-screen text) before generation; hook variants as *different methods*, not rewordings; names on screen = real product; dialogue = captions; flag composited-text beats; never a lonely giftee; hand back for a gate.
**Drop:** product first at ≈60% and "never a showcase" (X2); face-on-screen hook requirement (R16); cool→warm grade as a rule (visual director's call); uniform 4–5s (X8); brand end card (X3); "2nd-person" (X7); per-scene generation prompt + named tools (H10, tool-agnostic); reliance on retired `ai-film-studio.md` / `ai-emotional-video-ad-playbook.md` (script-method §5).
