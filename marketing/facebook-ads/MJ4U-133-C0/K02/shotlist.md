# MJ4U-133-K02 · shot list (role 05, O1 + O5) · "Dad said don't get him anything"

Planning pass, 2026-11-25. No generation run. Authority for words and timing: `K02/script.md` (Gate A approved, incl. ruling 2: "his idea" = one 2.9s shot with an in-camera push).
Ads: `MJ4U-133_C0_K02X1-H61` (arm A) and `-H63` (arm B). Body (2.00–20.00) is byte-identical in both (E13); only shot B1 differs.
Media for this concept: `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K02/` (create on first asset).
Product truth: `renders/MJ4U-133-K02-render.png` (3185×3000, transparent) is the only printed face shipped in beats 1–5. Turntable `turntable/K02/K02-34left.jpg`, `K02-34right.jpg` gives the body only (E37 amended).

## Ad-wide decisions (05)

| Item | Decision | Why |
|---|---|---|
| Caption band (9:16) | **Top band, y 270–430 px** (centre ≈350), 6% side margins, fixed for every caption in both ads (E58). 4:5: y 60–220 of 1350. | Beat 4 must show the names at ≥100 px (E39). At that scale the ornament fills the frame from y≈165 to the bottom, so a lower band would cover the names or the year (E60). Above the hats is the only clear band. All shots therefore keep faces and the ornament below y 450. |
| 4:5 path | Generate 9:16; key action inside y 285–1635 (the centred 4:5 crop) except beat 4, which has its own 4:5 move (below). | Round-wide rule 9. |
| Light / world | Christmas morning. Daylight from a window **off-screen camera-left**, cool-neutral; the tree's small warm lights soft in the background. K02's room: dark green velvet armchair, oak side table, cream walls. Kitchen (H63 only): pale oak table, daylight from off-screen top of frame. | One light logic for continuity; distinct from K01's grandparents' room (scene ledger: different cast, setting, palette). |
| Live hats | **Kids wear Santa hats in every shot** (match the print, fastest muted "that's them" read in beat 4). **Jacob is bareheaded, buzz cut** (the personalizer value; the print hides it under the hat). | Script conflict 4 (05 decides). The hat is an accessory, not an E44 trait. |
| Ornament size | **5 in** variant (longest side 12.7 cm; design is near-square, ~12.4 × 12.7 cm incl. hanger tab). Scale anchor in `refs/REFS-PLAN.md`. | E41. |
| Ornament face | Every generated shot carries a **placeholder** face (from the turntable). 06 replaces it with the K02 render by planar (corner-pin) tracking. No shipped frame shows generated figures, names or year (E37). | E37 amended. |
| Free-hang | The ornament faces camera in every used frame. No used window contains a free-hanging ornament without a hand on it, except ≤0.3s at the end of B5b; any sway is added in post on the 2D layer. | RENDERS.md K01 test (spin = FAIL). |

## Summary

| shot_id | tc | dur | serves (caption on screen) | regime | size / angle | move (ONE) | source | gen? |
|---|---|---|---|---|---|---|---|---|
| K02-H61-B1 | 0.00–2.00 | 2.0 | "He asked for nothing / this Christmas." | energy | MCU, eye level, box foreground low-left | push-in, fast-to-slow, MS→MCU | GEN-VIDEO from image first frame | yes |
| K02-H63-B1 | 0.00–2.00 | 2.0 | "He wrote one thing / on his list." (from 0.30) | energy | CU top-down (90°) | push-in in post 100→110% | GEN-VIDEO (locked-off) + post push + composited lettering | yes |
| K02-B2 | 2.00–4.60 | 2.6 | hook caption to 3.20, then "The kids didn't listen." | energy | MS, slightly low, OTS past Kobe | slow push-in | GEN-VIDEO from image first frame | yes |
| K02-B3 | 4.60–8.80 | 4.2 | "The kids didn't listen." to 6.00, then "He tried to look / unimpressed." | energy | CU face, eye level | slow push-in to his face | GEN-VIDEO from image first frame | yes |
| K02-B4 | 8.80–12.00 | 3.2 | "Every one of them. / Even Bailey and Luna." | stability | ECU insert, frontal | pan L→R along the ledge | STILL+MOVE (real render) | no |
| K02-B5a | 12.00–14.60 | 2.6 | "He pulled them in." (from 12.50) | energy | MWS, eye level, armchair | slow pull-back | GEN-VIDEO from image first frame | yes |
| K02-B5b | 14.60–17.50 | 2.9 | "Front and center. / His idea." (to 17.00) | energy→stability | MS → CU (push ends on hand + ornament) | push-in, steady, centred on the ornament | GEN-VIDEO from image first frame | yes |
| K02-B6 | 17.50–20.00 | 2.5 | end card "Personalize yours" + store | stability | shared plate | shared push-in | shared end card (Producer/06) | no (shared) |

