# MJ4U-133-K10 · shot list (role 05, O1 + O5) · planning pass

> 2026-11-25 · role 05 · planning only, nothing generated. Authority for words and timing: `K10/script.md` (Gate A). Rules applied: CRITERIA (E32, E35, E37 amended, E38–E41, E57–E60, E67), `council/verdict.md` round-wide rules 1–11, `05-BRIEF-FOR-VISUAL-DIRECTORS.md`.
> Ads: `MJ4U-133_C0_K10X1-H01_E0_v01` (shots B1A + B2…B8) and `MJ4U-133_C0_K10X1-H15_E0_v01` (shots B1B + B2…B8). Body B2–B8 is byte-identical in both (E13).
> Media root for this concept: `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K10/` (`refs/`, `ff/` first frames, `stills/`, `clips/`, `text/`).

## 0. Production method (applies to every shot below)

1. **Locked-off plates, camera move in post.** Every shot that carries a composite (DECORATIONS lettering, the real ornament face, a printed-hat crop) or a post focus pull is generated with a **fixed camera**, composited, and then given its ONE camera move in the edit on the finished composite. The composite never has to be tracked against a camera move. This follows council rule 5 (DECORATIONS on a static flap, focus pulls in post) and our toolchain (PIL + ffmpeg, no planar tracker). Cost: these video prompts need `ACK-OPENMOVE` at the prompt guard (the opening move is real, just applied in post); the Producer explains this to the user. Only B3 moves in camera.
2. **Ornament face = real render, always.** `ads/renders/MJ4U-133-K10-render.png` (3185×3000, ornament 2720×2731 px inside it). The generator may draw the ornament body from `turntable/K10/` for scale, light, contact and hanging (E37 amended). Its face is a placeholder and is fully covered by the real render layer (opaque, same silhouette). Any generated figure, name or year that shows outside the render layer = reject.
3. **No free-hanging ornament in generated motion** (K01 test: it spins). Hanging shots (B1B, B6, B7) put the real render on its own 2D layer, sway added in post (±2°, pivot at the cord top, damped over ~1.5 s); the gold cord is drawn in post from the branch to the hanger hole.
4. **Caption band (K10, 9:16): upper band, y 285–475 px at 1080×1920** (two lines, E4 size). Reason: B5 is the only placement where names ≥100 px (E39), the year not under a caption (E60) and the safe zone (E57) can all hold; a lower band would sit on "2026" while the names are read. Every shot therefore keeps faces, printed figures, names and year **between y 480 and y 1248**. 4:5 band set by 06 per shot (constraints in §3). → flag to 06/Producer (§4, F6).
5. **9:16 generated with a 4:5-safe centre** (council rule 9): key content inside x 65–1015, y 480–1248, which sits inside the 4:5 window (y 285–1635).
6. **Generated video: Seedance 2.0 Fast, 720p, 5 s generation, trimmed to the verified window.** Delivered at 1080×1920 (E19 minimum); 720p keepers are upscaled once, never called 1440.

## 1. Summary (one row per shot)

| shot_id | tc (edit) | dur | serves (caption on screen) | regime | size / angle | camera_move (ONE) | source_type | takes |
|---|---|---|---|---|---|---|---|---|
| K10-B1A (H01 only) | 0.00–2.00 | 2.0 | "He hid one ornament in her decorations box." | energy | CU, slightly high | post push-in 100→106 %, from frame 0 | GEN-VIDEO (locked) + composites | 3 |
| K10-B1B (H15 only) | 0.00–2.00 | 2.0 | "Her childhood ornaments finally have company." | energy | CU, eye level, shallow | rack focus ornament → bauble, 0.3–0.9 s (post) | STILL+MOVE (layered still) | 3 stills |
| K10-B2 | 2.00–4.30 | 2.3 | hook caption to 3.2, then "Every ornament in there was only hers." | energy | WS, eye level | post pan right→left, 4 % of width | GEN-VIDEO (locked) + composites | 3 |
| K10-B3 | 4.30–6.40 | 2.1 | "Every ornament in there was only hers." | energy | CU hands, high | in-camera slow push-in | GEN-VIDEO + tracked soft composite | 3 |
| K10-B4 | 6.40–9.00 | 2.6 | "She found the box. He watched." | energy | MS over-the-shoulder | rack focus box → Daniel, 7.9–8.3 s (post) | GEN-VIDEO (locked, deep focus) + tracked composite | 3 |
| K10-B5 | 9.00–12.20 | 3.2 | "Daniel, Grace and Mochi. 2026." | stability | ECU insert, top-down | post pull-back, names row → full ornament | STILL+MOVE (real render on generated palm still) | 3 stills |
| K10-B6 | 12.20–14.80 | 2.6 | "She hung theirs first." (from 12.7) | stability→energy | MCU, eye level | post push-in 100→105 % | GEN-VIDEO (locked) + 2D ornament layer + sway | 3 |
| K10-B7 | 14.80–17.50 | 2.7 | "First Christmas as two. / Plus Mochi." | energy | MS-WS, high angle | post lateral drift left→right, 3 % of width | GEN-VIDEO (locked) + 2D ornament layer + sway | 4 (cap 8) |
| K10-B8 | 17.50–20.00 | 2.5 | end card "Personalize yours" | stability | shared plate | shared (06, round-wide) | shared end card, not a K10 asset | 0 |

