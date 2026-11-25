# K10 · scene briefs (after Gate B only) · template §4.1

One block per generated asset. First frames (`-ff`) on Nano Banana Pro Edit, 9:16, 2K, 4:5-safe centre. Video on Seedance 2.0 Fast (first frame = the `-ff` keeper as @Image 1, ≤3 more refs), 720p, 5 s, trimmed to the verified window. Adapters: `image-prompt-method.md`, `seedance-prompt-method.md`, `image-to-video-prompt-method.md`; prompt guard applies.
**Guard note:** video briefs marked `CAMERA: fixed (move in post)` need `ACK-OPENMOVE` in the commandId. Reason, to be told to the user: the shot's one move is applied in the edit to the composited frame so DECORATIONS, the real ornament face and the focus pulls never need tracking against a camera move (council rule 5).
Common to every block: the ornament's generated face is a placeholder (E37); the real render replaces it. Named light sources stay off-screen. Positions are in 1080×1920 output pixels.

---

## K10-B1A (H01 hook)

```
BRIEF  K10-B1A-ff  v1     output: still   regime: energy
PURPOSE      "He hid one ornament in her decorations box." — frame 0: his hands hold the open gift box with the ornament, above her DECORATIONS box.
START STATE  [REF-D6 → character: hands, cuffs, ring] [PROP-kraft → product in box + scale] [PROP-moving-box → composition] [LOC-day → light/style]
SUBJECTS     <Daniel> hands (green Fair Isle cuffs, gold band) · <Kraft box> with the ornament · <Box>
FRAMING      CU, camera ~35° down from above-front, 35 mm, 9:16; kraft box centred at y≈880, ornament ≈360 px wide; far flap of <Box> upright behind,
             spanning y≈560–760; nothing important above y 480
CAMERA       n/a (still)
ACTION       his two hands hold <Kraft box> level by its two sides, thumbs on the outer rim, fingers under the base, box 10 cm above the open <Box>;
             inside <Box>: red tissue and two bundles wrapped in plain brown paper, a gap between them under the kraft box
SECONDARY    n/a
LIGHT        cool daylight from a window off-screen left, soft shadow of his hands falling right
SHOTS        n/a
MUST NOT CHANGE   ornament face-up, flat single sheet, hanger tab toward the far side · far flap a clean blank rectangle · 5+5 fingers · gold band left ring finger
TEXT         none generated. Composited later: "DECORATIONS" (text/DECORATIONS-marker.png) on the far flap; ornament face = renders/MJ4U-133-K10-render.png
DURATION     n/a
DRAFT/FINAL  3 variants · 2K = final · v1
ACCEPTANCE   frame reads "gift box with a family ornament" before compositing; flap frontal enough for a corner-pin; cuffs read as a man's
```

```
BRIEF  K10-B1A  v1        output: video   regime: energy
PURPOSE      Same; onset at 0.3 s = his hands lower the box in.
START STATE  [K10-B1A-ff → first frame] [REF-D6 → character hands] [P-34R → product body]
SUBJECTS     <Daniel> hands · <Kraft box> (ornament inside)
FRAMING      as the first frame
CAMERA       fixed (move in post: push-in 100→106 % from frame 0, ease-out) — ACK-OPENMOVE
ACTION       Shot 1: his hands lower <Kraft box> slowly straight down into the gap between the wrapped bundles and stop with it resting in the
             red tissue; his fingers stay on the box sides; the box stays level
SECONDARY    the red tissue flexes slightly where the box settles
LIGHT        unchanged daylight from off-screen left
SHOTS        Shot 1 only (one continuous shot)
MUST NOT CHANGE   ornament stays face-up and flat in the box, same size · far flap stays perfectly still · hands keep five fingers each ·
             no third hand · box keeps its shape
TEXT         no legible text in frame (composites added in post)
DURATION     generate 5 s · edit window 2.0 s (onset must fall in 0.2–0.4 s of the window)
DRAFT/FINAL  3 takes · 720p = final · v1
ACCEPTANCE   placeholder face trackable 0–1.5 s (no fingers over it); box motion vertical; flap static to the pixel (composite holds); ≥5 frames checked
```

