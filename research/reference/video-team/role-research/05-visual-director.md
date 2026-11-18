# Role 05: Visual Director. Research and spec

**Status:** research and spec, 2026-11-18. Proposed for the video-team methodology. Not yet adopted.
**Scope:** the role that turns an approved, time-stamped script (role 04) into a shot list or storyboard
and plans every visual asset behind it, including reference locking. It hands off to the editor (06) and QA (07).
**Tool-agnostic by design.** The role names no generator, stock library or LLM. Model-specific prompt
syntax lives in **per-tool adapter docs** (see §4.3). This file extracts the general principles from our
tool-specific docs (`seedance-prompt-method.md`, `image-prompt-method.md`, `image-to-video-prompt-method.md`,
`product-text-fidelity-2026.md`, `generation-prompt-guard.md`).

**Grades.** **[STRONG]** means two or more independent sources agree, or there is a primary or official source plus our own measurement.
**[MODERATE]** means one solid source, or several weak ones pointing the same way. **[WEAK]** means n≤2, vendor or practitioner opinion, or a house
hypothesis. **OWN** marks our measured production tests. They are facts about *making* the ads, not about how the ads perform.

---

## 1. Evidence summary

### a) Storyboard and shot-list practice: what a separate maker needs in order to execute

| # | Claim | Grade | Source |
|---|---|---|---|
| a1 | A usable shot description gives **shot size, who does what and where, the camera move with its speed or direction, the sound, and the duration**, in that order. On a fuller panel it also carries the exact script words, why the shot exists, and a to-do list of what the shot needs. | MODERATE | storyflow.so/blog/how-to-write-a-storyboard-shot-description-2026 · techsmith.com/blog/how-to-write-a-shot-list (shot no., size, angle, lens, continuity notes for props and costume, priority) |
| a2 | Cuts that **match an action** or stay **within a scene** are the hardest for viewers to notice (32.4% and 25.1% of such cuts missed, against 9.4% of between-scene cuts). Cues such as motion onset or a gaze carry attention across the cut. | STRONG (peer-reviewed eye-tracking) | Smith & Henderson, *Edit Blindness* (mdpi.com/1995-8692/2/2/11) · Smith, *Attentional Theory of Cinematic Continuity* (eprints.bbk.ac.uk/6679/1/6679.pdf) |
| a3 | ⚠️ **Implication for ads (our inference):** an invisible cut is smooth but adds no *energy*. Our shipped film had 8 clips joined by crossfades, and a change detector found **1 cut in 36.6s**. Use match cuts deliberately for meaning (for example, a name on the tag cuts to the same name on the wall), and use **hard visible scale jumps** for energy. | MODERATE (OWN measurement n=1 + a2 mechanism) | `ad-video-director-research.md` §0 |
| a4 | Keep screen direction consistent (the 180° rule) unless you break it on purpose. Re-establish geography with a wider shot when a subject crosses the line. This matters more for AI footage, because each clip is generated without knowing the shots next to it. | MODERATE (craft canon) | masterclass.com/articles/understanding-the-180-degree-rule-in-cinematography · adobe.com/…/what-is-the-180-degree-rule |
| a5 | **"Vary the angle" is not camera direction.** Shot sizes are composition. A storyboard must also name **one move** (dolly/push, pull, pan, tilt, track, orbit, crane, rack focus) with speed and direction. Without it the model defaults to a static or gently drifting camera. | MODERATE (OWN post-mortem + 5 converging vendor guides) | `ad-video-director-research.md` §1c–1d |
| a6 | Our own shooting script once had three designed shots in its `Camera` block, and none of them reached the generation prompt. **A storyboard field that is not compiled into the brief is lost.** | STRONG (OWN, documented) | `ad-video-director-research.md` §1b |

### b) Pacing and congruence between words and pictures