Rhythm check: 2.0 · 2.6 · 4.2 · 3.2 · 2.6 · 2.9 · 2.5, no adjacent equal (E32). Sizes: MCU or top-down CU → MS → CU → ECU → MWS → MS→CU → plate, no adjacent equal; every beat has a scale jump. All cuts hard (E30), including H63 kitchen → living room at 2.00. Cut rate 6 cuts / 20s = 0.30/s (E33 report).
**Frame-1 interrupt:** H61 = camera already pushing on frame 1 + kids' hands thrusting the box in from frame edge; H63 = text-first top-down sheet + the box sliding in. **The one surprise in the first 2s:** H61 = his palm snaps up at 0.3s ("no"); H63 = the gift lands right under "NOTHING".

## Per-shot detail

### K02-H61-B1 · 0.00–2.00 · arm A only
- **serves:** "He asked for nothing / this Christmas." (0.00–3.20). Picture: a gift is offered, he refuses.
- **size/angle:** MCU of Jacob seated in the armchair, eye level, 50 mm feel; open kraft box low-left foreground, ornament face-up inside at ~1/3 frame width (≈360 px), its centre at about x 330, y 1050.
- **camera_move:** push-in (dolly in), starts on frame 1, fast-to-slow ease, MS → MCU, ends with his face at y 480–800.
- **subject + action:** Jacob sits back in the armchair, right hand holding the cocoa mug at chest height. **One action:** at ~0.3s his left hand lifts off the armrest to chest height, palm toward the box, fingers up, elbow bent at his side; head tilts back slightly, eyebrows raised ("no thanks"). Kobe's two hands (green cuffs) enter from frame bottom-left holding the box flat, level, at Jacob's knee height. Mary's and Susan's Santa-hat pompoms and shoulders soft at the left frame edge (faces out of frame or soft).
- **source_type:** GEN-VIDEO, image first frame (brief `B-H61-FF`, `B-H61-VID`).
- **refs_required:** first frame → composition · Jacob front + ¾ → character · K02-34left → product body · scale plate → scale.
- **text_to_composite:** ornament face = K02 render, planar-tracked into the box (names not legible at this size; Santa hats + top of "2026" read). No other text.
- **continuity:** Jacob bareheaded, buzz cut, circle glasses, dark Fair Isle sweater, red lounge trousers; cocoa with whipped cream in right hand; box open, no lid, kraft, tissue under the ornament.
- **takes:** 3 first frames → 1 selected → 3 video takes, 5s each, 720p.
- **acceptance:** product VS2 at frame 0.00 and identifiable by 1.0s (E3); palm reads as a polite "no" at chest height, never at the lens; cocoa stays upright; box stays level, ornament stays face-up and still inside; ≤3 sharp faces (Jacob only sharp).
- **usable window:** take 0.0–2.0 expected (onset at 0.3 is in the clip); verify.
- **cut_in / cut_out:** ad start / hard cut to B2.

