# MJ4U-133-C0 · 01 Hook candidates · K10 + K13

> Role 01 (Hook Ideator), 2026-11-23. Round **C0** (concept-framework §6): each concept ships 2 hooks over one identical body; C0 hook arms are insurance, so the two arms
> differ in frame-1 picture **and** mechanism and are declared as bundles where format and trigger both change (hook-framework §6c).
> Concepts: **MJ4U-133-K10** (X1) and **MJ4U-133-K13** (X1) only. Hook ids **MJ4U-133-H01…H30** (H01–H15 = K10, H16–H30 = K13). Draft lines rejected before they became
> cards carry local draft ids (`K10-d#`, `K13-d#`), which are never registered.
> Inputs: `concepts/00A-candidates.md` (K10, K13 sections), `concepts/GATE0.md`, `concepts/00C-slate.md`, `BRIEF.md`, `CRITERIA.md`, `RENDERS.md`, the real renders
> `ads/renders/MJ4U-133-K10-render.png` / `MJ4U-133-K13-render.png`, `product.json` (F1–F10), `_ledgers/hooks.csv`.
> **Hook ledger is empty** (header only): no prior hook, no measured rate, so every F×T cell has <2 ledger entries and nothing here can repeat a ledger hook.
> **For the Producer:** strip the final section "RATIONALE (strip before 02)" and the `pass` column before the cards go to the critics.

## 0. Constraints every card obeys (from BRIEF / CRITERIA, locked)
- 20s ad; **hook window 0.0–2.0s** in both concepts (00A beat maps), same length for both ads of a concept (E14); body starts at 2.0s, identical in both ads (E13).
- Ornament **visible at 0.00s (VS1+)** and **identifiable as the family ornament by 1.0s** (E3). The ornament is always the real personalizer render, composited; it never glows,
  moves by itself, animates or changes its print (E29 / FR1). Props with words (note, labels, stocking names, collar tag) are composited text, never generator-drawn.
- Hook caption ≤10 words, on screen by 0.5s (E5, E12), house caption style, third person; audio = bed only (AU0) or a sync hit on the onset (AU1); **no voice** (neither concept declares dialogue).
- Onset by 0.5s (E26). Promise answered within 3s of the hook end (by ~5.0s) and fully paid by 12.0s (E28). No offer, deadline, price, count or review (E10).
- Casting = printed artwork (RENDERS.md) + caption pronouns (E45). Describe characters, never the viewer (E62).
- `paid_by` is written `first answer s → full payment s`.

### Element-tag key (codebook, concept-framework §4a)
SU subject · SZ shot size · ON onset (+ onset_s) · CT caption type · LB caption band (with exact word count) · TM caption on-time (+ caption_on_s) · AU audio · VS product at 0s · PC people in frame 1.
Hands only count as one person (PC1); hands of two people with a visible relation count as PC2.

---

## K10 · "Their first Christmas as two (and the dog)" · MJ4U-133-K10-X1

**Cast and artwork (fixed by `MJ4U-133-K10-render.png`):** printed L→R **Daniel** (man, light skin, black messy crop, green Fair Isle sweater, black coffee) · **Grace** (woman, light skin,
black long straight hair, red Fair Isle sweater, red-tartan pants, hot chocolate) · **Mochi** (Pembroke Welsh Corgi); all in Santa hats; year **2026**. Live cast: Daniel = "he" (husband),
Grace = "she" (wife), Mochi = live Corgi. Hands: Daniel's = green sweater cuffs, Grace's = red sweater cuffs.
**RV3 constraint:** names are not legible before the PROOF beat (9s). In every K10 hook the ornament is visible and readable as a family ornament (figures, hats, the wooden year shape),
but the names are cropped, turned or out of focus (VS1/VS2, never VS3).