| # | Claim | Grade | Source |
|---|---|---|---|
| b1 | Value is front-loaded. On TikTok, ~50% of an ad's recall impact lands in the first 2s and ~90% by 6s. Meta/Nielsen put ~47% of a video's value in the first 3s. eye square found 62.5% of viewers gone within 2.5s. | STRONG (three independent sources, all saying "early") | ads.tiktok.com/business/en-US/blog/resonance-key-factor-ad-effectiveness · eye-square.com MediaAttentionBenchmark PDF · Meta/Nielsen via `video-ad-decomposition-2026.md` |
| b2 | **A cut, movement or visual change in the first 1–2s** improves hook rate, and a static opening loses viewers. | MODERATE (practitioner sources + OWN: a static opening shot dropped hook3 from 14.68 to 5.87) | affectgroup.com TikTok metrics guide · `seedance-prompt-method.md` testC2/C3 |
| b3 | Cut rate: our only verified long-running niche winner (333 days) cuts every **~2.5s (0.40/s)**, while our failed film cut every 36.6s. Practitioners give **1.5–3s per cut** in the opening. The original pipeline's "3–6s per scene" is too slow for the hook segment. | WEAK–MODERATE (n=1 benchmark; huge effect size) | `ad-video-director-research.md` §0 · increditors.com |
| b4 | **Early surprise** binds attention across viewers and reduces zapping, and **rising joy** retains viewers. Emotion measures explained 72% of zapping variance in an eye-tracking and facial-coding experiment. | STRONG (peer-reviewed, JMR) | Teixeira, Wedel & Pieters 2012, JMR 49(2) (hbs.edu/faculty/Pages/item.aspx?num=40850) |
| b5 | **The picture must match the words at the same moment.** In Mayer's multimedia principles, *temporal contiguity* (corresponding words and pictures shown together) was supported in 9/9 tests (median d≈1.22; Ginns meta-analysis d=0.78). *Coherence* (cut extraneous material) held in 10/11 tests (median d=1.32), and *signaling* (cue the key element) in 3/3. | STRONG (meta-analytic, but from learning research rather than ads) | Mayer & Fiorella, Cambridge Handbook ch.12 (cambridge.org …/C98AB3A6CE760DD63C048936EA0B3B44; edtechuvic.ca PDF) |
| b6 | ⚠️ Mayer's *redundancy* principle (graphics plus narration beats graphics plus narration plus identical on-screen text) **does not transfer** to Meta feeds. Most feed views are sound-off, so the burned-in caption *is* the words channel and there is often no narration. The rule we take from b5 is congruence: **each shot shows what its caption says at that moment.** It is not "avoid captions". | MODERATE (inference; sound-off share is in our decomposition doc) | b5 + `script-method.md` R7 |
| b7 | Perceived ad clarity improves processing fluency, and fluency predicts attitude toward the ad and purchase intent (N=176/204). | MODERATE | academia.edu/28401309 (subjective processing fluency study) |

### c) Generative-video production method (tool-agnostic)