### K02-H63-B1 · 0.00–2.00 · arm B only
- **serves:** "He wrote one thing / on his list." (0.30–3.20). Picture: Dad's list says NOTHING; the gift lands next to it.
- **size/angle:** top-down CU (camera straight down), kitchen table. Sheet fills the centre; lettering y 560–880; box lands y 930–1240, x 300–780, never over the lettering.
- **camera_move:** generated locked-off; the move is a **post push-in 100→110%**, linear-to-ease-out, centred on x 540, y 900, frames 0–60 (so the composited lettering needs no track).
- **subject + action:** **One action:** Kobe's right hand (green cuff, kid-sized) slides the open box from the bottom frame edge up onto the sheet below the lettering, then lifts away to the bottom edge. Box edge visible at frame 0.00 (VS1); ornament fully in by ~0.5s (VS2). The table holds only the sheet, a pen beside it, and the box (03 §1: no mug in this frame).
- **source_type:** GEN-VIDEO (locked-off, image first frame) + MOTION-GFX lettering composite (brief `B-H63-FF`, `B-H63-VID`).
- **refs_required:** first frame (blank sheet, box at the bottom edge) → composition · Kobe hands view → character (cuff) · K02 render or flat turntable front → product body seen from above.
- **text_to_composite:** **"DAD'S LIST:"** line 1, **"1. NOTHING"** line 2, "NOTHING" underlined twice. Real lettering made in PIL with an adult handwriting font (blue ballpoint, slight per-letter jitter, multiply blend on the paper) or, better and free, a phone photo of the line handwritten by the owner on white paper; position on the sheet x 250–830, y 560–880 (9:16 at 100%). Legible from 0.00 to ≥1.0s and never covered (fix 3). Ornament face = K02 render, 2D-tracked (top-down, translation + small rotation only).
- **continuity:** kitchen is the only non-living-room set; hard cut at 2.00 is a time/place jump (allowed, E30).
- **takes:** 2 first frames → 1; 2 video takes, 5s, 720p (low-risk single hand slide).
- **acceptance:** the sheet surface stays blank in the generated clip (any generated scribble = reject; the composite needs a clean paper); hand has five fingers and kid proportions; box slides flat, without tipping; ornament face-up the whole time.
- **cut_in / cut_out:** ad start / hard cut to B2.

### K02-B2 · 2.00–4.60 · both ads (shared body)
- **serves:** hook caption to 3.20, then "The kids didn't listen." (3.20–6.00). Picture: the kids keep offering; he gives in and takes it.
- **size/angle:** MS, slightly low (chair height), over Kobe's right shoulder (Kobe soft, back to camera: curls, Santa hat, green sweater, arms forward holding the box). Mary stands left of the chair, Susan right, both watching the box. Jacob centre, y 480–1200.
- **camera_move:** slow push-in toward Jacob, linear-ease, ~8% scale over the window.
- **subject + action:** Jacob: **one action chain written as one motion:** his shoulders rise and drop in a big sigh, and with that motion his right hand sets the mug on the side table at the right frame edge, then both hands come forward and close on the box's sides (~4.0s in the edit). Kobe's arms stay extended, holding the box flat at Jacob's chest height until Jacob's hands close on it. Mary and Susan stand still, hands at their sides, smiling. Box stays flat and open; the ornament stays face-up, no lid, no unwrapping.
- **source_type:** GEN-VIDEO, image first frame (`B-B2-FF`, `B-B2-VID`).
- **refs_required:** first frame → composition · Jacob front → character · Mary front → character · Susan front → character · K02-34right → product body. (Kobe from behind is carried by the first frame.)
- **text_to_composite:** ornament face = K02 render, corner-pin tracked (oblique, moving box). Not legible as names; reads as a family ornament (RV3).
- **continuity:** same armchair, mug and wardrobe as H61; first body frame shows nothing that contradicts either hook caption (rule 8): no list, no wrapping.
- **takes:** 3 first frames; **4 video takes**, 5s, 720p.
- **acceptance:** exactly one hand-off; the mug ends on the table, upright; ≤3 sharp faces (Jacob, Mary, Susan); Kobe's face never turns to camera; box never tilts past ~20° from flat.
- **risk / fallback:** three motions in 2.6s is the highest physical risk in K02. If 4 takes fail: first frame with the mug already on the table and his hand just leaving it, action = both hands take the box. That changes what is seen (the set-down) → **needs 04's nod before use.**
- **cut_in / cut_out:** hard / hard to B3.