## K10-B1B (H15 hook)

```
BRIEF  K10-B1B  v1        output: still   regime: energy
PURPOSE      "Her childhood ornaments finally have company." — the family ornament hanging beside her old bauble, the couple behind, that evening.
START STATE  [LOC-evening → composition/light] [SCALE-branch → product on branch + scale] [PROP-baubles → prop] [REF-G1 → character] [REF-D1 → character]
SUBJECTS     <Ornament> · one faded-red <Baubles> bauble · <Grace> · <Daniel>
FRAMING      CU, eye level with the ornament, 85 mm, 9:16, **deep focus (everything sharp; blur added in post)**; ornament left of centre, centre y≈900,
             ≈360 px wide; bauble on the next branch right, centre y≈760; couple behind the tree upper right, faces y≈520–720
CAMERA       n/a (still; rack focus built in post)
ACTION       ornament hangs by its thin gold cord, face to camera; Grace rests her head on Daniel's shoulder, her right hand on his chest, his right arm
             around her shoulders, both looking at the tree; a half-open moving box beside them on the floor
SECONDARY    n/a
LIGHT        warm lamp light from off-screen right, deep blue night ambient from off-screen left
SHOTS        n/a
MUST NOT CHANGE   ornament flat single sheet facing camera · bauble plain with no text · tree has no string lights · faces clear of y<480
TEXT         none generated; ornament face replaced by the real render
DURATION     n/a (still; edit window 2.0 s)
DRAFT/FINAL  3 variants · 2K = final · v1
ACCEPTANCE   three depth planes separable by mask (ornament / bauble / background); couple on-model; reads as night
```

## K10-B2 (STAKES 1, body frame 1, visual reset)

```
BRIEF  K10-B2-ff  v1      output: still   regime: energy
PURPOSE      First body frame: daylight, wide, the bare tree, boxes not unpacked; Grace at the DECORATIONS box. Pays H01, resets H15.
START STATE  [LOC-day → composition/light] [REF-G4 → character, kneeling pose] [PROP-moving-box → prop] [PROP-tree → set]
SUBJECTS     <Grace> · <Box> · <Tree>
FRAMING      WS, eye level (1 m), 28 mm, 9:16; <Box> centre-left at y≈1000, side-on at 30°, far flap facing camera; <Tree> right third; Grace's head y≈700
CAMERA       n/a (still)
ACTION       Grace kneels on the rug facing <Box>, knees on the rug, left hand resting on the box's near edge, right hand on the folded near flap;
             far flap upright; top of the contents: a red tissue fold with a small kraft box edge peeking out
SECONDARY    n/a
LIGHT        cool-neutral daylight from a window off-screen left
SHOTS        n/a
MUST NOT CHANGE   tree bare, no lights · far flap blank · every box plain · Grace's hair loose, red sweater, tartan trousers, gold band
TEXT         none generated. Composited: "DECORATIONS" on the far flap; Santa-hat crop (text/K10-hat-crop.png) at the tissue fold
DURATION     n/a
DRAFT/FINAL  3 variants · 2K · v1
ACCEPTANCE   contrasts with B1B on light, size and tree state; no ornament visible on the tree
```

```
BRIEF  K10-B2  v1         output: video   regime: energy
PURPOSE      Same; she opens the near flap.
START STATE  [K10-B2-ff → first frame] [REF-G1 → character]
SUBJECTS     <Grace> · <Box>
FRAMING      as the first frame
CAMERA       fixed (move in post: pan right→left 4 % of width) — ACK-OPENMOVE
ACTION       Shot 1: her right hand lifts the near flap of <Box> and lays it back over the box's near side; her left hand stays on the near edge;
             her knees stay on the rug; her head tilts down toward the box
SECONDARY    loose hair moves slightly with her head
LIGHT        unchanged daylight
SHOTS        Shot 1 only
MUST NOT CHANGE   far flap stays perfectly still and upright · Grace stays kneeling · tree stays bare · other boxes unchanged
TEXT         no legible text in frame
DURATION     generate 5 s · edit window 2.3 s
DRAFT/FINAL  3 takes · 720p · v1
ACCEPTANCE   flap action complete inside the window; far flap static (composite holds); identity on-model on ≥5 frames
```