| # | Claim | Grade | Source |
|---|---|---|---|
| c1 | **Lock identity and product references before any shot is made.** Feed a fixed reference set to every shot, with the most important reference first, few references, and one job per reference. Too many references blur priorities. | STRONG (official model guide + OWN tests + industry workflow guides) | `seedance-prompt-method.md` §Asset strategy · `ai-product-review-consistency-method.md` · ciaro.pro character-bible guides · ai25.studio workflow |
| c2 | **One camera move and one primary action per shot.** Compound motion causes instability. In OWN testC, four simultaneous motions turned a seated dog into a standing one. | STRONG (official guide verbatim + OWN) | `seedance-prompt-method.md` rule 1 + post-mortem |
| c3 | **Describe only what moves, and never re-describe what the reference carries.** Re-describing makes the model redraw the subject, and a redrawn subject drifts. | STRONG (multiple vendor guides + OWN D4 failure) | `image-to-video-prompt-method.md` THE ONE RULE · `generation-prompt-guard.md` |
| c4 | **Locate every action in space, not just on the body.** "Raises his hand into the light" produced a palm-out *stop* gesture in a grief ad. Say where each limb goes relative to the body and the camera, and what it touches. | STRONG (OWN, reproduced on two providers) | `seedance-prompt-method.md` Test E rule 4 · `image-prompt-method.md` LIMB RULE |
| c5 | **Positive framing.** Negations ("no X", "only Y shows") steer generators badly. This holds for LLMs, CLIP and text-to-image models. | STRONG (Google guide + Physics-IQ Verified rewrite rationale + OWN D5a) | arxiv.org/html/2606.18943v1 · `image-prompt-method.md` |
| c6 | **Visual realism does not mean physical correctness.** Across leading models, physical understanding was "severely limited" and unrelated to realism. Solid mechanics did worse than fluids. Hands handling objects (unboxing, key-in-lock, rotating a product) stay high-risk. | STRONG (peer-reviewed benchmark + OWN) | physics-iq.github.io · Motamed et al., WACV 2026 · `ai-film-studio.md` hard rule 7 |
| c7 | **The generator renders the product's printed text inconsistently.** A name can stay legible while its letterform drifts. Generators also *invent* text: in our tests a model wrote its own name on the product, and another rewrote "Alex" as "Kloe" by 3.0s. **The real lettering is composited or comes from a real still.** | STRONG (OWN, repeated across tests and products) | `product-text-fidelity-2026.md` · `BUILD-STATE.md` QA lessons |
| c8 | **Close-ups where the name *is* the proof come from a high-resolution still plus a camera move applied in edit** (pan or zoom at native resolution). This beat generated motion on letterform, geometry, sharpness and cost, and still passed our motion gate (hook3 11.02). Text on soft goods survives moderate generated motion. | STRONG for our rigid products (OWN, measured) | `RESEARCH-REPORT-2026-10-ad-production.md` §3 |
| c9 | **Draft cheaply, select from N, lock what works.** Make 3–4 takes at low resolution, change one variable per iteration, and finalize the keeper at full resolution. Generation is probabilistic, so plan for *selection*. | MODERATE (vendor guides + OWN practice) | `image-to-video-prompt-method.md` §2, §7 |
| c10 | **QA every shot at full resolution across several frames, never on one frame or a contact sheet.** A wedding ring the cast never wore was missed on the sheet, and a fold made "feeling" read as "ceeling" on a single frame. | STRONG (OWN, two independent misses) | `image-prompt-method.md` fix pass · `script-method.md` R23 |
| c11 | **When the product itself is a reference, the generator may redraw it** (it swapped the man and redrew the panel). Sometimes the correct shot uses *no* product reference: describe the light or shadow and bring the real product in at its own cut. | MODERATE (OWN n=1) | `BUILD-STATE.md` C2-B4 v1→v2 |
| c12 | **The generator renders what you name.** Naming an off-screen light source made the model build a stained-glass window *in frame*, so the model drew the product we sell. Keep named sources explicitly off-screen, or put the real object in the start frame. | MODERATE (OWN n=1, decisive) | `seedance-prompt-method.md` Test E rule 6 |
| c13 | **Product truthfulness is a legal and policy constraint, not just taste.** Under the FTC Act, a representation that is likely to mislead a reasonable consumer, and is material, is deceptive. Meta bans "deceptive or misleading practices". Meta's *mandatory* AI-disclosure rule covers social-issue, electoral and political ads. Commercial ads are not required to self-disclose, but Meta can auto-label detected AI media, and the label cannot be removed. | STRONG (primary sources) | ftc.gov/news-events/topics/truth-advertising · federalreserve.gov FTCA §5 summary · transparency.meta.com/…/unacceptable-business-practices · facebook.com/business/help/1486382031937045 |
| c14 | Viewers often detect AI ads, rate them as more "annoying/boring/confusing", and show **weaker memory activation even for "high-quality" AI ads**. The stated takeaway is quality and authenticity. AI is not banned. | MODERATE (single vendor neuroscience study, NIQ 2024) | nielseniq.com/…/2024/niq-research-uncovers-hidden-consumer-attitudes-toward-ai-generated-ads |

### d) Creative diversity, fatigue and the scene ledger

| # | Claim | Grade | Source |
|---|---|---|---|
| d1 | **Meta groups ads that "share key visual and thematic attributes"** and treats them as variations of one creative: "learnings and delivery optimizations are shared at the creative level". Meta's advice is to make ads "truly different in look, feel, storyline, and message" rather than small tweaks. | STRONG (Meta official) | facebook.com/business/news/demystifying-creative-diversification · …/the-creative-advantage-unlocking-the-power-of-diversification-with-meta-andromeda |
| d2 | Meta separates **fatigue** (overexposure to the same asset) from **similarity** (assets that differ technically but look alike). Similarity also drives fatigue. | STRONG (Meta official) | same as d1 |
| d3 | Fatigue is measured **per creative across all ads, campaigns and placements**. Clicks and conversions get more expensive with every repeated exposure, with no "wear-in" for direct response. At 4 repeated exposures, conversion likelihood is down ~45%. Ads Manager's fatigue status counts "all recent exposures of the ad's image or video, including those from other campaigns from your Page". | STRONG (Meta first-party analysis + Meta help) | medium.com/@AnalyticsAtMeta/creative-fatigue-… · facebook.com/business/help/1346816142327858 |
| d4 | Meta has not published how its grouping works or what similarity threshold it uses. Exact "% similarity" claims and "Entity ID" are industry shorthand. | STRONG (as a caution) | lemonado.io/blog/meta-andromeda |
| d5 | ⇒ **A scene ledger is justified, keyed on the attributes Meta says it groups by**: visual setting, cast, framing, storyline and message. It should record more than filenames. Reuse across *different concepts* risks merging them into one creative. Reuse *inside a controlled test* (one body, two hooks) is deliberate and must be logged as such. | MODERATE (our synthesis of d1–d3) | — |