### K02-B3 · 4.60–8.80
- **serves:** "The kids didn't listen." to 6.00, then "He tried to look / unimpressed." (6.00–8.80). Picture: he fights a grin and loses.
- **size/angle:** CU on Jacob's face and upper chest, eye level, 85 mm feel; the box held at the bottom of frame (y ≥1150 at start, so its top edge sits in frame).
- **camera_move:** slow push-in to his face, ease-in-out, CU → tighter CU, ending with the eyes at y ≈ 620.
- **subject + action:** **one primary action = the expression arc:** eyes lower to the box, eyebrows lift, lips press together and the corners twitch, then the grin breaks fully by ~1.9s into the window (≈6.5s in the edit), cheeks lift, eyes crinkle behind the circle glasses. **End of the window (~8.0s):** both hands lift the ornament flat out of the box to just below his chin, face toward camera, held by its side edges with thumbs on the front rim (not by the hanger).
- **source_type:** GEN-VIDEO, image first frame (`B-B3-FF`, `B-B3-VID`).
- **refs_required:** first frame → composition · Jacob front, ¾ and smile expression → character · K02-34left → product body.
- **text_to_composite:** ornament face = K02 render, corner-pin tracked as it rises (rotation toward camera).
- **continuity:** glasses circle, wire-thin, black; beard full, grey-brown; sweater dark Fair Isle; box kraft.
- **takes:** 3 first frames; 3 video takes, **6s**, 720p.
- **acceptance:** muted read = delight, never annoyance (grin visible by 6.5s); thumbs on the rim, never covering the printed figures; the ornament rises flat and stays rigid (no bending); five fingers per hand.
- **risk / fallback:** if the lift fails in every take, end the window with the ornament still in the box at the frame bottom; B4 still reads as his POV. Changes what is seen → **needs 04's nod.**
- **cut_in / cut_out:** hard / hard to B4 (B4 reads as what he is holding).

### K02-B4 · 8.80–12.00 · PROOF (STILL+MOVE, no generation)
- **serves:** "Every one of them. / Even Bailey and Luna." Picture: all six members, by name.
- **source:** `renders/MJ4U-133-K02-render.png` at native resolution (E38). Background: a heavily defocused, darkened frame of the B3 keeper (his sweater and the room), so it reads as his POV. No hands composited (none needed: at this scale the ornament overflows the frame sides).
- **measured names on the v2 render (source px, re-measured 2026-11-25, 3185×3000, ornament bbox x 258–2578, y 0–2180):** Bailey x 468–636 (168) · Mary 828–978 (150) · Jacob 1175–1338 (163) · Kobe 1540–1676 (136) · Susan 1888–2036 (148) · Luna 2243–2376 (133); name row y ≈1060–1143. (v1 numbers superseded.)
- **move (9:16 1080×1920):** scale **0.60** (crop width 1800 source px → names 80–101 px wide, narrowest Luna 80, Kobe 82; E39 amended ≥75 px). Name row centre (src y 1100) at frame y ≈ 1190 (names y 1166–1216, above the 35% bottom zone); ornament top at frame y ≈ 530, hat tops ≈ 668, ornament bottom ≈ 1838, so the caption band (270–430) is clear. **Pan L→R:** source centre x **1158 → 1678** (constant y 1100; crop edge-to-edge of the ornament), ease-in-out (cubic), 8.80→12.00. Bailey–Susan in frame on the first frame; Luna fully in from about the midpoint, held to the cut. The year (src x 268–2560) is always ~¾ in frame; the full "2026" is read in B5b (ruling 2026-11-25 item 2). Moves first frame to last (E35). Grain and a slight warm grade to sit with B3.
- **4:5 move (1080×1350):** same scale 0.60 and pan; name row at y ≈ 905 of 1350, ornament top ≈ 245, band y 60–220 clear; the bottom quarter of the year is cropped (read in B5b).
- **text_to_composite:** none beyond the render itself (names, 2026 are the print).
- **acceptance:** every name exact and ≥100 px wide while it is the read, on ≥5 frames (E39); caption band never touches a face, name or the year (E60).
- **⚠ Conflict for 04 (not changed here):** the script says the pan "then settles on **2026**". At any scale where Luna and Kobe are ≥100 px, the year (≈2520 px source, 16× a name) can't fit the 1080 frame, so with one move the year is only ever partly in frame. Options: (a) **recommended:** the pan reads the names only; the full "2026" is read in B5b's end state (ornament large, centre frame, ~0.9s) and on the shared end card; (b) a single eased Ken-Burns path that widens to the whole ornament after Luna (≈11.0→12.0) — this is a pan plus a pull-out, which E35 counts as two moves, so it needs an owner waiver. 04 picks.
- **cut_in / cut_out:** hard (from his hands, B3) / hard to B5a.

