# MJ4U-133-C0: criteria sheet (edit + final QA)

> **Status: LOCKED 2026-11-23 for test MJ4U-133-C0** (6 concepts × 2 hooks = 12 ads, each in 9:16 and 4:5 = 24 files).
> **Changes after lock = S3 proposals only.** A new concern found by 06 or 07 is filed as an S3 "proposed criterion" for the user. It never turns into a fail after the fact. Only the user changes this sheet or waives an S2.
> **Users:** role 06 (Editor) builds to this sheet; role 07 (QA, final mode) judges every delivered file against it. Every line is a pass condition checkable on the delivered files (or, for the U group, on the upload package).
> **Sources (precedence top to bottom when they disagree):**
> 1. `marketing/facebook-ads/MJ4U-133-C0/BRIEF.md` (locked with the user 2026-11-23) and the user rulings in `research/reference/video-team/README.md` §6
> 2. `CLAUDE.md` hard rules (family connection, casting matches caption, ad-copy line breaks, media out of git)
> 3. `research/reference/video-team/concept-framework.md` §4 (hook elements) and §6 (C0 fixed list, test integrity)
> 4. `research/reference/video-team/README.md` §2 (rules) and §3 roles 06/07; `role-research/06-07-edit-qa.md` §2–§3
> 5. `research/reference/video-team/hook-framework.md` §5 (FR1–FR11) and §6c (arm distinctness)
> 6. `research/reference/script-method.md` R1–R24
> 7. Template and house caption style: `marketing/facebook-ads/suncatcher-phase1/EDIT-CRITERIA.md`, `CAPTION-SHEET.md`
>
> **Product facts:** `products/MJ4U-133-family-wood-ornament/product.json` F1–F10 (3 mm plywood, printed one side, 4/5/7 in, 2–10 members incl. pets, name ≤15 characters under each member, 4-digit year, family on a snowy ledge in Santa hats). Hero artwork: `products/MJ4U-133-family-wood-ornament/ads/source-images/hero-family-2026-tree.png`.

**How to read the "Lock" column.**
- **FIXED** = on the C0 fixed list (BRIEF "FIXED in every ad" + concept-framework §6). **Identical in every one of the 12 ads** (test integrity): a difference between ads is a broken test, not a style choice.
- **BRIEF** = a rule carried in BRIEF.md or ruled by the user.
- **HARD** = a policy, legal or production-correctness rule. Breaking it ships a wrong or rejected ad regardless of performance.
- **TEAM** = a video-team rule (README §2/§3, role specs).
- **report** = research or opinion grade. 07 measures and reports it as S3; it never blocks.

**Severity** (07): S1 blocker · S2 major · S3 minor. **PASS = zero S1 and zero S2.** S1 policy and rights items are never waived. A concept whose 2 ads (× 2 formats) don't all pass does not ship.
Strength labels are copied from each source: script-method STRONG / MODERATE / WEAK / HARD; 06-07 research [STRONG]/[MODERATE]/[WEAK]; decomposition [DATA]/[OPINION].

---

## (a) The criteria (72)

### A. Fixed list: identical in every ad (test integrity)