### e) Casting and representation

| # | Claim | Grade | Source |
|---|---|---|---|
| e1 | One survey of personalized-gift buyers (88% US) found a median buyer age of **42** and **64% female**, with 35–54-year-olds spending the most per occasion. Men were somewhat over-represented among memorial-gift buyers (38% vs 35%). Other reports put 25–34 as the largest single band. | WEAK–MODERATE (vendor surveys; methods not independently verified) | beyond-memories.com/…/state-of-personalized-gifting-2026 · printzware.com (Technavio/Grand View cited) |
| e2 | US women buy gifts for friends (52% vs 36%) and adult children (36% vs 26%) more than men do. Men slightly lead for spouses. **The occasion is the top consideration for both.** | MODERATE (YouGov) | today.yougov.com/…/54532-how-men-and-women-in-the-us-differ-in-gift-giving-habits |
| e3 | **Most US consumers do not feel represented in online ads, and 71% expect brands to promote diversity.** Latino and Black Americans are 1.8× more likely to see negative stereotyping. In a separate ad test, the most inclusive ad gave a +23pt purchase-intent lift against +10pt for an appealing but non-inclusive ad. | MODERATE (Meta-commissioned survey; Microsoft Gen-Z study) | facebook.com/business/news/insights/the-difference-diversity-makes-in-online-advertising · Microsoft Advertising *Psychology of Inclusion* PDF |
| e4 | **Our hard rules come from OWN failures and outweigh any demographic default:** casting matches the customized printed artwork (skin tone, hair); on-screen gender, age and role match every caption pronoun; the giftee is never shown alone; and Meta's Personal Attributes policy applies (describe the character, never the viewer). | STRONG/HARD (OWN + user feedback + Meta policy) | `script-method.md` R6, R18, R19 · memory `casting-matches-caption`, `emotional-ad-show-family-connection` |

### f) Covers and thumbnails for paid Reels/Feed

| # | Claim | Grade | Source |
|---|---|---|---|
| f1 | A video-ad thumbnail **shows before the video starts and after it ends**. By default Meta **dynamically picks up to 3 frames** with slight adjustments and serves each person the one it predicts works best. You can also upload a thumbnail or choose a frame. | STRONG (Meta help) | facebook.com/business/help/1439592126314666 |
| f2 | Autoplay needs a minimum share of pixels in view (25% on IG Feed, 50% on FB Feed and Reels, 100% on Stories). Once it plays, **the first frames *are* the cover**. The static thumbnail matters only with autoplay off, on data saver, in previews and in end states. | STRONG (Meta help) + MODERATE (practitioner) | facebook.com/business/help/2013114112289197 · roaspig.com · adespresso.com $1k thumbnail test |
| f3 | Claims that "custom thumbnails lift CTR 25–35%" are vendor numbers with no published method. **Do not cite them.** | — | roaspig.com (rejected as evidence) |
| f4 | ⇒ Of the original pipeline's "3 covers", the paid-ad version that is real is **frame 1 variants**, which is a hook test. A single thumbnail still is secondary and worth one asset, not three. | MODERATE (synthesis) | f1–f2 + `script-method.md` R1, R4 |

---

## 2. Role 05 spec: Visual Director

### 2.1 Mission
Put the script on screen so that **every second shows what its words say**, the **product is truthful and
identifiable from frame 1**, the cut has **energy**, and **every asset can be made by whatever generator,
camera or library is in use**. The role owns *what is seen*. It does not own *what is said* (04), *how
the pieces are assembled* (06) or *whether the result passes* (07).

### 2.2 Inputs (reject the handoff if any is missing)
1. **Approved script (04):** time-stamped beats, with caption text per beat, sound-off readable, concept and hook variants named.
2. **Product truth pack:** real product photos on a plain background (≥1500px, personalization legible), extra angles, any real footage, the exact personalization values that ship (or a flagged demo set), and the real lettering or artwork file.
3. **Brand kit:** palette, caption font, logo, safe-zone spec (9:16: keep text out of the top 14%, bottom 35% and 6% sides; Meta help 980593475366490).
4. **Scene ledger** (§2.6) for this product and store, plus the live list of running ads.
5. **Reference library:** previously locked cast and product reference sets (may be empty).
6. **Adapter docs** for each tool the producer has made available, plus that tool's cost and limits.

