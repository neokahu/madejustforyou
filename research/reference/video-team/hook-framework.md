# Hook framework: FORMAT × TRIGGER (general, product-agnostic)

> Research 2026-11-18, for role 01 (Hook Ideator), 02 (Critic), 03 (Selector). Extends `role-research/01-03-hooks.md` (Hook Card §2, gift library M1–M11 §4); does not repeat its evidence on judges, pre-testing or Meta similar-ad grouping.
> **Tool-agnostic by rule.** No generator, model, editor or stock library is named. "Impossible visual" means any synthetic or composited shot, however made.
> Grades: **[STRONG]** peer-reviewed or platform first-party · **[MODERATE]** large practitioner dataset or preprint · **[WEAK]** opinion, lore, single anecdote. "Evidence missing" means we searched and found none.
> House rules referenced: R1 product identifiable by 1s, R6 describe the character never the viewer, R18 grandparent alive and present (`script-method.md`); G1–G6, S1–S5 (`01-03-hooks.md` §2).

---

## 0. Why two axes

The M1–M11 library mixes two different questions in one label. "Reaction cold-open" is an **execution** (a face mid-emotion at 0.0s). "Relationship callout" is mostly a **psychological lever** (the giver recognises their person). "Light/transformation onset" is both. Because of this blend:

1. **We cannot learn from results.** If M5 wins, we don't know whether the *onset* (format) or the *wonder* (trigger) did it, so the next hook can't reuse the right part.
2. **Diversity is fake.** Ten cards over six "mechanisms" can all be one trigger (recognition) wearing different clothes; the pool looks wide and tests one idea.
3. **New formats have no slot.** Fake-reality, native-UI, question and UGC-confession hooks don't fit any M-code, so the Ideator never proposes them.

The fix separates the axes:
- **FORMAT (F)**: *how* the first 0–3s is built: what is in the pixels at 0.0s, what changes by 0.5s, how caption and audio are used. It is a production spec. Changing F changes frame 1, so it changes how Meta groups the ad (`01-03-hooks.md` §1c).
- **TRIGGER (T)**: *why* a viewer stays past 3s: the psychological process the hook engages. It is a hypothesis about the buyer.
- **Attention primitives (P)**, a thin third layer: pre-attentive features that make the eye land at ~0.3s (onset, face, animal, legible text). Necessary, never sufficient: capture without relevance is wasted (pmid:20377287) [STRONG]. Every card names which P it uses; P is not a test arm.

A hook card = **one primary F × one primary T** (+ optional secondary T) + its P. M-codes survive as named gift recipes, i.e. specific (F, T) instances (§4).

Industry practice already splits these: Motion's 2026 benchmark tags *visual format* ("how the ad looks") separately from *hook tactic* ("what the ad says to earn the first three seconds"), and advises pairing them deliberately (https://motionapp.com/library/research/creative-benchmarks-2026/top-hook-tactics) [MODERATE].

---

## 1. FORMAT families (execution axis)

15 families. "Frame 1 must contain" is the minimum spec the Critic checks. Caption form is the default; audio role assumes ~80–85% sound-off plays (so audio never carries meaning).

