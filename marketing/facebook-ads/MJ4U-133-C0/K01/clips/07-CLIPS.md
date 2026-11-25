# K01 clips · 07 QA, SHOT mode, gate C (2026-11-26)

I (role 07, independent of 05) measured before reading `CLIPS.md`. Here is what I did:
- I probed every clip with ffprobe. All are 720×1280, 24 fps constant; H76, H79 and B6a run 4.04 s, B3 and B6b run 5.04 s.
- For each clip I built a contact sheet at 0.5 s steps.
- Inside each claimed window I pulled at least 5 full-resolution frames and made 1:1 crops of the risk areas (hands, rings, fingertip against the print, ornament, background faces).

Frames are in the 07 scratchpad and are not kept in the repo.

Standards: `CRITERIA.md` (locked), `K01/shotlist.md`, BRIEF rulings to 2026-11-26 (K01 ornament = **7 in**), `RENDERS.md` (no spin, faces camera), and 07's first-frame rulings in `first-frames/07-SHOT.md`.
All ornament faces in these clips are generator placeholders. The real render replaces them in post (E37), so placeholder names and the 3D-styled figures are S3 carried to Gate D, not repeated below.

## Summary

| shot | take | verdict | accepted window (take s) | needed | re-take est. |
|---|---|---|---|---|---|
| H76-1 | v1 | **PASS** | 0.00–2.00 | 2.0 | — |
| H79-1 | v1 | **PASS** (S3) | 0.00–2.00 | 2.0 | — |
| B3 | v2 | **FIX · S2** (05 re-take) | none yet; 1.8–4.1 only if the fingertip is fixed | 2.3 | $0.78 (5 s) |
| B3 | v1 | REJECT (agree with 05) | — | — | — |
| B6a | v1 | **FIX · S2** (05 new first frame + re-take) | none (clean part is 1.6–≈3.2 = 1.6 s) | 2.6 | $0.14 FF edit + $0.63 (4 s) |
| B6b | v1 | **PASS** (S3) | 1.00–3.70 | 2.7 | — |

## Per clip

### H76-v1: PASS, window 0.00–2.00
Evidence (frames 0.0, 0.5, 1.0, 1.5, 2.0):
- The right hand lifts the lid up and away from frame 1, and the lid is off the box and leaving frame top-right by 2.0 s.
- The left hand rests on the box's near edge with fingers outside the box. Each hand has 5 fingers and no ring at 1:1.
- The ornament lies face-up, still, one only, with no tilt, flip or spin in any sampled frame. The lid never passes over a hand.
- Push-in straight down; no generated text other than the placeholder face.

Carried S3: the outline is not the real cut (FF-H76 ruling); 06 covers it with the full render plus the edge.

### H79-v1: PASS, window 0.00–2.00
Evidence (frames 0.0, 0.4, 0.8, 1.2, 1.6, 2.0):
- Emma leans in from 0.4 s, and the hug lands around 1.2 s with her hands at Grandma's collarbone, not her throat.
- Two sharp faces. Grandma: grey bun, no hat, no glasses. Emma: blonde pigtails under the hat at 0.4 s.
- Both of Grandma's hands are bare at 1:1. No tears.
- Faces stay below the caption band. At 1280 scale the band runs y 193–333; Emma's eyes are at ≈y 430 at 0.4 s and Grandma's eyes at ≈y 480 at 2.0 s. Only hair and hat fall in the band.

Defect lines:
- `[S3] H79-v1 · 00:01.40–00:02.00 · shotlist acceptance "Grandma's hand stays over her mouth" · at 2.0 s her right hand has moved down to Emma's forearms; she laughs · 06 (may end at 1.60 if wanted; 2.0 s needed, so keep 0.00–2.00) · —`
- `[S3] H79-v1 · whole window · E41 scale (carried) · the placeholder in the box is ≈4.5 in in a deep box · 06 composites the render at 7 in · Gate D scale vs thumb on ≥5 frames`

### B3-v2: FIX S2, re-take (05)
Evidence (frames 0.0 and 1.8, 2.3, 2.8, 3.3, 3.8, 4.1; 1:1 and 4× crop at x 270–450, y 330–480):
- The fingertip and nail rest **on the printed Cooper hat tip and over most of the white pompom**, not just "a few px of the white edge".
- A side-by-side with frame 0.0 (no finger) shows the red hat tip and the pompom hidden under the nail from 1.8 s to the end of the take.
- The finger is a thumb-like digit entering from the right. The plate is static and the hand is bare.

Defect lines:
- `[S2] K01-B3-v2 · 00:01.80–00:05.04 · R24 / shotlist acceptance "fingertip never covers any printed pixel" · nail covers Cooper's printed hat tip + pompom (crop x≈320–420 y≈360–440 at 720w, every frame from 1.8 s) · 05 re-take (finger stops on tissue ≥1 finger-width right of the pompom); alternative 06: roto the finger and shift it ≈70 px right over clean tissue, then 07 re-checks · re-check the finger vs print on ≥5 frames`
- `[S2→carried] K01-B3-v2 · window · shotlist "Cooper ≥450 px at 1080w" · Cooper ≈195 px at 720w ≈ 293 px at 1080w (the FF-B3-t2 S2 stands); 06's ≈1.45× crop closes it · 06 · Gate D Cooper width + plate sharpness`