| # | Criterion (pass condition) | Source | Strength | Lock | Enforced (06 step · 07 check · sev) |
|---|---|---|---|---|---|
| E1 | Length **20.00s ±1 frame**, both formats, all 12 ads | BRIEF FIXED; CF §6 (15–25s); R10 | user-locked; R10 MODERATE; Meta Feed ≤15s [A] is the counter (see conflicts) | **FIXED** | 06 §2 step 2 · 07 T4, I3 · S1 |
| E2 | Every ad delivered as **9:16 and 4:5**; the 4:5 is **re-framed per shot** (no letterbox, no blind centre crop) | BRIEF FIXED; README §3-06 | [STRONG] Meta | **FIXED** | 06 step 8 · 07 T1, I3 · S1 |
| E3 | **Product visible from frame 1 (0.00s)** at VS1 or higher (HE8: present; ≥1/3 width = VS2; names legible = VS3), and **identifiable as the family ornament by 1.0s** | BRIEF FIXED (VS1+); CF §4a HE8, §6; R1; hook gate G1 | R1 **STRONG** | **FIXED** | 07 V6, C6 (frames 0.00 / 0.5 / 1.0) · S1 |
| E4 | **House caption style, same treatment in all 12 ads:** bold sans (house = Arial Bold), white, sentence case, black outline outside the glyph (10px at 1080w; ≥8px) + soft shadow, ~60px cap height at 1080w (84px font; scale ×1.333 at 1440w), ≤2 lines, centred, hard on/off (no fades) | BRIEF FIXED ("captions, house style"); CAPTION-SHEET final D5; caption-design | outline > shadow: verified 3-0 | **FIXED** | 06 step 5 · 07 C4, I3 · S2 |
| E5 | **Hook caption on screen by 0.5s** (HE6 TM1/TM2) | CF §4b (fix by rule); decomposition "Captions" row | [DATA] / MODERATE | **FIXED** | 07 frames 0.00 / 0.5 · S2 |
| E6 | **One music bed in all 12 ads:** AI-generated on a paid/commercial plan, the **same file hash**, starting on frame 1 at the **same track offset**; audio runs the full 20s | BRIEF FIXED; CF §6; R13 | R13 MODERATE | **FIXED** | 06 step 6 · 07 T3, I2 · S1 |
| E7 | **No VO or dialogue**, unless the concept's locked script declares dialogue because its format needs it; then the same voice and lines in both ads of that concept | BRIEF FIXED; R13; README §5 (voice per concept) | R13 MODERATE | **FIXED** | 07 S1 (vs script) · S1 |
| E8 | CTA button **"Shop Now"** on every ad | BRIEF FIXED; R8 | R8 MODERATE | **FIXED** | upload · 07 I5 · S1 at upload |
| E9 | **End card identical in all 12 ads:** the text **"Personalize yours"** verbatim + the store name lockup, the only CTA in the video, on screen **≥2.0s through the last frame**, over a **moving** plate of the real ornament (no frozen card); same text, treatment, position, start time and plate frames in every ad (zero pixel diff across ads inside the end-card window) | BRIEF FIXED; R8; R12; 06 step 7 | R12 WEAK (moving end); single CTA [STRONG] | **FIXED** | 06 step 7 · 07 B2, I1, I3, S1 · S1 |
| E10 | **Offer: none.** No price, discount, "sale", free shipping, bundle, deadline, "order by" or "arrives by Christmas" claim anywhere: picture, captions, VO or end card | BRIEF FIXED ("no discount, no deadline claim") | user-locked | **FIXED** | 07 S1, P2 · S1 |
| E11 | **Advantage+ creative enhancements that alter the video OFF** (auto-crop, text, music, overlays, touch-ups); asset customization **9:16 → Stories/Reels, 4:5 → Feed**; settings recorded | BRIEF FIXED; 06-07 I5 | [STRONG] Meta dev docs | **FIXED** | upload · 07 I5 · S1 at upload |
| E12 | **Hook elements fixed by rule** (not C0 variables): hook audio cue = bed only or a sync hit on the onset (AU0/AU1; AU3 only in a declared-dialogue concept); hook caption **≤10 words** | CF §4b (user directive 2026-11-19); hook card spec | MODERATE | **FIXED** | 07 C1, S1 · S2 |

### B. Test integrity inside a concept and across the round