## K10-B3 (STAKES 2)

```
BRIEF  K10-B3-ff  v1      output: still   regime: energy
PURPOSE      "Every ornament in there was only hers." — her hands with her old baubles; the hidden box soft at the bottom.
START STATE  [REF-G6 → character hands] [PROP-baubles → prop] [PROP-moving-box → prop] [LOC-day → light]
SUBJECTS     <Grace> hands · <Baubles> · <Box>
FRAMING      CU, high angle looking into the box, 50 mm, 9:16; her hands centre y≈800; kraft-box edge + tissue fold in the bottom third (y≈1050–1240), soft
CAMERA       n/a
ACTION       her right hand holds one faded-gold bauble by its cap, palm under it, just above the tissue; her left hand rests on the box's near rim;
             two other baubles lie on the rug at frame left
SECONDARY    n/a
LIGHT        daylight from off-screen left
SHOTS        n/a
MUST NOT CHANGE   5 fingers each · gold band left ring finger · baubles text-free · red cuffs at frame edges
TEXT         none generated; hat crop composited at the tissue fold
DURATION     n/a
DRAFT/FINAL  3 variants · 2K · v1
ACCEPTANCE   reads as "her own old ornaments"; space for the hat crop at the fold
```

```
BRIEF  K10-B3  v1         output: video   regime: energy
PURPOSE      Same; she lifts one bauble out.
START STATE  [K10-B3-ff → first frame] [REF-G6 → character hands]
SUBJECTS     <Grace> hands · the faded-gold bauble
FRAMING      as the first frame
CAMERA       slow push-in toward her right hand, ending with the bauble centred
ACTION       Shot 1: slow push-in. Her right hand lifts the bauble slowly up out of the box to chest height, palm under it; her left hand stays on the rim
SECONDARY    tissue settles where the bauble left
LIGHT        unchanged
SHOTS        Shot 1 only
MUST NOT CHANGE   the bauble stays one rigid sphere, same colour · no second bauble appears in her hand · five fingers each hand
TEXT         no legible text in frame
DURATION     generate 5 s · edit window 2.1 s
DRAFT/FINAL  3 takes · 720p · v1
ACCEPTANCE   push is smooth and single; tissue fold region trackable for the soft hat crop
```

## K10-B4 (TURN)

```
BRIEF  K10-B4-ff  v1      output: still   regime: energy
PURPOSE      "She found the box. He watched." — over her shoulder, the box coming up; Daniel in the doorway.
START STATE  [REF-G3 → character, back of head] [REF-D4 → character, leaning pose] [PROP-kraft → product in box] [LOC-day → composition/light]
SUBJECTS     <Grace> · <Daniel> · <Kraft box>
FRAMING      MS over Grace's right shoulder, camera at her shoulder height, 35 mm, **deep focus**, 9:16; her head and shoulder foreground left;
             <Box> centre at y≈1050; doorway upper right with Daniel's face at y≈560–680
CAMERA       n/a
ACTION       Grace kneels at the box; her left hand pinches the fold of red tissue, lifted aside and held at the box's left rim; her right hand
             grips <Kraft box> by its sides just inside the box; Daniel leans his left shoulder on the door frame, arms folded, looking at her
SECONDARY    n/a
LIGHT        daylight from off-screen left; the doorway slightly dimmer
SHOTS        n/a
MUST NOT CHANGE   ornament face-up in the kraft box, unoccluded · Daniel green sweater, arms folded · 5 fingers · gold bands
TEXT         none generated; real render tracked over the placeholder
DURATION     n/a
DRAFT/FINAL  3 variants · 2K · v1
ACCEPTANCE   Daniel and the box both sharp (masks need a deep-focus plate); his face clear of y<480
```