05's note ("touches the white edge by a few px") is a **DISAGREE**: it covers printed artwork, so a matte under the static re-composite would show the finger passing *under* the ornament.

### B6a-v1: FIX S2, new first frame + re-take (05)
Evidence (frames 0.0, 0.5, 1.0, 1.3, 1.8, 2.2, 2.6 and sheet to 4.0; crops of the hand region and the background faces):
- **Extra arm (05 flag, confirmed):** 0.0–1.3 s, an adult-sized hand with a green Fair Isle cuff points in from the frame-right edge. Grandma's two hands are on the ornament and Leo's left hand is at his waist, so this hand belongs to nobody. It withdraws to the right by ≈1.5 s; nothing is there at 1.8 s.
- **Leo's gesture:** Leo's own right hand first appears at ≈1.9 s, already at his chest, pointing toward the ornament. The planned arc from the cut edge to his chest never happens. It reads as "me!", which is acceptable.
- **Background, Gate A ruling:**
  - Grandpa, Sarah and Michael start looking at each other or at Leo (0–1.0 s) and turn to the lens by 1.8 s. In this reverse OTS, looking at the lens reads as looking at Grandma and the ornament, so I would accept the "everyone" read.
  - Sharp faces at 2.6 s: Leo sharp; Michael and Grandpa semi-sharp; Sarah soft. That is 3, the limit, and they sharpen further as the push lands.
- **Grandpa wears a Santa hat** throughout (shotlist: grandparents bare-headed, as printed).
- After ≈3.3 s the ornament drifts off frame-left ("2026" cut at 3.5 s).
- The ornament faces camera with no spin. It is ≈7 in in Grandma's hands.

Defect lines:
- `[S2] B6a-v1 · 00:00.00–00:01.50 · E47 anatomy / V2 spurious object · third adult hand (green Fair Isle cuff) points from frame-right while Grandma's two hands hold the ornament and Leo's left hand is at his waist (frames 0.5, 1.0, 1.3) · 05: new first frame (NBP edit of FF-B6a-t3: remove the right-edge hand, put Leo's own right index at the ornament's right cut edge, arm traceable to his shoulder) + one 4 s take · re-check the arm count on ≥5 frames`
- `[S2] B6a-v1 · window · shotlist length 2.6 s · the only clean span is ≈1.6–3.2 s (1.6 s); the ornament leaves frame-left after ≈3.3 s · 05 re-take · re-check window ≥2.6 s`
- `[S2] B6a-v1 · 00:00.00–00:04.04 · shotlist fixed decision "grandparents bare-headed" (matches the print) · Grandpa in a Santa hat, semi-sharp by 1.8 s · 05 in the same FF edit · re-check`
- `[S3] B6a-v1 · 00:01.80–00:02.60 · round-wide rule 2 (≤3 sharp) · Leo + Michael + Grandpa readable at the end of the push · 05 re-take: deeper background blur · re-check`
- `[S3] B6a-v1 · whole take · R24 · Grandma's right thumb on the front face by the snowman · 06 thumb roto · Gate D`

05's "Leo touches chest by ~2.0 s, PASS conditional, 0.00–2.60": **DISAGREE**. 0.0–1.5 s contains the extra arm, and FF-B6a-t3 already shows it at frame 0.0. 07's own earlier acceptance of FF-B6a-t3 ("no extra arm found") was wrong: the arm is visible at frame 0 of the clip.

### B6b-v1: PASS, window 1.00–3.70 (2.7 s, equal to the shot length)
Evidence (frames 1.0, 1.5, 2.0, 2.5, 3.0, 3.7; hand crops at 1:1):
- Grandpa's hand (red cuff) rests over Grandma's (green cuff). Both lower away together and are out of the ornament by ≈2.5 s. Each hand has 5 fingers, with no ring at 1:1.
- The ornament hangs by the thin gold cord through the tab, face to camera, with no swing or spin up to 3.7 s.
- One move (push-in). The family is soft in the bokeh.

Defect lines:
- `[S3] B6b-v1 · 00:02.50–00:03.70 · shotlist "back resting against needles" · it hangs free in front of the needles; no rotation in the window · 06 sway in post only · Gate D`
- `[S3] B6b-v1 · window · E41 (carried from FF) · reads ≈8–9 in vs 7 · User accept / 06 · Gate D`
- `[S3] B6b-v1 · bokeh frame-left · E44 (carried) · grey-haired adult in a cream sweater matches no cast member · 06 keep soft · Gate D playback`

## Shots with no accepted clip or still

| shot | status |
|---|---|
| B3 | re-take (above) |
| B6a | re-take (above) |
| **B4** | **stuck. No clip.** Per the 2026-11-26 ruling it is now an ornament-free plate plus composite; no plate or video exists yet (≈$0.14 + $0.63) |
| B2 | still+move from FF-B2-t2 (accepted earlier with the 06 crop); no generation owed |
| B5 | real render still+move; no generation (04 caption block still open in the shotlist) |
| B7 | shared end card (06) |

Re-take total K01: B3 $0.78 + B6a ≈$0.77, ≈ **$1.55**; plus B4, ≈$0.77, not yet generated.