### 2.3 Outputs
**O1. Shot list / storyboard.** One row per *shot*, not per beat. A beat may hold 1–3 shots.

| Column | Content | Rule |
|---|---|---|
| `shot_id` | `<ad>-<beat><letter>`, e.g. `C1-B2a` | Stable. QA and the ledger reference it. |
| `tc_in–tc_out` | Edit timecode, in seconds | Varied lengths. Hook segment 1.0–2.5s per shot; never uniform. |
| `serves` | Exact caption or VO words on screen during this shot | **Congruence (b5):** the picture shows this. |
| `regime` | `energy` or `stability` | Energy for hooks and narrative beats. Stability for product truth and name close-ups. |
| `size/angle` | ECU / CU / MCU / MS / WS / OTS, plus angle | Adjacent shots differ by at least one size step (scale jump). |
| `camera_move` | ONE named move, with direction, speed and end state | Required. "Static/locked" allowed only after shot 1 and only with a stated reason. |
| `subject_action_in_space` | Who or what, the single primary action, and where each limb or object is relative to the body, the camera and other objects | LIMB RULE. Emotion written as physical detail. |
| `source_type` | REAL-PHOTO · REAL-FOOTAGE · CUSTOMER-PHOTO · STILL+MOVE (generated or real still, move in edit) · GEN-VIDEO · STOCK · MOTION-GFX | Chosen by §2.5. |
| `refs_required` | Reference IDs from the locked set, each with a role (character / product / scale / composition / light) | Few references, one job each, most important first. |
| `text_to_composite` | Every legible string in frame: name, caption, prop text | Never generated. List the source file. |
| `continuity` | Wardrobe, props, hand state (ring or no ring), light direction, screen direction, time of day, product scale vs anchor | Carried from the reference sheet. |
| `takes / draft→final` | N takes; draft and final resolution | Default 3 takes for people and hands, 1 for low-risk shots. |
| `acceptance` | Shot-specific pass criteria beyond the standard checklist (§2.7) | e.g. "dog stays seated", "palm never faces camera", "Alex ≥100px wide at end crop". |
| `cut_in / cut_out` | Hard, or match on action/shape/word (state which), plus the intended transition | Hard cut is the default. A dissolve is only for a real time jump. |

**O2. Reference sheet** (the gate artifact, §2.4 step 3). Per recurring person: 8 separate full-resolution
views (front, ¾L, ¾R, full standing, full seated, hands, two expressions), generated from views 1–3 to
avoid drift chaining. Per product: a real hero photo, any angles, and a **scale-anchored plate** (the product
beside a familiar object at true size). Plus the real lettering cut-out and props that carry identity or text.
Each entry lists its traits as **2–3 stable features** (the label reused in every brief) and its **must-not-change
list** (e.g. "no ring", "glasses wire-rimmed", "dog seated").

**O3. Generation briefs.** One per generated asset, in the §4 template. The adapter turns each brief into a prompt.

**O4. Asset plan and budget:** REUSE vs NEW per shot, takes, cost estimate from the tool's adapter, and order of work.

**O5. Frame-1 / cover pack:** frame-1 spec per hook variant, plus one thumbnail still (§3.4).

**O6. Scene-ledger update** (§2.6), written when the ad ships, not when it is planned.

### 2.4 Procedure
1. **Read the script beat by beat** and split beats into shots. For every shot write `serves` first; a shot that serves no words or caption needs a stated reason, otherwise it is extraneous (coherence, b5). The product must be identifiable by 1s (R1) and the personalization must be the hero visual (R2), unless the script is a deliberate story-film test cell (R20).
2. **Rhythm pass.** Set durations: hook shots 1.0–2.5s, others 2–5s, no two adjacent shots the same length and size, and at least one scale jump per beat. Mark frame 1's pattern interrupt (motion on frame 1, text-first, unusual angle, CU after WS) and the **one designated surprise** in the first 2s (b4). Target cut cadence ≈ the benchmark (~0.4 cuts/s), provisional because n=1.
3. **Reference lock (HARD GATE).** List every recurring person, product, prop and location the shots need. Reuse locked sets from the library, otherwise build them. Check the casting against **every caption pronoun and the printed artwork**. Hand to QA (07) for an identity, scale and on-model check, then to the approver. **No scene asset is made before sign-off.** At the reference stage a fix costs one still; afterwards it costs a reshoot.
4. **Source choice** for each shot (§2.5) and the ledger check (§2.6). Log any reuse.
5. **Write the generation briefs** (§4). For each tool in use, run the brief through that tool's adapter doc and the mechanical prompt guard, if one exists.
6. **Draft pass:** low resolution, N takes, one variable changed per retry. Self-check against §2.7 before passing anything to QA.
7. **Final pass** of the keepers at delivery resolution. Composite real text and stills. Build the camera move on stills at native resolution.
8. **Handoff to 06/07** (§2.9). After ship, **update the ledger**.