```
BRIEF  K10-B4  v1         output: video   regime: energy
PURPOSE      Same; she lifts the box out.
START STATE  [K10-B4-ff → first frame] [REF-D1 → character] [P-34L → product body]
SUBJECTS     <Grace> · <Daniel> · <Kraft box>
FRAMING      as the first frame
CAMERA       fixed (move in post: rack focus box → Daniel at the end of the window) — ACK-OPENMOVE
ACTION       Shot 1: Grace's right hand lifts <Kraft box> slowly straight up out of the tissue to her chest height, fingers on the box sides below the rim;
             her left hand keeps holding the tissue fold aside. Daniel stays leaning on the door frame, arms folded; his cheeks lift into a small
             closed-mouth smile
SECONDARY    tissue paper shifts as the box rises
LIGHT        unchanged
SHOTS        Shot 1 only
MUST NOT CHANGE   Daniel stays in place, arms folded (no step, no unfold) · ornament stays face-up and flat in the box, same size ·
             five fingers per hand · Grace stays kneeling
TEXT         no legible text in frame
DURATION     generate 5 s · edit window 2.6 s
DRAFT/FINAL  3 takes · 720p · v1
ACCEPTANCE   box lift vertical, placeholder trackable (no fingers over it); Daniel static enough for one static mask; smile visible by window end
```

## K10-B5 (PROOF) — still + move, E38

```
BRIEF  K10-B5  v1         output: still   regime: stability
PURPOSE      "Daniel, Grace and Mochi. 2026." — the real ornament flat in her open palm (the names read).
START STATE  [SCALE-palm → composition + scale] [REF-G6 → character hands] [P-34R → product body/edge] [LOC-day → light]
SUBJECTS     <Grace> left hand · <Ornament>
FRAMING      top-down ECU, 50 mm, 9:16 at 4K (keeper); ornament centred, ≥1100 px wide in the 2K draft; background red tissue in the open box, soft
CAMERA       n/a (move in post: pull-back, parameters in shotlist B5)
ACTION       her left palm open and flat, fingers together; the ornament lies flat on palm and fingers, overhanging both sides; thumb beside the
             left edge touching only the wood edge; red cuff at the bottom edge
SECONDARY    n/a
LIGHT        soft daylight from off-screen left; thin shadow of the ornament edge on her palm to the right
SHOTS        n/a
MUST NOT CHANGE   ornament one flat 3 mm sheet, size ≈1.5× palm width · thumb never over the print · 5 fingers · gold band
TEXT         none generated; the real render (names, year) is composited flat at native resolution over the placeholder
DURATION     n/a (edit 3.2 s)
DRAFT/FINAL  3 variants at 2K → keeper re-made at 4K · v1
ACCEPTANCE   placeholder silhouette fully covered by the render; E39 and E60 measured on the move (shotlist B5)
```

## K10-B6 (CONNECTION 1, pivot)

```
BRIEF  K10-B6-ff  v1      output: still   regime: stability
PURPOSE      "She hung theirs first." — the only ornament on the bare tree, her hand just letting go, Daniel coming in.
START STATE  [SCALE-branch → product on branch] [REF-G2 → character] [REF-D3 → character] [LOC-day → composition] 
SUBJECTS     <Grace> · <Daniel> · <Ornament> · <Tree>
FRAMING      MCU, eye level with the ornament, 50 mm, 9:16; tree lower right; ornament on a front branch, centre y≈1000, ≈450 px wide;
             Grace behind-left of the tree at ¾, face y≈560–720; doorway behind her right shoulder with Daniel just inside it, soft
CAMERA       n/a
ACTION       ornament hangs by its gold cord, face to camera; Grace's right hand is behind the ornament, fingertips touching its back near the top;
             her left arm rests at her side; Daniel stands in the doorway, arms at his sides, hands resting against his thighs
SECONDARY    n/a
LIGHT        late-afternoon golden daylight from off-screen left
SHOTS        n/a
MUST NOT CHANGE   our ornament is the only thing on the tree · no lights · her fingers stay behind the ornament · faces clear of y<480
TEXT         none generated; real render layer over the placeholder, cord drawn in post
DURATION     n/a
DRAFT/FINAL  3 variants · 2K · v1
ACCEPTANCE   reads "she just put it there"; golden light warmer than B2
```