| # | Criterion (pass condition) | Source | Strength | Lock | Enforced |
|---|---|---|---|---|---|
| E13 | The two ads of a concept (`K{nn}X{n}-H{a}` and `-H{b}`) are **frame-identical and audio-identical outside the hook window**: zero frame-hash/pixel diff, same music offset and gain, LUFS within 0.2 LU | README §2.8; 06-07 I1/I2 | STRONG (house framework) | TEAM | 06 step 3 (control first, hook swapped) · 07 I1, I2 · S1 |
| E14 | The hook window (0.00 → its declared end, incl. the hook caption, ≤3.2s) is written in the concept's locked script and is the **same length in both ads** of the concept, so the body starts on the same frame | follows from E1 + E13; CAPTION-SHEET D4 precedent | — | TEAM | 07 I1 · S1 |
| E15 | The two hooks of a concept **differ in the frame-1 picture** (subject, framing or onset event), never by caption only | hook-framework §6c; README §3-03 | [STRONG] Meta groups same-visual ads | TEAM | 07 frame 0.00 of both ads · S2 |
| E16 | Each concept's frame 1 differs from the frame 1 of every ad of **another** concept, and of every running ad, on ≥2 of setting, cast, framing, colour (scene ledger) | README §3-05 scene ledger | [STRONG] Meta grouping; window is house | TEAM | 07 vs `_ledgers/scene-ledger.csv` · S2 |
| E17 | **Naming:** file `MJ4U-133_C0_K{nn}X{n}-H{nn}_E0_{916\|45}_v{NN}.mp4`; Meta ad name = ad key `MJ4U-133_C0_K{nn}X{n}-H{nn}_E0_v{NN}`; codes match `cells.csv` / `hooks.csv`; no delivered version overwritten | BRIEF; README §4a | MODERATE | TEAM | 07 I4 · S2 |
| E18 | **Whole concepts ship:** both hooks × both formats pass, or the concept waits (no concept with 1 ad or 1 format) | 06-07 §3 | STRONG for us | TEAM | 07 verdict · S1 for the concept |

### C. Technical spec (measured on the delivered file)

| # | Criterion | Source | Strength | Lock | Enforced |
|---|---|---|---|---|---|
| E19 | 9:16 ≥1080×1920 (target 1440×2560); 4:5 ≥1080×1350 (target 1440×1800); square pixels; nothing below 1080 upscaled and called 1440 | README §3-06; Meta Ads Guide | [STRONG] | TEAM | 07 T1 · S1 |
| E20 | H.264, progressive, constant fps equal to the recipe fps (same fps in all 12), no edit lists | 06-07 T2 | [STRONG] | TEAM | 07 T2 · S1 |
| E21 | Stereo AAC ≥128 kbps | 06-07 T3 | [STRONG] | TEAM | 07 T3 · S1 |
| E22 | Integrated **−16 LUFS ±1** (−18 ±1 if declared dialogue leads); **true peak ≤ −1 dBTP measured after encoding**; no clipping | README §3-06; AES TD1008 | [STRONG] standard / [MODERATE] applied to Meta | TEAM | 06 step 6 · 07 T5 · S2 |
| E23 | No unplanned black (≥2 frames), freeze (≥0.5s) or silence (≥0.3s) | 06-07 T6 | [STRONG] broadcast QC | TEAM | 07 T6 · S2 |
| E24 | ≤3 flashes in any 1s; no shock or sensational imagery | WCAG 2.3.1; 06-07 T7, P6 | [STRONG] | HARD | 07 T7, P6 · S1 |

### D. Hook (0–3s)

| # | Criterion | Source | Strength | Lock | Enforced |
|---|---|---|---|---|---|
| E25 | **Muted 0–3s cold read:** someone who did not build the ad says what is sold (a personalized family ornament) and who it is for | G1; 06-07 C6; R7 | "mandatory" (plan rule) / R7 STRONG | TEAM | 07 C6 · S2 |
| E26 | **The opening shot moves:** an onset by 0.5s (ON1–ON5; never a static frame 1) | R4; CF §4a HE3; README §3-05 "shot 1 must move" | R4 MODERATE | TEAM | 07 V6 · S2 |
| E27 | Hook shots are **1.0–2.5s** each | README §3-05 rhythm | MODERATE (front-loaded value) | report | 07 · S3 |
| E28 | The body **pays the hook's promise within 3s of the hook's end**; the promise is fully paid **by 12.0s** | hook gate G3; README §3-04 | MODERATE | TEAM | 07 S2 (watch hook + next 3s) · S2 |
| E29 | **If a hook is fake-reality (F4):** a truth frame (the real ornament in a real setting) by ≤1.5s; the impossibility acts on the world around the ornament, never on the ornament (it never glows, floats, moves by itself, animates its printed figures or changes its print); the impossible part is obviously impossible; no fake UI; no "real" / "true story" text | hook-framework FR1–FR3, FR8, FR9 | **HARD** | HARD | 07 S2, P2 · S1 |

### E. Pacing, cuts, camera