### Arms (step 1)
| Arm | Reference cell (00A plan) | Hypothesis, one line | Axis vs the other arm |
|---|---|---|---|
| **A · The secret** | F9×T1 (he hides the box) | Opening **before she has seen it** (his secret, her not knowing) holds the giver longer than the payoff, because the open loop is "what will she do?" | mechanism (bundle: F and T both change vs B's reference) |
| **B · It landed** | F10×T4 (her face as she opens it) | Opening **on the moment it lands** (her emotion, it in her hands or on their tree) holds the giver longer, because the giver is buying that moment | mechanism (bundle) |
Every A card shows frame 1 before Grace has the ornament; every B card shows it already received or hung. A card's own axis tag is "format" when it shares the other arm's reference trigger.

### What the body can pay (step 2)
| Second | Body beat (fixed) | Promises it can pay |
|---|---|---|
| 2.0–6.0 | STAKES: first apartment, moving boxes; Grace unpacks the DECORATIONS box and finds her old single-person childhood ornaments | "first apartment / first Christmas married", "still in boxes", "her old ornaments have only her", "which box", "she's unpacking" |
| 6.0–9.0 | TURN: she finds the small box; Daniel watches from the doorway | "he hid something", "she hasn't found it yet", "who it's from" |
| 9.0–12.0 | PROOF: ornament in her palm; Daniel, Grace, Mochi, 2026 legible | "what's on it", "all three of them", "his face / her face on it", "theirs, not just hers" |
| 12.0–17.0 | CONNECTION: she hangs it first on their tiny tree; arms round him; Mochi jumps between them | "what goes on first", "the face he was waiting for", "first Christmas as three" |
Not payable (invalid promises): anything about price, delivery, how it is made, a proposal or wedding scene, the dog doing anything with the ornament, a second ornament.

### Hook Card pool · K10 (step 3)
Common to all K10 cards: concept `MJ4U-133-K10` · execution `MJ4U-133-K10-X1` · cep **RC3 partner (wife) × OC7: their first Christmas married, first apartment** ·
asset_source base = real K10 render composited into every shot (names never generator-drawn) + live Daniel / Grace / Mochi from locked cast references.
policy base for every card: third person, no viewer attribute (E62) · pronouns he = Daniel, she = Grace · names not legible before 9s (RV3) · no offer.

#### MJ4U-133-H01 · KEEP
| Field | Value |
|---|---|
| arm · axis | A The secret · mechanism (bundle) — **A reference cell** |
| format · trigger · trigger_2 | F9 in-medias-res (mid-action) · T1 curiosity · T7 |
| primitives · truth_frame · mechanism | P1 onset, P4 text · — · — |
| frame1_visual | Close, slightly high: Daniel's hands (green sweater cuffs) hold a small open kraft gift box; the ornament lies face-up in red tissue inside, Santa-hatted figures and the wooden "2026" shape readable, names below the box rim. Under his hands an open moving box with "DECORATIONS" marked on the flap. Ornament ≈1/3 frame width. |
| onset_0_5s | 0.3s: his hands lower the open box down into the DECORATIONS box between wrapped bundles; the ornament face stays visible through 1.5s. |
| caption | "He hid one ornament in her decorations box." (8) |
| audio_cue | Soft thud synced to the box settling (0.4s) over the bed |
| promise | He has hidden something for her: what is it, and what will she do when she finds it? |
| paid_by | 2.0 (she opens that same box) → 6.0 (she finds it, he watches) → 9.0 full (names) |
| asset_source | base + DECORATIONS label composited; tissue/box props |
| policy | base · pass |
| tags | SU4 · SZ2 · ON2 @0.3 · CT1 · LB3 (8) · TM2 @0.2 · AU1 · VS2 · PC1 |

#### MJ4U-133-H02 · KEEP
| Field | Value |
|---|---|
| arm · axis | B It landed · mechanism (bundle) — **B reference cell** |
| format · trigger · trigger_2 | F10 reaction cold-open (laugh-cry) · T4 joy/tenderness · T1 |
| primitives · truth_frame · mechanism | P2 face, P1, P4 · — · M3 |
| frame1_visual | Close on Grace (East Asian, long straight black hair, red Fair Isle sweater) kneeling among moving boxes, warm lamp light; her eyes are down on the ornament she holds in both hands at the bottom of frame (figures and hats readable, names out of focus). |
| onset_0_5s | 0.3s: her hand goes to her mouth and a laugh breaks through wet eyes. |
| caption | "She thought she was just unpacking." (6) |
| audio_cue | Bed only |
| promise | Something in those boxes stopped her: what did she find, and who put it there? |
| paid_by | 2.0 (the unpacking it interrupted) → 6.0 (the small box, Daniel at the door) → 9.0 full |
| asset_source | base (ornament composited into her hands) |
| policy | base · pass |
| tags | SU2 · SZ2 · ON2 @0.3 · CT1 · LB2 (6) · TM2 @0.2 · AU0 · VS1 · PC1 |

#### MJ4U-133-H03 · KEEP
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F8 POV (giver's hands, over the counter) · T7 desire · T9 |
| primitives · truth_frame · mechanism | P1, P4 · — · M8 |
| frame1_visual | First-person from Daniel's eyes: his hands (green cuffs) low behind the kitchen counter hold the ornament upright, figures facing camera, names turned down. Beyond the counter, soft focus, Grace kneels at the DECORATIONS box with her back to him (two people, same room). |
| onset_0_5s | 0.3s: Grace starts to turn her head; his hands snap the ornament down below the counter edge (it stays half in frame). |
| caption | "POV: she hasn't found it yet." (6) |
| audio_cue | Bed only |
| promise | He's planned the moment she finds it: will she find it, and how will she react? |
| paid_by | 2.0 (she keeps unpacking) → 6.0 (she finds the box, he watches from the doorway) → 12.0 (she hangs it, arms round him) |
| asset_source | base + POV plate; Grace from locked refs |
| policy | base · POV label describes the scene, not the viewer · pass |
| tags | SU4 · SZ3 · ON2 @0.3 · CT6 · LB2 (6) · TM1 @0.0 · AU0 · VS2 · PC2 |

#### MJ4U-133-H04 · KEEP
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F5 reveal (lid lift) · T7 desire · T1 |
| primitives · truth_frame · mechanism | P1, P4 · — · — (M1 pattern without the name: RV3) |
| frame1_visual | ECU from above: Grace's hands (red cuffs) on a small kraft box, the lid already lifted a third so the hats and the top of the wooden year show; tissue edges; old childhood ornaments soft in the background. |
| onset_0_5s | 0.3s: the lid comes fully off; the whole printed family (Daniel, Grace, the Corgi) shows, the names stay under the tissue fold. |
| caption | "The first ornament that's theirs, not just hers." (8) |
| audio_cue | Light tap synced to the lid coming off |
| promise | Why is this one "theirs"? Who is on it? |
| paid_by | 2.0 (her old ornaments, each only her) → 9.0 full (Daniel, Grace, Mochi legible) |
| asset_source | base; box/tissue props |
| policy | base · pass |
| tags | SU4 · SZ1 · ON2 @0.3 · CT1 · LB3 (8) · TM2 @0.2 · AU1 · VS2 · PC1 |

#### MJ4U-133-H05 · KEEP
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F2 text-led statement · T3 recognition (CEP) · T9 |
| primitives · truth_frame · mechanism | P4, P1 · — · M9 |
| frame1_visual | Wide, eye level: a small living room stacked with moving boxes, their tiny tabletop tree bare on one box. Foreground, on the nearest box, the ornament lies propped in its open box at ≈1/3 width (figures and wooden year readable, names soft). Background: Daniel and Grace each carrying a box. |
| onset_0_5s | 0.3s: Daniel drops his box onto the stack (it bounces); caption on at 0.2s. |
| caption | "Their first Christmas married. Mostly still in boxes." (8) |
| audio_cue | Thud synced to the box landing |
| promise | Newlyweds' first Christmas in a half-unpacked home: how does it become Christmas? |
| paid_by | 2.0 (unpacking the DECORATIONS box) → 9.0 (the ornament) → 12.0 (hung first) |
| asset_source | base; wide plate with both cast |
| policy | base · "married" describes the characters · pass |
| tags | SU1 · SZ4 · ON2 @0.3 · CT1 · LB3 (8) · TM2 @0.2 · AU1 · VS2 · PC2 |

#### MJ4U-133-H06 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F7 comparison (row, A→B) · T3 recognition · T7 |
| primitives · truth_frame · mechanism | P1, P4 · 0.3s (the real ornament at true size beside the props) · M7 |
| frame1_visual | Overhead on the rug: a row of Grace's old childhood ornaments (a baby shoe, a ballet slipper, a felt star; all text-free, each "only her"), an empty gap at the end of the row. |
| onset_0_5s | 0.3s: Daniel's hand (green cuff) sets the family ornament into the gap; figures up, names toward the rug edge. |
| caption | "Her old ornaments. And the first one with him." (9) |
| audio_cue | Wood click synced to the ornament touching down |
| promise | What makes the new one different: who is on it? |
| paid_by | 2.0 (she unpacks these same old ornaments) → 9.0 full |
| asset_source | base; text-free props |
| policy | base · pass |
| tags | SU4 · SZ3 · ON2 @0.3 · CT1 · LB3 (9) · TM2 @0.2 · AU1 · VS1 (VS2 from 0.3s) · PC1 |

#### MJ4U-133-H07 · KEEP (exploration, the only K10 F4)
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F4 fake reality (scale play) · T4 joy/tenderness · T2 |
| primitives · truth_frame · mechanism | P1, P2 (at distance), P4 · **1.0s** · — |
| frame1_visual | Close on the top half of the real ornament hanging on a branch (hats, faces, the snowy ledge; names cropped below frame). On the ledge, beside the printed Daniel and Grace, sit a **tiny live Daniel and Grace** (2 cm tall, seen at three-quarter back, faces small), legs dangling over the snow edge. The ornament is unchanged: no glow, no movement, print exact. |
| onset_0_5s | 0.3s: tiny Grace leans her head onto tiny Daniel's shoulder. At 1.0s hard cut (truth frame): the real ornament on their tiny tree in the living room, real-size Daniel and Grace on the sofa beyond, Mochi on the rug. |
| caption | "First Christmas married. One ledge for all three." (8) |
| audio_cue | Bed only |
| promise | How did the three of them end up on one ornament? |
| paid_by | 1.0 (truth frame: it's their ornament on their tree) → 9.0 full (names) |
| asset_source | base composite + scale-play plate (tiny people at distance) + real-scale truth plate |
| policy | base · FR1 product unchanged · FR2 obviously impossible (tiny people) · FR3 truth 1.0s · FR4 metaphor "a place together" · FR5 n/a · FR7 faces small/at distance (needs 07 shot pass) · FR8/FR9 pass · E29 pass |
| tags | SU7 · SZ1 · ON2 @0.3 · CT1 · LB3 (8) · TM2 @0.2 · AU0 · VS2 · PC2 |

#### MJ4U-133-H08 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F3 question (rhetorical, about the characters) · T1 curiosity · T3 |
| primitives · truth_frame · mechanism | P1, P4 · — · M6 |
| frame1_visual | Medium: their tiny tabletop tree on a moving box, completely bare; at its foot, the ornament standing in its open box (≈1/3 width, figures facing camera, names soft). Dim room. |
| onset_0_5s | 0.3s: the tree's string lights blink on; real warm light falls on the ornament (it does not glow). |
| caption | "Their first tree together. What goes on first?" (8) |
| audio_cue | Click synced to the lights |
| promise | Which ornament goes on their first tree first? |
| paid_by | 2.0 (the decorations being unpacked: the candidates) → 12.0 full (she hangs this one first) |
| asset_source | base; tree plate |
| policy | base · question is about the characters' tree, no viewer attribute · pass |
| tags | SU6 · SZ3 · ON3 @0.3 · CT2 · LB3 (8) · TM2 @0.2 · AU1 · VS2 · PC0 |

#### MJ4U-133-H09 · KEEP (exploration)
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F14 native artefact (handwritten note in scene) · T1 curiosity · T9 |
| primitives · truth_frame · mechanism | P4, P1 · — · — |
| frame1_visual | Close from above into the open DECORATIONS box: the ornament in its small open box on top of the tissue (figures readable, names under a fold), a yellow sticky note in Daniel's handwriting stuck to the box rim: "Open this one LAST. –D". |
| onset_0_5s | 0.3s: Daniel's fingertip (green cuff) presses the note flat; it lifts at one corner. |
| caption | (the note is the caption) "Open this one LAST. –D" (5) |
| audio_cue | Bed only |
| promise | He wants this opened last: what's in it, and why last? |
| paid_by | 2.0 (she opens that box) → 6.0 (she finds it, he watches) → 9.0 full |
| asset_source | base; note text composited (not generated) |
| policy | base · physical artefact in scene, no UI (G8 pass) · "D" = Daniel |
| tags | SU5 · SZ2 · ON2 @0.3 · CT5 · LB2 (5) · TM1 @0.0 · AU0 · VS2 · PC1 |

#### MJ4U-133-H10 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F11 hands/process (wrapping) · T7 desire · T9 |
| primitives · truth_frame · mechanism | P1, P4 · — · M10 |
| frame1_visual | ECU on a moving box used as a table: Daniel's hands (green cuffs) at a small open box, the ornament face-up inside, a sheet of red tissue held above it; a roll of tape and a box cutter beside it. |
| onset_0_5s | 0.3s: the tissue folds down over the lower half of the ornament (names covered); figures and hats stay visible. |
| caption | "He wrapped it before they'd unpacked a single plate." (9) |
| audio_cue | Tissue crinkle synced to the fold |
| promise | It mattered to him more than unpacking: what is it, and for when? |
| paid_by | 2.0 (still unpacking) → 6.0 → 9.0 full |
| asset_source | base; props |
| policy | base · pass |
| tags | SU4 · SZ1 · ON2 @0.3 · CT1 · LB3 (9) · TM2 @0.2 · AU1 · VS2 · PC1 |

#### MJ4U-133-H11 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F13 direct address, silent (character to camera, no speech) · T1 curiosity · T9 |
| primitives · truth_frame · mechanism | P2 face, P1, P4 · — · — |
| frame1_visual | Medium-close: Daniel (green Fair Isle sweater) to camera, holding the ornament up beside his face (figures to camera, names cropped by his fingers); behind him, soft, Grace unpacking at the boxes. |
| onset_0_5s | 0.3s: he raises a finger to his lips. |
| caption | "Don't tell her. It's in the decorations box." (8) |
| audio_cue | Bed only (no speech; the line is a caption) |
| promise | A secret against her: what is it, will she find it? |
| paid_by | 2.0 → 6.0 → 9.0 full |
| asset_source | base; Daniel from locked refs |
| policy | base · character in a story, no customer claim (G8 F13 pass) · no AU3 |
| tags | SU2 · SZ2 · ON2 @0.3 · CT5 · LB3 (8) · TM2 @0.2 · AU0 · VS2 · PC2 |

#### MJ4U-133-H12 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F6 transformation (same frame, time cut) · T4 joy/tenderness · T3 |
| primitives · truth_frame · mechanism | P1, P4 · **0.4s** (the ornament hung, as it truly is) · M5 |
| frame1_visual | Wide, locked: one corner of the apartment on moving day, cold daylight, bare walls, boxes; the tiny tree bare on a box, the ornament in its open box beside it (≈1/4 width, figures readable). |
| onset_0_5s | 0.4s hard cut, same framing: evening, lamps on, the tree lit, the ornament hanging on it; Daniel and Grace on the floor against the sofa, Mochi between them. |
| caption | "Same corner. Their first Christmas as three." (7) |
| audio_cue | Soft hit synced to the cut |
| promise | How did the box corner become their Christmas, and who are "three"? |
| paid_by | 0.4 (the after state) → 2.0 (back to unpacking) → 12.0 full (she hangs it, Mochi jumps in) |
| asset_source | base; two locked-off plates of the same corner |
| policy | base · G7: ornament shown exactly as it is at 0.4 · pass |
| tags | SU6 · SZ4 · ON4 @0.4 · CT1 · LB2 (7) · TM2 @0.2 · AU1 · VS1 · PC0 |

#### MJ4U-133-H13 · KEEP
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F10 reaction (two faces) · T7 desire (the face he bought) · T1 |
| primitives · truth_frame · mechanism | P2 faces, P1, P4 · — · M3 |
| frame1_visual | Close two-shot: Grace in front, holding the ornament up at chin height (figures readable, names below her fingers), Daniel just behind her shoulder in soft focus, watching her face. |
| onset_0_5s | 0.3s: her face opens into a wide, wet-eyed smile; he grins. |
| caption | "This is the face he hid it for." (8) |
| audio_cue | Bed only |
| promise | What did he hide, and where? |
| paid_by | 2.0 (moving boxes) → 6.0 (the box, he at the doorway) → 9.0 full |
| asset_source | base; both from locked refs |
| policy | base · pass |
| tags | SU2 · SZ2 · ON2 @0.3 · CT1 · LB3 (8) · TM2 @0.2 · AU0 · VS2 · PC2 |

#### MJ4U-133-H14 · KEEP
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F1 onset (subject pops in) · T2 surprise · T9 |
| primitives · truth_frame · mechanism | P1, P3 animal, P4 · — · — |
| frame1_visual | Close from above into the open DECORATIONS box: tissue, wrapped bundles, and tucked in one corner the small open box with the ornament (figures readable, names under tissue). Still. |
| onset_0_5s | 0.3s: Mochi the Corgi's head pops up over the box edge and sniffs straight at the small box. |
| caption | "Mochi found it first. She still hasn't." (7) |
| audio_cue | Small hit synced to the pop |
| promise | Something is hidden for her in that box: when will she find it? |
| paid_by | 2.0 (she opens the same box) → 6.0 (finds it) → 9.0 full (Mochi on it too) |
| asset_source | base; Corgi from locked refs (no interaction with the ornament) |
| policy | base · dog never touches or moves the ornament · pass |
| tags | SU3 · SZ2 · ON2 @0.3 · CT1 · LB2 (7) · TM2 @0.2 · AU1 · VS2 · PC0 |

#### MJ4U-133-H15 · KEEP
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F2 text-led statement · T5 nostalgia/bittersweet → warm · T3 |
| primitives · truth_frame · mechanism | P4, P1 · — · — |
| frame1_visual | Close: the ornament already hanging on their tiny tree in the foreground (≈1/3 width; figures, hats, the Corgi and the wooden year read, names soft). On the next branch hangs one of Grace's old childhood baubles (text-free). Behind, soft: a half-open moving box and Grace leaning into Daniel. |
| onset_0_5s | 0.3s rack focus from the new ornament to the old bauble beside it; caption on at 0.2s. |
| caption | "Her childhood ornaments finally have company." (6) |
| audio_cue | Bed only |
| promise | How did her single, childhood ornaments end up next to a family one? |
| paid_by | 2.0 (she unpacks those childhood ornaments) → 9.0 (Daniel, Grace, Mochi) → 12.0 (she hangs it first) |
| asset_source | base; text-free bauble prop |
| policy | base · pass |
| tags | SU1 · SZ2 · ON1 @0.3 (rack focus) · CT1 · LB2 (6) · TM2 @0.2 · AU0 · VS2 · PC2 (soft, background) |

### K10 coverage check (pool of 15)
| Rule (hook-framework §6b) | K10 pool | Status |
|---|---|---|
| ≥6 formats, no format >4 | 13 formats: F1, F2×2, F3, F4, F5, F6, F7, F8, F9, F10×2, F11, F13, F14 (max 2) | pass |
| ≥5 triggers, no trigger >6 | 6 triggers: T1×4, T7×4, T4×3, T3×2, T2×1, T5×1 (max 4) | pass |
| ≥8 cards in S★ cells | 13 (all but H08 F3×T1 = S and H11 F13×T1 = S) | pass |
| ≥3 exploration cards in cells with <2 ledger entries | ledger empty, so all 15 qualify; deliberate exploration: H07 F4×T4, H09 F14×T1, H11 F13×T1, H08 F3×T1 | pass |
| no ✕ cell; W only with reason | none ✕, none W | pass |
| F4 ≤2 cards, ≤1 F4 arm; FR1–FR11 | 1 card (H07), FR checks in its policy row | pass |
| near-duplicates (same F + T + frame-1 subject) | none: the two F10 cards differ in T (H02 T4 vs H13 T7); the two F2 cards differ in T (H05 T3 vs H15 T5) | pass |
| every card: product at 0.00s, identifiable by 1.0s, names soft (RV3) | yes (VS1 on H02, H06, H12; VS2 elsewhere) | pass |

### K10 kept cards (step 5) · 10 kept, 5 per arm
| id | Arm | F × T | One line |
|---|---|---|---|
| MJ4U-133-H01 | A | F9×T1 | His hands lower the open box into her DECORATIONS box · "He hid one ornament in her decorations box." |
| MJ4U-133-H03 | A | F8×T7 | His POV hiding it behind the counter as she turns · "POV: she hasn't found it yet." |
| MJ4U-133-H05 | A | F2×T3 | Wide box-filled flat, ornament in the foreground, a box drops · "Their first Christmas married. Mostly still in boxes." |
| MJ4U-133-H09 | A | F14×T1 | His sticky note on the small box · "Open this one LAST. –D" |
| MJ4U-133-H14 | A | F1×T2 | Mochi pops up and sniffs the hidden box · "Mochi found it first. She still hasn't." |
| MJ4U-133-H02 | B | F10×T4 | Grace's face, hand to mouth, ornament in her hands · "She thought she was just unpacking." |
| MJ4U-133-H04 | B | F5×T7 | Lid off in her hands, the printed three appear · "The first ornament that's theirs, not just hers." |
| MJ4U-133-H07 | B | F4×T4 | Tiny Daniel and Grace sit on the real ornament's ledge; truth frame 1.0s · "First Christmas married. One ledge for all three." |
| MJ4U-133-H13 | B | F10×T7 | Two-shot, her smile, him behind · "This is the face he hid it for." |
| MJ4U-133-H15 | B | F2×T5 | Ornament hung beside her old bauble, rack focus · "Her childhood ornaments finally have company." |
Kept: 8 formats (F1, F2, F4, F5, F8, F9, F10, F14), 6 triggers (T1, T2, T3, T4, T5, T7). The arm reference cells (H01 F9×T1, H02 F10×T4) differ in frame-1 subject (SU4 hands+box vs SU2 face), shot, people and onset.
Culled at step 5 (good cards, cut for the 10 cap): H06, H08, H10, H11, H12 (reasons in the rationale section).

### K10 self-rejected (step 4) and merge drops (step 7)
| id | Line / card | Reason |
|---|---|---|
| K10-d1 | "What do you give your wife for your first married Christmas?" | Second person + the viewer's marital status (role-file hard rule; F3 must stay third person about the characters) |
| K10-d2 | F13: Daniel says to camera "Our first Christmas married, so I made us this." | Needs spoken dialogue (AU3); K10 declares no dialogue (E12). "I made us this" also reads as a customer claim (IC4) |
| K10-d3 | "Wait till she sees what's inside." | Cliché ("wait for it" family) |
| K10-d4 | "The perfect first gift for newlyweds." | Cliché, and a caption with no frame |
| K10-d5 | F5 name reveal: ECU "Daniel · Grace · Mochi" legible at 0.3s | Breaks RV3 (names only at the 9s PROOF beat); would recode the execution to RV1 |
| K10-d6 | Mochi carries the ornament to Grace in his mouth | The body can't pay it (she finds it in the box, 6–9s); a dog chewing the product misreads the product |
| K10-d7 | F15 "Couples everywhere are hanging these" | No true count or quote in the fact sheet (F15/T6 needs real proof; E10/README §2.7) |
| K10-d8 | F1×T4 ECU of the hung ornament as the tree lights snap on, "The only ornament on their first tree." | At ECU under the lights the names read before 9s (RV3); same tree frame as H08/H12 |
| K10-p2a | Pass 2, rack focus from her single-name bauble to the box: "Every ornament she owns has only one name." | Near-duplicate of H06/H04 (her old ornaments vs the new one). Its caption is listed as an alternative for H06 in the rationale |
| K10-p2c | Pass 2, F9×T9: Mochi nose-boops the box, Daniel shushes from the doorway, "Mochi found Grace's surprise first." | Same frame-1 subject as H14 (dog at the DECORATIONS box) and H11 (finger to lips); merged into H14 |
| K10-p2d | Pass 2, F8×T9 dog's-eye POV up at the tree, "Mochi just noticed he's on the tree." | Ornament small and soft at the top of frame: not identifiable by 1.0s (E3) |
| K10-p2e | Pass 2, F5×T1: her hand reaches past the box with an "Open last – D" tag | Near-duplicate of H09 (note) and H01 (same box framing) |

---

## K13 · "Biscuit is still on the tree" (exploration, pet memorial) · MJ4U-133-K13-X1

**Cast and artwork (fixed by `MJ4U-133-K13-render.png`):** printed L→R **Mom** (woman, light skin, ginger long waves, green Fair Isle sweater, plaid pants, whipped cocoa) ·
**Noah** (kid boy, ginger tousled crop, red Fair Isle sweater) · **Lily** (kid girl, ginger pigtails, red Fair Isle sweater, plaid pants) · **Biscuit** (Golden Retriever, right end); all in Santa hats;
year **2026**. The printed label is **"Mom"**, so captions say Mom (00A's "Mum" is wrong for this render). Live cast: Mom, Noah, Lily. **No live dog, ever**: Biscuit is only the printed
figure or a static past photo (Golden Retriever). Pronouns: "he/his/him" = Biscuit only, "she" = Mom; the kids are named. Hands: Mom = green cuffs, kids = red cuffs.
**Memorial rules:** no F4 (00A, FR5), no humor (IC2), Biscuit never moves, returns or "visits" (IC9); no caption implies he comes back. **RV2:** the ornament (with the golden dog figure as a cue)
is visible in the hook, but Biscuit's printed name is never the read before the PROOF beat (names soft or cropped).

### Arms (step 1)
| Arm | Reference cell (00A plan) | Hypothesis, one line | Axis vs the other arm |
|---|---|---|---|
| **A · Without him** | F2×T5 ("First Christmas without Biscuit.") | **Holding the absence** in the hook (his collar, bed, stocking, box) stops the right buyer, because recognition of the loss creates the need the ornament answers | format when the card holds T5 (reference pair = format-arm, T5 held); mechanism (bundle) otherwise |
| **B · Still on the tree** | F6×T5 (empty bed → ornament) | **Showing within the hook that he is still with the family** (his figure on the ornament, the family around it) stops the right buyer and protects against a sad opener in a Christmas feed | format (T5 cards); mechanism (bundle) otherwise |
Every A card ends its hook on the absence (the ornament present but not yet his place); every B card shows Biscuit's place on the family ornament by ≤1.0s.

### What the body can pay (step 2)
| Second | Body beat (fixed) | Promises it can pay |
|---|---|---|
| 2.0–6.0 | STAKES: the empty dog bed by the tree; Noah and Lily quiet | "first Christmas without him", "his bed", "the kids went quiet", "what's missing" |
| 6.0–9.0 | TURN: Mom kneels and shows them the ornament | "what Mom is holding", "Mom kept / made something", "what she gives them" |
| 9.0–12.0 | PROOF: ornament close; Biscuit's figure + name + 2026 legible among the family | "he's still on it", "all four", "one more family member", "still at the end" |
| 12.0–17.0 | CONNECTION: the kids hang it together, Mom's arms round both; one hangs the collar beside it | "they hang it", "beside his collar", "Noah smiles" |
Not payable: anything with a live or moving dog, a ghost or return, a new puppy, price, delivery, how it is made.

### Hook Card pool · K13 (step 3)
Common to all K13 cards: concept `MJ4U-133-K13` · execution `MJ4U-133-K13-X1` · cep **RC5 pet (memorial: the family dog Biscuit) × OC1: the family's first Christmas without him** ·
asset_source base = real K13 render composited (names never generator-drawn) + live Mom / Noah / Lily from locked refs; Biscuit only as printed figure or static past photo.
policy base for every card: third person, no viewer attribute (E62, IC7) · he = Biscuit, she = Mom, kids by name, "Mom" spelling · no F4, no humor, no live or moving dog (IC9/FR5) · Biscuit's name never the read before 9s.

#### MJ4U-133-H16 · KEEP
| Field | Value |
|---|---|
| arm · axis | A Without him · format (T5 held vs B reference) — **A reference cell** |
| format · trigger · trigger_2 | F2 text-led (bittersweet line) · T5 nostalgia/bittersweet · T3 |
| primitives · truth_frame · mechanism | P4, P2, P1 · — · — |
| frame1_visual | Medium: Noah and Lily (ginger, red sweaters) kneel at an open decorations box by the half-decorated tree; Lily holds a small red dog collar in both hands, both kids looking at it. At the left edge, Mom's hand (green cuff) holds the new ornament low (figures and the golden dog visible, names soft). |
| onset_0_5s | 0.3s: the collar's tag swings as Lily lifts it; by 1.0s Mom's hand raises the ornament into the lamp light (≈1/3 width). |
| caption | "First Christmas without Biscuit." (4) |
| audio_cue | Bed only |
| promise | How does this family do Christmas without him, and what is Mom holding? |
| paid_by | 2.0 (the empty bed, the kids quiet) → 6.0 (Mom shows them) → 9.0 full (Biscuit on it) |
| asset_source | base; collar prop |
| policy | base · describes the family, not the viewer · pass |
| tags | SU2 · SZ3 · ON2 @0.3 · CT1 · LB1 (4) · TM1 @0.0 · AU0 · VS1 · PC2 |

#### MJ4U-133-H17 · KEEP
| Field | Value |
|---|---|
| arm · axis | B Still on the tree · format (T5 held vs A reference) — **B reference cell** |
| format · trigger · trigger_2 | F6 transformation (absence → presence, cut) · T5 nostalgia → warm · T4 |
| primitives · truth_frame · mechanism | P1, P4 · **0.4s** (the ornament as it truly is, hung) · M5 |
| frame1_visual | Close, low: the empty dog bed beside the tree, a dent in the cushion, the red collar lying on it. Above it, on the lowest branch, the ornament hangs in soft focus (≈1/4 width; figures and the golden dog shape visible). |
| onset_0_5s | 0.4s hard cut up to a medium-close of the ornament on that branch, sharp: the family and the golden dog at the end of the ledge, hats, the year; names still soft. |
| caption | "His bed is empty. His spot on the tree isn't." (10) |
| audio_cue | Soft hit synced to the cut |
| promise | Whose spot, and how is he still on the tree? |
| paid_by | 0.4 (the ornament) → 2.0 (the bed, the kids quiet) → 9.0 full (Biscuit + name) |
| asset_source | base; bed/collar plate; no dog |
| policy | base · G7: the ornament exactly as it is at 0.4 · pass |
| tags | SU6 · SZ2 · ON4 @0.4 · CT1 · LB3 (10) · TM2 @0.2 · AU1 · VS1 · PC0 |

#### MJ4U-133-H18 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | A · format (T5) |
| format · trigger · trigger_2 | F9 in-medias-res (mid-action) · T5 · T1 |
| primitives · truth_frame · mechanism | P1, P4 · — · — |
| frame1_visual | ECU into the decorations box: Lily's hand (red cuff) draws a red dog collar out of the tissue; beside it the ornament lies face-up (figures visible, names under tissue). |
| onset_0_5s | 0.2s: the collar tag pulls free and swings. |
| caption | "His collar was still in the decorations box." (8) |
| audio_cue | Tag jingle synced to the pull |
| promise | Whose collar, and what happens now? |
| paid_by | 2.0 (the empty bed) → 6.0 → 9.0 full |
| asset_source | base; collar prop |
| policy | base · pass |
| tags | SU4 · SZ1 · ON2 @0.2 · CT1 · LB3 (8) · TM2 @0.2 · AU1 · VS2 · PC1 |

#### MJ4U-133-H19 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F3 question (about the characters) · T1 curiosity · T5 |
| primitives · truth_frame · mechanism | P2, P4, P1 · — · M6 |
| frame1_visual | Medium: Mom (ginger long waves, green sweater) sits on the floor by the tree, the ornament in her lap in both hands (figures visible, names soft); Noah and Lily lean against her; the empty dog bed soft in the foreground. |
| onset_0_5s | 0.3s: Mom lifts the ornament toward the kids. |
| caption | "Biscuit isn't here this year. What goes on the tree?" (10) |
| audio_cue | Bed only |
| promise | What goes on the tree in his place? |
| paid_by | 2.0 (the empty bed) → 6.0 (Mom shows them) → 12.0 full (they hang it) |
| asset_source | base |
| policy | base · question about the family's tree, not the viewer · pass |
| tags | SU2 · SZ3 · ON2 @0.3 · CT2 · LB3 (10) · TM2 @0.2 · AU0 · VS2 · PC2 |

#### MJ4U-133-H20 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F5 reveal (lid lift) · T4 tenderness · T3 |
| primitives · truth_frame · mechanism | P1, P4 · — · — |
| frame1_visual | ECU from above: Mom's hands (green cuffs) hold a small box, lid lifted a third; Noah's and Lily's hands (red cuffs) at the box edges. |
| onset_0_5s | 0.3s: the lid comes off; the whole printed family on the ledge, the golden dog at the right end (names soft). |
| caption | "This year's ornament still has all four of them." (9) |
| audio_cue | Tap synced to the lid |
| promise | Who are the four? |
| paid_by | 2.0 (the empty bed: who is missing) → 9.0 full |
| asset_source | base |
| policy | base · pass |
| tags | SU4 · SZ1 · ON2 @0.3 · CT4 · LB3 (9) · TM2 @0.2 · AU1 · VS2 · PC2 |

#### MJ4U-133-H21 · KEEP
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F10 reaction cold-open · T4 tenderness · T5 |
| primitives · truth_frame · mechanism | P2 face, P1, P4 · — · M3 |
| frame1_visual | Close on Noah (ginger tousled hair, red sweater), eyes red-rimmed; Mom's hand (green cuff) enters low holding the ornament in front of him (figures and the golden dog visible, names soft). |
| onset_0_5s | 0.3s: his trembling mouth breaks into a small smile. |
| caption | "Noah hadn't smiled since the collar came out." (8) |
| audio_cue | Bed only |
| promise | What made him smile? |
| paid_by | 2.0 (why he was quiet: the empty bed) → 6.0 (Mom shows them) → 9.0 full |
| asset_source | base; Noah from locked refs |
| policy | base · "he" never used for Noah (reserved for Biscuit) · pass |
| tags | SU2 · SZ2 · ON2 @0.3 · CT1 · LB3 (8) · TM2 @0.2 · AU0 · VS1 · PC2 |

#### MJ4U-133-H22 · KEEP
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F8 POV (the giver, Mom) · T7 desire (thought made visible) · T4 |
| primitives · truth_frame · mechanism | P1, P4, P2 · — · M8 |
| frame1_visual | First person from Mom kneeling: her hands (green cuffs) hold the ornament out toward Noah and Lily, who sit beside the empty dog bed looking up at it; ornament ≈1/3 width (figures and the golden dog at the end readable, names soft). |
| onset_0_5s | 0.3s: her hands push it forward into the lamp light; Lily's hand rises toward it. |
| caption | "Mom kept a spot on the ledge for him." (9) |
| audio_cue | Bed only |
| promise | Who is "him", and what do the kids do? |
| paid_by | 2.0 (the empty bed) → 9.0 (Biscuit on the ledge) → 12.0 (they hang it, Mom's arms round them) |
| asset_source | base; POV plate |
| policy | base · pass |
| tags | SU4 · SZ3 · ON2 @0.3 · CT1 · LB3 (9) · TM2 @0.2 · AU0 · VS2 · PC2 |

#### MJ4U-133-H23 · KEEP (exploration)
| Field | Value |
|---|---|
| arm · axis | A · format (T5) |
| format · trigger · trigger_2 | F14 native artefact (handwritten box label in scene) · T5 · T1 |
| primitives · truth_frame · mechanism | P4, P1 · — · — |
| frame1_visual | Close from above: a cardboard box lid with a kid's marker handwriting "BISCUIT'S STUFF" (composited); inside, a red collar, a worn tennis ball, and on top the ornament (figures readable, names soft). |
| onset_0_5s | 0.3s: Lily's hand (red cuff) folds the lid flap fully open. |
| caption | (the label is the caption) "Biscuit's stuff" (2) |
| audio_cue | Bed only |
| promise | Who was Biscuit, and why is a new ornament in his box? |
| paid_by | 2.0 (the empty bed) → 6.0 (Mom shows them) → 9.0 full |
| asset_source | base; label text composited; props |
| policy | base · physical artefact, no UI (G8 pass) |
| tags | SU5 · SZ2 · ON2 @0.3 · CT6 · LB1 (2) · TM1 @0.0 · AU0 · VS2 · PC1 |

#### MJ4U-133-H24 · KEEP
| Field | Value |
|---|---|
| arm · axis | A · format (T5) |
| format · trigger · trigger_2 | F1 onset (lights) · T5 · T3 |
| primitives · truth_frame · mechanism | P1, P4 · — · M4 |
| frame1_visual | Medium, dim: the mantel with four knit stockings, names stitched (composited) "Mom", "Noah", "Lily", "Biscuit"; in the foreground, hanging from the garland, the ornament (≈1/3 width; figures and the golden dog readable, names soft). |
| onset_0_5s | 0.3s: the garland's fairy lights click on; real warm light falls on the stockings and the ornament (it does not glow). |
| caption | "Four stockings still up this year." (6) |
| audio_cue | Click synced to the lights |
| promise | Why is his stocking still up? |
| paid_by | 2.0 (the empty bed) → 9.0 (Biscuit still on the ornament) → 12.0 |
| asset_source | base; stocking names composited |
| policy | base · pass |
| tags | SU1 · SZ3 · ON3 @0.3 · CT4 · LB2 (6) · TM2 @0.2 · AU1 · VS2 · PC0 |

#### MJ4U-133-H25 · KEEP (merged with a pass-2 card)
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F11 hands/process (hanging it) · T7 desire · T4 |
| primitives · truth_frame · mechanism | P1, P4 · — · — |
| frame1_visual | Close at a branch: Noah's and Lily's hands (red cuffs) hold the ornament by its string, Mom's hand (green cuff) steadying from below; the top half faces camera (hats, faces, the golden dog at the end; names below frame). Mom's face soft behind. |
| onset_0_5s | 0.3s: the string loop drops over the branch and the hands let go; the ornament hangs still. |
| caption | "Noah and Lily hang it beside his collar." (8) |
| audio_cue | Soft hit synced to the string settling |
| promise | Whose collar, and what is "it"? |
| paid_by | 2.0 (the empty bed: "his") → 9.0 (Biscuit on it) → 12.0 full (hung beside the collar) |
| asset_source | base; hands from locked refs |
| policy | base · pass |
| tags | SU4 · SZ2 · ON2 @0.3 · CT1 · LB3 (8) · TM2 @0.2 · AU1 · VS2 · PC2 |

#### MJ4U-133-H26 · KEEP
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F7 comparison (past photo beside the ornament, one frame) · T3 recognition · T5 |
| primitives · truth_frame · mechanism | P1, P4, P3 (dog in the photo) · **0.0s** (the real ornament beside the photo) · M7 |
| frame1_visual | Close: on a side table under the tree, a framed past photo of Mom, Noah and Lily on the sofa with Biscuit (a live Golden Retriever in the photo, static); right beside it the ornament hangs from the lowest branch, the same four on its ledge (≈1/3 width; names soft). |
| onset_0_5s | 0.3s: Lily's hand (red cuff) sets the photo frame upright under the ornament. |
| caption | "Same four. Biscuit still at the end." (7) |
| audio_cue | Soft click synced to the frame touching down |
| promise | Is that really him at the end of the ornament? |
| paid_by | 2.0 (the empty bed: he's gone) → 9.0 full (Biscuit + name at the end of the ledge) |
| asset_source | base; past photo generated from the locked cast + a Golden Retriever matching the print |
| policy | base · the photo is clearly the past and static (IC9 pass) · pass |
| tags | SU1 · SZ2 · ON2 @0.3 · CT4 · LB2 (7) · TM2 @0.2 · AU1 · VS2 · PC1 |

#### MJ4U-133-H27 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F10 reaction · T1 curiosity · T4 |
| primitives · truth_frame · mechanism | P2, P1, P4 · — · — |
| frame1_visual | Close on Mom (ginger long waves, green sweater) kneeling, looking down at the kids off-frame, the ornament at her chin in one hand (figures and the golden dog visible, names soft). |
| onset_0_5s | 0.3s: she takes a breath and starts to smile. |
| caption | "Mom had one more ornament this year." (7) |
| audio_cue | Bed only |
| promise | What is it, and who is it for? |
| paid_by | 2.0 → 6.0 → 9.0 full |
| asset_source | base |
| policy | base · pass |
| tags | SU2 · SZ2 · ON2 @0.3 · CT1 · LB2 (7) · TM2 @0.2 · AU0 · VS2 · PC1 |

#### MJ4U-133-H28 · culled (step 5)
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F2 text-led (relationship callout by name) · T3 recognition · T4 |
| primitives · truth_frame · mechanism | P4, P2, P1 · — · M2 |
| frame1_visual | Medium: Mom, Noah and Lily on the sofa, Lily holding the ornament up between them (≈1/3 width, the golden dog at the right end visible, names soft), all three looking at it. |
| onset_0_5s | 0.3s: Lily lifts it up; caption on at 0.2s. |
| caption | "Mom, Noah, Lily. And Biscuit, still on the end." (9) |
| audio_cue | Bed only |
| promise | Who is Biscuit, and why "still"? |
| paid_by | 2.0 (the empty bed) → 9.0 full |
| asset_source | base |
| policy | base · pass |
| tags | SU2 · SZ3 · ON2 @0.3 · CT3 · LB3 (9) · TM2 @0.2 · AU0 · VS2 · PC2 |

#### MJ4U-133-H29 · KEEP
| Field | Value |
|---|---|
| arm · axis | A · mechanism (bundle) |
| format · trigger · trigger_2 | F9 in-medias-res (private ritual) · T3 recognition · T5 |
| primitives · truth_frame · mechanism | P2, P1, P4 · — · M4 |
| frame1_visual | Medium-low: Lily (ginger pigtails, red sweater) sits on the floor beside the empty dog bed, her hand resting on its edge; Noah quiet beside her; Mom kneels into the left of frame holding the ornament low (figures readable, names soft). |
| onset_0_5s | 0.3s: Mom's knee touches down and the ornament comes into the lamp light (it does not glow). |
| caption | "Lily still checks the dog bed every morning." (8) |
| audio_cue | Bed only |
| promise | What will Mom give them, and will it help? |
| paid_by | 2.0 (the empty bed, the kids quiet) → 6.0 (Mom shows them) → 9.0 full |
| asset_source | base |
| policy | base · pass |
| tags | SU2 · SZ3 · ON2 @0.3 · CT1 · LB3 (8) · TM2 @0.2 · AU0 · VS1 · PC2 |

#### MJ4U-133-H30 · KEEP
| Field | Value |
|---|---|
| arm · axis | B · mechanism (bundle) |
| format · trigger · trigger_2 | F5 reveal (fingers open) · T2 surprise · T4 |
| primitives · truth_frame · mechanism | P1, P4 · — · — |
| frame1_visual | ECU: the ornament in Mom's open palm (green cuff), her fingers curled over its right end; the Mom, Noah and Lily figures in Santa hats and the wooden "2026" visible (names soft). |
| onset_0_5s | 0.4s: her fingers open to show a golden dog figure in a Santa hat at the end of the ledge; his name stays soft. |
| caption | "Mom's ornament has one more family member." (7) |
| audio_cue | Soft hit synced to the reveal |
| promise | Who is he, and why is he on it? |
| paid_by | 2.0 (the empty bed explains who) → 9.0 full (Biscuit's name legible) |
| asset_source | base (real-still ECU + hand plate) |
| policy | base · the dog figure is static print, uncovered by the hand, never animated (IC9 pass) · pass |
| tags | SU4 · SZ1 · ON2 @0.4 · CT1 · LB2 (7) · TM2 @0.2 · AU1 · VS2 · PC1 |

### K13 coverage check (pool of 15)
| Rule (hook-framework §6b) | K13 pool | Status |
|---|---|---|
| ≥6 formats, no format >4 | 11 formats: F1, F2×2, F3, F5×2, F6, F7, F8, F9×2, F10×2, F11, F14 (max 2) | pass |
| ≥5 triggers, no trigger >6 | 6 triggers: T5×5, T3×3, T1×2, T4×2, T7×2, T2×1 (max 5) | pass |
| ≥8 cards in S★ cells | 12 (all but H19 F3×T1, H29 F9×T3, H30 F5×T2, which are S) | pass |
| ≥3 exploration cards in cells with <2 ledger entries | ledger empty, so all 15 qualify; deliberate exploration: H23 F14×T5, H30 F5×T2 (surprise in a memorial), H26 F7×T3 | pass |
| no ✕ cell; W only with reason | none ✕, none W | pass |
| F4 | 0 (barred: memorial, FR5, 00A) | pass |
| near-duplicates (same F + T + frame-1 subject) | none: the two F10 cards differ in T and subject (Noah T4 / Mom T1); the two F2 cards differ in T; the two F5 cards differ in T and subject (box / palm); the two F9 cards differ in T and subject | pass |
| every card: product at 0.00s, identifiable by 1.0s, no live dog, names soft (RV2) | yes | pass |

### K13 kept cards (step 5) · 10 kept: arm A 4, arm B 6
| id | Arm | F × T | One line |
|---|---|---|---|
| MJ4U-133-H16 | A | F2×T5 | Kids holding his collar, Mom's ornament at the edge · "First Christmas without Biscuit." |
| MJ4U-133-H23 | A | F14×T5 | Kid-written "BISCUIT'S STUFF" box opens, the ornament on top · label as caption |
| MJ4U-133-H24 | A | F1×T5 | Mantel lights click on: four stockings, the ornament in front · "Four stockings still up this year." |
| MJ4U-133-H29 | A | F9×T3 | Lily's hand on the empty bed, Mom kneels in with the ornament · "Lily still checks the dog bed every morning." |
| MJ4U-133-H17 | B | F6×T5 | Empty bed with collar, cut up to the ornament above it · "His bed is empty. His spot on the tree isn't." |
| MJ4U-133-H21 | B | F10×T4 | Noah's red eyes break into a smile at the ornament · "Noah hadn't smiled since the collar came out." |
| MJ4U-133-H22 | B | F8×T7 | Mom's POV holding it out to the kids by the bed · "Mom kept a spot on the ledge for him." |
| MJ4U-133-H25 | B | F11×T7 | The kids' hands hang it, Mom steadying · "Noah and Lily hang it beside his collar." |
| MJ4U-133-H26 | B | F7×T3 | Past family photo with Biscuit set under the ornament · "Same four. Biscuit still at the end." |
| MJ4U-133-H30 | B | F5×T2 | Mom's fingers open to show the golden dog on the ledge · "Mom's ornament has one more family member." |
Kept: 10 formats, 5 triggers (T2, T3, T4, T5, T7). The arm reference cells (H16 F2×T5, H17 F6×T5) differ in frame-1 subject (SU2 kids with the collar vs SU6 empty bed), shot, people (PC2 vs PC0) and onset (ON2 vs ON4).
Culled at step 5: H18, H19, H20, H27, H28 (reasons in the rationale section).

### K13 self-rejected (step 4) and merge drops (step 7)
| id | Line / card | Reason |
|---|---|---|
| K13-d1 | "Did you lose your dog this year?" | Asserts the viewer's grief (IC7, R6, E62) |
| K13-d2 | "For the family that lost their dog this year." | A callout that pins a grief attribute on the viewer's family (R6) |
| K13-d3 | F3 to the giver role: "What do you hang for the dog who isn't here?" | Implies the viewer's loss (R6) |
| K13-d4 | "Gone but never forgotten." / "Forever in our hearts." | Clichés (role-file list) |
| K13-d5 | "Biscuit came home for Christmas." | Implies the dead dog returning in the present (FR5, IC9) |
| K13-d6 | F4: golden light shaped like Biscuit on the wall, or the printed dog "wagging" | F4 barred for this memorial (FR5, 00A); animating the print breaks FR1/E29 |
| K13-d7 | T9: Biscuit's printed figure "stealing" Lily's cocoa | Humor is invalid for a memorial (IC2); animates the print |
| K13-d8 | F13: Lily to camera, "We didn't put his stocking away." | Needs spoken dialogue (AU3), which K13 does not declare (E12); a silent grieving child to camera reads staged |
| K13-d9 | ECU of "Biscuit" printed under the golden dog at 0.2s | Makes the name the read at 0–1s (RV1), which recodes the execution away from RV2 |
| K13-p2a | Pass 2, F14×T1: a note on the box, "He's coming with us this year." | Present-tense return wording for the deceased (FR5/IC9). Its caption "Mom wasn't ready to leave him off the tree." is kept as an alternative in the rationale |
| K13-p2c | Pass 2, F11×T7: three hands hang it on the branch | Same F and frame-1 subject as H25; merged into H25 (trigger T7 taken from it) |
| K13-p2e | Pass 2, F8×T3: kid-height POV of the empty bed with the collar, "The first Christmas the dog bed stays empty." | Same frame-1 subject as H17 and H29 (the empty bed with the ornament secondary) |

---

## Handoff to 02
Send the 20 kept cards (K10: H01, H02, H03, H04, H05, H07, H09, H13, H14, H15 · K13: H16, H17, H21, H22, H23, H24, H25, H26, H29, H30) **without** the RATIONALE section,
with every card in the same table format, in a fresh order per judge. Frame-1 stills for the critics are MOCKs (no assets exist yet) and must be labelled MOCK.
Ledger rows (`_ledgers/hooks.csv`) are written by the Producer after 03 selects, with `test_id` MJ4U-133-C0, the arm, the axis and the nine element tags above.

---

## RATIONALE (strip before 02)

**Process.** Pass 1 (this session) wrote 14 K10 and 13 K13 cards. Pass 2 was a separate, independent run given only the brief and the cells pass 1 left empty
(K10: T5, T9-primary, F5×T1; K13: F5×T1, F9×T3, F14×T1, F1×T4, F6×T4, F3×T3, F8×T3, F11×T7, T2). It returned 5 cards per concept.
Merged: K10 H15 (pass 2, F2×T5); K13 H29 (pass 2, F9×T3) and H30 (pass 2, F5×T2); K13 H25 took the pass-2 F11×T7 trigger. The other pass-2 cards are in the merge-drop rows.
Pass 2 deliberately avoided naming Biscuit in captions; pass 1 names him in H16, H23, H26, which is fine: the caption names him, and the 9–12s close-up proves he is printed on the ornament.

**Arm design.**
- K10 keeps the 00A plan (F9×T1 vs F10×T4) as the reference cells and widens each arm into a hypothesis that several formats can express: *before she has it* vs *after it landed*.
  The two references change both F and T, so the pair is a declared bundle. It is insurance in C0: if the late reveal (RV3) is a stop problem, arm B carries the emotion up front.
- K13 keeps the 00A plan (F2×T5 vs F6×T5). The reference pair is a format-arm with T5 held, which is the cleanest read available. Arm B also insures against judge C's register warning
  (a sad opener in a Christmas feed): every B card reaches Biscuit's place on the family ornament by ≤1.0s.

**Why each K10 keep.** H01 is the planned A cell; the hands and box read the gift at once. H02 is the planned B cell; the face is the strongest primitive, and its caption gives context without naming the gift.
H03 is the giver's POV (M8), the buyer's own seat. H04's reveal puts the whole printed family on screen by 0.3s without the names (RV3-safe); its caption sets up the "theirs vs hers" STAKES beat at 2s.
H05 is the CEP read (newlyweds, first Christmas); the box drop gives it an onset. H09 is the only native-artefact card; the note copy is the caption, a low-cost exploration of F14.
H07 is the one F4, for the scale-play hypothesis; the ornament is untouched and the truth frame comes at 1.0s. H13 is the smile-seeking card (T7). H14 uses the animal primitive and keeps the dog off the product.
H15 brings T5 into the pool and pays off at 2s exactly.
**Culled K10.** H06 (comparison) overlaps H04 and H15 on the old-vs-new idea; alternative caption from pass 2: "Every ornament she owns has only one name." H08: the question format has weak lab evidence and the frame repeats the tree.
H10 repeats H01's hands-and-box frame. H11: a silent "talking" head with a finger to the lips may read as a creator ad and adds little over H03. H12: the wide shot keeps the ornament at VS1 (smallest E3 margin) and repeats H07's flash-forward to the hung ornament.
**K10 watch items for 02/03.** H07 needs an 07 shot pass on the tiny faces (FR7) and should be read on hold rate as well as hook rate (FR10). H03's "POV:" label is a scene label, not the viewer. H05's "married" describes the characters.
Every K10 hook shows Grace and Daniel in the same flat with the same boxes, so the two picked hooks must still differ on frame-1 subject (E15). The reference pair does.

**Why each K13 keep.** H16 is the planned A cell: 4 words, the kids and the collar, Mom's ornament as the answer already at the edge. H17 is the planned B cell: absence turns to presence inside 0.4s, so the hook carries the turn.
H23 (F14, a kid-written label) and H24 (a stocking still up, M4 ritual) recognise the loss without anyone stating grief. H29 is a private ritual (M4), third person and specific.
H21 uses a child's face for the smile (named, so "he" stays Biscuit's). H22 is the buyer's own seat (Mom's POV), and "kept a spot" is the thought made visible.
H25 is connection-first (three hands). H26 makes the product truth the hook: the same four people in an old photo and on the ornament. H30 is the one tasteful surprise: the hand uncovers the dog figure; nothing animates.
**Culled K13.** H18 overlaps H16 (collar). H19: the question card has weak evidence, and Mom alone in the centre risks a lonely read. H20 overlaps H30 (both F5 reveals); H30 fills the empty T2 cell.
H27: Mom alone at frame 1, a second F10. H28: naming all four in the caption pre-empts the PROOF beat.
**K13 watch items.** Track hides and negative comments on every K13 ad (00C guardrail). The past photo in H26 is an AI image of the locked cast, and its dog must match the printed Golden Retriever.
In H23 the ornament sits in "Biscuit's stuff" box while the body has it in Mom's hand at 6s. That is consistent if Mom put it there, and 04 can make it explicit.
"Noah" and "Lily" in captions must match the printed spelling. Alternative caption from pass 2 for an A card: "Mom wasn't ready to leave him off the tree."

**W cells.** None used. **Ledger.** Empty, so no reuse was possible and the exploration floor is met by construction. The deliberate exploration picks are listed per concept.
