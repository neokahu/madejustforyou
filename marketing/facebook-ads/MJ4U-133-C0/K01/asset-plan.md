# MJ4U-133-K01 · asset plan and budget (O4) · role 05, 2026-11-25

Prices (Atlas, per the 05 brief): Nano Banana Pro Edit **$0.14/img** · Seedream v5 Pro Edit **~$0.04/img** · Seedance 2.0 Fast ref-to-video **$0.072/s at 720p** (5s take = $0.36, as billed for the K01 test clip).
New media goes to `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K01/` (`refs/`, `ff/`, `clips/`, `stills/`), named by shot_id + take, backed up with `scripts/backup-media.sh`.

## 1 · Reuse vs new, per shot

| shot_id | Source | Reuse | New assets | Takes |
|---|---|---|---|---|
| K01-H76-1 | GEN-VIDEO | turntable P1–P3 | FF-H76 still + clip | FF 3 · video 3 |
| K01-H79-1 | GEN-VIDEO | turntable P1 | FF-H79 still + clip | FF 3 · video 4 |
| K01-B2 | STILL+MOVE | **take 2** (composition; fallback base) | re-staged still | 3 + 2 fix edits |
| K01-B3 | GEN-VIDEO plate + real render | render | FF-B3 plate (Seedream) + clip | FF 2 · video 2 |
| K01-B4 | GEN-VIDEO | turntable P1, P3 | FF-B4 still + clip | FF 3 · video 3 |
| K01-B5 | STILL+MOVE | **real render (SVG re-rendered at 2×)** + blurred L1 plate | none | 0 |
| K01-B6a | GEN-VIDEO | turntable P1, P2 | FF-B6a still + clip | FF 3 · video 4 |
| K01-B6b | GEN-VIDEO | turntable P1–P3; test-clip recipe | FF-B6b still + clip | FF 2 · video 3 |
| K01-B7 | shared end card | round asset (06) | none | 0 |

## 2 · Cost

| Line | Count | Unit | Cost |
|---|---|---|---|
| Cast refs (Grandma, Grandpa, Emma, Leo 8 each; Michael, Sarah, Cooper 3 each; ~4 retakes) | 45 | $0.14 | $6.30 |
| REF-P5 scale plate (2 frames + 1 retake) | 3 | $0.14 | $0.42 |
| L1 empty-room plate | 1 | $0.14 | $0.14 |
| First frames: H76 3, H79 3, B2 5, B4 3, B6a 3, B6b 2 | 19 | $0.14 | $2.66 |
| First frame B3 plate (no faces) | 2 | $0.04 | $0.08 |
| Video drafts: H76 3, H79 4, B3 2, B4 3, B6a 4, B6b 3 (5s each) | 19 | $0.36 | $6.84 |
| **Planned subtotal** | | | **$16.44** |
| Reserve: ~1 extra take per video shot + ~7 image retakes | 6 + 7 | | $3.14 |
| Reserve: re-run the 6 keepers at 1080p if the tool offers it (price unconfirmed, assumed ~2.25×) | 6 | ~$0.81 | $4.86 |
| **Ceiling** | | | **≈ $24.50** |

Already spent on K01: turntable share ~$0.10, test clip $0.36, beat-2 stills $0.28 (≈ $0.74).
**K01 share of the $300 production cap: ≈ $25 (8%)**, under the even share of $50 per concept. Hard stop: more than 8 takes on any shot → fallback (round-wide rule 10).
Owner action: AtlasCloud balance is ~$15. The planned subtotal alone ($16.44) is above it, so top up before Gate B work starts.

## 3 · Order of work (cheapest failure first)