| # | Criterion | Source | Strength | Lock | Enforced |
|---|---|---|---|---|---|
| E30 | **Hard cuts by default.** A dissolve (≤0.4s) only at a time/place jump marked in the locked script; never at the hook boundary or inside the hook window | R11; 06 step 4; CAPTION-SHEET D2 | R11 MODERATE | TEAM | 06 step 4 · 07 T8 · S2 |
| E31 | **Detected cuts = planned cuts** (scene detection vs the recipe; a missing cut = a mushy dissolve, an extra one = a glitch) | 06-07 T8; director §0 | [STRONG] own measurement | TEAM | 07 T8 · S2 |
| E32 | Non-hook shots **2–5s**, lengths varied; **no two consecutive shots the same length** (equal = within ±1 frame) | R11; README §3-05; script-method pre-flight | R11 MODERATE | TEAM | 07 cut list · S2 |
| E33 | Cut rate reported per ad (gift median 0.22 cuts/s, max 0.50; 05 provisional target ≈0.4) | R11 evidence; README §3-05 | directional; n=1 | report | 07 · S3 |
| E34 | Motion gate reported: hook3 ≥8, motion ≥6, cuts/s ≥0.15, onsets/s ≥0.25, static ≤10% | `research/scripts/motion_qa.py` | n=1 benchmark | report | 06 self-check · 07 T8 · S3 |
| E35 | **One camera move per shot**; every still moves from its first frame to its last (never a frozen frame); the **closing frame moves** | README §3-05; R12; 06 step 4 | R12 WEAK; TEAM rule | TEAM | 07 V6 · S2 |
| E36 | Only shots accepted by 07 shot mode (Gate C) are used, and only inside their **verified in/out window** | README §3-05/07 | TEAM | TEAM | 07 vs recipe · S1 |

### F. Product truth (MJ4U-133 ornament)

| # | Criterion | Source | Strength | Lock | Enforced |
|---|---|---|---|---|---|
| E37 | The ornament in every shot is the **real artwork** (the personalizer render / hero file) composited, or a real photo/still. A generator never draws the ornament, its printed figures, the names or the year | R21; README §2.5; BRIEF rules carried | **HARD** | HARD | 07 V3, P2 · S1 |
| E38 | Beats where the names or year are the read use a **high-res still of the real artwork with the move added in the edit**, never a generated push-in (rigid 3 mm wood) | R22 | **HARD** | HARD | 07 V3 · S1 |
| E39 | **Every printed name and the 4-digit year are exact** (character for character vs the artwork file and the caption sheet) and **legible by eye on ≥5 frames** per proof beat; each name ≥100px wide at 1080w (≥133px at 1440w) while it is the read (a pan may read the names one by one) | R2; R23; 06-07 V4 | R2 STRONG; R23 HARD | HARD | 07 V4, C1 · S1 |
| E40 | **Shape and build as shipped:** flat 3 mm plywood cut to the outline of the design (family on a snowy ledge in Santa hats, the year in big 3D-*look* printed numbers); full-colour print on **one side only** (no printed back); no raised, embossed or extruded relief, no light or glow of its own | F1, F2, F9; P2; FR1 | **HARD** (Meta "accurately represent") | HARD | 07 V3, P2 · S1 |
| E41 | **Plausible scale** for 4 / 5 / 7 in, matching the scale-anchored plate (in hands, on a branch); when hung, it hangs by a string through its hole | F1, F3; README §3-05 reference lock | **HARD** | HARD | 07 V3 · S1 |
| E42 | The artwork shown is an **orderable design**: 2–10 members; only the characters man, woman, kid boy, kid girl, baby, dog, cat; names ≤15 characters; pets as personalizer breeds/coats | F4, F5, F7, F8; P2 | **HARD** | HARD | 07 P2 · S1 |
| E43 | **No invented facts:** no stats, counts, ratings, reviews, testimonials or claims outside F1–F10 (e.g. "handmade", "#1", "10,000 families", shipping speed) | README §2.7; BRIEF; FTC rule 2024 | [STRONG] statute | HARD | 07 P2, P4 · S1 |

### G. Casting, story, connection

