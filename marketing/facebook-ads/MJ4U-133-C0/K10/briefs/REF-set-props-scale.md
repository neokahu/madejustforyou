# K10 · props, locations and scale plates (Gate B assets) · template §4.1

Tool class: image. Props on Seedream v5 Pro Edit (cheap, no people); locations and scale plates on Nano Banana Pro Edit. Adapter: `image-prompt-method.md`. All 2K, 1 take each (+1 retake allowance in the asset plan).

```
BRIEF  K10-PROP-tree  v1        output: still   regime: stability
PURPOSE      The one tiny tree that appears bare in B2/B6/B7 and decorated in B1B; anchors the location across the time jump.
START STATE  no reference (text-to-image)
SUBJECTS     <Tree> := ~120 cm real fir, sparse layered branches, in a round woven seagrass floor basket
FRAMING      full tree, eye level, centred, plain warm-grey background, 4:5
CAMERA       n/a (still)
ACTION       n/a (object)
SECONDARY    n/a
LIGHT        soft daylight from camera left
SHOTS        n/a
MUST NOT CHANGE   branches bare green, no lights, no ornaments, no topper · basket woven, no tag
TEXT         no legible text in frame
DURATION     n/a
DRAFT/FINAL  1 take · 2K · v1
ACCEPTANCE   reads as a small real tree (needles, trunk visible at the base), not artificial plastic; open front branch at ~90 cm height for the ornament
```

```
BRIEF  K10-PROP-moving-box  v1  output: still   regime: stability
PURPOSE      The DECORATIONS box of B1A/B2/B3/B4 (H01's promise). Lettering is composited later.
START STATE  no reference
SUBJECTS     <Box> := plain brown corrugated moving box ~45×35×35 cm, four top flaps
FRAMING      three-quarter view from slightly high, plain background, 4:5
CAMERA       n/a
ACTION       n/a — the far flap stands upright facing camera, the two side flaps fold outward, the near flap lies folded over the contents
SECONDARY    n/a
LIGHT        soft daylight from camera left
SHOTS        n/a
MUST NOT CHANGE   every surface is plain brown cardboard, the far flap a clean blank rectangle (space for DECORATIONS) · tape on the bottom seam only
TEXT         no legible text in frame
DURATION     n/a
DRAFT/FINAL  1 take · 2K · v1
ACCEPTANCE   far flap flat and frontal enough to corner-pin the lettering; no printed arrows, logos or words
```

```
BRIEF  K10-PROP-kraft  v1       output: still   regime: stability
PURPOSE      The small gift box he hides; holds the ornament at true 5 in scale.
START STATE  [P-34R → product body / scale]
SUBJECTS     <Kraft box> := small open kraft-paper gift box ~15×15×5 cm lined with red tissue
FRAMING      slightly high three-quarter, plain background, 4:5
CAMERA       n/a
ACTION       the ornament from Image 1 lies face-up in the red tissue inside the box, hanger tab toward the far side, ~1 cm of tissue showing on every side
SECONDARY    n/a
LIGHT        soft daylight from camera left
SHOTS        n/a
MUST NOT CHANGE   ornament stays one flat 3 mm sheet with one edge around its outline, same size relation to the box · box plain kraft, no ribbon, no lid in frame
TEXT         no legible text generated (the ornament face is a placeholder, replaced by the real render)
DURATION     n/a
DRAFT/FINAL  1 take · 2K · v1
ACCEPTANCE   box-to-ornament scale per REFS-PLAN §1; ornament not raised or layered (E40)
```

```
BRIEF  K10-PROP-baubles  v1     output: still   regime: stability
PURPOSE      Grace's childhood ornaments (B3, B1B): must read as old and hers, never as family ornaments.
START STATE  no reference
SUBJECTS     <Baubles> := four worn glass Christmas baubles ~6–7 cm: faded red, faded gold, pale blue, one with a chipped silver cap
FRAMING      top-down on red tissue, 4:5
CAMERA       n/a
ACTION       n/a — laid in a loose row with gaps between them
SECONDARY    n/a
LIGHT        soft daylight from camera left
SHOTS        n/a
MUST NOT CHANGE   scuffed glass, dulled colour, small paint loss · plain surfaces with no names, initials, dates, pictures or logos
TEXT         no legible text in frame
DURATION     n/a
DRAFT/FINAL  1 take · 2K · v1
ACCEPTANCE   clearly old; clearly text-free at full res
```

