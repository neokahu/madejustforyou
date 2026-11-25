# K02 clips · 07 QA, SHOT mode, gate C (2026-11-26)

I (role 07, independent of 05) measured before reading `CLIPS.md`. Here is what I did:
- I probed every clip with ffprobe. All are 720×1280, 24 fps constant; H61 and B2 run 4.04 s, H63 and B5a run 5.04 s, B3 runs 6.04 s.
- For each clip I built a contact sheet at 0.5 s steps.
- Inside each claimed window I pulled at least 5 full-resolution frames and made 1:1 crops of hands, rings, faces and the ornament.

Standards: `CRITERIA.md` (locked), `K02/shotlist.md`, BRIEF rulings to 2026-11-26 (K02 = 5 in), `RENDERS.md` (no spin, faces camera).
Ornament faces are generator placeholders and the real K02 render replaces them in post (E37). Placeholder names and figures are S3 carried to Gate D.

## Summary

| shot | take | verdict | accepted window (take s) | needed | re-take est. |
|---|---|---|---|---|---|
| H61-B1 | v2 | **PASS** (S3) | 0.90–2.90 | 2.0 | — |
| H61-B1 | v1 | REJECT (agree with 05) | — | — | — |
| H63-B1 | v2 | **PASS** (S3) | 0.30–2.30 | 2.0 | — |
| H63-B1 | v1 | REJECT (agree with 05) | — | — | — |
| B2 | v1 | **PASS** (S3) | 0.70–3.30 | 2.6 | — |
| B3 | v2 | **FIX · S2** (05 re-take) | none (clean span 0.0–≈2.4 s) | 4.2 | $0.94 (6 s) |
| B3 | v1 | REJECT (generated "2023" plaque = E37/E40 S1 if shipped) | — | — | — |
| B5a | v1 | **FIX · S2** (05 re-take, or 06 ring paint-out + user ruling on 4 faces) | none yet; 0.3–2.9 if fixed | 2.6 | $0.78 (5 s) |

## Per clip

### H61-v2: PASS, window 0.90–2.90
Evidence (frames 0.9, 1.3, 1.7, 2.1, 2.5, 2.9):
- Push-in from frame 1 of the window.
- His left hand leaves the mug at ≈1.5 s and is up, palm toward the box at chest height, by 2.1 s. It reads as a polite "no thanks", never a stop sign at the lens.
- The mug stays upright. Kobe's green-cuff hands hold the box level, and the ornament lies face-up and still.
- One sharp face (Jacob): glasses, beard, buzz cut. No ring at 1:1 on either hand.

Defect lines:
- `[S3] H61-v2 · 00:00.90–00:01.50 · shotlist onset 0.3 s · gesture onset ≈0.6 s into the window (camera motion is on frame 1, so the hook still moves from 0.00) · — accept · —`
- `[S3] H61-v2 · 00:02.50–00:02.90 · E3 product visible · the box drifts low; the ornament is mostly cropped by 2.9 s (still in frame at 2.5) · 06 shift the 4:5/9:16 framing up or end the track at 2.5 · Gate D`
- `[S3] H61-v2 vs B2/B3/B5a · E46 continuity · the beard reads dark brown here and ginger-brown in the body clips (different light) · 06 grade match at the 2.00 cut · Gate D cut ±1 frame`

### H63-v2: PASS, window 0.30–2.30
Evidence (frames 0.3, 0.7, 1.1, 1.5, 1.9, 2.3):
- The box edge is in frame at 0.3 s. The box slides up flat from ≈0.5 s without tipping and stops with its top edge at the sheet's bottom edge, so the lettering zone stays clear.
- The ornament is face-up in the box, upright.
- The kid's hand has 5 fingers and a green cuff.
- The sheet stays clean (printed rule lines, no scribble).

Defect lines:
- `[S3] H63-v2 · 00:00.30–00:02.30 · shotlist "generated locked-off" · the sheet drifts ≈40–50 px up at 720w over the window (slight generated push) · 06 2D-track the sheet's corners for the lettering · Gate D lettering lock on ≥5 frames`
- `[S3] H63-v2 · window · shotlist action "hand lifts away" · hand stays on the box rim to the end · — accept · —`

### B2-v1: PASS, window 0.70–3.30
Evidence (frames 0.7, 1.2, 1.7, 2.2, 2.7, 3.3; hand crops):
- One hand-off, written as one motion: the mug goes onto the right-edge table, then both hands come forward and close on the box sides by ≈3.0–3.3 s.
- Kobe stays soft with his back to camera, arms level.
- Sharp faces are Mary, Jacob and Susan (3). The box stays flat and open, and the ornament lies face-up.
- **Ring check, 1:1:** no ring on either of Jacob's hands at 1.7, 2.7 or 3.3. The ring did not regrow from the edited first frame.

Defect lines:
- `[S3] B2-v1 · 00:02.70–00:03.30 · continuity · a black wristwatch shows on Jacob's left wrist (not seen in H61/B5a) · 06 accept or paint · Gate D`
- `[S3] B2-v1 · 00:03.00–00:03.30 · anatomy check · Jacob's and Kobe's hands are both on the box; no merge seen at 1:1 · — · Gate D`

### B3-v2: FIX S2, re-take (05)
Evidence (frames 0.0, 0.8, 1.6, 2.4, 3.2, 4.0, 4.2; hand crops):
- The expression arc is good: brows at 0.8 s, full grin by ≈1.6 s.
- The ornament lies **rotated 180° in the box from frame 0** ("2026" upside down to camera, hanger tab toward the lens). It comes up out of the box still upside down at 3.5–4.0 s, front toward camera.
- The body is a wide strip of about 2.5:1 (the real render is about 1.06:1), and the 2026 is printed above the figures, so the composite can't sit on it right-side up.
- Fingers cover the front rim at 3.2–4.0 s.
- No rings at 1:1.