| # | Criterion | Source | Strength | Lock | Enforced |
|---|---|---|---|---|---|
| E44 | **Casting matches the printed artwork:** every person or pet presented as the ornament's family matches their printed figure (character type/age class, skin tone, hair style and colour, glasses; dog breed; cat breed and coat), and the members presented as "the family" are the members on the artwork | R19; BRIEF; README §2.6 | **HARD** | HARD | 07 V1 · S1 |
| E45 | **Casting matches the caption:** every pronoun, role word and name in captions or dialogue matches the person on screen (gender, age, role); no hands-only hand-off where it matters who gives and who receives | CLAUDE.md hard rule; memory casting-matches-caption; 06-07 V1 | **HARD** (house) | HARD | 06 step 1 · 07 V1 · S1 |
| E46 | **Same identity in every shot** (face, hair, clothes, the cast sheet's must-not-change list) | 06-07 V1 | TEAM | TEAM | 07 V1 · S1 |
| E47 | **No morphs** (hands, fingers, faces, pets) and no spurious objects | 06-07 V2 | TEAM | TEAM | 07 V2 · S1 on the product or a face, else S2 |
| E48 | **Family connection:** at least one shot shows relatives together with the ornament (giving it, hanging it, gathered at the tree); the giftee is never shown alone as the payoff | CLAUDE.md hard rule; R17; README §2.6 | R17 WEAK, kept as a house rule | HARD (house) | 07 S3 · S2 |
| E49 | **Everyone is alive and present-tense** unless the concept is declared a memorial concept; in a memorial concept, no deceased person or pet moves, speaks or "returns" in the present (memories only in a clearly past grade) | R18; FR5 | **HARD** (house) / FR5 HARD | HARD | 07 S3, P6 · S1 |
| E50 | **Each shot shows what its line says** (picture matches caption) | README §3-05; 06-07 S2 | TEAM | TEAM | 07 S2 · S2 |
| E51 | **Beat map, hook caption, every caption and the end-card text match the locked script and caption sheet verbatim** (spelling, names, punctuation) | 06-07 S1, C1 | plan | TEAM | 06 step 1 (diff) · 07 S1, C1 · S1 for names/hook/CTA, else S2 |
| E52 | Emotional pivot at ~55–65% of the runtime (11–13s); warmth by the end | R15; README §3-04 | R15 WEAK | report | 07 S3 · S3 |
| E53 | Personalization as the hero visual: report the seconds in which names or year are legible | R2 | STRONG, but no number given | report | 07 · S3 |

### H. Captions and text policy

| # | Criterion | Source | Strength | Lock | Enforced |
|---|---|---|---|---|---|
| E54 | **Captions carry the story muted:** the cold reader (E25) can retell the story at the end, sound off | R7; 06-07 C6 | R7 **STRONG** | TEAM | 07 C6 · S2 |
| E55 | **Reading budget:** each caption ≤2.5 words/s and ≥2.0s on screen, ≤2 lines; ≤45 caption words per ad (aim 35–40) | README §3-04; CAPTION-SHEET D3 | STRONG for us (user test) | TEAM | 07 C2 · S2 |
| E56 | **No flashes or movement:** the next caption starts on the frame the last one ends, or after a clean gap ≥0.5s; no caption moves, reflows, adds lines or changes band while up; no word-by-word pop-in (word highlight only with declared dialogue, inside a stable phrase) | README §3-06; suncatcher E36 | verified (no-lift) / TEAM | TEAM | 07 C2 (caption on/off ±0.1s) · S2 |
| E57 | **Safe zones:** 9:16 keeps all text and the logo out of the top 14%, bottom 35% and 6% each side, and clear of the lower-right action rail; 4:5 keeps ≥10% bottom and ≥6% sides | README §3-06; Meta safe-zone page | [STRONG] (9:16) / [WEAK] (4:5) | TEAM | 07 C3 · S2 (S1 if the CTA or a name is covered) |
| E58 | **One fixed caption band per ad per format** (the end-card text is a separate fixed element, E9) | README §3-06 | TEAM | TEAM | 07 C2 · S2 |
| E59 | **Contrast:** each caption is readable at the lowest-contrast frame it crosses (≥3:1, large/bold text) | caption-design; WCAG 2.2 | verified 3-0 / [STRONG] | TEAM | 07 C4 · S2 |
| E60 | Captions **never cover a face, the ornament's printed figures, the names, the year or the payoff** | caption-design #5; 06-07 C5 | verified checklist | TEAM | 07 C5 · S2 |
| E61 | With declared dialogue: captions match the spoken words, timing within ±0.2s | 06-07 C7 | TEAM | TEAM | 07 C7 · S2 |
| E62 | **Describe the characters, never the viewer:** no caption, VO or end-card line asserts or asks about the viewer's attributes (age, family status, grief, health, money, religion). Second-person *relationship* lines are allowed (user ruling 2026-11-18) | R6; README §2.4 | **HARD** | HARD | 07 P1 · S1 |
| E63 | **No fake testimonial:** the story is never framed as a real customer or review; no "real", "true story" or "actual customer" over synthetic footage | FTC rule 2024; FR9; 06-07 P4 | [STRONG] | HARD | 07 P4 · S1 |

### I. Brand, rights, finish

| # | Criterion | Source | Strength | Lock | Enforced |
|---|---|---|---|---|---|
| E64 | **Store name and logo:** correct lockup, spelled correctly, wordmark ≥~40px tall at 1080w, over moving picture, inside the safe zone | 06-07 B1, B3; feed F13 | [STRONG] single CTA / [WEAK] size | TEAM | 07 B1, B3 · S2 (S1 for a misspelling) |
| E65 | **Music licence evidence in the recipe:** service, paid/commercial plan tier, generation date, terms URL; no consumer-library or licensed commercial track | README §6.2; 06-07 P3; Meta Reels guide | [STRONG] (Meta) / gap (AI terms) | HARD | 06 input 6 · 07 P3 · S1 |
| E66 | **AI-performer disclosure: none**, by user ruling 2026-11-18 (NY GBL §396-b known). Identical across all 12 ads | README §6.1 | user ruling | BRIEF | 07 P5 · PASS by ruling (S1 if a disclosure appears on some ads only) |
| E67 | **4:5:** no face, printed figure, name or year on or past the crop edge in any shot | 06-07 V5 | [STRONG] Meta "frame your story" / house | TEAM | 06 step 8 · 07 V5 · S2 |
| E68 | **Grade continuity;** no flicker or temporal shimmer in generated clips at playback speed | 06-07 V7 | TEAM | TEAM | 07 V7 (real-time playback) · S2 / S3 |

### U. Delivery and upload package

| # | Criterion | Source | Strength | Lock | Enforced |
|---|---|---|---|---|---|
| E69 | **Build recipe per ad:** every source with its hash and in/out points, per-shot transforms per format, caption-sheet version, music hash + offset + licence, loudness target, render settings, the tool as free text; it re-renders an identical frame hash on a sampled segment | README §3-06 | TEAM | TEAM | 06 · 07 I (recipe check) · S2 |
| E70 | **Self-check and contact sheet delivered:** frames at every cut ±1 frame, every caption change, first and last frame, both formats; measured self-check values (07 reads them only after measuring) | 06-07 §2 | TEAM | TEAM | 06 · 07 · S2 |
| E71 | **Media out of git** and backed up to Drive (`scripts/backup-media.sh`); one row per ad × format in `products/_registry/ad-creatives.csv` + Sheet re-pushed, QA status `PENDING` until 07 rules | CLAUDE.md; README §2.9 | house rule | HARD (house) | 06 · 07 I4 · S2 |
| E72 | **Ad copy:** primary text authored as an array of lines in `products/MJ4U-133-family-wood-ornament/ads/ad-content.json`, line-broken (never a paragraph), passing `engine/upload_draft.py --validate-only`; it carries no offer (E10) and no viewer-attribute line (E62) | CLAUDE.md; memory ad-copy-linebreak-format | house rule | HARD (house) | upload · S2 (S1 if it breaks E10 or E62) |

---

## (b) QA sampling for this round (07 final mode)

Per file: frames at 0.00, 0.5, 1.0 and 3.0s · every planned and detected cut ±1 frame (reconcile the lists) · every caption on/off ±0.1s · each shot's midpoint · the last frame · every names/year beat on ≥5 frames · then one real-time viewing on a phone-sized screen muted, and one unmuted.
Per concept: the two ads compared outside the hook window (E13), and frame 0.00 of both (E15). Per round: the end-card window across all 12 ads (E9), the music hash and offset (E6), and frame 1 of every concept against the other concepts and the scene ledger (E16).
Defect line: `[S#] file · mm:ss.ff–mm:ss.ff · E# · evidence · fix owner (Editor / 05 shot / 04 script / User) · re-check items`. A re-check reruns groups A, B and C plus the failed items.

## (c) Dropped from the suncatcher template

Suncatcher-only items were removed: the fixed beat map and hook texts (E2/E12 there), "Alex" and breed legibility on the wall shadow, the window light, grief-to-warmth as a fixed arc, the CTA "Make one that's only theirs", the IG-Feed 9:16 extra cell (F15), and the audit tables. Generic rules were kept and adapted to a printed rigid ornament with several names and a year.

## (d) Conflicts between sources and how they were resolved

1. **Offer.** CF §6 and `/video:new` list "one offer" as fixed; BRIEF says "offer: none". BRIEF (locked with the user) wins: E10.
2. **Length.** CF §6 allows 15–25s and Meta's Feed guidance says ≤15s; BRIEF fixes 20s. 20s in both formats (E1). Feed ≤15s is a known deviation (same waiver precedent as 2026-10-09), not a defect.
3. **CTA wording.** R8 wants a create/customize verb plus "today/now"; BRIEF locks "Personalize yours". BRIEF verbatim (E9). "Personalize" meets the verb part; no "today" is added, which also avoids an urgency read in a no-offer round.
4. **End card vs moving close.** R12 says no frozen end card (logo small over a moving shot); BRIEF requires an end card with the store name. The end-card text and store name sit over a moving plate of the real ornament, ≥2s, identical frames in all 12 ads (E9).
5. **Frame 1.** R1 says frame 1 shows the gift, not a room; BRIEF/CF HE8 set the floor at VS1 (present, may be under 1/3 width). The floor is VS1 at 0.00 with the ornament identifiable by 1.0s (E3). R1's stricter "gift is the frame-1 subject" is not imposed, because the frame-1 subject is a later H1 test factor.
6. **Transitions.** R11 says no crossfades; 06 allows dissolves at story time jumps (and the suncatcher used one). Hard cuts by default; a ≤0.4s dissolve only at a scripted time/place jump, never at or inside the hook window (E30).
7. **Cut rate.** 05 targets ≈0.4 cuts/s (n=1); R11 gives a gift median of 0.22 and the user asked for slower cutting in emotional ads. Shot-length bounds are enforced (E27 reported, E32 S2); the cut rate itself is reported only (E33).
8. **File naming.** The 06-07 research example (`MJ4U-120_C1-H2_E0_916_v03`) predates README §4a; the §4a ad key used in BRIEF wins (E17).
9. **Caption fades and band.** The suncatcher re-edit allowed fades ≤0.15s and put the CTA in its own top band; the final CAPTION-SHEET uses hard on/off. House style = hard on/off (E4). One fixed body band per ad and format; the end-card text is a separate fixed element (E58, E9).
10. **Reading rate.** Suncatcher E33 allowed ≤3 w/s; the house rule (user test) is ≤2.5 w/s, ≥2.0s (E55).
11. **Hook caption length.** The hook card allows ≤10 words; CF §4b prefers ≤7 (LB1–LB2). ≤10 is enforced (E12); ≤7 is preferred, not checked. CF §4b also says HE2 (tight frame 1) and HE4 (caption type) are "fixed by rule" but names no HE4 level, so neither is enforced in C0; both are tagged only.
12. **Loudness.** −16 LUFS for music-led ads vs −18 when VO leads: the target follows the concept's declared dialogue (E22). Within a concept both ads share one target (E13).
13. **Music licence status.** README §6.2 still lists "paid plan to confirm"; BRIEF says paid plan. E65 requires the plan evidence in the recipe before render; without it, S1.
14. **One bed for six concepts** (not a source conflict, a tension): CF §6 fixes one sound/music bed while the six concepts may differ in register. The sheet enforces one bed (E6). If a concept's register clashes with it, that is a user question (S3 proposal), not an editor choice.