1. **Gate B refs:** views 1–3 for all seven, then REF-P5 and L1 (≈ $3.50). 07 shot mode → owner. Then views 4–8 for the four main cast.
2. **B2 re-stage** (the control's riskiest frame, $0.70). 07 decides the re-stage vs the take-2 fallback.
3. **All first frames** (≈ $2.00). 07 checks identity, scale and casting at image prices before any video.
4. **Video drafts**, one shot at a time, 3–4 takes each, one variable changed per retry; self-check §2.7 on ≥5 full-res frames; mark usable windows.
5. 06 composites the real render onto every ornament face, builds B2/B3/B5 moves, B6b sway.
6. Hold B5 until 04 rules (shotlist § BLOCKED).

## 4 · Edit-side moves and composites (handoff to 06)

| shot_id | Move parameters | Composite |
|---|---|---|
| K01-B2 | Still 2K (1536×2752) or 4K. Start crop = full width, centred. End crop width = start/1.06, centre on the box (x mid, y = box centre). 2.6s, linear for 60% then ease-out. | Real render corner-pinned onto the ornament in the box (static, 4 corners) |
| K01-B3 | Over the locked composite: scale 100% → 110% centred on Cooper's figure, 2.3s, ease-in-out | Static corner-pin of the real render; fingertip layer kept above it where it overlaps the cut edge |
| K01-B5 | Source = SVG at 2× (6370 px wide). In 1× units: start crop width 850 px centred on Michael–Leo (x ≈2150) on the name row; end = whole ornament inside output y 500–1280 (crop width ≈4150, s≈0.26). Position eases out (moves early), scale eases in (widens late), 3.2s. 06 tabulates each name's width per frame for E39. **On hold for 04.** | Render on a blurred L1 plate with a soft contact shadow |
| K01-B6b | Sway in post on the 2D layer: rotation about the hanger hole, ±2°, one slow cycle (~2.2s) decaying, starting when the hands clear (~0.9s into the window) | Planar track of the real render; the gold cord kept from the plate |
| H76, H79, B4, B6a | n/a (camera move is in the generated clip) | Planar 4-corner track per clip; H76 lid roto ~0.0–0.6s; B6a fingertip layer at the cut edge |

## 5 · Known risks (for 06/07)

1. **B5 is blocked:** line 1 of its caption is 1,436 px vs 950 px safe width (E4/E57), and E39 (names ≥100 px) cannot coexist with a caption band that avoids the print (E60). 04/owner decision.
2. **B2 trade-off:** pulling back so the faces clear the band and the box clears the bottom UI zone shrinks the faces (~60–80 px). If readability drops, the fallback keeps take 2's scale and accepts the box partly under the bottom UI in 9:16 (fine in 4:5).
3. **B3 resolution:** the figure layers in the SVG are Teeinblue `_large.webp` rasters. Cooper is ~290 px wide in the 3,185 px render. Check the layer's native size before final; if it is too soft at ≥450 px, frame B3 as a CU (Cooper ~300 px) instead of an ECU.
4. **H79 hug:** two faces + a fast embrace, the highest AI-tell risk; 4 takes budgeted; 07 AI-tell pass.
5. **Spin:** any free-hanging moment in B6b; the window is cut before rotation; STILL+MOVE fallback.
6. **Tracking:** hand-held ornaments (B4, B6a) need a stable planar track; the briefs keep thumbs on the cut edges and the face ±10° of square.
7. **Frame-1 overlap with K04 H33** (both open on a kraft box and hands). Producer: confirm the two differ in ≥2 of setting/cast/framing/colour.
8. **Tool fit:** confirm in the Seedance adapter whether Atlas ref-to-video can pin the first frame (the K01 test used refs only). If not, run the shots as image-to-video from the first frame, with the turntable carried by the first frame.

## 6 · Scene ledger (O6)
`marketing/facebook-ads/_ledgers/scene-ledger.csv` is empty. Rows for K01's shipped shots are written when the ads ship, not now. B2, B3, B4, B5, B6a, B6b and B7 are byte-identical across `-H76` and `-H79` (controlled test reuse, logged). Tell the media buyer Meta may treat the two as one creative.
