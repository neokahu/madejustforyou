# K01 reference assets · briefs (GATE B inputs)

One brief block per reference set; each view is one call. Labels and must-not-change lists: `../refs/REFS-PLAN.md` §2.

```
BRIEF  REF-C<n>-<person>  v1 (one per person; views listed below)   output: still   regime: stability
PURPOSE      Identity lock for <person> so every first frame and video reuses one face/look. Not shown in
             the ad.
START STATE  view 1 (front): [take-2 crop of <person>, upscaled → character identity]
                             [render figure crop of <person> → character traits: hair, glasses, sweater]
             views 2–8: [views 1–3 of this person → character] (no chaining from later views)
SUBJECTS     <person> := the 2–3 stable features in REFS-PLAN §2
FRAMING      single subject, centred, plain warm-grey studio background, 50 mm look; head-and-shoulders
             for views 1–3; full body for standing/seated views; hands view fills the frame. 2:3.
CAMERA       n/a
ACTION       per view, every limb placed. Defaults: standing = weight on both feet, palms resting
             against the sides of the thighs; seated = hands resting on the thighs with a gap between
             them, fingers slightly apart so five show on each hand; hands view = both hands palm-down
             on a grey table, a clear gap between them, all ten fingers visible
SECONDARY    n/a
LIGHT        soft window light from camera-left, off-screen
SHOTS        n/a
MUST NOT CHANGE   REFS-PLAN §2 list for this person (glasses round for Grandpa; bare fingers; hats as
             listed; trousers as listed)
TEXT         none; no labels on the image
DURATION     n/a
DRAFT/FINAL  1 take per view, +1 for any view that fails 07 · 2K · 2K · v1
ACCEPTANCE   Gate B checklist (REFS-PLAN §3)
```

| Set | Views (one call each) |
|---|---|
| REF-C1 Grandma (8) | front · ¾L · ¾R · full seated in an armchair · full standing · hands · gentle smile · moved: left hand over her mouth, fingers along the upper lip, eyes bright and dry |
| REF-C2 Grandpa (8) | front · ¾L · ¾R · full seated · leaning-in profile (head forward ~10 cm, glasses on) · hands (red cuffs) · smile · warm look down |
| REF-C3 Emma (8) | front · ¾L · ¾R · full standing · leaning over a chair back, forearms on it · hands · smile · upper body, arms wrapped forward as in a hug from behind |
| REF-C7 Leo (8) | front · ¾L · ¾R · full standing · kneeling · pointing hand (right index out, other fingers curled, five countable) · grin · profile |
| REF-C4 Michael (3) | front · ¾L · full standing |
| REF-C6 Sarah (3) | front · ¾R · full standing |
| REF-C5 Cooper (3) | sitting, front · sitting, side · head close-up, mouth closed |

```
BRIEF  REF-P5  v1                           output: still (2 frames)   regime: stability
PURPOSE      Scale anchor for the 5 in ornament (E41): (a) held in two adult hands; (b) lying in the
             kraft box on red tissue.
START STATE  [REF-P1 render front → product body] [REF-P2 ¾L → product body (edge)]
             [REF-C1 hands view → character: hands] (for b: no hands)
SUBJECTS     <Ornament> := one flat 3 mm plywood sheet cut to the outline, coin-thin edge, hanger tab
             with a hole, thin gold metallic cord
FRAMING      (a) the ornament held at chest height against a plain warm-grey background, front square to
             camera, filling ~55% of frame width; (b) top-down onto an open plain kraft box ~6 × 6 × 2 in
             with red tissue, the ornament lying flat inside with a thumb's width of tissue around it. 4:5.
CAMERA       n/a
ACTION       (a) both hands hold it from behind, thumbs on the left and right outer cut edges, fingertips
             visible above the top edge; (b) n/a
SECONDARY    n/a
LIGHT        soft even key from camera position, off-screen
SHOTS        n/a
MUST NOT CHANGE   single flat sheet, printed on the front only, no layered relief; front face clear of
             fingers; cord thin gold
TEXT         none generated; real render composited over the placeholder face before 07 sees it
DURATION     n/a
DRAFT/FINAL  1 take each (+1 retake) · 2K · 2K · v1
ACCEPTANCE   the ornament is ~12.7 cm wide against an adult hand (~18 cm long) and the 6 in box
```

```
BRIEF  L1-PLATE  v1                          output: still   regime: stability
PURPOSE      The empty K01 living room (no people, no ornament) as a location reference for FF-B4,
             FF-B6a, FF-B6b, and a blurred bokeh plate behind B5.
START STATE  [take 2 → location (tree, chair, bookshelf, fireplace, lamp)]
SUBJECTS     n/a (no people, no product)
FRAMING      take-2 viewpoint, 9:16, the armchair empty, tree centre-left
CAMERA       n/a
ACTION       n/a
SECONDARY    n/a
LIGHT        as take 2
SHOTS        n/a
MUST NOT CHANGE   room layout and palette as in take 2
TEXT         none; no legible text in frame (book spines soft)
DURATION     n/a
DRAFT/FINAL  1 take · 2K · 2K · v1
ACCEPTANCE   no people, no ornaments that resemble the product
```