| F | Family (folds in) | Definition | Sub-variants | Frame 1 must contain | Typical caption | Audio role | Evidence |
|---|---|---|---|---|---|---|---|
| F1 | **Onset / pattern interrupt** ("visual hook") | A still frame that changes suddenly by 0.5s; the change *is* the hook | light hits / object drops / snap zoom / hard cut to scale jump / colour floods in | A near-still composition with the product in it, and the onset event by ≤0.5s | Short, lands *after* the onset (≤6 words) | Sync hit on the onset (click, chime); optional | Motion onset more salient than smooth motion (PMC3711149) [STRONG]; Meta "start bold… more motion" (facebook.com/business/news/mobile-first-creative), Google ABCD 2+ shots in 5s [STRONG, first-party] |
| F2 | **Text-led statement** (negative/warning line, list/number, wordplay, callout) | The caption is the main stimulus over a simple, relevant picture | statement / callout ("For the grandma who…") / number ("80 years. 4 grandkids. 1 blanket.") / bittersweet line | Legible line by 0.5s, high contrast, inside 4:5 safe zone; product visible behind it | 5–10 words, one break | Bed only | Upworthy: wording shifts CTR; negative words +~2.3% CTR each (Robertson 2023, *Nat Hum Behav*) [STRONG, text not video]; text-forward statics over-index on hit rate (Motion 2026) [MODERATE] |
| F3 | **Question / direct address** | Opens with a question or line spoken *to* the viewer | rhetorical question / "what do you give…" / quiz | Question legible by 0.5s + the object it is about | ≤10 words, ends "?" | Optional VO repeating it | Question headlines: no gain or negative in lab (Scacco & Muddiman 2019; pike.psu.edu/publications/chi21.pdf) [STRONG, text]; vendor claims +3–6 pts (adlibrary.com/posts/hook-rate) [MODERATE] |
| F4 | **Fake reality / impossible visual** | A plainly impossible event: physics break, scale play, object alive, dream logic | scale play (giant/tiny) / physics break (light pours, letters lift) / object comes alive / world reacts to object | The impossible element *and* the real product (true size, true artwork) in one frame or by 1s | Grounding line that makes it a metaphor (≤8 words) | Sound designed to sell the impossibility; optional | Mechanism strong (surprise, §2 T2); **no ad-format test found** — see §5 |
| F5 | **Reveal (hidden → shown)** | Something concealed is uncovered inside 3s | blank → name types on / cover lift / unwrap / pull-back from ECU / focus pull | The concealing state that already shows *what kind* of object it is (G1) | Sets the expectation ("Watch the last line.") | Reveal sting | Practitioner gift tier-1 (`video-ad-decomposition-2026.md`) [WEAK–MODERATE]; curiosity mechanism [STRONG] |
| F6 | **Transformation / before-after** | State A → state B of the same space or person | grey → colour / empty → filled / old photo → now / B&W → colour | State A legible, with the cause of B (the product) in frame | Names the change or the time gap | Swell on the transition | "Transformation" in Motion top formats (Health & Wellness) [MODERATE]; **never** product-result claims faked (FTC, Meta) |
| F7 | **Comparison / split-screen** | Two options side by side or cut A/B | generic vs theirs / store-bought vs made / then vs now | Both halves readable at phone size; the "theirs" side is the real product | "Any X. Or *her* X." | none | "Contrast" in Motion hook list [MODERATE]; uniqueness motive (pmid:15901395) [STRONG mechanism] |
| F8 | **POV / first-person** | Camera is the viewer's eyes; usually the giver's hands | giver's hands hand-off / "POV:" caption / over-shoulder | Hands + product in lower third, recipient or setting implied | "POV: …" or character line | Diegetic room tone | Motion lists POV format [MODERATE]; vendor "character POV +4–10 pts" [MODERATE, unaudited] |
| F9 | **In-medias-res / storytime** | Starts mid-scene or mid-sentence; the story is already moving | mid-dialogue line / caption "He didn't say anything for a long time." / timestamped moment | A scene with action already underway; product present (R1) | First-person-of-character or narrator line | Dialogue or ambience; caption duplicates it | "Storytelling" in Motion spend-use list [MODERATE]; Teixeira 2012 emotion engagement [STRONG] |
| F10 | **Reaction cold-open** | A face mid-emotion before any context | gasp / tears / laugh / stunned silence | Face in tight framing, emotion readable at 360px, product in frame | Third-person context line | Breath / silence | Motion: "Reaction video" top hit rate in a vertical [MODERATE]; joy/surprise reduce zapping (Teixeira, Wedel & Pieters, *JMR* 2012) [STRONG] |
| F11 | **Hands / process / unboxing** (demo, making-of, "satisfying" loop) | Hands doing a specific act with the product | unbox / personalise (type the name, match the photo) / craft close-up / satisfying loop | Hands + product ECU, the act legible | Labels the act ("We matched his ears from this photo.") | Real tactile sound | Motion: Unboxing, Behind-the-scene, Demo in top lists [MODERATE]; thought must be cued (pmid:22774790) [STRONG mechanism] |
| F12 | **Sound-led / ASMR** | Audio is the primary stimulus | whisper / crinkle / chime / name spoken | A frame that still passes G1 muted | Must carry everything | Primary — which is the problem | ASMR ads: mainly negative overall, positive only for ASMR-responsive viewers (Esade / *J Retailing & Consumer Services*; dobetter.esade.edu/en/ASMR-advertising) [MODERATE]; sound-off majority |
| F13 | **Talking head / UGC-style** (green-screen, meta, confession) | A person speaks to camera | character confession / creator-style / green-screen over product or photo | Face in tight framing + product in hand or behind | Burned subtitles of the line | VO is the carrier; subtitles mandatory | TikTok first-party: native, creator-style "TikTok-first" (ads.tiktok.com/business/en-US/blog/creative-best-practices-top-performing-ads) [STRONG first-party]; Motion founder/testimonial formats [MODERATE] |
| F14 | **Native-UI mimic** (text thread, notes app, social post, letter, post-it) | The hook looks like a familiar non-ad artefact | group-chat screenshot on a phone in hand / handwritten note / notes-app list / comment card | The artefact *physically in scene* (phone in a hand, note on a fridge) + product in frame | The artefact's own text | Notification-like sounds ✕ (see §5/§7) | Motion: Text message, Social post mockup, Letter, Post-it in top lists [MODERATE]; Meta bans "non-existent functionality" (fake play buttons/notifications) [STRONG] |
| F15 | **Social-proof opener** | Volume, crowd or review shown first | wall of customer photos / review card / "N windows like this" | Real customers' artefacts only, product visible | True number or real quote only | none | No hook-level evidence [WEAK]; fabricated proof illegal (FTC 2024 rule) |