### 2.5 Source-choice decision rules (first match wins)
| If the shot… | Use | Why |
|---|---|---|
| shows the product **as the proof** (name, artwork, geometry read closely) | **REAL-PHOTO or a reference-faithful high-res still → camera move applied in edit** | c7, c8, c13. The model never draws what we sell. |
| shows the product in a **wide or medium scene, not read closely** | GEN-VIDEO from a start frame that contains the real product (or a composite of it), with the product pinned by a constraint | c3, c11. Drift is invisible at this size. Verify scale against the anchor. |
| needs **personal proof** ("this is someone's real dog/family") | CUSTOMER-PHOTO (with permission) or REAL-FOOTAGE | Authenticity (c14). Never fabricate a "real customer". |
| is a **human emotional beat** (face, breath, a gaze) | GEN-VIDEO from the locked character set, with one move and the action located in space | c1, c4. Locked references hold identity. |
| needs **hands manipulating** the product (unbox, rotate, hand over) | Reframe so the action is implied (hand resting, box closed, before and after); otherwise best-of-N with the receiver's face visible | c6, casting memory. Mechanical hand actions are high-risk. |
| is a **metaphor or hard-to-film context** (light through a window, a memory, a place) | GEN-VIDEO or STILL+MOVE | Where generation earns its keep. |
| has **motion that is the content but is generic** (rain, steam, hands typing, a street) | STOCK, if it is licensed and casting- and time-consistent; otherwise GEN-VIDEO | Cheap, physically correct motion (c6). |
| is **text-first, a name reveal, an offer or a CTA** | MOTION-GFX over footage | Exact typography; works sound-off. |
| is a **still with nothing that should move** | STILL+MOVE, never a frozen frame | The motion gate fails static (≤10% static frames). |

### 2.6 The scene ledger (anti-repeat, adapted to Meta's grouping)
One row per shipped shot: `date · ad_id · concept · shot_id · setting · cast_ids · product_presentation
(hero/in-scene/shadow/box) · size+move · palette/light · frame1? · asset_file · reuse_reason`.
- **Exclude** a setting+cast+framing combination already used by a *different concept* within the last 30
  days, or by any currently running ad. Meta groups by visual and thematic attributes (d1). Thirty days is our
  default, not a Meta number (d4).
- **Allowed and logged:** byte-identical reuse inside a controlled test (the same body across hook variants;
  the same name-reveal beat across concepts when the plan locks it). Tell the media buyer that Meta may treat
  these ads as one creative.
- **Required for frame 1:** each new concept's first second must differ from every running ad's first second in at least two of
  setting, cast, framing and colour.

### 2.7 Shot acceptance checklist (self-check before QA; QA re-runs it independently)
Judge every check at **full resolution on ≥5 frames spread across the clip**.
1. **Serves:** a muted viewer would match the picture to the caption it sits under.
2. **Product truth:** shape, artwork, colour and scale match the real product and the scale anchor. No invented product or second product in frame.
3. **Text:** every legible string is the real one. No model-invented words, names, logos or watermarks anywhere in frame.
4. **Identity:** face, hair, glasses, wardrobe and accessories match the reference sheet, including the must-not-change list (rings!).
5. **Anatomy:** five fingers per visible hand, limbs where the brief put them, no fused objects, eyes as specified.
6. **Physics:** objects rest and hang correctly, light comes from the stated side, shadows are consistent, nothing floats or morphs (seated stays seated).
7. **Casting:** gender, age, role and skin/hair match the caption pronouns and the printed artwork. The giftee is shown with connection, not alone.
8. **Motion:** the named move happened, the opening shot moves, and there is no slow-drift mush. Motion score passes the gate where one exists.
9. **Usable window:** mark the in and out seconds that pass. Drift often starts late (a name rewritten by 3.0s), so **never extend past the verified window.**
10. **Frame safety:** key subject and product fall inside the safe zone in 9:16, and a 4:5 crop path exists.