Defect lines:
- `[S2] K02-B3-v2 · 00:00.00–00:04.20 · E40 shape as shipped / shotlist "lift the ornament face toward camera" · ornament upside down (rotated 180°) and its outline ≈2.5:1 vs the render's 1.06:1; at the lift (3.5–4.0 s) the product shows upside down to camera · 05 re-take (first frame with the ornament right-way-up to camera and the real cut outline from the turntable; or 04's fallback: end with the ornament in the box) · re-check orientation and outline on ≥5 frames`
- `[S2] K02-B3-v2 · window · shotlist length 4.2 s · usable before the lift ≈0.0–2.4 s; 05's 0.0–4.0 includes the upside-down lift and is still 0.2 s short · 05 re-take · re-check window ≥4.2 s`

05's "KEEP 0.0–4.0; cut by 4.0 s, after ≈4.2 s it stands up upside-down" is a **DISAGREE**: the ornament is already upside down in the box from 0.0 s and while lifted.

### B5a-v1: FIX S2 (05 re-take recommended)
Evidence (frames 0.3, 0.8, 1.3, 1.8, 2.3, 2.9; crops of faces and of the hand holding the ornament):
- In-camera pull-back. Jacob's left arm draws the kids in, and everyone laughs. Bailey's head rests on the right armrest, still.
- The ornament is held at chest/knee height, face to camera, with no spin.
- **Ring (05 flag): CONFIRMED.** A metal band is on the ring finger of the hand holding the ornament at 0.3, 1.3, 2.3 and 2.9 s (1:1 crop, x≈300–480, y≈700–840).
- **Kobe** turns his face to camera from ≈0.8–1.3 s and laughs sharp to the end. That makes **4 sharp faces**: Jacob, Mary, Susan, Kobe.
- His thumb sits on the printed "6".

Defect lines:
- `[S2] K02-B5a-v1 · 00:00.30–00:02.90 · must-not-change list / continuity (ring removed in B2 on purpose; family without a mother, GATE0) · ring on Jacob's ring finger, every sampled frame · 05 re-take (FF edit to remove the ring first, ≈$0.14) or 06 tracked paint-out (≈2.6 s, small moving hand) · re-check the ring finger at 1:1 on ≥5 frames`
- `[S2] K02-B5a-v1 · 00:01.30–00:02.90 · round-wide rule 2 / shotlist acceptance ≤3 sharp faces · Kobe's face turns to camera and is sharp (4 sharp faces) · 05 re-take (Kobe's face into Jacob's shoulder) or User ruling · re-check the face count on ≥5 frames`
- `[S3] K02-B5a-v1 · window · R24 · Jacob's thumb on the printed "6" · 06 thumb roto over the composite · Gate D`
- `[S3] K02-B5a-v1 · window · E44 · Bailey wears a collar and no Santa hat (the print shows a Santa hat; hats are accessories here) · — · —`

## Rings, all requested
- **B2:** none (1:1).
- **B3-v2:** none (1:1).
- **H61-v2:** none.
- **B5a:** ring present (S2 above).

## Shots with no accepted clip or still

| shot | status |
|---|---|
| B3 | re-take (above) |
| B5a | re-take (above) |
| **B5b** | **missing. No clip generated** (FF `K02-B5b-FF-t6.png` exists; ≈$0.78, 5 s) |
| B4 | real render still+move; no generation |
| B6 | shared end card (06) |

Re-take total K02: B3 $0.94 + B5a $0.78 (+ ≈$0.14 FF ring edit) = **≈$1.86**. Plus B5b, $0.78, not yet generated.

## Re-check 2026-11-26b (07, SHOT mode, independent of 05)
07 extracted 5 frames inside each claimed window at full res (720×1280) plus 1:1 crops at the risk points, before reading 05's notes.
| item | frames | verdict | reason |
|---|---|---|---|
| B3-v4 | 1.4/2.4/3.4/4.4/5.5 | **ACCEPT 1.40–5.60** (composite-conditional) | ornament lies flat in the box all take, never lifted; box in frame; brows → grin ≈3.3 s; glasses, beard stable; no rings. The placeholder sits 180° to camera; 06 corner-pins the real render in the same orientation and outline (physics: it faces Jacob) and must cover the placeholder fully; 07 checks the pin at gate D |
| B5a-v2 | 0.3/0.9/1.5/2.2/2.9 + 1:1 hand crops at 0.9, 2.2 | **ACCEPT 0.30–2.90** | no ring on the ornament hand at 1:1; Kobe shows the back of his head only → 3 sharp faces (Jacob, Mary, Susan); Bailey (white dog) still on the armrest; nobody stands; ornament front to camera (tracked render). Push-in instead of pull-back: S3 |
| B5b-v2 | 2.0/2.5/3.0/3.5/4.0 | **ACCEPT 2.00–4.00** | hand releases ≈2.2 and is down by 3.0; ornament hangs still, shape held; Mary (red Fair Isle, purple trousers) and Luna (white cat, dark patches) match the cast. **OPEN beyond the clip:** beat 5b is 2.9 s and the script keeps the "2026 end-state read ≥0.9 s at ≈60 % width"; in this wide clip the ornament is ≈10 % of width. No source for that 0.9 s is defined (05/06; E32 2 s floor applies) |