**Folded in, not separate:** list/number → F2; negative/warning statement → F2 (R6 limits who the warning is about); green-screen/meta → F13; storytime → F9; demonstration/satisfying loop → F11; interruption/notification → F14.

---

## 2. TRIGGERS (psychology axis)

| T | Trigger | Mechanism (why it holds past 3s) | Evidence | Gift-ad note |
|---|---|---|---|---|
| T1 | **Curiosity / information gap** | A perceived, closable gap makes people seek the missing piece (Loewenstein 1994, doi:10.1037/0033-2909.116.1.75). Inverted U: too vague and too concrete both lose (≈9k Upworthy tests, PMC11704130) | [STRONG] (text) · "Curiosity" in both Motion leaderboards [MODERATE] | One concrete anchor + one unanswered *what next*; never hide *what is sold* (MJ4U-111 lesson) |
| T2 | **Surprise / expectation violation / novelty** | Gaze goes to what changes beliefs: Bayesian surprise drew 72% of saccades (84% where observers agreed) in video (Itti & Baldi 2009, *Vision Res*, pmid:18834898). Unexpected-**and-relevant** information is best remembered; unexpected-irrelevant confuses (Heckler & Childers 1992, *JCR* 18:475). Surprise moment-to-moment reduced zapping (Teixeira 2012) | [STRONG] · Motion "interrupt cluster" (shocking statement, contrarian, confession): lower hit rate, higher variance [MODERATE] | The engine of F1, F4, F6. Must resolve to relevance fast |
| T3 | **Recognition / close-other relevance** | Self-relevance works through *relational* processing, not mere name display (PMC6368470); category entry points are retrieval cues (Ehrenberg-Bass, `ad-science-foundations.md` §4) | [STRONG] mechanism | The viewer is the giver: they must recognise *their person* or *their moment*. R6: describe the character, never the viewer |
| T4 | **Positive emotion: joy, tenderness, awe** | Joy and surprise raise engagement and cut zapping by concentrating attention (Teixeira, Wedel & Pieters 2012, *JMR*) | [STRONG] | Warmth that shows connection, not a lonely giftee (house rule) |
| T5 | **Nostalgia / bittersweet (sadness → warmth)** | Personal-nostalgia ads produce more favourable ad/brand attitudes than non-nostalgic (Muehling & Pascal 2011, *J Advertising* 40:2); negative words raise clicks (Robertson 2023) | [STRONG] for attitudes; [STRONG] for clicks (news) | Native to memorial and grandparent products. Sadness must turn warm inside the ad; drama alone buys views, not buyers |
| T6 | **Social proof** | People infer value from others' choices (general persuasion) | [WEAK] at hook level; no hook-specific study found | Cold legitimacy; velocity rounds only (M11) |
| T7 | **Desire / anticipated outcome** (the smile the giver buys; "thought made visible") | Givers are rewarded by the recipient's immediate reaction (smile-seeking, pmid:29920154); they buy thoughtfulness/uniqueness (pmid:15901395, 28914152) | [STRONG] mechanism | The core gift trigger: show the outcome the buyer is purchasing |
| T8 | **Urgency / occasion / loss of opportunity** | Promotional "act now" hooks (newness, urgency, FOMO, event) top Motion's 2026 hit-rate list, in a BFCM-heavy window [MODERATE]. Gain vs loss *framing* barely differs in persuasion (O'Keefe & Jensen, r≈.03) [STRONG] | Mixed | Real deadlines only (order-by date). Fake countdowns/scarcity = Meta Prohibited Commercial Practices. Never "before you lose them" at the viewer (R6) |
| T9 | **Humor** | Humor raises attitude to ad and brand and positive affect; effects run mainly through affect (Eisend 2009, *JAMS* 37:191) | [STRONG] | Grandparent "pretends not to care" works; **invalid for memorial** |
| T10 | **Contrarian / cognitive dissonance** | A claim that contradicts belief creates tension to resolve | Motion lists contrarian/myth-busting [MODERATE]; our decomposition ranks it Tier 3 for gifts | System-2; fights the emotion arc. Allowed only as a deliberate exploration card |