### K02-B5a · 12.00–14.60
- **serves:** "He pulled them in." (12.50–14.60). Picture: Dad hugs all three kids; the dog pushes in. Family connection (E48).
- **size/angle:** MWS, eye level, the armchair centred; Jacob seated, kids pressed in from both sides and the front.
- **camera_move:** slow pull-back (dolly out), ease-out, MS → MWS, ending with Bailey's head in frame right.
- **subject + action:** start state (first frame): Mary and Susan already leaning on the chair's arms, Kobe kneeling at his knee. **One action (Jacob):** his left arm sweeps around Mary's and Susan's backs and draws all three against his chest; his right hand stays on his right knee holding the ornament flat, face to camera. Kids: laugh, shoulders shaking (one shared reaction). Kobe's face turns into Jacob's shoulder (back of his head to camera), so sharp faces = Jacob, Mary, Susan. **Bailey:** front paws and head already resting on the right armrest at the start and staying there, still, mouth closed (no jump, no lick).
- **source_type:** GEN-VIDEO, image first frame (`B-B5a-FF`, `B-B5a-VID`). Council: reserve headroom here.
- **refs_required:** first frame → composition · Jacob front → character · Mary front → character · Susan front → character · Bailey ¾ → character. (Ornament body carried by the first frame; ≤5 refs.)
- **text_to_composite:** ornament face = K02 render, corner-pin tracked on his knee (small, near-static).
- **continuity:** ornament out of the box now (box gone from frame); mug on the side table; Bailey white short coat, black nose, no collar tag text.
- **takes:** **4 first frames; 4 video takes**, 5s, 720p.
- **acceptance:** four humans with correct limb counts and no merged arms; Bailey stays still with paws on the armrest; the ornament stays still on his knee, face to camera; ≤3 sharp faces.
- **cut_in / cut_out:** hard / hard to B5b.

### K02-B5b · 14.60–17.50 · last story shot (rule 7)
- **serves:** "Front and center. / His idea." (14.60–17.00), and the shot holds to 17.50 with K02's own ornament in frame. Picture: Mary suggests a side branch; Dad points to the centre and hangs it there himself.
- **size/angle:** MS at the tree (Mary left, Jacob right, the tree centre-back), eye level; push ends in a CU of his hand and the ornament dead centre (ornament ≈ 60% frame width at the end, so the full "2026" is legible ≥0.9s).
- **camera_move:** push-in (dolly in), steady, ease-in-out, centred on the ornament, MS → CU (Gate A ruling 2: no cut).
- **subject + action:** start state (first frame, held poses that read in the first ~0.8s): Mary's right arm extended toward a low side branch at frame left; Jacob's left index finger pointing at the centre of the tree; his right hand holding the ornament on a centre branch by its lower edge, the gold cord already looped over the branch through the hole. **One action (Jacob):** his right fingers open and his hand lowers away below the ornament at the very end of the window. Mary: lowers her arm (secondary, slow). **Luna** sits under the tree, head tilted up, still.
- **source_type:** GEN-VIDEO, image first frame (`B-B5b-FF`, `B-B5b-VID`). K01 test precedent: hand + ornament hanging by the gold cord from a branch = PASS.
- **refs_required:** first frame → composition · Jacob front → character · Mary front → character · K02-34right → product body · Luna front → character.
- **text_to_composite:** ornament face = K02 render, corner-pin tracked through the push; optional sway (≤3°, 0.8 Hz damped) added in post on the 2D layer after his hand leaves.
- **continuity:** gold thin metallic cord; same tree as the room in B2–B5a (background lights); kids' hats on.
- **takes:** 3 first frames; **4 video takes**, 5s, 720p.
- **acceptance:** the ornament faces camera (±15°) in every used frame, no rotation; the cord runs through the hanger hole to one branch; at the end of the window his hand has left or is leaving; ≤0.3s of free hang in the used window; Luna stays seated; scale vs his hand matches the plate.
- **cut_in / cut_out:** hard / hard to the shared end card at 17.50.

