# MJ4U-133-C0 · K06 "First Christmas as four" · O1 shot list + O5 frame-1 pack (role 05, planning pass, 2026-11-25)

Ads: `MJ4U-133_C0_K06X1-H46_E0_v01` (arm A) · `MJ4U-133_C0_K06X1-H50_E0_v01` (arm B). Body 2.00–20.00 is shared and frame-identical (E13).
Authority: `K06/script.md` beat table (words, timing). Round-wide rules: `council/verdict.md` § Round-wide rules for 05 (1–11). E37 as amended.
Status: **plan only, nothing generated.** Reference lock (GATE B) is still open: see `refs/REFS-PLAN.md`.

## 0 · Geometry every shot uses (measured on the real render, 2026-11-25)

Render `renders/MJ4U-133-K06-render.png`, 3185×3000 RGBA. Ornament alpha bbox x 270–2936, y 194–2925 (2666×2731). Hanger hole ≈ (1500, 260).
Printed names (Chewy, #783D08), measured in render px: **Dad 117 w** (x 643–759) · **Mom ≈152 w** · **Sofia 187 w** (x 1811–1997) · **Mateo 199 w** (x 2433–2631); name letter height ≈ 66–75 px; name row y ≈ 1670–1745.
Figure stacks (hat top → name bottom, render px): Dad 330→1740 (1410) · Mom 430→1740 (1310) · Sofia 760→1740 (980) · Mateo 950→1745 (795). Figure centres x: Dad 690 · Mom 1340 · Sofia 1905 · Mateo 2500.
**Pixel budget:** the baby figure's source cliparts are 800 px "_large" webp at 228.8 artwork units = 3.50 px/unit; the render is 3.70 px/unit, so the render is ≈1.06× native. Higher-res originals are not available (CDN 403 on `_original`, no-suffix, png, jpg). Names and year are vector text and stay sharp at any scale.

**Camera notation:** `s` = render scale on the 1080×1920 screen (render px → screen px). `s ≤ 1.0` means no upscale of the real artwork. A STILL+MOVE camera is given as `s` plus the render point placed at a screen point.

**K06 fixed caption band (E58), 9:16:** y 280–480 (14.6–25.0%), centred, ≤2 lines, x 65–1015 (6% sides). Every product shot keeps hats and faces below y 480 (E60). Printed names during their read sit at **y ≤ 1440** (see risk R1: this is below the 65% line).
**4:5 crop path (rule 9):** product beats crop the 9:16 at y 200–1550; 06 places the 4:5 band separately (E58 per format). People beats: centred crop y 285–1635.

## 1 · Shot table

Hook shots differ per arm (0.00–2.00). Everything from 2.00 is one body.

| shot_id | tc | serves (exact words on screen) | regime | size/angle | camera_move (ONE) | subject + action in space | source_type | refs_required (role) | text_to_composite | continuity | takes · draft→final | acceptance (beyond §2.7) | cut in / out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **K06-A-1** (arm A) | 0.00–2.00 | "First Christmas as four." (0.00–3.20) | energy | MS → CU, straight on, eye level with the ornament | **Push-in**, fast-in / ease-out (easeOutCubic), already moving on frame 0. Start s 0.284, render (1603,1560) at screen (540,888) → end s 0.52, render (2500,1350) at screen (540,960) (keeps the sliver of Mom's hat at the left edge below the band). 90% of the travel done by 1.6s | The K06 ornament hangs by its thin gold cord from a lit fir branch, printed face square to camera, still. Camera arrives on printed Mateo (right end of the ledge). Post life: fairy-light bokeh twinkle layer (luminance 0.85–1.0, 0.5–1.5 Hz per light) | STILL+MOVE: plate **P1** (generated physical body on the branch) + real render layer on top, both on one camera transform | render → product face · P1 → composition/light/scale | none generated. Printed names/year = render layer. Caption = 06 | night, warm tungsten key from camera left (off-screen), cool fill; tree bokeh warm white; ornament 5 in scale per SA1 | P1: 3 takes · draft 2K → final 4K | Frame 0 already moving. "Mateo" ≥100 px by 1.5s (s≥0.50). Render layer never above s 1.0; P1 layer upscale ≤1.5× at end (≤1.24× at 2K, ≤0.88× at 4K). Hats clear of y 480 all shot | in: start of ad · out: **hard cut** |
| **K06-B-1** (arm B) | 0.00–2.00 | "The newest one / on the ledge." (0.00–3.20) | energy | ECU (printed baby) → MS (whole ornament on branch) | **Pull-back** (snap). 0.00–0.20 micro-drift s 1.18→1.15 (frame 0 moves); 0.20–1.00 snap pull to s 0.284, easeInOutExpo, sync hit at ≈0.25s; 1.00–2.00 slow settle s 0.284→0.30 (never frozen). Start render (2530,1350) at (540,970) → end render (1603,1560) at (540,888) | Printed baby Mateo fills the safe window: Santa hat (top 498), bottle, "Mateo" (bottom 1436), 51% of frame width; then the whole ornament on the branch with all four + 2026 | STILL+MOVE: render layer + P1 plate (P1 layer extra-defocused while s>0.6) | render → product face · P1 → composition/light | none generated | as K06-A-1 | uses P1 (no extra asset) | **H50 crop gate: PASS** (see §3). "Mateo" 235 px wide at frame 0. Hat top ≥ y 490; name bottom ≤ y 1440. Sofia's knee sliver at left edge ≤60 px or none | in: start of ad · out: **hard cut** |
| **K06-2** | 2.00–6.00 | (2.00–3.20 hook caption of each arm) then "Big sister Sofia. / Mom. Dad." (3.20–6.00) | stability | CU, straight on, ledge level | **Lateral slide (truck) left**, constant speed with soft ends (easeInOutSine), s 0.667 constant. Render (1905, y) at screen x 540 → render (690, y) at screen x 540; vertical: name bottom r1740 at screen y 1430 throughout | Camera-only slide along the ledge over printed Sofia → Mom → Dad. At 2.00 Sofia is centred with **Mateo still visible at the right edge** (rule 8: arm B's caption must not point at Sofia) and Mom part-visible left. Sofia read 2.0–3.2, Mom 3.6–4.6, Dad 5.0–6.0 | STILL+MOVE: render layer + P1 layer (defocused ≈12 px) | render → product face · P1 → background light | none generated | P1 bokeh, same grade as hook | n/a (no new asset) | E39 at s 0.667: Sofia 125 px, Mom 101 px, **Dad 78 px (fails 100 px: risk R1)**. Hats ≥ y 490 (Dad hat top lands at 490). Names y 1386–1430 | in: **hard cut** · out: **hard cut** |
| **K06-3** | 6.00–8.80 | "All four, / on one ornament." | energy | CU (whole ledge) → WS (ornament small on the tree) | **Pull-back** (dolly out), slow, ease-out. Start s≈0.45 (all four + names, ornament overflows the frame sides slightly) → end s≈0.24 (ornament ≈60% width, branch and lit tree around it, wider than K06-A-1's start) | Ornament hangs on the branch face-on, still; real parallax between needles, ornament and bokeh. "2026" fully in frame by the end | **GEN-VIDEO plate V3** (generated slow push-in from a P1-matched frame, **played reversed** in edit) + real render **tracked** over the placeholder face (planar: scale + translate) | V3 first frame = P1 (composition) · K06 front render, 34left, 34right (product body) | none generated; the plate's face is a placeholder, fully covered | P1 set, light, grade | V3: 3 takes · 720p (1080p optional) | Ornament faces camera on every frame of the window, rotation ≤3°, no spin, no back visible, cord stays attached. Generated face fully covered by the track on ≥5 frames. Fallback: STILL+MOVE pull-back on P1 with 2.5D parallax (free) | in: **hard cut** · out: **hard cut** |
| **K06-4** | 8.80–12.00 | "Mateo got / the end spot." | stability | MS (full ornament) → MCU (right end), straight on | **Push-in toward the right end**, slow, easeInOutSine. Start s 0.33, render (1603,1560) at (540,960) → end s 0.52, render (2250,1350) at (540,960) | The render full frame, straight on (macro on the tree; background = P1 heavily defocused). Ends with Mateo (and Sofia) large at the right end of the ledge | STILL+MOVE: render layer (4K source, s ≤0.52 = downscale) + P1 defocused ≈20 px | render → product face · P1 → background | none generated | P1 grade; no sway (stability) | n/a | E39: all four names + 2026 legible by eye at start (Dad 39 px, Mom 50, Sofia 62, Mateo 66; the read is Mateo); at end Mateo 103 px. Year bottom ≤ y 1320. Mom's hat at end ≥ y 480 | in: **hard cut** · out: **hard cut** |
| **K06-5a** | 12.00–14.60 | "Sofia showed Mateo / where he sits." (12.50–17.00; 12.00–12.50 no caption) | energy | MS, slightly low (Sofia's eye height), 9:16 | **Push-in** (dolly in), slow, ≈6% over the shot, ends MS | Living room at night. Frame right foreground: the ornament already hangs on a lower branch at Sofia's chest height, face to camera. Frame left-centre: Sofia (C3), body ¾ to camera facing right toward the tree, right arm extended, **fingertips leave the top edge of the hanger tab** and her hand lowers to her side (the one action). Centre-right, ≈60 cm behind: Mom (C2) stands holding Mateo (C4) swaddled upright against her chest, both arms wrapped round him, Mateo's face ¾ to camera, still. Behind Sofia, soft focus: Dad (C1), his left hand resting on Sofia's left shoulder. All four in frame | GEN-VIDEO from image first frame **F5a**; real render tracked over the ornament face; ornament sway added in post on the render layer (±2°, decaying over 1.5s after release) | F5a → first frame/composition · C3 front → character · C2 front → character · K06 front + 34right → product body | none generated. Render over the ornament; fingertip roto on the hanger tab only | cast per REFS-PLAN (no Santa hats); same tree/lights as P1; key camera left off-screen | F5a: 4 takes (image) · V5a: 3 takes (+1 reserve) · 720p | ≤3 sharp faces (Sofia, Mom, Mateo; Dad soft). Fingertips touch only the hanger tab, never the print. Ornament: no spin, face-on, ≤10° rotation in the window. Mateo near-still (no limb flail, slow blink max). Mom's both arms around Mateo throughout | in: **hard cut** · out: **hard cut** |
| **K06-5b** | 14.60–17.50 | (same caption to 17.00; 17.00–17.50 no caption) | energy | MCU two-shot + ornament foreground, eye level | **Lateral truck right**, slow, ease-in-out, ≈8% of frame width, ends with Mateo's face right of centre | Same layout as 5a, tighter. Frame right foreground: the ornament (in frame to 17.50, rule 7). Frame left: Sofia, ¾ to camera, right arm raised, index finger pointing at the ornament ≈10 cm away (never touching); **her pointing arm lifts ≈20° to point at Mateo's face ≈15 cm away** (the one action; Mateo is behind and above the ornament from camera). Mom smiles, gaze down to Mateo. Mateo near-still, eyes open. Dad soft at frame left behind Sofia | GEN-VIDEO from image first frame **F5b**; real render tracked over the ornament face | F5b → first frame · C3 front → character · C2 front → character · C4 front → character · K06 front → product body | none generated | as 5a; screen direction kept (ornament right, Sofia left) | F5b: 4 takes · V5b: 4 takes · 720p | Finger never touches ornament or baby; 5 fingers, index extended, thumb tucked. Ornament face-on to 17.50 and composited render legible (names not required). Mateo still. Sofia reads as a big sister (age 6–7), Mateo as an infant | in: **hard cut** · out: **hard cut** to the end card |
| **K06-6** | 17.50–20.00 | "Personalize yours" + store lockup | — | shared end card | shared (BRIEF: hero on the tree, slow push-in) | identical in all 12 ads (E9) | shared round asset, not built by K06 | n/a | n/a (06 round-level) | n/a | n/a | E9 owned at round level | in: hard cut · out: end |

Shot lengths: 2.0 · 4.0 · 2.8 · 3.2 · 2.6 · 2.9 · 2.5 (unchanged from 04; E32 holds). Cuts: 6 hard cuts in 20 s (0.3 cuts/s).
Size sequence (arm A): MS→CU · CU · CU→WS · MS→MCU · MS (live) · MCU (live) · end. Arm B: ECU→MS · CU · … Each adjacent pair changes scale or world (see risk R4 for A-1 → 2).

## 2 · Stills: move parameters for 06 (native-resolution moves)

Built as two layers sharing one 2D camera: the **render layer** sampled from the 3185×3000 PNG (never from a pre-composited downscale), and the **P1 plate layer** registered to it by a 4-point warp (06 stores the warp once at Gate B). Ease names are the Motion Prompt camera pack (#027 dolly in, #029 tracking).

| shot | t | s | render point → screen point | ease | P1 layer |
|---|---|---|---|---|---|
| A-1 | 0.00 → 2.00 | 0.284 → 0.52 | (1603,1560)→(540,888) ⇒ (2500,1350)→(540,960) | easeOutCubic | sharp; twinkle layer on |
| B-1 | 0.00 → 0.20 | 1.18 → 1.15 | (2530,1350)→(540,970) | linear | defocus 10 px |
| B-1 | 0.20 → 1.00 | 1.15 → 0.284 | ⇒ (1603,1560)→(540,888) | easeInOutExpo | defocus → sharp |
| B-1 | 1.00 → 2.00 | 0.284 → 0.30 | (1603,1560)→(540,888) | linear | sharp; twinkle on |
| 2 | 2.00 → 6.00 | 0.667 | x: render 1905 → 690 at screen 540; y: render 1740 at screen 1430 | easeInOutSine | defocus 12 px |
| 4 | 8.80 → 12.00 | 0.33 → 0.52 | (1603,1560)→(540,960) ⇒ (2250,1350)→(540,960) | easeInOutSine | defocus 20 px |

## 3 · H50 crop gate (council must-fix 2): **PASS, no re-render needed**

- Requirement: the baby-figure ECU at 1080w with ≤1.5× upscale.
- Result: the ECU at s 1.18 is the largest frame the safe zones allow (hat top at y 498 under the band, name bottom at y 1436). That is 1.18× the render, or ≈1.25× the native clipart. The limit comes from the safe zones, not from pixels.
- At the 1.5× ceiling the stack would be 1193 px tall. The hat would then go under the caption band or the name would drop to y≈1690, so 1.5× is not usable for layout reasons anyway.
- If the stricter 65% line holds for names (risk R1), the ECU drops to s 0.94: the figure is 44% of the width and "Mateo" is 187 px. It still reads as a close on one figure.
- Re-rendering larger would not add detail. The figure cliparts top out at 800 px, and only the vector names and year would get sharper.

## 4 · O5 · Frame-1 pack + thumbnail

| | Arm A · H46 | Arm B · H50 |
|---|---|---|
| Frame 0 picture | Whole K06 ornament on the lit branch at 70% width (s 0.284). Red Santa hats and the big wooden "2026" against dark green needles and warm bokeh. Camera already moving in | Printed baby Mateo alone, large: Santa hat, bottle, "Mateo". Warm bokeh above the hat. No other figure readable |
| Pattern interrupt | Motion on frame 0 (fast push) + saturated red/wood against dark green | Unusual scale (ECU of a printed character), then the snap pull-back |
| The one surprise (≤2s) | The push lands on a **baby** at the end of the ledge (≈1.6–1.8s) | The baby turns out to sit on a family ornament with 3 others + 2026 (0.25–1.0s, sync hit) |
| Caption on frame 0 | "First Christmas as four." in the K06 band | "The newest one / on the ledge." in the K06 band |
| Distinct from the other arm | WS-ish whole ornament vs ECU one figure; push-in vs pull-back (03 accepts this "weak pair") | — |
| Frame-1 vs round (E16) | Setting "ornament on a tree" is also the shared end card's (K02 family, different ornament). Different cast, framing and palette weight; 07 checks it | ECU of a printed figure: no other concept opens on this |
| Source file | `ads/MJ4U-133-C0/K06/frame1/K06-A-f0.png` (export at Gate C) | `…/K06/frame1/K06-B-f0.png` |

**Thumbnail still (one, shared by both arms so it doesn't add a variable):** the K06-3 end frame. The whole ornament hangs on the branch at ≈60% width, all four names and 2026 visible, warm tree around it, no caption. Export as `…/K06/frame1/K06-thumb.png` at 1080×1920 and as a 4:5 crop.

## 5 · Known risks (for 07 and the owner)

- **R1, S1 candidate: E39 conflicts with E57/E60 for "Dad" (and "Mom").**
  - A 3-letter name needs s ≥ 0.855 to reach 100 px.
  - Keeping the figure's hat below the caption band (y 480) and the name above the 65% line (y 1248) caps Dad at s 0.52, which is 61 px.
  - The plan's default lets names sit at y ≤ 1440, about 75% down, inside Meta's Reels lower zone but with none of our text there. That gives s 0.667: Mom 101 px, **Dad 78 px**.
  - Needs a ruling on one of two options: (a) accept ≥75 px or a letter height of ≥44 px for 3-letter names, or (b) allow the band over Dad's hat tip and his name at about 75%, which gets s 0.855.
  - This affects every concept with "Dad" or "Mom" printed, so it is round-wide.
- **R2.** Names at y 1386–1430 in beat 2 sit inside the Reels bottom-35% UI area. On Reels placements the ad's primary text overlay may cover them. 07 should check with Meta's safe-zone overlay.
- **R3, arm B rule 8.** The body opens on Sofia under "The newest one on the ledge". This is mitigated by keeping Mateo visible at the right edge of the 2.00 frame. 07 cold read.
- **R4, arm A.** A-1 ends at s 0.52 on Mateo, then beat 2 opens at s 0.667 on Sofia: the same object at a similar scale, which may feel like a jump cut. The background also changes from a sharp tree to defocused, which helps. A-1 and beat 4 both push toward Mateo, but they differ in background, start size and speed.
- **R5, wording to 04.** "2026 coming into frame below them" (beat 3): in 9:16 the year is visible from the start of the shot. The pull-back reveals the branch and tree, not the year. Nothing changes on screen unless 04 wants the start tighter.
- **R6.** V3, V5a and V5b: generated ornaments can spin (K01 test). Use only the face-on window, and track the real render over it. V5a has fingertip roto on the hanger tab.
- **R7.** Beat 5 has four people including an infant, and 5b has a pointing hand. Best-of-4. Fallback for 5b if 8 takes fail: Sofia's arm is already pointing at Mateo at frame 0 and only her head turns to the ornament. That keeps the same meaning, but 04 would need to confirm it.
- **R8.** Seedance at 720p is upscaled 1.5× for 1080 delivery, so faces in 5a/5b may soften. 1080p is optional; its cost is not yet verified.
- **R9.** Live Santa hats: 05 decided **none** (hair is a stable feature, hats drift, and sweaters carry the print-to-live match). The owner can overrule at Gate B.