**Attention primitives (P), named on every card:** P1 motion onset (PMC3711149) · P2 face, which draws gaze independent of task (Cerf et al. 2008, NIPS) · P3 animal, which gets category-specific attention priority (New, Cosmides & Tooby 2007, *PNAS*) · P4 legible text by 0.5s (vendor +4–9 pts, [MODERATE]). **Frame-1 simplicity rule:** feature clutter (dense detail, colour, edges) *hurts* attention to the brand, while design complexity (structured, deliberate composition) *helps* (Pieters, Wedel & Batra 2010, *J Marketing* 74:48, 249 eye-tracked ads) [STRONG].

---

## 3. FORMAT × TRIGGER matrix

`S★` natural/strong **and** fits emotional personalized-gift ads · `S` natural/strong, but neutral or off-fit for our gifts · `W` workable, weaker pairing · `·` no natural link · `✕` invalid as normally executed (reason in notes)

| F \ T | T1 Curio | T2 Surpr | T3 Recog | T4 Joy | T5 Nostal | T6 Proof | T7 Desire | T8 Urgency | T9 Humor | T10 Contra |
|---|---|---|---|---|---|---|---|---|---|---|
| F1 Onset | S | **S★** | W | **S★** | **S★** | · | W | · | W | · |
| F2 Text-led | **S★** | W | **S★** | W | **S★** | S | W | S | S | S |
| F3 Question | S | · | **S★**ᵃ | · | W | W | W | W | W | S |
| F4 Fake reality | S | **S★** | W | **S★** | Wᵇ | ✕ᶜ | W | · | S | · |
| F5 Reveal | **S★** | S | **S★** | **S★** | S | · | **S★** | W | W | · |
| F6 Transform | S | **S★** | W | **S★** | **S★** | ✕ᵈ | S | · | W | · |
| F7 Compare | W | W | **S★** | · | · | W | **S★** | · | S | S |
| F8 POV | S | W | **S★** | **S★** | S | · | **S★** | S | S | · |
| F9 In-medias-res | **S★** | S | S | S | **S★** | · | W | W | S | W |
| F10 Reaction | **S★** | S | W | **S★** | **S★** | Wᵉ | **S★** | · | S | · |
| F11 Hands/process | S | W | S | W | W | · | **S★** | W | · | · |
| F12 Sound-led | Wᶠ | Wᶠ | Wᶠ | Wᶠ | Wᶠ | · | Wᶠ | · | Wᶠ | · |
| F13 Talking head | S | W | **S★** | S | S | ✕ᵍ | S | S | S | S |
| F14 Native-UI | **S★**ʰ | S | S | W | **S★** | Wⁱ | W | W | S | W |
| F15 Proof opener | W | · | W | W | · | Sⁱ | W | W | · | · |

Notes: ᵃ question addressed to the giver *role*, third person about the recipient ("What do you give the grandma who keeps every drawing?"); "Did you lose your dog?" is ✕ (R6). ᵇ memorial nostalgia via impossible visual has high creepiness risk (§5 FR5). ᶜ impossible visuals may never act as proof (crowds, reviews, numbers). ᵈ before/after "results" that the product doesn't produce = misrepresentation. ᵉ a reaction is the *benefit*, not proof (`ad-science` §3①); presenting a staged/AI reaction as a real customer's = ✕. ᶠ sound can only *add* to a frame that passes G1 muted; F12 as the sole carrier is ✕. ᵍ an AI or actor face saying "I bought this and…" implies a real customer endorsement (FTC Endorsement Guides / 2024 fake-review rule) = ✕; a *character* speaking inside a story is fine. ʰ only as a physical artefact in scene; full-screen system UI, notification badges, fake play buttons = ✕ (Meta "non-existent functionality", facebook.com/business/help/757209948405699). ⁱ real quotes and true counts only.