### K02-B6 · 17.50–20.00 · shared end card
Not a K02 asset: the round's shared plate (hero on the tree, push-in, "Personalize yours" + store name), same frames in all 12 ads (E9). See risk R2 below about the hero vs the render.

## O5 · Frame-1 pack and thumbnail

| Arm | Frame 1 (0.00) | Onset | Product at 0.00 | Caption | Interrupt / surprise |
|---|---|---|---|---|---|
| A · H61 | MCU Jacob in the green armchair, cocoa in hand; open kraft box with the ornament face-up low-left, ~1/3 width, held by green-cuffed kid hands; two Santa-hat pompoms soft at the left edge | camera already pushing on frame 1; palm up at 0.3s | VS2, Santa hats + top of "2026" | "He asked for nothing / this Christmas." in the top band from 0.00 | surprise = the "no" palm against a gift |
| B · H63 | top-down kitchen table: sheet with "DAD'S LIST: / 1. NOTHING" (composited) centre; the box's edge at the bottom frame edge | post push from frame 1; box slides in at 0.3s (sync hit AU1) | VS1 at 0.00 → VS2 by ~0.5s | "He wrote one thing / on his list." from 0.30 | text-first + top-down angle; the gift lands under "NOTHING" |

Distinctness vs other concepts' frame 1 (ledger rule, ≥2 of setting / cast / framing / colour): H61 differs from K01's armchair opening in cast and colour (green velvet, daylight); H63 is the round's only top-down kitchen frame. Confirm against the other 05 shot lists when they land.

**Thumbnail still (one):** the B5b end state: Jacob's hand just below the ornament hanging dead centre on the tree, render composited at full sharpness, all six names and "2026" legible, no caption text burned in. Exported 9:16 and 4:5 from the keeper's last clean frame. Meta's auto-pick candidates (first, mid, last) are frame 1 of each arm, B4 and the shared end card, all truthful.

## Known risks (for 07 and the Producer)

- **R1 Skin tone, render vs hero (owner).** The re-exported render prints Mary, Kobe and Susan noticeably **lighter (tan)** than the hero file (brown, like Jacob); Susan's locs are shorter with gold cuffs on the render. Live casting must match the file shipped in beats 1–5 (E44), and the shared end card shows the hero 0.5s later. See `refs/REFS-PLAN.md` § Decision needed.
- **R2 End card shows the same family in a different version** (drinks, Susan's locs, kids' skin). Goes away if the neutral end-card render is made, or if the K02 render is re-exported to match the hero.
- **R3 Planar tracking on five moving shots** (H61, B2, B3, B5a, B5b). 06 needs a corner-pin tracker (OpenCV homography on the placeholder's corners). B3's lift (face rotating toward camera) and B5a (small, in the hug) are the hardest.
- **R4 B2 action density** (sigh + set mug down + take box in 2.6s) and **R5 B5a four-person hug**: up to 8 takes each, then the fallback (B2 fallback needs 04).
- **R6 B5b free-hang spin** after the hand leaves: cut before any rotation; sway in post only.
- **R7 B4 year read** (conflict above, 04 decides).