Shot lengths in order: 2.0 / 2.3 / 2.1 / 2.6 / 3.2 / 2.6 / 2.7 / 2.5 s → no equal neighbours, every body shot 2–5 s (E32). Sizes in order (H01): CU → WS → CU → MS → ECU → MCU → MS-WS → end card; (H15): CU → WS → … Every adjacent pair differs by at least one size step; every beat is one shot, so each beat boundary is a scale jump. Moves in order: push / pan / push / rack / pull / push / drift / (06): no adjacent repeat. All cuts hard (E30); no dissolve anywhere, including the H15 time jump (the reset is carried by picture, §2 B2). Cut rate 7 cuts / 20 s = 0.35 cuts/s (E33 report).

## 2. Shot detail (all spec columns)

### K10-B1A · HOOK, ad H01 · 0.00–2.00
- **serves:** "He hid one ornament in her decorations box." (caption 0.0–3.2; it runs on over B2).
- **regime / size:** energy · CU, camera slightly high (~35° down), 35 mm feel.
- **camera_move:** post push-in on the composite, 100 % → 106 %, starts on frame 0, ease-out, ends centred on the kraft box as it settles. Generated plate is locked (ACK-OPENMOVE).
- **subject_action_in_space:** Daniel's two hands (green Fair Isle cuffs at the wrist edge of frame, gold band on his left ring finger) hold a small open kraft gift box from its two sides, thumbs on the outer rim, fingers under the base; box level, 10 cm above an open moving box. ONE action: from 0.3 s his hands lower the kraft box straight down into the moving box between two bundles wrapped in newspaper-free plain brown paper, and stop with the box resting in red tissue at ~1.2 s; hands stay on the box. The far flap of the moving box stands upright behind the contents, facing camera (DECORATIONS goes here). Ornament lies face-up in red tissue inside the kraft box, hanger tab toward the far side, ≈1/3 frame width at frame 0 (≈360 px), face visible to ≥1.5 s.
- **source_type:** GEN-VIDEO from an image first frame (rule 5 hands handling → best-of-N; rule 2 product in scene, body from turntable). Composites: real render (planar-tracked while the box lowers), DECORATIONS.
- **refs_required:** `ff/K10-B1A-ff.png` → first frame · `REF-D6 hands` → character (hands, cuff, ring) · `K10-34right.jpg` → product body (scale/edge) · `PROP-moving-box` → composition.
- **text_to_composite:** "DECORATIONS" (`text/DECORATIONS-marker.png`, black marker capitals) corner-pinned to the far upright flap, static plate; ornament face = `renders/MJ4U-133-K10-render.png`, tracked 4-corner over the placeholder 0.0–1.5 s, then held/occluded as the box settles. No other legible text (wrapping paper plain).
- **continuity:** Daniel = green Fair Isle cuff, gold band left ring finger, no watch. Daylight, window off-screen left (same light as B2: this is the same morning, before she opens it). Same moving box, flap and red tissue as B2–B4. Ornament scale: 5 in ≈ 1.5× his palm width.
- **takes / draft→final:** first frame 3 variants (2K) → 3 video takes 720p/5 s (final = draft resolution).
- **acceptance:** frame 0 already reads "family ornament in a gift box" (figures, hats, the 2026 shape; names unreadable by size ≈25 px, RV3); onset by 0.5 s; hands 5+5 fingers, no extra hand; box goes down, not sideways; the flap stays still (composite sits on it without slip); ornament never tilts past ~20° from face-up (track holds); green cuffs are men's knit cuffs.
- **cut_in / cut_out:** in = start of ad · out = hard cut at 2.00 to B2 (wide, she opens *that* box; the caption carries over and B2 pays it).