```
BRIEF  K10-B6  v1         output: video   regime: stability
PURPOSE      Same; release + he steps in.
START STATE  [K10-B6-ff → first frame] [REF-G1 → character] [REF-D1 → character]
SUBJECTS     <Grace> · <Daniel>
FRAMING      as the first frame
CAMERA       fixed (move in post: push-in 100→105 %) — ACK-OPENMOVE
ACTION       Shot 1: Grace draws her right hand back from behind the ornament and lowers it to her side, eyes on the ornament, a small smile;
             Daniel takes one step in from the doorway and stops behind her right shoulder, hands at his sides
SECONDARY    a few needles on the branch tremble as her hand leaves
LIGHT        unchanged golden light
SHOTS        Shot 1 only
MUST NOT CHANGE   her hand passes behind the ornament, never in front of it · Daniel takes one step only · faces on-model
TEXT         no legible text in frame
DURATION     generate 5 s · edit window 2.6 s
DRAFT/FINAL  3 takes · 720p · v1
ACCEPTANCE   nothing of the generated ornament visible outside the render silhouette after compositing; release inside the first ~0.6 s of the window
```

## K10-B7 (CONNECTION 2) — council-flagged multi-body shot

```
BRIEF  K10-B7-ff  v1      output: still   regime: energy
PURPOSE      "First Christmas as two. / Plus Mochi." — the couple and their dog together by the tree, our ornament sharp in front.
START STATE  [REF-G5 → character] [REF-D1 → character] [REF-M2 → character dog] [LOC-day → composition/light]
SUBJECTS     <Grace> · <Daniel> · <Mochi> · <Tree> (top front branch only)
FRAMING      MS-WS, high angle (camera ~2.1 m, 25° down), 35 mm, deep focus, 9:16; faces y≈520–720; Mochi y≈1000–1230;
             top front branch of the tree in the foreground right at y≈700–900 with an empty space for the ornament
CAMERA       n/a
ACTION       Grace stands beside the tree half-turned toward Daniel, her hands rising toward his chest; Daniel faces her, hands at her waist;
             Mochi sits on the rug at their feet facing them, head level
SECONDARY    n/a
LIGHT        late-afternoon golden daylight from off-screen left
SHOTS        n/a
MUST NOT CHANGE   Mochi seated, haunches down, both front paws on the rug · tree branch bare · ≤3 sharp faces (2 + dog) · gold bands
TEXT         none generated; the ornament + cord are composited in post
DURATION     n/a
DRAFT/FINAL  3 variants · 2K · v1
ACCEPTANCE   all three on-model; Mochi inside y≤1230 (4:5 + UI safe); empty branch space reads natural
```

```
BRIEF  K10-B7  v1         output: video   regime: energy
PURPOSE      Same; she turns into his arms, both look down at Mochi.
START STATE  [K10-B7-ff → first frame] [REF-G8 → character expression] [REF-D8 → character expression] [REF-M4 → character dog, looking up]
SUBJECTS     <Grace> · <Daniel> · <Mochi>
FRAMING      as the first frame
CAMERA       fixed (move in post: lateral drift left→right 3 %) — ACK-OPENMOVE
ACTION       Shot 1: Grace turns into Daniel's chest and rests her hands flat on it; Daniel's arms close around her back, hands meeting at her lower back;
             both lower their eyes to Mochi, cheeks lifting into closed-mouth smiles. Mochi stays seated and tilts his head up toward them;
             his tail sweeps gently on the rug
SECONDARY    Grace's hair swings slightly with the turn
LIGHT        unchanged golden light
SHOTS        Shot 1 only
MUST NOT CHANGE   Mochi stays seated with both front paws on the rug the whole time · arms stay separate, five fingers per hand ·
             faces on-model, eyes dry · tree branch unchanged
TEXT         no legible text in frame
DURATION     generate 5 s · edit window 2.7 s
DRAFT/FINAL  4 takes (cap 8) · 720p · v1; retry order (one variable each): (1) re-roll, (2) drop the tail sweep, (3) first frame already in the embrace
ACCEPTANCE   no jump, no stand; hug reads within 1.5 s; both gazes down at the dog by window end; ≥5 frames at full res for hands, paws, faces
```
