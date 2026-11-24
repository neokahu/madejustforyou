# MJ4U-133-C0 · 01 hook candidates · K04 + K06

> Role 01 (Hook Ideator), 2026-11-23. Round **C0**, so each concept gets 2 hook arms. Hook ids **MJ4U-133-H31 to H60** (H31–H45 = K04, H46–H60 = K06).
> Sources: `concepts/00A-candidates.md` (K04 and K06 sections only), `GATE0.md`, `00C-slate.md`, `00B-rescore-K06-A/B/C.md`, `BRIEF.md`, `CRITERIA.md`,
> `product.json` (F1–F10), `RENDERS.md`, the real renders `MJ4U-133-K04-render.png` / `MJ4U-133-K06-render.png` (viewed), `_ledgers/hooks.csv`, `_ledgers/codebook.csv`.
> Method: `hook-framework.md` (F × T, FR1–FR11, §6 coverage), `role-research/01-03-hooks.md` §2 and §4, README §2.
> **For the Producer:** the final section "RATIONALE" must be stripped before the cards go to 02. Short ids (`H31`) below mean `MJ4U-133-H31`.

## 0. Rules applied to every card (from BRIEF + CRITERIA)

| Rule | Value | Source |
|---|---|---|
| Hook window | **0.00–2.00s in both ads of each concept**, body starts on the same frame (2.00s) | E14, beat maps (HOOK 0–2) |
| Product at 0.00s | VS1 or higher; identifiable as the family ornament by 1.0s | E3 |
| Onset | something changes by 0.5s; no static frame 1 (ON0 not used) | E26 |
| Caption | ≤10 words, on screen by 0.5s, third person, characters only (never the viewer's attributes) | E5, E12, E62 |
| Audio | bed only (AU0) or one sync hit on the onset (AU1); no voice: neither concept declares dialogue | E12 |
| Pay | first pay ≤5.0s (within 3s of the hook's end), fully paid by 12.0s | E28 |
| Product truth | only the real personalizer render; camera moves and compositing only; never redrawn, never animated | BRIEF, E29, E39 |
| Offer | none: no price, deadline or "order by" | E10 |
| Fake reality | ≤1 card per concept pool, FR1–FR11, truth frame ≤1.5s | E29, FR11 |

**Ledger state:** `_ledgers/hooks.csv` has a header and no rows. No hook has run for any product, so **every F×T cell has <2 ledger entries** and nothing here reuses a ledger hook.
The exploration floor (≥3 cards per pool) is met by construction. The cards are named in §1.4 / §2.4 by the under-used cells the framework points to (F4, F14, F3, F6).

**What the real renders fix (casting and captions must match):**
- **K04**, left→right: **Grandpa**: deep-brown skin, short grey hair, **round (circle) glasses**, green sweater, whipped-cream cocoa in a glass mug, no hat. **Grandma**: deep-brown skin, grey short curls, red sweater, red-plaid trousers, tea cup, no hat. **Olivia**: adult woman, deep-brown skin, long black box braids, Santa hat, white/cream sweater, latte. **Rosie**: Beagle.
  *Note for 05:* in the render Rosie wears **no** Santa hat, but `RENDERS.md` says "Olivia and Rosie keep hats". The render wins. No hook below depends on it.
- **K06**, left→right, all in Santa hats: **Dad**: tan skin, short black hair, red sweater, coffee. **Mom**: tan skin, long straight brown hair, green sweater, cocoa. **Sofia**: kid girl, black high ponytail, **red sweater + plaid trousers** (not the "red plaid pyjamas" of the card spec), cocoa. **Mateo**: baby, wispy light hair, white sweater, baby bottle. Printed spelling is **"Mom"**.
- Pronouns. K04: "she" = Olivia; "he" = Grandpa. K06: "he" = Mateo only; "she" = Sofia; Mom and Dad by title.

**Element-tag codes** (codebook, concept-framework §4a): SU subject · SZ shot size · ON onset (+ second) · CT caption type · words · caption on (s) · AU audio · VS product at 0s · PC people at frame 1.
`cell` = the matrix mark in hook-framework §3 (S★ / S / W).

---

## 1. MJ4U-133-K04 · "She got Grandpa's glasses right" · execution MJ4U-133-K04-X1

Core AN2 · BY1 · RC1×OC1 · X1 = ST6 · PV1 · PF3+PF1 · PX3 · RV2 · EM1. CEP on every card: **adult granddaughter (buyer) → her grandparents × Christmas**.

### 1.1 Arms (step 1)
Axis: **mechanism-arm, declared as an F×T bundle** (format and trigger both change; discovery only, so a winner is not attributable to F or T alone). This is the plan cell's first option ("F11×T7 vs F7×T3").
- **Arm A · F11×T7 "thought made visible".** *Hypothesis:* showing the giver's own act of matching a detail stops and holds the giver better than showing the match itself. Frame 1 = hands and the ornament, no face.
- **Arm B · F7×T3 "that's him".** *Hypothesis:* showing the source (Grandpa's photo) next to his printed figure, so the viewer recognises the person, stops and holds better than the giver's act. Frame 1 = Grandpa's face in a photo beside the print.

### 1.2 What the body can pay (step 2)
2.0–3.5s last year's photo: Grandpa in the same round glasses · 3.5–5.0s same photo: Grandma's red sweater, a mug · 6–9s Olivia's finger moves photo → ornament (sweater, mug, Rosie) ·
9–12s whole ornament, every name + "2026" legible · 12–17s Grandpa unwraps it, taps his own glasses, laughs, side-hug with Olivia · 17–20s on their tree.
**Not payable:** a portrait/likeness claim (the details are personalizer style options, F6) · the dog before 6s · Grandma's own reaction · anything about other years.

### 1.3 Pool (15 cards, step 3). Table A: codes and element tags
| id | arm · axis | format (sub) | T | T2 | P | truth_frame | M | SU | SZ | ON @s | CT | words | cap on | AU | VS | PC | cell |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H31 | A · mechanism (bundle) | F11 match-tap | T7 | T3 | P1 P4 | — | M10 | SU4 | SZ1 | ON2 @0.3 | CT1 | 5 | 0.2 | AU1 | VS2 | PC0 | S★ |
| H32 | A · mechanism (bundle) | F11 personalise (store personalizer) | T7 | T3 | P1 P4 | — | M10 | SU5 | SZ2 | ON2 @0.3 | CT1 | 5 | 0.2 | AU1 | VS2 | PC1 | S★ |
| H33 | A · mechanism (bundle) | F11 unbox-lift | T7 | T4 | P1 P4 | — | M10 | SU1 | SZ2 | ON2 @0.3 | CT1 | 7 | 0.2 | AU0 | VS2 | PC0 | S★ |
| H34 | B · mechanism (bundle) | F7 photo vs ornament split | T3 | T4 | P2 P1 P4 | 0.0 | — | SU2 | SZ2 | ON4 @0.3 | CT4 | 6 | 0.2 | AU1 | VS2 | PC1 | S★ |
| H35 | B · mechanism (bundle) | F7 then-vs-now split | T3 | T5 | P2 P1 P4 | 0.0 | — | SU2 | SZ2 | ON3 @0.3 | CT1 | 5 | 0.2 | AU1 | VS2 | PC1 | S★ |
| H36 | explore | F7 generic vs theirs | T7 | T3 | P1 P4 | 0.0 | M7 | SU1 | SZ2 | ON4 @0.3 | CT3 | 6 | 0.2 | AU1 | VS2 | PC0 | S★ |
| H37 | explore | F3 quiz | T3 | T1 | P4 P1 | — | — | SU1 | SZ2 | ON5 @0.1 | CT2 | 4 | 0.1 | AU1 | VS2 | PC0 | S★ |
| H38 | explore | F8 giver POV | T3 | T9 | P2 P1 P4 | — | M8 | SU4 | SZ2 | ON2 @0.4 | CT3 | 3 | 0.2 | AU0 | VS2 | PC1 | S★ |
| H39 | explore | F10 reaction | T4 | T3 | P2 P1 | — | M3 | SU2 | SZ2 | ON2 @0.2 | CT1 | 5 | 0.2 | AU0 | VS1 | PC1 | S★ |
| H40 | explore | F10 two-shot | T9 | T4 | P2 P1 | — | — | SU2 | SZ3 | ON2 @0.3 | CT1 | 8 | 0.2 | AU0 | VS1 | PC2 | S |
| H41 | explore | F10 giver anticipation | T7 | T4 | P2 P1 | — | — | SU2 | SZ2 | ON2 @0.3 | CT1 | 8 | 0.2 | AU0 | VS1 | PC1 | S★ |
| H42 | explore | F4 scale play | T2 | T7 | P1 P4 | 1.0 | — | SU7 | SZ4 | ON2 @0.3 | CT1 | 5 | 0.2 | AU1 | VS2 | PC1 | S★ |
| H43 | explore | F14 text thread on phone | T1 | T3 | P4 P1 | — | — | SU5 | SZ2 | ON2 @0.3 | CT5 | 5 | 0.1 | AU0 | VS1 | PC0 | S★ |
| H44 | explore | F2 list / specific | T3 | T4 | P4 P1 | — | — | SU1 | SZ1 | ON5 @0.1 | CT4 | 7 | 0.1 | AU0 | VS2 | PC0 | S★ |
| H45 | explore | F5 pull-back from ECU | T1 | T3 | P1 P4 | — | M6 | SU1 | SZ1 | ON4 @0.2 | CT2 | 4 | 0.1 | AU1 | VS2 | PC0 | S★ |

### 1.3 Pool. Table B: the card content
| id | frame1_visual (0.00s) | onset_0_5s | caption | audio_cue | promise | paid_by (s) | asset_source | policy |
|---|---|---|---|---|---|---|---|---|
| H31 | Top-down ECU of the real ornament lying on a wooden table. Grandpa and Grandma fill ~70% of the width, with Grandpa's round glasses at centre and the printed names just below frame. A corner of last year's photo at the right edge. Olivia's fingertip (deep-brown skin, cream knit cuff) hovers. | 0.3s: the fingertip taps the frame of the printed glasses once and rests there, never covering the lenses or a name. | She got Grandpa's glasses right. | Soft wood-tap sync hit on the tap; bed. | These glasses are exactly his, and she made sure. | **2.5** (photo: Grandpa in the same round glasses) · full **9.0** | Real K04 render composited flat on a table plate; live hand insert; camera moves only. | R6 ✓ · "she" = Olivia; hand cast as Olivia ✓ · grandparents alive, present at 12s ✓ |
| H32 | Over Olivia's shoulder (braids at frame left): a laptop on her knees, its screen a **real capture** of the store personalizer showing this exact design (~40% of the frame), cursor on the glasses option. | 0.3s: she clicks "Circle" and the round glasses appear on Grandpa's preview (the real tool, recorded). | She picked Grandpa's glasses first. | Click sync hit; bed. | She is building it to look like him, detail by detail. | **2.5** (photo shows the glasses she was matching) · full **9.0** | Screen recording of the live personalizer building the K04 design (never a mock UI); laptop plate. | R6 ✓ · real UI of our own store, no added badges or notifications ✓ · "she" = Olivia (braids, cream sweater) ✓ · **flag:** until 6s the ornament is the on-screen preview, not the wood object; E3 "identifiable as the family ornament by 1s" depends on the preview reading as one |
| H33 | Close on an open kraft box on a table, tissue folded back, the ornament face-up inside (~55% width); Olivia's two hands enter from the bottom. | 0.3s: she lifts it out by the string and steadies it with a thumb on the hanger tab, Grandpa's glasses facing the camera. | She matched it to last year's photo. | Bed. | Which photo, and how close is the match? | **2.0** (photo appears) · **2.5** (glasses match) · full **9.0** | Real render composited on a hand-held card (thumb on the tab only, never on the print); any swing is hand-driven. | ✓ · hand-held moving composite = 05/07 risk |
| H34 | Vertical split, readable at phone size. Left: last year's printed photo, close on Grandpa (round glasses, green sweater, grin). Right: the ornament's Grandpa figure at the same scale and eye line, with the hanger and cut edge visible. | 0.3s: both halves snap-zoom together onto the glasses (ON4). | Same glasses. Same grin. Same Grandpa. | Sync hit on the zoom; bed. | Everything else on it matches him too. | **2.5** (photo continues: Grandma's red sweater, mug) · full **9.0** | Photo prop of the same AI cast (05 locks it) + real render; split built in the edit. | R6 ✓ · G7: the product half is unaltered from 0.0s ✓ · photo = same cast as the body ✓ |
| H35 | Vertical split. Left: an old, faded photo of a much younger Grandpa in the same round glasses. Right: the ornament's Grandpa figure. | 0.3s: the faded left photo warms to full colour (ON3). | Different decade. Same round glasses. | Sync hit on the colour change; bed. | He has always been "the glasses", and she knew it. | **2.5** (last year's photo, same glasses) · full **9.0** | New "old photo" prop of a young Grandpa (identity across ages = 05 risk) + real render. | ✓ · old photo = memory, not a death cue; Grandpa live at 12s (R18) ✓ |
| H36 | Split. Left: a plain generic "Grandpa" ball ornament (neutral prop, no brand look-alike). Right: this ornament, Grandpa's figure and glasses forward. | 0.3s: the left half slides out and the right fills the frame. | A grandpa ornament. Or Grandpa's ornament. | Sync hit on the slide; bed. | This one is specifically him. | **2.5** · full **9.0** | Neutral generic prop (must not resemble any real competitor product) + real render. | ✓ · no claim about other products |
| H37 | The ornament hanging on a lit tree, framed so the four figures fill the width and the names sit just below the frame edge. | 0.1s: question pops on (ON5), then a slow push toward Grandpa's glasses. | Which one is Grandpa? | Sync hit on the pop; bed. | One detail gives him away. | **2.5** (photo: Grandpa in those glasses) · names legible **9.0** | Real render on a tree plate; camera move only. | R6 ✓: the question is about a character · names cropped only inside the hook; E39 still met at PROOF |
| H38 | Olivia's POV across a kitchen table: her hands (deep-brown, cream cuffs) hold the ornament upright in the lower third. Real Grandpa (short grey hair, round glasses, green sweater) sits behind in soft focus. | 0.4s: he leans in and pushes his glasses up his nose as focus racks to him. | Grandpa, meet Grandpa. | Bed. | Will he see himself in it? | **2.5** (photo, same glasses) · full **9.0** (his figure + "Grandpa" printed); laugh at 12s | Live Grandpa plate (05 cast lock) + real render composited in her hands. | Caption has no giver pronoun, so the hands-only shot is safe (E45) ✓ · alive, present ✓ |
| H39 | Grandpa close, mid-laugh, one finger tapping his own round glasses. The unwrapped ornament is held beside his face (~25% width) with his printed figure visible; Grandma's red sleeve at the frame edge. | 0.2s: the tap and the laugh break together. | He found his glasses first. | Bed. | What about the glasses delights him? | **2.5** · full **9.0** | A separate take of the CONNECTION moment, used only inside the hook window (E13). | "he" = Grandpa ✓ · dramatized reaction, not a testimonial ✓ |
| H40 | Medium two-shot: Grandpa holds the ornament by his cheek, with Grandma beside him (grey short curls, red sweater) laughing. | 0.3s: he lifts it to cheek height and copies the printed grin. | Grandpa says the cartoon got his good side. | Bed. | How close is the cartoon to him? | **2.5** · full **9.0** | Live two-person plate + real render in his hand. | Affectionate, not an age joke ✓ |
| H41 | Close on Olivia (box braids, cream sweater) mid-smile, looking down at the ornament on her lap (~30% width), Grandpa's printed glasses facing the camera. | 0.3s: her smile widens and she lifts it into frame. | Olivia can't wait for Grandpa to see this. | Bed. | What will Grandpa see? | **2.5** · full **9.0** · reaction 12.0 | Live Olivia plate + real render in her hands. | About Olivia's state, not the viewer's ✓ |
| H42 | Wide on a real kitchen table: the real ornament leans upright against a mug (~40% width). A **tiny Olivia** (about 1/10 of frame height, seen from behind at a distance) stands in front of it holding a big magnifying glass toward Grandpa's printed glasses. | 0.3s: she raises the magnifier into place. The lens magnifies the print as real optics would; the print never changes. | She checked every detail. Twice. | Sync hit on the raise; bed. | What was she checking it against? | truth frame **1.0** (hard cut to normal scale: her real hand sets last year's photo beside the same ornament) · **2.0** photo · **2.5** · full **9.0** | Composited miniature + real render on a table plate. | **FR1–FR11:** the impossible part = a tiny person (obvious); the ornament never moves or changes; no face ECU; truth frame 1.0 ≤1.5; metaphor of care; no "real" text; the only F4 in this pool ✓ |
| H43 | Olivia's hand holds her phone over the kitchen table. On screen is one sent bubble with her question (an in-scene artefact: no system banner, no badge). The ornament lies on the table below the phone, in focus (~30% width). | 0.3s: Grandma's reply "Round. Always round." appears in the thread (filmed screen, silent). | Grandpa's glasses: round or square? | Bed (no notification sound). | She is getting one detail exactly right. | **2.5** (photo shows round) · full **9.0** | Filmed phone with a built thread + real render on a table plate. | G8/FR8: artefact physically in scene ✓ · Grandma alive (she texts) ✓ · the question belongs to a character, not the viewer ✓ |
| H44 | ECU of the hanging ornament on Grandpa's glasses, tree bokeh behind. | 0.1s: caption pops (ON5); a slow slide right across Grandma's red sweater. | Round glasses. Red sweater. Rosie the beagle. | Bed. | Every one of these is them. | **2.5** (photo: glasses, sweater) · Rosie 6–9 · full **9.0** | Real render on a tree plate; camera move only. | ✓ |
| H45 | Extreme close on the printed round glasses and the eyes behind them, with the print and wood grain visible. | 0.2–0.9s: fast pull-back to Grandpa's figure, then the whole ornament with all four (ON4). | Whose glasses are these? | Sync hit on the pull-back; bed. | Whose, and how does the gift know? | **0.9** (Grandpa's figure) · **2.5** photo · full **9.0** | Real high-res render; camera move only. | ✓ |

### 1.4 Coverage check (pool of 15, step 3)
| Rule | Result |
|---|---|
| ≥6 formats | **9**: F11 ×3, F7 ×3, F10 ×3, F3, F8, F4, F14, F2, F5 ✓ (max 3, cap 4) |
| ≥5 triggers | **6**: T7 ×5, T3 ×5, T1 ×2, T4, T9, T2 ✓ (max 5, cap 6) |
| ≥8 S★ | **14** (H40 F10×T9 = S) ✓ |
| ≥3 exploration | Ledger empty, so all 15 qualify. Named: **H42** F4×T2, **H43** F14×T1, **H37** F3×T3 ✓ |
| No ✕; W with reason | none ✕, none W ✓ |
| F4 ≤2 per pool, FR1–FR11 | 1 (H42) ✓ |
| Near-duplicates (same F + T + frame-1 subject) | H31/H32/H33 share F11×T7 but differ in subject (SU4 tap on print / SU5 screen / SU1 box) ✓ · H34/H35 share F7×T3, but the left half is a different photo (last year vs decades ago) and the onset differs (zoom vs colour) ✓ |

### 1.5 Self-rejected (step 4). These never received an H-id.
| ref | line (frame) | reason |
|---|---|---|
| SR-K04-1 | "Grandpa can finally see himself." (Grandpa squints at it at arm's length) | Eyesight joke = mocks age (T9 rule: affectionate, never age) |
| SR-K04-2 | F13 Olivia to camera: "I matched every detail from one photo." | Needs a voice; K04 declares no dialogue (E12); a first-person buyer line reads as a customer endorsement (matrix ᵍ) |
| SR-K04-3 | "The perfect gift for the grandpa who has everything." | Cliché |
| SR-K04-4 | F15 "Thousands of grandpas found their glasses." | Invented count (E7, FTC) |
| SR-K04-5 | F9×T9 the real beagle sniffs printed Rosie: "Rosie approved hers first." | The body first shows the dog at 6–9s, >3s after the hook ends (E28) |
| SR-K04-6 | F4 printed Grandpa winks / his glasses glint | Animates the product (FR1, E29) |
| SR-K04-7 | "Grandparents won't be here forever." | A loss/age warning aimed at the viewer (R6); a grief cue against R18 |
| SR-K04-8 | "Order by Dec 11 for Grandpa's tree." | Deadline claim (E10) |
| SR-K04-9 | Kid-granddaughter version of H31 | The buyer must be an adult woman (Gate 0 fix) |
| SR-K04-10 | F12 tap-tap on the print as the hook | Meaning sits in the sound; fails muted |
| SR-K04-11 | F1×T1 snap zoom from the whole ornament onto the glasses: "Look at Grandpa's glasses." | H45 in reverse (same content, same T); kept H45 |
| SR-K04-12 | F6×T5 young-Grandpa photo match-cuts to the ornament: "Round glasses since before she was born." | Same prop and promise as H35; kept the comparison version |
| SR-K04-13 | F7×T3 top-down, her hand slides the photo in beside the ornament: "Grandpa in the photo. Grandpa on the ornament." | Repeats the body's 6–9s TURN picture; frame 1 too close to arm A's hands |
| SR-K04-14 (pass 2) | F1×T2 a hand flips the ornament face-up: "Grandpa's new ornament has his real glasses." | "real glasses" reads as the physical eyewear (misleading); first pay at 12s (E28) |
| SR-K04-15 (pass 2) | F2×T5 "Every Christmas with Grandpa, now on one ornament." | Implies many years on one ornament (it prints one year); first pay at 6s (E28) |
| SR-K04-16 (pass 2) | F5×T7 tissue peels back in a wrapped box: "Olivia hides Grandpa's glasses in the gift." | Same picture as H33 (box + tissue) and a clickbait caption; folded into H33 |
| SR-K04-17 (pass 2) | F9×T5 her finger slides off the photo toward the ornament: "Olivia swaps last year's photo for this." | Copies the body's 6–9s beat; nothing bittersweet, so T5 is mis-tagged |

### 1.6 Kept: 10 cards to 02 (step 5)
| arm | kept | one line |
|---|---|---|
| A · F11×T7 | **H31** | Fingertip taps Grandpa's printed round glasses: "She got Grandpa's glasses right." |
| A · F11×T7 | **H32** | Real personalizer capture, she clicks "Circle": "She picked Grandpa's glasses first." |
| A · F11×T7 | **H33** | She lifts it from the box, glasses forward: "She matched it to last year's photo." |
| B · F7×T3 | **H34** | Split, Grandpa's photo beside his printed figure, snap-zoom to the glasses: "Same glasses. Same grin. Same Grandpa." |
| B · F7×T3 | **H35** | Split, decades-old photo warms to colour beside the print: "Different decade. Same round glasses." |
| explore | **H38** | Her POV holding it up, real Grandpa leans in behind: "Grandpa, meet Grandpa." (F8×T3) |
| explore | **H39** | Grandpa mid-laugh tapping his own glasses, ornament by his face: "He found his glasses first." (F10×T4) |
| explore | **H42** | Tiny Olivia with a magnifier at the printed glasses, truth cut at 1.0s: "She checked every detail. Twice." (F4×T2) |
| explore | **H43** | Phone thread above the ornament, reply "Round. Always round.": "Grandpa's glasses: round or square?" (F14×T1) |
| explore | **H45** | Pull-back from the printed glasses ECU to the whole ornament: "Whose glasses are these?" (F5×T1) |

Kept coverage: 7 formats (F11, F7, F8, F10, F4, F14, F5) · 5 triggers (T7, T3, T4, T2, T1) · 2 cards per arm or more ✓.
**Arm distinctness (§6c, E15):** every arm-A frame 1 is the ornament or its preview with hands and **no face**. Every arm-B frame 1 is **Grandpa's face in a photo** split beside the print. A and B differ in subject (SU4/SU5/SU1 vs SU2), people (PC0 vs PC1) and onset event ✓.

---

## 2. MJ4U-133-K06 · "First Christmas as four" · execution MJ4U-133-K06-X1 (rebuilt card)

Core AN5 · BY3 · RC4×OC6 · X1 = ST1 · PV4 · PF1 · PX4 · RV1 · EM3 (PF4 edge shot dropped: no physical sample). CEP on every card: **family of four (self-buyers) × baby's first Christmas / new arrival**.

### 2.1 Arms (step 1)
Axis: **mechanism-arm, declared as an F×T bundle**. This is the plan cell's arm "F2×T3 vs F5×T7".
- **Arm A · F2×T3 "the line names the moment".** *Hypothesis:* a caption that names the moment over the full, legible ornament ("as four") makes the family recognise themselves and stop. Frame 1 = the ornament with all printed members present.
- **Arm B · F5×T7 "the newest one appears".** *Hypothesis:* seeing the newest member uncovered on the ornament (the outcome the self-buyer wants) stops and holds better than being told. Frame 1 = Mateo hidden or isolated, then revealed.

### 2.2 What the body can pay (step 2)
2.0s close on the baby figure, "Mateo" legible · ~3.0s Sofia · ~4.0s Mom · ~5.0s Dad (camera slide, names legible) · 6–9s pull back: all four + "2026" · 9–12s full still, every name + year ·
12–17s live: Sofia lifts it onto the tree, Mom beside her holding real Mateo, Dad's hand on Sofia's shoulder, Sofia points from the printed baby to the real one · 17–20s ornament on the tree.
**Not payable:** the 3 mm edge or wood thickness (no sample) · other years or a yearly tradition · a giver/recipient hand-off (self-buyer) · a likeness claim for the baby.

### 2.3 Pool (15 cards, step 3). Table A: codes and element tags
| id | arm · axis | format (sub) | T | T2 | P | truth_frame | M | SU | SZ | ON @s | CT | words | cap on | AU | VS | PC | cell |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H46 | A · mechanism (bundle) | F2 occasion statement | T3 | T4 | P4 P1 | — | M9 | SU1 | SZ2 | ON5 @0.1 | CT4 | 4 | 0.1 | AU0 | VS3 | PC0 | S★ |
| H47 | A · mechanism (bundle) | F2 list / roll-call | T3 | T4 | P4 P1 | — | M9 | SU1 | SZ1 | ON4 @0.2 | CT4 | 6 | 0.1 | AU1 | VS3 | PC0 | S★ |
| H48 | explore | F2 occasion | T8 | T5 | P4 P1 | — | M9 | SU1 | SZ2 | ON5 @0.1 | CT1 | 5 | 0.1 | AU0 | VS3 | PC0 | S |
| H49 | B · mechanism (bundle) | F5 hand-cover lift | T7 | T4 | P1 P4 | — | M1 | SU4 | SZ2 | ON2 @0.4 | CT1 | 7 | 0.2 | AU1 | VS2 | PC0 | S★ |
| H50 | B · mechanism (bundle) | F5 pull-back from ECU | T7 | T3 | P1 P4 | — | M1 | SU1 | SZ1 | ON4 @0.2 | CT1 | 6 | 0.1 | AU1 | VS3 | PC0 | S★ |
| H51 | B · mechanism (bundle) | F5 unwrap (tissue) | T7 | T4 | P1 | — | M1 | SU4 | SZ2 | ON2 @0.3 | CT4 | 7 | 0.2 | AU1 | VS1 | PC0 | S★ |
| H52 | explore | F1 light onset | T4 | T3 | P1 P4 | — | M5 | SU1 | SZ2 | ON3 @0.3 | CT1 | 4 | 0.2 | AU1 | VS3 | PC0 | S★ |
| H53 | explore | F10 reaction (kid) | T4 | T3 | P2 P1 | — | M3 | SU2 | SZ2 | ON2 @0.2 | CT1 | 6 | 0.2 | AU0 | VS1 | PC1 | S★ |
| H54 | explore | F9 quoted line | T9 | T3 | P4 P1 | — | — | SU4 | SZ2 | ON2 @0.3 | CT5 | 8 | 0.2 | AU0 | VS3 | PC0 | S |
| H55 | explore | F4 scale play | T4 | T2 | P1 | 1.0 | — | SU7 | SZ4 | ON2 @0.3 | CT1 | 7 | 0.2 | AU1 | VS2 | PC1 | S★ |
| H56 | explore | F3 quiz | T1 | T3 | P4 | — | M6 | SU1 | SZ2 | ON5 @0.1 | CT2 | 7 | 0.1 | AU0 | VS3 | PC0 | S |
| H57 | explore | F6 then/now (photo → ornament) | T5 | T4 | P1 P4 | 0.6 | — | SU5 | SZ2 | ON2 @0.4 | CT1 | 6 | 0.2 | AU0 | VS1 | PC2 | S★ |
| H58 | explore | F7 generic vs theirs | T7 | T3 | P4 P1 | 0.0 | M7 | SU1 | SZ2 | ON4 @0.3 | CT1 | 7 | 0.2 | AU1 | VS3 | PC0 | S★ |
| H59 | explore | F7 printed vs real split | T3 | T4 | P2 P1 | 0.0 | — | SU2 | SZ2 | ON4 @0.4 | CT1 | 3 | 0.2 | AU1 | VS3 | PC1 | S★ |
| H60 | explore | F14 text on phone | T1 | T3 | P4 P1 | — | — | SU5 | SZ2 | ON2 @0.4 | CT5 | 7 | 0.1 | AU0 | VS1 | PC0 | S★ |

### 2.3 Pool. Table B: the card content
| id | frame1_visual (0.00s) | onset_0_5s | caption | audio_cue | promise | paid_by (s) | asset_source | policy |
|---|---|---|---|---|---|---|---|---|
| H46 | The ornament hanging on a lit tree branch, medium-close (~70% width): all four figures in Santa hats, names legible, Mateo at the right end. | 0.1s: caption on (ON5); slow push toward Mateo. | First Christmas as four. | Bed. | Who is the fourth? | **2.0** (Mateo close, name legible) · full **6.5** (all four + 2026) | Real K06 render on a tree plate; camera moves only. | "four" = 4 printed figures = 4 live people at 12s ✓ · about the family, not the viewer ✓ · no tradition implied ✓ |
| H47 | ECU of Dad's printed figure and the name "Dad". | 0.2s: whip-pan right along the ledge, landing on Mateo at 0.6s with a sync hit (ON4). | Dad. Mom. Sofia. And now, Mateo. | Sync hit on the landing; bed. | Mateo is new: the family just grew. | **2.0** (Mateo close) · 3.0–5.0 Sofia, Mom, Dad · full **6.5** | Real render; the whip-pan is a camera move on the still. | Names verbatim from the render ("Mom") ✓ |
| H48 | Ornament on the branch, close on its right half: Sofia and Mateo with names legible, "26" below. | 0.1s: caption on; slow push. | There's only one first Christmas. | Bed. | This ornament marks it. | **2.0** · full **6.5** (year) | Real render on a tree plate. | Occasion only: no deadline, no "order by" (E10) ✓ · T8 used for the occasion's uniqueness, not scarcity |
| H49 | The ornament on the branch, close (~65% width): Dad, Mom and Sofia legible. Sofia's small hand (tan, red sweater cuff) covers the right end where Mateo sits. | 0.4s: she pulls her hand away; the baby figure and "Mateo" appear. | Look who made it onto the ornament. | Sync hit on the reveal; bed. | The newest one is on it, so the family is complete. | **0.5** (reveal) · **2.0** · full **6.5** | Live child-hand insert over the real render (occlusion compositing = 05/07 risk). | Hand cast = Sofia (kid, tan, red cuff) ✓ · no pronoun in the caption ✓ |
| H50 | ECU of the printed baby: Santa hat, bottle, "Mateo" legible below. | 0.2–1.0s: fast pull-back to the whole ornament (ON4). | The newest one on the ledge. | Sync hit on the pull-back; bed. | Who else is up there with him? | **1.0** · **2.0** · full **6.5** | Real high-res render; camera move only. | ✓ |
| H51 | Top-down: an open box on a table, with tissue over the ornament except the four Santa hats and the hanger tab. Mom's hands (tan, green cuffs) at the edges. | 0.3s: she folds the tissue back; the four figures appear, the baby last. | All four of them. Even the newest. | Paper sync hit; bed. | The baby made it onto the family ornament. | **0.8** · **2.0** · full **6.5** | Real render composited under a live tissue/hands plate. | Hands = Mom; no pronoun ✓ · self-buyer unboxing, not a gift hand-off ✓ |
| H52 | Dim evening room, tree lights off. The ornament hangs on the branch in soft window light (~55% width), names readable. | 0.3s: the tree lights switch on around it (ON3). The ornament is only lit by them and never glows. | Lights on. Everyone's here. | Soft chime sync hit; bed. | Who is "everyone"? | **2.0** (Mateo) · full **6.5** (all four) | Real render on a tree plate with a light change on the plate. | The light acts on the scene, not the product (E29 spirit) ✓ |
| H53 | Sofia close (black high ponytail, red sweater), delighted, holding the ornament at chin height (~30% width), a finger on the printed baby. | 0.2s: she grins and turns it toward the camera. | Sofia found her brother on it. | Bed. | Where is her brother, and where is she? | **2.0** · **3.0** (her figure) · full **6.5** | Live child plate + real render composited in her hands. | "her" = Sofia ✓ · child holding a composite = risk |
| H54 | The ornament on the branch, close; Sofia's finger enters, pointing at her own printed figure. | 0.3s: she taps her own figure. | Sofia's first question: "Am I on it too?" | Bed (no voice: captioned only). | The big sister checking she is part of it. | **3.0** (slide reaches Sofia + name) · full **6.5** | Real render + live finger insert. | No declared dialogue, so the line is caption-only (AU0) ✓ |
| H55 | Wide on a real lit tree branch: the real ornament hangs (~40% width). A **tiny Sofia** (about 1/8 of frame height, seen from behind) stands on the branch beside it, arm out as if presenting it. | 0.3s: she flings both arms up toward the printed baby. | Sofia is showing everyone her little brother. | Sync hit; bed. | Who is the little brother? | truth frame **1.0** (hard cut to normal scale, ornament close on the branch) · **2.0** · **3.0** · full **6.5** | Composited miniature + real render on a tree plate. | **FR1–FR11:** she stands on the branch, never on the flat printed ledge; the ornament never moves; the tiny person is obvious; no face ECU; truth frame 1.0; metaphor = pride; the only F4 in this pool ✓ |
| H56 | The ornament close: all four, names legible. | 0.1s: question pops; push toward the right end. | Which one joined the family this year? | Bed. | Spot the new arrival. | **2.0** · full **6.5** | Real render. | About characters, not the viewer ✓ |
| H57 | Mom's fingers hold a printed photo from last Christmas in front of the tree: Mom (pregnant, green sweater), Dad and Sofia smiling. The ornament hangs behind, visible above the photo's edge (VS1). | 0.4s: the photo lowers out of frame and the ornament behind comes sharp, Mateo on it. | Last Christmas, he was a bump. | Bed. | He is here now, and on the ornament. | truth frame **0.6** · **2.0** (Mateo close) · full **6.5** | Photo prop of the same cast a year earlier (identity lock = 05 risk) + real render on a tree plate. | The pregnancy describes a character, not the viewer ✓ · "he" = Mateo, on the print from 0.6s ✓ · no other year's ornament shown ✓ |
| H58 | Split. Left: a generic "Baby's First Christmas" bootie-shaped ornament (neutral prop, no names). Right: this ornament with all four. | 0.3s: the left half slides away and the right fills the frame. | Baby's first Christmas. Or the whole family's. | Sync hit; bed. | This one holds everyone, not just the baby. | **2.0** · full **6.5** | Neutral generic prop (no real competitor look-alike) + real render. | ✓ |
| H59 | Split at phone size. Left: the ornament's right end (Sofia, Mateo, "26"), "Mateo" legible. Right: soft blur. | 0.4s: a soft wipe reveals the right half: real baby Mateo in Mom's arm, white sweater, same eye line. | Mateo, meet Mateo. | Sync hit on the wipe; bed. | The baby on the ornament is this baby. | **2.0** · full **6.5**; live again 12–17 | Real render + live infant plate (AI infant close-up = 07 shot-QA risk). | No likeness claim: "meet", not "looks like" ✓ · "Mateo" printed = cast ✓ |
| H60 | Mom's hand holds her phone in front of the tree; on screen one received bubble from "Abuela" (in-scene artefact, no system banner). The ornament hangs behind the phone, softly in focus (~25% width). | 0.4s: Mom lowers the phone and the ornament comes sharp, Mateo on it. | Abuela's first text: "Is Mateo on it?" | Bed (no notification sound). | Is he? | **0.6** · **2.0** (Mateo close) · full **6.5** | Filmed phone with a built thread + real render on a tree plate. | G8/FR8 ✓ · Abuela = an off-screen, living grandmother ✓ · "you" never addresses the viewer ✓ |

### 2.4 Coverage check (pool of 15, step 3)
| Rule | Result |
|---|---|
| ≥6 formats | **10**: F2 ×3, F5 ×3, F7 ×2, F1, F10, F9, F4, F3, F6, F14 ✓ (max 3, cap 4) |
| ≥5 triggers | **7**: T7 ×4, T3 ×3, T4 ×3, T1 ×2, T8, T9, T5 ✓ (max 4, cap 6) |
| ≥8 S★ | **12** (H48 F2×T8, H54 F9×T9, H56 F3×T1 = S) ✓ |
| ≥3 exploration | Ledger empty, so all 15 qualify. Named: **H55** F4×T4, **H60** F14×T1, **H57** F6×T5 ✓ |
| No ✕; W with reason | none ✕, none W ✓ |
| F4 ≤2 per pool, FR1–FR11 | 1 (H55) ✓ |
| Near-duplicates | H46/H47 (F2×T3): full ornament vs single-figure ECU + whip-pan ✓ · H49/H50/H51 (F5×T7): hand cover / ECU pull-back / box ✓ |

### 2.5 Self-rejected (step 4). These never received an H-id.
| ref | line (frame) | reason |
|---|---|---|
| SR-K06-1 | "Your baby's first Christmas deserves this." | Asserts the viewer's family status (R6, E62); cliché |
| SR-K06-2 | F6 last year's three-person ornament → this one: "Last year: three. This year: four." | Shows another year's ornament and implies a tradition (card rule) |
| SR-K06-3 | F11 side-on 3 mm edge, thumb along the cut: "Real wood, cut to their shape." | Needs a physical sample we don't have (00B re-score); "real" over a composite also fails FR9 |
| SR-K06-4 | Any "Mum" version | Printed name is "Mom" (US store) |
| SR-K06-5 | F13 Mom to camera: "We almost forgot to add Mateo." | Needs a voice (no declared dialogue, E12); reads as a customer testimonial (matrix ᵍ) |
| SR-K06-6 | F4 the printed baby waves; snow falls off the printed ledge | Animates the product (FR1, E29) |
| SR-K06-7 | "Get it before Christmas sells out." | Deadline/scarcity claim (E10, Meta prohibited practices) |
| SR-K06-8 | F2×T3 wide live shot of all four by the tree, ornament in the foreground: "All four of them, on one ornament." | Four cast-matched people including an infant in frame 1 (production risk flagged by all three re-score judges); its promise duplicates H46 |
| SR-K06-9 | F8×T4 Mom's POV, the baby's hand grabs the ornament: "Mateo found himself first." | Infant hand on a composited ornament at 0.4s = the highest compositing risk; judge C flagged child-hands POV for a self-buyer |
| SR-K06-10 | F11×T7 personalizer capture, members added one by one: "The last one Mom added: Mateo." | The three-figure preview reads as an earlier version (implied tradition); duplicates the K04 personalizer card across concepts |
| SR-K06-11 (pass 2) | F1×T2 the ornament hangs upside-down from Mom's fingers and is flipped: "Dad, Mom, Sofia, and Mateo — their first ornament." | A gimmick onset on a hand-rotated composite; "their first ornament" implies a series |
| SR-K06-12 (pass 2) | F3×T3 Mom holds the ornament beside the real baby: "Does baby Mateo look like this?" | Invites a likeness judgment the product does not promise (style options, not portraits); first pay at 12s (E28). Its comparison idea was kept as H59 |
| SR-K06-13 (pass 2) | F9×T1 camera already mid-slide along the ledge: "Whose names are hiding on this ornament?" | Copies the body's 2–6s pan |
| SR-K06-14 (pass 2) | F14×T5 handwritten note propped beside it: "Mateo's very first Christmas, Sofia's new little brother." | Note text plus an 8-word caption is over the 2s reading budget; second F14 with a weak T5 fit |

### 2.6 Kept: 10 cards to 02 (step 5)
| arm | kept | one line |
|---|---|---|
| A · F2×T3 | **H46** | Full ornament on the lit branch, push toward the baby: "First Christmas as four." |
| A · F2×T3 | **H47** | ECU "Dad", whip-pan along the ledge landing on the baby: "Dad. Mom. Sofia. And now, Mateo." |
| B · F5×T7 | **H49** | Sofia's hand covers the baby figure, lifts at 0.4s: "Look who made it onto the ornament." |
| B · F5×T7 | **H50** | ECU of the printed baby, fast pull-back to all four: "The newest one on the ledge." |
| explore | **H52** | Tree lights switch on around the ornament at 0.3s: "Lights on. Everyone's here." (F1×T4) |
| explore | **H54** | Sofia taps her own printed figure: "Sofia's first question: 'Am I on it too?'" (F9×T9) |
| explore | **H55** | Tiny Sofia presents the ornament from the branch, truth cut at 1.0s: "Sofia is showing everyone her little brother." (F4×T4) |
| explore | **H57** | Last Christmas's photo (Mom pregnant) lowers to reveal the ornament: "Last Christmas, he was a bump." (F6×T5) |
| explore | **H59** | Split, printed Mateo then the real baby wipes in: "Mateo, meet Mateo." (F7×T3) |
| explore | **H60** | Mom lowers her phone ("Is Mateo on it?") to reveal it: "Abuela's first text: 'Is Mateo on it?'" (F14×T1) |

Kept coverage: 8 formats (F2, F5, F1, F9, F4, F6, F7, F14) · 6 triggers (T3, T7, T4, T9, T5, T1) · 2 cards per arm ✓.
**Arm distinctness (§6c, E15):** arm A frame 1 shows **all printed members** at the start (H46) or the left end (H47), with the line carrying the moment. Arm B frame 1 **withholds the baby** (a hand over him, H49) or isolates him (ECU, H50).
**Pairing caution for 03:** H47 and H50 both open on an ECU of one printed figure (Dad vs Mateo). Prefer **H46 vs H49 or H50**, or **H47 vs H49**; avoid **H47 vs H50**.

---

## 4. Handoff to 02 (strip §5 first; send cards without rationale, author or generation order)
- **K04:** H31, H32, H33, H34, H35, H38, H39, H42, H43, H45 (Tables 1.3 A+B, rows only).
- **K06:** H46, H47, H49, H50, H52, H54, H55, H57, H59, H60 (Tables 2.3 A+B, rows only).
- Shuffle the order before sending. The `arm` column stays (02 needs it for G9 and §6c). This file's §1.1/§2.1 hypotheses stay with the Producer and 03.

---

