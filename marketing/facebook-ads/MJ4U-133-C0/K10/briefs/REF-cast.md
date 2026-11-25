# K10 · cast reference briefs (Gate B assets) · template §4.1

Tool class: image (Nano Banana Pro t2i for views 1–3, Nano Banana Pro Edit for views 4–8 with views 1–3 as references). Adapter: `research/reference/image-prompt-method.md` ("Character reference set — 8 slots"). Prompt guard applies. Each view is one asset; fields common to a set are written once in its block and each view row fills FRAMING / ACTION / LIGHT. 2K, one view per call, 2 variants on views 6 and 7 (the ones that drifted on the owner set).

---

```
BRIEF  K10-REF-D (Daniel, views D1–D8)  v1      output: still ×8   regime: stability
PURPOSE      Lock <Daniel> for every K10 shot he appears in (B1A hands, B1B soft, B4 doorway, B6 step-in, B7 hug).
             The viewer must later recognise the same man in green as "He".
START STATE  D1–D3: no reference (text-to-image), [P-front → light/style: NO — not used; the print is a cartoon]
             D4–D8: [D1 → character] [D2 → character] [D3 → character]
SUBJECTS     <Daniel> := young East Asian-American man, late 20s, short black messy-crop hair,
             green Fair Isle sweater with a white reindeer band
FRAMING      per view (table); plain warm-grey seamless background; 9:16 portrait for D4/D5, 4:5 for the rest
CAMERA       n/a (still)
ACTION       per view (table); every limb placed
SECONDARY    n/a (still)
LIGHT        soft window light from camera left, gentle fill from right; same in all eight
SHOTS        n/a (still)
MUST NOT CHANGE   hair stays short black messy crop · sweater green with white snowflake + reindeer band, green ribbed cuffs ·
             charcoal trousers · left ring finger wears one plain thin gold band, every other finger bare · no watch ·
             clean-shaven · eyes open · natural skin texture, light grain
TEXT         no legible text in frame
DURATION     n/a (still)
DRAFT/FINAL  1 take per view (2 for D6, D7) · 2K draft = final · variable changed: n/a (v1)
ACCEPTANCE   same face across D1–D8 at full res; D6 counts 5+5 fingers with a gap between the hands; ring on left ring finger only;
             reads unambiguously as a man (E45 "He")
```

| view | FRAMING | ACTION (limbs located) |
|---|---|---|
| D1 front | head-and-shoulders, eye level, 85 mm, centred | faces camera, shoulders square, arms relaxed below frame, neutral relaxed mouth |
| D2 ¾ left | head-and-shoulders, eye level | head and body turned 45° to camera-left, eyes following the turn |
| D3 ¾ right | head-and-shoulders, eye level | turned 45° to camera-right |
| D4 full standing | full body, eye level, 35 mm | left shoulder leaning on a white door frame at his left side, arms folded across his chest (right hand tucked under left upper arm, left hand on right upper arm), weight on his right foot |
| D5 full seated | full body, slightly high | sits cross-legged on a rug, forearms resting on his knees, hands loosely open on his knees |
| D6 hands | close-up of both hands, top-down, 50 mm | both hands rest palm-down on a wooden table with a clear gap of table between them, fingers slightly spread so all five of each show; green ribbed cuffs at the wrists |
| D7 expr: small smile | head-and-shoulders, eye level | lips closed, mouth corners lifted slightly, cheeks raised a little, eyes soft and slightly narrowed |
| D8 expr: warm smile down | head-and-shoulders, camera slightly high | chin lowered, eyes looking down past the camera's lower edge, closed-mouth smile, eye corners crinkled |

---