```
BRIEF  K10-LOC-day  v1          output: still   regime: stability
PURPOSE      Lock the room layout for B2/B4/B6/B7 (doorway, window side, boxes, tree spot).
START STATE  [PROP-tree → set] [PROP-moving-box → set]
SUBJECTS     <Room> := small apartment living room, mid-move
FRAMING      wide, eye level (1 m), 28 mm, 9:16 with key content inside the central 4:5 area
CAMERA       n/a (still)
ACTION       n/a — empty room: the tree from Image 1 stands at frame right on a rug; moving boxes like Image 2 stacked two high along the back wall;
             an open doorway at back right leads to a dim hallway
SECONDARY    n/a
LIGHT        cool-neutral daylight from a window off-screen left, falling across the rug; the window itself stays out of frame
SHOTS        n/a
MUST NOT CHANGE   tree bare, no lights · doorway back right · boxes plain · no people, no dog
TEXT         no legible text in frame
DURATION     n/a
DRAFT/FINAL  1 take · 2K · v1
ACCEPTANCE   window never in frame; nothing written anywhere; same tree as PROP-tree
```

```
BRIEF  K10-LOC-evening  v1      output: still   regime: stability
PURPOSE      The same room later that evening (H15 flash-forward); must differ in light, not in layout.
START STATE  [LOC-day → composition]
SUBJECTS     <Room> (same)
FRAMING      same as LOC-day
CAMERA       n/a
ACTION       n/a — two boxes now open and half unpacked, tissue on the rug
SECONDARY    n/a
LIGHT        night: warm 2700 K lamp light from off-screen right, deep blue ambient from the off-screen window left
SHOTS        n/a
MUST NOT CHANGE   layout, tree, doorway identical to Image 1 · tree has no lights · no people
TEXT         no legible text in frame
DURATION     n/a
DRAFT/FINAL  1 take · 2K · v1
ACCEPTANCE   unmistakably night and warm vs LOC-day (needed for the 2.0 s reset)
```

```
BRIEF  K10-SCALE-palm  v1       output: still   regime: stability
PURPOSE      Scale anchor for every hand shot (E41): 5 in ornament in an adult palm.
START STATE  [P-front → product body] [P-34R → product body/edge] [REF-G6 → character hands]
SUBJECTS     <Ornament> := the ornament in Images 1–2 · <Grace> hands
FRAMING      top-down, 50 mm, 4:5, plain red tissue background
CAMERA       n/a
ACTION       her left palm open and flat, fingers together; the ornament lies flat on palm and fingers, overhanging both sides of the palm;
             her thumb lies beside the ornament's left edge touching only the wood edge
SECONDARY    n/a
LIGHT        soft daylight from camera left, a thin shadow of the ornament edge on her palm to the right
SHOTS        n/a
MUST NOT CHANGE   ornament is one flat 3 mm sheet, one edge around the outline, size ≈1.5× her palm width · 5 fingers · gold band left ring finger
TEXT         no legible text generated (placeholder face)
DURATION     n/a
DRAFT/FINAL  1 take (+1) · 2K · v1
ACCEPTANCE   relation matches REFS-PLAN §1 when measured (ornament width / palm width 1.4–1.6)
```

```
BRIEF  K10-SCALE-branch  v1     output: still   regime: stability
PURPOSE      Scale anchor for hanging shots (B1B, B6, B7).
START STATE  [P-front → product body] [P-34L → edge, gold cord] [PROP-tree → set] [PROP-baubles → prop]
SUBJECTS     <Ornament> · <Tree> · one <Baubles> bauble
FRAMING      close-up of one fir branch, eye level, 85 mm, 4:5
CAMERA       n/a
ACTION       the ornament hangs by its thin gold cord from the branch, face to camera; one 8 cm faded-red bauble hangs on the next branch to the right
SECONDARY    n/a
LIGHT        soft daylight from camera left
SHOTS        n/a
MUST NOT CHANGE   ornament face to camera, flat single sheet · ornament width ≈1.6× the bauble diameter · cord thin gold metallic
TEXT         no legible text generated
DURATION     n/a
DRAFT/FINAL  1 take (+1) · 2K · v1
ACCEPTANCE   ratio holds when measured; ornament plausibly light on the branch (branch barely bends)
```