**How to read it:** the gift core is the T3/T4/T5/T7 block across F1, F5, F8, F9, F10, which is where M1–M11 already live. The matrix's job is to push 1–2 cards per pool into *under-used* `S★` cells (F4×T2/T4, F14×T1/T5, F3×T3, F13×T3, F2×T5, F6×T5) and keep `✕` cells out.

---

## 4. M1–M11 as instances of the framework, and the gaps

### 4a. Mapping
| M | Gift mechanism | Primary F | Primary T (secondary) | Primitives | Note |
|---|---|---|---|---|---|
| M1 | Personalization reveal | F5 Reveal | T7 Desire (T1) | P4 text, P3 if pet | Name = proof of the thought, not the stop |
| M2 | Relationship callout | F2 Text-led | T3 Recognition | P4 | Live arm H2 |
| M3 | Reaction cold-open | F10 Reaction | T4 Joy (T7) | P2 face | Barred at hook layer in Phase 1 (concept 02 body) |
| M4 | Private-ritual recognition | F9 In-medias-res (still life) | T3 (T5) | P3 bed/leash | Weak P1: needs an onset added |
| M5 | Light/transformation onset | F1 Onset / F6 | T2 Surprise (T4) | P1 | Only M-code that uses T2 |
| M6 | Concrete curiosity gap | F5 partial reveal / F2 | T1 Curiosity | P4 | Must show what is sold (G1) |
| M7 | Generic vs theirs | F7 Compare | T7 (T3) | P4 | |
| M8 | Giver POV / hand-off | F8 POV | T7 (T4) | hands | |
| M9 | Occasion / CEP | F2 or F9 | T3 (T8 when a real deadline) | P4 | |
| M10 | Thought made visible | F11 Hands/process | T7 | hands, P4 | |
| M11 | Quiet social proof | F15 Proof opener | T6 | — | Velocity only, true numbers |

**What the mapping shows:** the library uses 10 of 15 formats but leans on **3 triggers** (T3, T7, T4: 8 of 11 cards). T2 surprise appears once (M5); T5 nostalgia only as a secondary; T9 humor, T8 urgency and T1-led native formats are absent. Formats F3, F4, F12, F13, F14 have no recipe at all.