### K10-B1B · HOOK, ad H15 · 0.00–2.00 (flash-forward, evening)
- **serves:** "Her childhood ornaments finally have company." (caption 0.2–3.2).
- **regime / size:** energy · CU, eye level with the ornament, 85 mm feel, shallow depth.
- **camera_move:** rack focus (#033) from the new ornament (sharp at frame 0) to the old bauble on the next branch, 0.3 → 0.9 s, cubic ease-in-out; ornament ends ~6 px blur at 1080w, bauble sharp. Built in post on a deep-focus still split into 3 depth layers (ornament + its branch / bauble + its branch / background).
- **subject_action_in_space:** foreground left-of-centre: the real ornament hanging by its gold cord from a fir branch, face to camera, ≈1/3 frame width, centre at y ≈ 900. Next branch right and 10 cm behind: one old childhood bauble (worn, faded red glass, chipped silver cap, text-free), centre at y ≈ 760. Background, soft, upper right behind the tree (faces between y 520 and 720, clear of the band): Grace leaning her head on Daniel's shoulder beside a half-open moving box, warm lamp light. Still: no limb action; the motion is the focus pull plus a gentle post sway on the ornament layer (±1°).
- **source_type:** STILL+MOVE (generated deep-focus still; ornament body placeholder in the still for light and cord; real render layer over it).
- **refs_required:** `LOC-evening` → composition/light · `PROP-tree` → set · `PROP-baubles` → prop · `REF-G1 Grace front` → character · `REF-D1 Daniel front` → character · `K10-34left.jpg` → product body/scale.
- **text_to_composite:** ornament face = real render (static layer, sway in post); bauble text-free; no other text.
- **continuity:** same tiny tree as B2/B6/B7, now with a few baubles; **evening**: dark blue window off-screen left, warm 2700 K lamp off-screen right. Grace red sweater / Daniel green sweater as all day. No string lights on the tree in any shot.
- **takes:** 3 still variants (2K), pick 1.
- **acceptance:** ornament identifiable at frame 0 (VS2, ≈1/3 width); names unreadable (≈25 px); bauble has no text, logo or monogram; couple soft but on-model (hair, sweater colours); band zone y 285–475 holds no face; the background visibly differs from B2 on light (warm night vs cool day), tree state (decorated vs bare) and size (CU vs WS).
- **cut_in / cut_out:** in = start of ad · out = **hard cut at 2.00 to B2 = the visual reset** (daylight, wide, bare tree, unopened boxes).

### K10-B2 · STAKES 1 · 2.00–4.30 (body frame 1)
- **serves:** hook caption to 3.2 (either arm), then "Every ornament in there was only hers." (3.2–6.4).
- **regime / size:** energy · WS, eye level (camera ~1 m), 28 mm feel, deep focus.
- **camera_move:** post pan right→left, 4 % of frame width, linear-ease-in-out over 2.3 s, ending with Grace and the box on the left third.
- **subject_action_in_space:** small apartment living room, cool daylight from a window off-screen left. Right third: the same tiny tree (~120 cm, fir in a woven basket on the floor), **bare**. Background: moving boxes stacked two high against the wall, doorway at back right (empty). Centre-left: Grace kneels on the rug facing the DECORATIONS box (box side-on to camera at 30°), knees on the rug, left hand on the box's near edge. ONE action: her right hand lifts the near (folded) flap open and lays it back. The far flap is already upright and static (DECORATIONS). Inside, at the top, the kraft box under one fold of red tissue: one printed Santa hat and the box edge show.
- **source_type:** GEN-VIDEO (locked) from an image first frame + composites (DECORATIONS on the far static flap; printed Santa-hat crop + kraft edge).
- **refs_required:** `ff/K10-B2-ff.png` → first frame · `REF-G4 Grace full kneeling/seated` → character · `LOC-day` → composition/light · `PROP-tree` → set.
- **text_to_composite:** "DECORATIONS" (same file as B1A, perspective-matched, static) · Santa-hat crop `text/K10-hat-crop.png` (cut from the real render: Grace's hat) under the tissue fold. Nothing else legible (other boxes blank).
- **continuity:** same box/flap/tissue as B1A; tree bare, no lights; Grace red Fair Isle sweater, red-tartan pants, hair loose down her back, gold band; daylight cool-neutral (~5200 K). Mochi not in shot.
- **takes:** 3 first-frame variants → 3 video takes.
- **acceptance (incl. council rule 8):** **frame at 2.00 contradicts neither hook caption**: the DECORATIONS box is in frame and legible (pays H01), the tree is bare and the room un-unpacked so it reads as *earlier* than H15 (no ornament visible on the tree; no "alone" bauble on it). Flap with lettering never moves; she moves only the near flap; knees stay on the rug; no text appears on other boxes.
- **cut_in / cut_out:** in = hard cut from B1A/B1B · out = hard cut to B3 (WS → CU hands).

### K10-B3 · STAKES 2 · 4.30–6.40
- **serves:** "Every ornament in there was only hers."
- **regime / size:** energy · CU hands, high angle (looking down into the box), 50 mm feel.
- **camera_move:** in-camera slow push-in toward her hands (Seedance, one move), ends with the bauble centred.
- **subject_action_in_space:** Grace's hands above the open box, red Fair Isle cuffs at the frame edge. Two old childhood baubles already lie on the rug beside the box (frame left). ONE action: her right hand lifts one worn bauble (faded gold glass, text-free) up out of the tissue by its cap, palm under it, to chest height; her left hand rests on the box rim. Bottom third, soft: the kraft box edge and the printed Santa hat under the red tissue fold (she does not look at it).
- **source_type:** GEN-VIDEO (in-camera move) from an image first frame; the hat crop is 2D-tracked (position + scale only, blurred to match; small and soft, so track error is invisible).
- **refs_required:** `ff/K10-B3-ff.png` → first frame · `REF-G6 Grace hands` → character (hands, cuffs, ring) · `PROP-baubles` → prop.
- **text_to_composite:** Santa-hat crop (same file as B2), soft. Baubles text-free.
- **continuity:** daylight from left; gold band left ring finger; same tissue fold position as B2.
- **takes:** 3 first frames → 3 video takes.
- **acceptance:** 5 fingers per hand; bauble stays one rigid sphere (no morph, no second bauble appearing in hand); hat + box edge visible but soft in the bottom third the whole window; no text on baubles.
- **cut_in / cut_out:** hard in · hard out to B4.

### K10-B4 · TURN · 6.40–9.00
- **serves:** "She found the box. He watched." — "He watched" is paid by Daniel's face reading sharp ≈8.2–9.0 (E50).
- **07 ruling (2026-11-26):** first frame is mirrored (Grace foreground RIGHT, Daniel in the doorway back right as in B2/B6); accepted, not flipped. Read "left/right" below accordingly.
- **regime / size:** energy · MS over Grace's right shoulder, camera at her shoulder height, deep focus plate.
- **camera_move:** rack focus (#033) in post, box → Daniel, 7.9 → 8.3 s, cubic ease-in-out; before it Daniel ≈8 px blur, after it box ≈6 px blur. **No push** (E35, one move; see F2).
- **subject_action_in_space:** foreground left: back of Grace's head and right shoulder (hair, red sweater), kneeling at the box. Her left hand holds the fold of red tissue already lifted aside (pinched between thumb and fingers, held still at the box's left rim). ONE action: her right hand lifts the kraft box up out of the tissue to chest height, fingers on the box's sides below the rim, ornament face-up inside and unoccluded. Background, upper right, framed by the doorway (face at y ≈ 560–680): Daniel leans his left shoulder on the door frame, arms folded, still; at the end a small closed-mouth smile (cheeks lift).
- **source_type:** GEN-VIDEO (locked, deep focus) from an image first frame; ornament face composited with a 4-corner track (the box moves); focus pull via masks in post (Daniel's mask static: he does not move).
- **refs_required:** `ff/K10-B4-ff.png` → first frame · `REF-G3 Grace ¾ right` → character (back of head/hair) · `REF-D4 Daniel full standing` → character · `K10-34left.jpg` → product body/scale.
- **text_to_composite:** ornament face = real render, tracked, softened (names unreadable by size + focus, RV3).
- **continuity:** daylight left; Daniel green Fair Isle sweater, dark trousers, gold band; Grace's hair loose; same box, tissue.
- **takes:** 3 first frames → 3 video takes.
- **acceptance:** Daniel stays leaning (no walking, no arm unfold) so the static mask holds; box lifts vertically; no finger crosses the ornament face; face reads at 8.3–9.0 on ≥5 frames; Daniel matches cast (E44/E45: he = man in green).
- **cut_in / cut_out:** hard in · hard out to B5 (MS → ECU, the biggest scale jump in the ad).

### K10-B5 · PROOF · 9.00–12.20
- **serves:** "Daniel, Grace and Mochi. 2026." (9.0–12.2).
- **regime / size:** stability · ECU insert, top-down onto her open left palm (90°).
- **camera_move:** ONE post pull-back from the names row to the full ornament, cubic-bezier(0.70, 0, 0.30, 1) (slow start, settles), 3.2 s. Parameters in 1080×1920 output pixels, ornament-relative (06 maps them onto the composite still):
  - **start:** ornament displayed **1650 px wide** (names ≈115 px wide, E39), horizontal centre x = 540, names-row centre y = 1215 → hats top ≈ y 494, Daniel's name x ≈ 113–211, Mochi's ≈ 881–979; all three names inside the safe zone and readable together.
  - **end:** ornament **820 px wide**, top (hanger) at y = 480, centre x = 540 → names ≈ y 933–963, "2026" ≈ y 974–1245, whole ornament inside the safe zone.
  - names stay ≥100 px (ornament ≥1430 px) for ≈1.4 s; 06 measures and reports (E39 on ≥5 frames).
- **subject_action_in_space:** her left palm open and flat, fingers together, ornament lying flat on palm and fingers (5 in ≈ 1.5× palm width, overhanging both sides), her thumb alongside the left edge touching only the wood edge, never crossing the print. Red Fair Isle cuff at the bottom edge. Background: red tissue inside the open box, soft.
- **source_type:** STILL+MOVE (E38): generated still (palm + placeholder) at 4K, real render composited flat at native resolution.
- **refs_required:** `REF-G6 Grace hands` → character · `SCALE-palm` → scale anchor · `K10-34right.jpg` → product body (edge thickness) · `LOC-day` → light.
- **text_to_composite:** **"Daniel", "Grace", "Mochi", "2026" exist only as the real render** (exact; R23 read by eye on ≥5 frames).
- **continuity:** daylight from left (soft shadow of the ornament edge on her palm to the right); gold band on left ring finger visible at the end framing.
- **takes:** 3 still variants at 2K, keeper re-made at 4K.
- **acceptance:** E39 measured; caption band (y 285–475) covers only the hanger tab at the start and nothing at the end (E60); thumb never over print; 5 fingers; no generated print visible anywhere at the render's edges.
- **cut_in / cut_out:** hard in · hard out at 12.20 to B6 (caption gap 12.2–12.7, E56).

### K10-B6 · CONNECTION 1 (pivot) · 12.20–14.80
- **serves:** "She hung theirs first." (12.7–15.0; 12.2–12.7 no caption).
- **regime / size:** stability → energy · MCU, eye level with the ornament, 50 mm feel.
- **camera_move:** post push-in 100 → 105 %, ease-in-out, toward the ornament.
- **subject_action_in_space:** late-afternoon golden daylight from off-screen left. The tiny tree fills the lower right; the ornament hangs on a front branch, face to camera, ≈42 % frame width, centre y ≈ 1000 [superseded 2026-11-26 by 07 ruling 5: keep the render at the first frame's true-5-in size ≈23 % width; 42 % ≈ 13 in]: the first and only ornament on it. Grace stands just behind and left of the tree, facing camera at ¾ (face y ≈ 560–720). ONE action (Grace): her right hand, behind the ornament with fingertips on its back near the top, draws back and lowers to her side. ONE action (Daniel): from the doorway behind her right shoulder he takes one step in and stops behind her, soft. Ornament sway (post, on the real render layer) starts on her release.
- **source_type:** GEN-VIDEO (locked) from an image first frame with the ornament body placeholder (contact + scale); real render layer covers it fully (her hand is behind it, so no roto); cord drawn in post.
- **refs_required:** `ff/K10-B6-ff.png` → first frame · `REF-G2 Grace ¾ left` → character · `REF-D3 Daniel ¾ right` → character · `K10-34left.jpg` → product body.
- **text_to_composite:** ornament face = real render, sway layer.
- **continuity:** tree bare except this ornament (no baubles yet, no lights); golden light warmer than B2 (time passes, E52 warmth by the end); same sweaters.
- **takes:** 3 first frames → 3 video takes.
- **acceptance:** hand passes **behind** the ornament (never in front of its print); after release the placeholder may move, but nothing of it shows outside the render silhouette; Daniel's step = one step, no walk-through; 07 cold-reads the caption-vs-picture (script C6: release reads as "hung it").
- **cut_in / cut_out:** hard in · hard out to B7.

### K10-B7 · CONNECTION 2 · 14.80–17.50 (own-ornament shot to 17.5, council rule 7)
- **serves:** "First Christmas as two. / Plus Mochi." (15.0–17.5).
- **regime / size:** energy · MS-WS, high angle (camera ~2.1 m, 25° down), 35 mm feel, deep focus.
- **camera_move:** post lateral drift left → right, 3 % of frame width, linear-ease, ends with the ornament on the right third.
- **subject_action_in_space:** foreground right, sharp: the ornament hanging from the tree's top front branch, ≈30 % width, centre y ≈ 850 (2D layer, post sway ±1°). Mid-ground centre: Grace and Daniel by the tree, faces y ≈ 520–720. ONE action (Grace): she turns from the tree into Daniel's chest, her hands coming to rest flat on his chest. ONE action (Daniel): his arms close around her back, hands meeting at her lower back. Both then lower their gaze to Mochi; cheeks lift, eyes crinkle (closed-mouth smiles). ONE action (Mochi): seated on the rug at their feet (y ≈ 1000–1230), facing them, head tilts up toward them; tail lies on the rug with a gentle sweep. Mochi stays seated, all four paws on the floor.
- **source_type:** GEN-VIDEO (locked) from an image first frame **without** the ornament (no hand contact here); real render + cord composited in post. Council-flagged multi-body shot: best-of-N, budget reserve.
- **refs_required:** `ff/K10-B7-ff.png` → first frame · `REF-G1` + `REF-D1` → characters · `REF-M2 Mochi seated ¾` → character · `LOC-day` (golden variant via prompt) → light.
- **text_to_composite:** ornament face = real render (names may be legible here; allowed after 9 s).
- **continuity:** same golden light as B6; tree bare except our ornament; Mochi = red-and-white Pembroke, red collar, no hat; both gold bands.
- **takes:** 4 video takes planned, cap 8 (council rule 10). **Fallback after 8:** first frame already in the embrace; action reduced to "both lower their gaze to Mochi and smile"; Mochi still (head up).
- **acceptance:** ≤3 sharp faces (2 + dog) ✓; no jump, no standing up (Mochi); hug hands 5 fingers, no arms merging; no tears; ornament sharp in frame through 17.5 s.
- **cut_in / cut_out:** hard in · hard out at 17.50 to the shared end card.

### K10-B8 · CTA end card · 17.50–20.00
Shared round-wide plate (BRIEF ruling: hero ornament on the tree, slow push-in, "Personalize yours" + store name; or the neutral render if made). Built once by 06 for all 12 ads (E9). No K10 asset; K10's own ornament is in frame to 17.5 inside B7.

## 3. Composite and frame-safety map (for 06)
| shot | composites (file → position) | band check (y 285–475) | 4:5 note (E67) |
|---|---|---|---|
| B1A | DECORATIONS → far flap, static corner-pin · render → kraft box, tracked 0–1.5 s | ornament y 700–1060, clear | ornament fully inside y 285–1635 |
| B1B | render → foreground branch, sway layer · rack-focus masks | couple faces ≥ y 520 | keep bauble + ornament inside the crop |
| B2 | DECORATIONS → far flap · hat crop → box top | Grace's head ≈ y 700 | box + flap inside the crop |
| B3 | hat crop, 2D track, blurred | n/a (no face) | — |
| B4 | render → kraft box, 4-corner track, softened | Daniel's face y 560–680 | Daniel's face inside the crop |
| B5 | render flat on palm still | covers hanger tab only at start | **start framing crops the outer "2" and "6" of 2026 at both frame edges (needed for names ≥100 px); see F3** |
| B6 | render sway layer + drawn cord | faces y 560–720 | — |
| B7 | render sway layer + drawn cord | faces y 520–720 | Mochi (y ≤1230) inside the crop |

## 4. Flags back to 04 / owner (not changed here)
- **F1 · DECORATIONS placement (1A, B2).** The lettering sits on the **far flap, which stands upright and never moves**; in B2 Grace opens the **near** flap. The words and the shown action ("she opens the flap of the DECORATIONS box") are unchanged; only which flap. Needs 04 OK.
- **F2 · B4 camera.** Script: "slow push toward the box" + council's post focus shift box → Daniel. Two moves break E35, so B4's one move is the **rack focus**; no push. The tissue lift is shown **in progress at the cut** (her left hand already holds the fold aside) so the generated action is one hand-lift of the box. Needs 04 OK.
- **F3 · B5 move and E67.** Script: "slow pan Daniel → Grace → Mochi, settling on the full ornament". At names ≥100 px all three names fit in frame together, so the move is **one pull-back** from the names row to the full ornament (pan + settle would be two moves). Geometry forces the start framing to cut the outer digits of "2026" at the frame edges for ≈1.4 s; the end frame shows 2026 whole. 07 to rule whether E67 ("year on the crop edge") applies to this deliberate close-up; if it does, E39 and E67 cannot both hold at 1080 px wide for this layout.
- **F4 · Mochi's wag (B7).** Script "looks up and wags (no jump)". Planned as "head tilts up, tail sweeps gently on the rug, stays seated"; if the tail morphs, the wag is dropped and Mochi just looks up. Tell 04.
- **F5 · Casting (owner, at Gate B).** The print shows light skin + straight black hair for both. Planned cast: an East Asian-American couple, late 20s (matches the print and the hook cards' read; no other C0 concept casts East Asian, so it also varies the slate). Both wear plain gold wedding bands (first Christmas married, per the concept card). Owner can veto at Gate B.
- **F6 · Caption band (06/Producer).** K10 needs the **upper** band (y 285–475). If the round fixes one band position for all 12 ads (E4 "same treatment"), B5 must be re-planned smaller (names <100 px → E39 fail). Decide before 06 builds.
- **F7 · Names in 1A.** Card/script: "names below the rim". At ≈1/3 width the names are ≈25 px and unreadable by size, so no rim occlusion is staged. No change to the picture.

## 5. O5 · Frame-1 pack per hook arm + thumbnail

| | H01 (arm A, "the secret") | H15 (arm B, "it landed") |
|---|---|---|
| frame 0.00 | CU, slightly high: Daniel's green-cuffed hands hold the open kraft box, real ornament face-up in red tissue (≈1/3 width), DECORATIONS legible on the upright flap behind | CU: the real ornament hanging sharp on the fir branch (≈1/3 width), the old red bauble soft on the next branch, the couple soft and warm behind |
| pattern interrupt | unusual high angle + motion from frame 0 (post push) + hands drop at 0.3 s | rack focus at 0.3 s pulls the eye off the product onto the worn bauble |
| designated surprise (≤2 s) | the gift goes *into her* DECORATIONS box (hiding, not giving) | the old bauble is clearly a child's and clearly hers, beside a family ornament |
| palette / light | kraft + cardboard browns, red tissue, cool daylight | warm 2700 K lamp, deep green fir, red glass, night window |
| E15 (arms differ by picture) | subject hands+box vs tree; framing high CU vs eye-level CU; onset hand drop vs rack focus | ✓ |
| E16 vs other C0 concepts | **risk:** three hooks in the round open on hands + a kraft box (K01 H76 lid, K04 H33, K10 H01). K10 H01 differs on setting (moving box, apartment), cast (young man's green Fair Isle cuffs), framing (box lowered *into* a larger box, high angle). 07 to confirm ≥2 attributes against the other 05 shot lists. | tree + ornament frames also open K06 H46 and K13 H17; H15 differs on light (night lamp), the second object (old bauble) and the soft couple. 07 to confirm. |
| deliverables | `MJ4U-133-C0/K10/frame1/K10-H01-f0.png` (composited frame 0) | `…/K10-H15-f0.png` |

Scene ledger: `_ledgers/scene-ledger.csv` is empty (no MJ4U-133 ad has shipped), so no reuse to log. O6 rows are written at ship (one per shot above; B2–B8 logged once as shared between the two K10 ads).

**Thumbnail still (one):** B7 keeper frame at ≈17.3 s, composited (Grace in Daniel's arms looking down at Mochi, the real ornament sharp foreground right), no text. It shows the product, the family and the dog in one frame. Alternate: B5 end frame (full ornament in her palm). File: `…/K10/frame1/K10-thumb.png`.