```
BRIEF  K10-REF-G (Grace, views G1–G8)  v1       output: still ×8   regime: stability
PURPOSE      Lock <Grace> for B1B, B2–B7. The viewer must recognise the same woman in red as "She".
START STATE  G1–G3: no reference (text-to-image) · G4–G8: [G1 → character] [G2 → character] [G3 → character]
SUBJECTS     <Grace> := young East Asian-American woman, late 20s, long straight black hair past the shoulders with a centre part,
             red Fair Isle sweater
FRAMING      per view (table); plain warm-grey seamless background; 9:16 for G4/G5, 4:5 for the rest
CAMERA       n/a (still)
ACTION       per view (table); every limb placed
SECONDARY    n/a (still)
LIGHT        soft window light from camera left, gentle fill from right
SHOTS        n/a (still)
MUST NOT CHANGE   hair black, straight, loose past the shoulder blades, centre part, no fringe · red sweater with a white Fair Isle band,
             red ribbed cuffs · red-tartan trousers · left ring finger one plain thin gold band, other fingers bare · small gold stud earrings ·
             eyes open · natural skin texture
TEXT         no legible text in frame
DURATION     n/a (still)
DRAFT/FINAL  1 take per view (2 for G6, G7) · 2K = final · v1
ACCEPTANCE   same face across G1–G8; G6 left palm flat and fully visible with 5 fingers; ring left ring finger only; reads as a woman (E45 "She")
```

| view | FRAMING | ACTION (limbs located) |
|---|---|---|
| G1 front | head-and-shoulders, eye level, 85 mm | faces camera, hair falling in front of both shoulders, arms relaxed below frame |
| G2 ¾ left | head-and-shoulders | turned 45° to camera-left |
| G3 ¾ right | head-and-shoulders, from slightly behind her right shoulder | turned 120° away so the back of her head, the hair length and her right cheek line show (B4 over-the-shoulder) |
| G4 full kneeling | full body, eye level, 35 mm | kneels upright on a rug, knees on the rug, hands resting on her thighs |
| G5 full standing | full body, eye level | stands, weight on both feet, hands resting together at her waist, fingers interlaced lightly |
| G6 hands | close-up, top-down, 50 mm | left hand palm-up, open and flat, fingers together, resting on red tissue paper; right hand palm-down beside it with a clear gap of tissue between them; red ribbed cuffs at both wrists |
| G7 expr: quiet surprise | head-and-shoulders | lips parted slightly, brows lifted a little, eyes widened a little and looking down-left |
| G8 expr: warm smile down | head-and-shoulders, camera slightly high | chin lowered, eyes looking down, closed-mouth smile, eye corners crinkled |

---

```
BRIEF  K10-REF-M (Mochi, views M1–M4)  v1       output: still ×4   regime: stability
PURPOSE      Lock <Mochi> for B7 ("Plus Mochi."). Must read as the printed Corgi.
START STATE  M1: [P-front → character: breed, coat pattern of the printed dog only; it is a cartoon, so look not style]
             M2–M4: [M1 → character]
SUBJECTS     <Mochi> := red-and-white Pembroke Welsh Corgi, large upright ears, plain red collar
FRAMING      per view; plain warm-grey seamless floor and background; 4:5
CAMERA       n/a (still)
ACTION       per view; the dog is seated in every view
SECONDARY    n/a (still)
LIGHT        soft window light from camera left
SHOTS        n/a (still)
MUST NOT CHANGE   seated: haunches on the floor, both front paws flat on the floor side by side · red/sable coat, white blaze, white chest,
             white front legs and paws · natural full fluffy tail lying on the floor · plain red collar with no tag · no hat, no clothing
TEXT         no legible text in frame
DURATION     n/a (still)
DRAFT/FINAL  1 take per view · 2K = final · v1
ACCEPTANCE   breed + coat match the print (E44); 4 legs, normal paws; ears upright in every view; same white blaze shape across views
```

| view | FRAMING | ACTION |
|---|---|---|
| M1 front seated | full body, camera at the dog's eye level | sits facing camera, mouth closed, ears up |
| M2 ¾ seated | full body, camera slightly high (B7 angle) | sits turned 45° to camera-right, mouth slightly open |
| M3 side seated | full body, profile facing camera-left | sits, tail lying out behind on the floor |
| M4 looking up | full body, camera high | sits, head tilted up 30° toward a point above camera-left, ears up |