### 4b. Missing gift-relevant combos (worked examples)
Products as in `01-03-hooks.md` §4: **dog-memorial suncatcher** (stained-glass panel, breed silhouette + name; projects coloured light and the name onto the wall in sun) and **grandma gift** (blanket/magnet with all grandkids' names; grandma alive and present, R18). Captions third person (R6).

| New | (F × T) | Suncatcher: frame 1 / onset / caption | Grandma gift: frame 1 / onset / caption | Watch-outs |
|---|---|---|---|---|
| N1 | **F4 × T4** scale play | A tiny man sits inside the patch of coloured light on the wall like a sunlit meadow, the dog's silhouette beside him; by 1.0s pull back: it's the *real, static* projection on a real wall, the man on his sofa looking at it / "Some afternoons he gets to sit with him again." | Grandma, tiny, asleep inside a giant fold of the blanket, her grandkids' names around her like hills; pull back to the real blanket on her lap in her armchair / "She says it's like being held by all four." | §5 truth frame by ≤1.5s; projection shown exactly as the product makes it |
| N2 | **F4 × T2** physics break | Rain outside, grey room; one shaft of sunlight comes *only* through the panel, as if summoned / "It's always 4 o'clock for him." | The four names lift off the blanket like birds, circle her once, and settle back exactly as printed; she laughs / "Every one of them came home for her birthday." | N2 suncatcher sits closer to implying a capability (light without sun) → caption must make it a metaphor; flag for G7 |
| N3 | **F14 × T1** text thread | A phone in a woman's hand by a window: "look at your wall at 4pm 🧡" from a friend; the light begins to bloom behind the phone / no extra caption | Family group chat on grandma's phone on the table, "Grandma??? why aren't you answering 😭"; behind it she's wrapped in the blanket reading the names / "She was busy." | Artefact physically in scene; no system notification overlay, no fake sounds |
| N4 | **F3 × T3** question to the giver role | Friend holding the boxed panel at a front door / "What do you bring when 'sorry for your loss' isn't enough?" | Grandma's fridge covered in drawings / "What do you give the grandma who kept every drawing?" | Never "Did *you* lose…" (R6); "you" = the giver's role only |
| N5 | **F13 × T3** character confession | A woman to camera, the panel in her hands: "When her dog died I didn't know what to say. So I didn't say anything. I brought this." | A teen to camera holding the blanket: "Grandma says don't get her anything. So we made her everyone." | A character in a story, not a customer review; no "I ordered from…" claims |
| N6 | **F6 × T5** then/now | B&W photo of the dog in a sunny window → match-cut to the same window today, grey, then sun hits and colour floods in / "Same window. Same 4 o'clock." | Faded photo of grandma holding a newborn → today, the same grandma under a blanket with that baby's name and three more / "She held each of them first." | Grandma alive and present (R18); old photo = memory, not a death cue |
| N7 | **F1 × T9** humor | — (humor invalid for memorial) | Grandma waves the gift away ("don't get me anything"); hard cut: she's tugging the blanket back from a grandkid who sat on it / "She didn't want anything." | Keep it affectionate, not mocking age |
| N8 | **F9 × T1** mid-dialogue | Child's voice over the projection: "Mom… why is Max on the wall?" (subtitled) | "Grandma, read the last name." She pauses on it; her face changes / caption duplicates the line | Dialogue must be subtitled; G1 still has to pass muted |
| N9 | **F2 × T5** bittersweet line | Empty dog bed in sunlight, panel in the window above / "Twelve years of him waiting at this window." | Blanket folded on an empty dining chair at a full family table / "Her chair is never empty at Christmas." ⚠ | Grandma version reads as death → ✕ by R18; shows how T5 must be checked against R18 |

---

## 5. Fake-reality / impossible-visual hooks in depth

**What they are.** Shots that could not happen: scale play (tiny people, giant objects), physics breaks (light, gravity, time), objects coming alive, the world reacting to an object, dream logic. AI generation made them cheap, which is why they are now everywhere in feeds.

**Why they could work (attention).** They are pure expectation violation (T2). Surprise is a strong attractor of gaze in video (Itti & Baldi 2009) [STRONG]; unexpected-but-relevant material is better remembered than expected or irrelevant material (Heckler & Childers 1992) [STRONG]; incongruity with the *ad* schema mainly drives arousal (Loef & Verlegh 2002, repub.eur.nl/pub/193) [MODERATE]. Motion's "interrupt cluster" hooks (shocking statement, contrarian, confession) have lower hit rates but higher variance: "when they connect, they connect hard" [MODERATE]. **No study or dataset was found that measures hook rate for surreal/impossible video openers specifically.** Evidence missing; treat as a hypothesis.

**Why they could backfire.**
- **AI negative halo.** NIQ found consumers identify most AI-generated video ads and rate them more "annoying", "boring" and "confusing", with weaker memory activation and a possible negative halo on the brand (nielseniq.com/global/en/news-center/2024/niq-research-uncovers-hidden-consumer-attitudes-toward-ai-generated-ads) [MODERATE: industry neuro study, ads unnamed]. Higher perceived AI involvement raised engagement (comments, CTR) but also negative emotion (Hanson, Carlson & Pressler, *J Advertising Research* 2025, "Scary Good AI Advertising") [STRONG]. So an impossible hook may *raise* hook rate and still *lower* trust. Measure both.
- **Extreme incongruity confuses.** Unexpected-and-irrelevant fails (Heckler & Childers). Spectacle unrelated to the gift is wasted capture.
- **Uncanny / creepy in grief.** Near-human faces in the uncanny valley are disliked (Mathur & Reichling 2016, *Cognition*) [STRONG]. Ethicists warn specifically against using simulations of the dead for advertising (Hollanek & Nowaczyk-Basińska 2024, *Philosophy & Technology*; cam.ac.uk news) [STRONG as ethics, not ad-effect data]. A memorial ad that "brings the dog back" can read as exploitation.
- **Misrepresentation.** Showing a product doing what it can't is deceptive even with a prop, and the use of an undisclosed mock-up to "demonstrate" is a separate deception (FTC v. Colgate-Palmolive, 380 U.S. 374, 1965) [STRONG]. Meta requires ads to "accurately represent your… product" and bans "misleading claims or unrealistic expectations" and images of "non-existent functionality" (facebook.com/business/help/757209948405699) [STRONG first-party]. By contrast, the FTC Policy Statement on Deception treats claims no reasonable consumer would take literally (obvious exaggeration) as unlikely to deceive (ftc.gov/legal-library/browse/ftc-policy-statement-deception) [STRONG]. **The line: surreal context is fine; a surreal product capability is not.**

**Hard rules (FR) for any F4 card with a real product**
| # | Rule | Test the Critic applies |
|---|---|---|
| FR1 | **Product truth zone.** The product's shape, size, material, artwork, printed names *and its output* (the projection's colour, sharpness, brightness; the print on the blanket) appear exactly as the real product makes them. The impossible acts on the world *around* the product, never on what the product does. | Would a buyer expect the product to do the impossible thing? If yes → FAIL |
| FR2 | **Obvious, not plausible.** The impossible element must be unmistakably impossible (tiny people, flying letters). Subtle "enhancements" that could be real (brighter light, a sharper name on the wall, light without sun) are the worst case. | Cold reader: "is this real?" must be answered "obviously not", for the impossible part only |
| FR3 | **Truth frame by ≤1.5s, product identifiable by 1s (R1).** Pull back or cut to the real product in a real setting inside the hook; record the second in `truth_frame`. | `truth_frame` ≤ 1.5s and shows the real asset |
| FR4 | **Metaphor of the product's meaning.** The impossibility makes literal what the gift means ("sits with him again", "held by all four"), not random spectacle. | Can the caption explain the impossibility in ≤8 words? |
| FR5 | **No dead resurrected in the present.** In memorial products: no deceased pet/person moving, returning, speaking or "visiting" now; memories only as clearly past (flashback grade); never animate a customer's real photo of the deceased. Silhouettes and light stay inanimate. | Any present-tense return of the deceased → FAIL |
| FR6 | **Never proof.** Impossible visuals never appear in proof, demo, review, count or reaction-as-evidence roles. | F4 × T6 = ✕ |
| FR7 | **Impossibility on objects, light and scale; not on near-human faces.** Faces in impossible shots must clear 07 shot-QA for AI tells; prefer people at a distance or real-photo plates. | Face ECU inside an impossible shot → needs an explicit 07 pass |
| FR8 | **No fake interface.** No fake buttons, notifications or players, even as surreal elements. | Meta non-existent-functionality rule |
| FR9 | **No "real" claims.** Never caption or VO "real", "true story", "actual customer" over synthetic footage. | Text check |
| FR10 | **Measure trust, not just stop.** Run F4 as its own arm against a control of the *same trigger* in another format; read hook rate *and* hold rate (bait-and-switch shows as high hook / low hold) and scan comments for "AI"/"fake" before scaling. | Pre-registration line names hold rate as a secondary gate |
| FR11 | **Budget: ≤2 F4 cards per 15-card pool, ≤1 F4 arm per concept.** | Coverage check §6 |