### 2.8 Failure modes and guards (each observed in our builds)
| Failure | Guard |
|---|---|
| Camera direction written in the storyboard, lost before generation | Brief template has a required `camera_move` field. The adapter refuses to emit a prompt without it. |
| Static or slow opening (hook3 3.59 vs 18.05 benchmark) | Shot 1 always carries a move. Motion gate in QA. Hard cuts by default. |
| Identity drift across clips; extra wedding ring appears | Reference gate, must-not-change list, full-resolution hand QA. |
| Model writes its own name or another name on the product | No generated text, ever. Composite the real lettering; trim to the verified window. |
| Model draws the product (invented stained-glass window; redrawn panel when the product was a reference) | Named sources stay off-screen. Product from real stills. Try "no product reference" for light-only shots. |
| Stop-gesture or punched-through hand | LIMB RULE. Every limb placed and given a contact point. "No hand" is a valid fix. |
| Pose morph (dog sat, then stood) | One move. Constraint naming the specific failure ("stays seated"). |
| Product oversized in wide shots | Scale-anchored reference. Product in close/medium framing unless verified. |
| Casting contradicts captions or artwork | Pronoun and artwork check at the reference gate and again per shot. |
| Lonely giftee | Every emotional beat shows a relationship cue (a giver, a photo, a second person, a memory). |
| One-frame QA misread or miss | ≥5 frames, full resolution. |
| Looks "AI": weak memory, negative halo (c14) | Prefer real stills for product proof; give the imperfection cues (handheld, grain); reject plastic skin and over-smooth motion. |