---

## 6. Ideator coverage rules + Hook Card changes

### 6a. New and changed Hook Card fields
| Field | Status | Content |
|---|---|---|
| `format` | **NEW, required** | One F-code + sub-variant, e.g. `F4 scale-play` |
| `trigger` | **NEW, required** | One primary T-code |
| `trigger_2` | NEW, optional | One secondary T-code |
| `primitives` | NEW, required | P-codes present in frame 1 (`P1 onset · P2 face · P3 animal · P4 text`); ≥1 required |
| `truth_frame` | NEW, required for F4/F6/F7 (blank otherwise) | Second at which the real product is shown as it truly is/does |
| `mechanism` | **CHANGED → optional** | M-code if the card instantiates a gift recipe (§4a); `—` for new combos |
| `arm` | CHANGED | Adds the arm's **axis**: `format-arm`, `trigger-arm`, or `mechanism-arm` (both) |

All other fields unchanged (`01-03-hooks.md` §2). The hook ledger gains `format`, `trigger`, `primitives` columns so results can be read per cell.

### 6b. Coverage rules for a pool of ≥15 cards
1. **≥6 formats and ≥5 triggers** represented; each card has exactly one primary F and one primary T.
2. **Caps:** no format on >4 cards; no trigger on >6 cards (40%).
3. **Gift core floor:** ≥8 cards in `S★` cells.
4. **Exploration floor:** ≥3 cards (20%) in cells with <2 entries in the hook ledger, drawn from `S★`/`S` cells (§3). Fake reality counts here, capped by FR11.
5. **No `✕` cells**, ever. `W` cells allowed only with a one-line reason in `rationale`.
6. **Near-duplicate (within pool):** same F **and** same T **and** same frame-1 subject → keep one. (Replaces "same frame + mechanism".)
7. **Two independent passes** if a model ideates (unchanged); the second pass is told which cells the first left empty.
8. **Self-cull to 8–10** keeps ≥4 formats and ≥3 triggers among survivors.