### 2.9 Handoff to 06 Editor and 07 QA
Deliver a folder per ad: `shotlist` (O1, with each shot's verified in/out window), `refs/` (O2), every accepted
asset named by `shot_id`, **text plates and lettering files with their exact paste position**, camera-move parameters for
STILL+MOVE shots (start and end centre plus crop width, ease), the frame-1/cover pack, and a list of known
risks per shot. The editor must not re-time a shot outside its verified window or swap the source type without
returning it to 05. QA receives the same checklist (§2.7) and judges independently. **05 does not grade its own work as
final.**

---

## 3. Recommendations

### 3.1 Art/continuity: inside role 05 as a gated sub-function, verified by QA. Not a separate role.
**Why inside.** The references a shoot needs are determined by the shot list: which angles, which hand
state, which props carry text, and where scale must be anchored. Our worst production loss happened at a role boundary.
The DP's camera plan was written and then discarded before generation (a6). Splitting art from shot design adds
another boundary of the same kind, and the person writing the briefs would be using references they did not design. The
team is small and agent-run. Every extra handoff is a place where context drops.
**What stays separate.** *Verification.* References are approved by 07 QA plus the human approver, never by
the role that built them. The old studio's real value was the **hard gate**, not a separate crew member, and the
gate is kept.
**When to split later.** If the store runs several products in parallel and the **reference library** (cast
and product sets reused across many ads) becomes a standing asset with its own maintenance, split it out as an
*Asset Librarian / Continuity* role that owns the library and ledger. Shot design stays in 05.

### 3.2 The original's 4 sources, adapted
| Original | Ours | Change |
|---|---|---|
| Owner's video library | **Real product photos and footage** (+ a growing library of accepted shots) | Mandatory for product-proof shots, not just one option among several (c13). |
| Real photos when the voice turns personal | **Customer and UGC photos (permissioned)** | Same trigger. Never fabricate "real" testimonials or pets. |
| AI images for metaphors and hard contexts | **STILL+MOVE** and **GEN-VIDEO**, split | Stills plus an edit-applied move are the default for anything that must stay exact. Generated motion goes where motion and emotion are the content. |
| Stock when motion is the content | **STOCK** (kept) | Plus a fit check on casting, era and season. |
| — | **MOTION-GFX** (added) | Name reveals, text-first hooks, CTA. |

### 3.3 Anti-repeat log: keep it, re-key it to Meta's grouping (§2.6)
The original excludes recently used scenes for *viewer* freshness. In paid ads there is a second reason,
which is stronger and documented: Meta groups look-alike ads and shares learning across them (d1), and
fatigue is counted per creative across campaigns (d3). So the ledger records visual and thematic *attributes*,
not just clip IDs, and it separates **deliberate test-control reuse** (allowed) from **cross-concept
repetition** (blocked).

### 3.4 Audience fit: replace "25–50, local ethnicity" with story-and-artwork casting
- On-screen people play **story roles**: the giver (buyer proxy, typically 35–55 and more often a woman, e1–e2, WEAK–MODERATE) and the recipient (whose age is set by the product: grandparent 65–85, pet owner, parent).
- **The hard rules beat the demographics (e4):** match the printed artwork, match the caption pronouns, show connection, and never imply the viewer's personal attributes.
- **Diversify casting across concepts, not within a test cell.** It widens relevance (e3) and helps creative diversity (d1). Hold casting fixed inside a controlled hook test.

### 3.5 "3 covers": convert to a frame-1 pack plus one thumbnail
- Paid placements autoplay, so **frame 1 is the cover** (f2). Deliver one frame-1 spec per hook variant the
  plan asks for. These are the real test variable and belong to the hook test, not to "covers".
- Deliver **one thumbnail still**: a product+name hero frame with clean text inside the safe zone. Meta shows it before start,
  after end, and with autoplay off (f1). Leaving the thumbnail on automatic is acceptable. Meta then picks up to 3 frames
  itself, so make sure every candidate frame (first, mid, last) is on-brand and truthful.
- Drop "same hook, 3 backgrounds" as a deliverable. Background-only variants are the small tweaks Meta
  groups as one creative (d1).

---

## 4. Generation brief template (tool-agnostic)

### 4.1 Fields. Every brief has all of them; "n/a" must be written explicitly.
```
BRIEF  <shot_id>  v<n>                      output: still | video   regime: energy | stability
PURPOSE      caption/words this shot serves; the one thing the viewer must see
START STATE  start frame or reference list, each with ONE role:
             [ref-id → character | product | scale-anchor | composition | light/style | camera-path]
SUBJECTS     label := 2–3 stable features (reuse the label everywhere; never re-describe a referenced subject)
FRAMING      shot size, angle, lens feel, subject position (thirds), aspect ratio + crop-safe area
CAMERA       ONE named move: direction, speed, ease, end state   (shot 1 must move)
ACTION       ONE primary action per subject, verb-led, quantified, gentle;
             every limb located: where it is relative to body/camera/objects and what it touches;
             emotion as physical detail
SECONDARY    ambient motion allowed on non-product elements (curtain, light band, steam)
LIGHT        source + side (named sources stay OFF-SCREEN) + change across the shot
SHOTS        for video: named Shot 1 / Shot 2 (each its own single move), no timecodes in the prompt
MUST NOT CHANGE   the specific failure modes for this shot, positively phrased
             ("dog stays seated", "ring finger bare", "panel geometry exactly as reference")
TEXT         none generated. List composited strings + file + position, or "no legible text in frame"
DURATION     generate length vs edit window (generate ≥ edit; trim to the verified window)
DRAFT/FINAL  takes N · draft resolution · final resolution · variable changed since last version
ACCEPTANCE   shot-specific checks added to the §2.7 checklist
```

### 4.2 Principles every adapter must keep (whatever the model)
Use positive framing. Keep prompts short (the length cap comes from the adapter). Lead with the camera move when the tool weights early words.
Give every reference a role. Never re-describe what a reference carries. Use one move and one primary action per shot. Locate
limbs in space. Name emotion as physical detail. Generate no text and keep the product un-drawn. Write constraints that
name *our* failure modes, not generic boilerplate. Draft low, select from N, change one variable at a time.

### 4.3 Where per-tool adapter docs plug in
`research/reference/video-team/adapters/<tool>.md`, one per generator in use. Each adapter defines: the field
order and syntax that tool prefers, how it accepts references (count limit, indexing, roles), its
camera-move vocabulary and reliability, the word cap, negative-prompt support, structured parameters vs prose
(aspect, duration, resolution, seed), its minimum and billable duration, cost per second or image, and known
failure modes with tested fixes. Treat the current docs as the first adapters: `seedance-prompt-method.md`
(video), `image-prompt-method.md` (three image models), and `image-to-video-prompt-method.md` (i2v cheat sheet).
The mechanical prompt guard (`generation-prompt-guard.md`) is the enforcement layer. Extend it per adapter
so the brief→prompt step is checked before any spend. **Comparing tools:** either write each arm in its own
adapter grammar, or keep one prompt and mark the non-native arms as indicative only (`seedance-prompt-method.md` scope note).

---

## 5. Open items
- The cut-rate target rests on one benchmark ad. Score 10 or more Ad-Library-verified winners before hard-coding it.
- Whether multi-reference conditioning beats a single start frame for identity across many clips is still untested here (report §9).
- The ledger's 30-day exclusion window is a house default, so revisit it once creative-level fatigue data exists for our account.
- Thumbnail strategy: test automatic vs a chosen still on one ad set before standardizing.