### 6c. Distinctness between test arms (used by 01 and 03)
- Arms differ on **exactly the declared axis**: a *format-arm* holds T fixed and changes F; a *trigger-arm* holds F fixed and changes T; a *mechanism-arm* changes both (discovery only, because it is not attributable).
- Whatever the axis, arm winners **must show a different frame-1 picture** (subject, framing or onset event). Caption-only difference over the same picture is iteration by Meta's own definition and will share delivery ([STRONG], `01-03-hooks.md` §1c).
- The Phase-1 H1/H2 arms are a **trigger-arm inside F5/F2**: H1 = F5×T7 (name shown), H2 = F2×T3 (relationship). Record them that way in the ledger.

---

## 7. Critic and Selector implications

**02 Critic: new gates (binary, Stage A)**
| Gate | Applies to | Pass condition |
|---|---|---|
| **G7 Truth frame** | F4, F6, F7 (and any card with an impossible or composited element) | FR1–FR3: the product and its output are shown as they truly are by `truth_frame` ≤1.5s; nothing impossible is attributable to the product's function |
| **G8 Format policy** | F12, F13, F14, F15, F4-memorial | F12: passes G1 muted; F13: character speech, no implied real-customer endorsement; F14: artefact in scene, no interactive UI or system notification; F15: true number or real quote with source in the fact sheet; F4 memorial: FR5 |
| **G9 Tag validity** | all | The card actually does what its F and T tags say (a T2 card contains an expectation violation; an F1 card has an onset by 0.5s). Mis-tagged = return to Ideator for re-tag, not a quality fail, because wrong tags poison the ledger |

**Stage B anchors adjusted per format (S1 Stop power):** a format-specific "5" anchor so text-led and visual-led cards aren't judged on the same picture test:
- F2/F3/F14: line readable in ≤0.5s at 360px, ≤8 words.
- F1/F4/F6: onset or impossibility legible within 1s, frame-1 feature clutter low (Pieters 2010).
- F10/F13: face tight, emotion readable at phone size.

**S3 Open loop for T2 cards:** a "5" also requires the surprise to resolve to relevance inside 3s (Heckler & Childers).

**Calibration set:** the 4 known past hooks should span ≥2 formats so the panel isn't calibrated on one format only.

**03 Selector:**
- Step 4 (distinctness) now checks the declared arm axis (§6c) plus a different frame-1 picture.
- For an F4 arm, the outsider cold read adds one question: "Does the product itself do anything impossible?" A "yes" → reserve.
- The pre-registration line names the axis: "format-arm: F4 vs F1, T4 held".

---

## 8. Evidence gaps

1. **No hook rate by hook type.** Searched Motion, Foreplay, Varos, Benly-derived and vendor posts: none publishes hook rate *by* hook or format type. Motion's 2026 report (≈550–579k creatives, ~6k accounts) ranks hook tactics and visual formats by **hit rate and spend-use ratio**, where a "winner" is defined by spend relative to the account (≈10× median), not hook rate; tags are machine-classified; the window (Sep 2025–Jan 2026) is BFCM-heavy, which inflates promotional hooks; gifts are not a reported vertical [MODERATE]. Benly's 12k-ad medians (~28% Feed, ~31% Reels) are not split by type.
2. **No test of surreal/impossible openers.** The attention mechanism is strong (Itti & Baldi; Heckler & Childers); its net effect for an *AI-made* surreal hook, after NIQ-type halo, is unknown.
3. **No personalized-gift hook test of any kind** (same as `01-03-hooks.md` §5). Every `S★` mark in §3 is a reasoned hypothesis from mechanisms plus our own audits, not a measured result.
4. **Text-to-video transfer.** Curiosity, question and negativity evidence comes from headlines (Upworthy, lab studies); transfer to a video's frame 1 is assumed.
5. **Visual vs caption vs audio contribution in frame 1** is not isolated by any first-party or peer-reviewed study (already noted in `01-03-hooks.md` §1b).
6. **ASMR/sound-led** evidence is small and mixed (mostly negative except for ASMR-responsive viewers); sound-off share makes it a low priority.
7. **Native-UI formats** rank well in Motion lists, but the boundary between an allowed in-scene artefact and banned "non-existent functionality" is enforced by review, not published thresholds. Treat as review risk.
8. **What to fill it with:** our own ledger. Once ≥20 hooks are measured with `format`/`trigger` tags, compare hook and hold rate by F and by T (not by cell, which will be too sparse), and re-weight the exploration floor toward cells that beat the arm median.
