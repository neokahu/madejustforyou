# MJ4U-133-C0 · K04 · asset plan and budget (O4) · role 05, 2026-11-25

Planning pass: **$0 spent.** Prices (BRIEF for 05, Atlas): Nano Banana Pro Edit $0.14/img · Seedream v5 Pro Edit ~$0.04/img · Seedance 2.0 Fast ref-to-video $0.072/s at 720p (matches the K01 test: 5 s = $0.36). Final-res video price is **not verified**: assumed ≈$0.16/s at 1080p; check `atlas_get_model_costs` before Gate C, or upscale the 720p keeper instead.
AtlasCloud balance ≈ $15: the owner tops up before Gate B.

## 1. Reuse vs new, per shot
| shot_id | REUSE (exists) | NEW generated | NEW post-only (free) |
|---|---|---|---|
| K04-1A | render, turntable ¾L/¾R | F1 still, video clip | render tracked over the face; 4% push |
| K04-1B | render | PROP-young-grandpa, 1B-R plate | split, fade→colour grade, push, render warp |
| K04-B2 | render, screen recording | F1 still, video clip | render static comp; screen before/after plates (cursor patch); green key |
| K04-B3 | render | F1 still, video clip | render static comp; 6% push |
| K04-B4 | render | plate | composite at native res; push 1200→1500 px |
| K04-B5a | render, turntable | F1 still, video clip | render tracked |
| K04-B5b | render, turntable | F1 still, video clip | render tracked |
| K04-B6 | shared end card (Producer) | — | — |
Shared across shots: REF-C1…C4 sets, PROP-lastyear-photo (B2, B3), scale plate (all).

## 2. Cost estimate
| Item | Tool (adapter) | Units | Cost |
|---|---|---|---|
| REF-C1 Grandpa (8 views; v1–3 ×2, v4–8 ×1, +2 retakes) | Nano Banana Pro Edit | 13 | $1.82 |
| REF-C2 Grandma (same) | NBP Edit | 13 | $1.82 |
| REF-C3 Olivia (same, +1 hands retake) | NBP Edit | 14 | $1.96 |
| REF-C4 Rosie (3 views ×2) | NBP Edit | 6 | $0.84 |
| PROP-lastyear-photo | NBP Edit | 3 | $0.42 |
| PROP-young-grandpa (+1 age edit) | NBP Edit | 4 | $0.56 |
| PROD-scale-plate | Seedream v5 Pro Edit | 2 | $0.08 |
| K04-1B-R plate | NBP Edit | 2 | $0.28 |
| F1 stills: 1A, B2, B3, B5a, B5b (3 takes each) | NBP Edit | 15 | $2.10 |
| K04-B4 plate | Seedream v5 Pro Edit | 2 | $0.08 |
| **Images subtotal** | | **74** | **$9.96** |
| K04-1A clip, 4 s × 5 takes | Seedance 2.0 Fast r2v 720p | 20 s | $1.44 |
| K04-B2 clip, 6 s × 3 | same | 18 s | $1.30 |
| K04-B3 clip, 4 s × 3 | same | 12 s | $0.86 |
| K04-B5a clip, 4 s × 4 | same | 16 s | $1.15 |
| K04-B5b clip, 5 s × 4 | same | 20 s | $1.44 |
| **Video drafts subtotal** | | **86 s** | **$6.19** |
| Final-res re-run of 5 keepers (23 s, ≈$0.16/s, unverified) | same, 1080p | 23 s | ≈$3.68 |
| **PLANNED TOTAL** | | | **≈ $19.83** |
| Contingency: B2 fallback (4 keyframe edits + 3 first/last clips × 2 takes) | NBP + video | 4 img + 24 s | $2.29 |
| Contingency: takes 6–8 on 1A, 5–8 on B5a/B5b | video | 48 s | $3.46 |
| **CEILING (stop and ask above it)** | | | **≈ $25.6; hard stop $30** |
K04's share of the $300 production cap (1/6) is $50. Council rule 10 puts the whole round at ~$120–150, i.e. ~$20–25 a concept; K04 plans at ~$20 and caps at $30. Past 8 takes on any shot, use the shot's fallback (rule 10), not more re-rolls.

## 3. Order of work (each step gates the next)
1. **Free, now:** tracking test (OpenCV homography) on `turntable/K01/K01-test-hang-seedance.mp4`; cut the screen before/after plates and verify ≥5 frames each at full res; owner decides on the optional real-phone re-record.
2. **Gate B build:** REF-C1/C2/C3/C4 → PROP-lastyear-photo, PROP-young-grandpa → scale plate, 1B-R plate. Contact sheets + match sheets → **07 shot mode → owner.** (~$7.9)
3. **Arm-B frame-1 check (no reserve):** build the 1B still from the locked props (post only, free); 07 + a fresh muted cold read. If it fails, stop arm B and tell the Producer (01 owes a new F7×T3 card).
4. **F1 stills** (image-first, rule 3): 1A, B2, B3, B5a, B5b, B4 plate → 07 shot mode. (~$2.2)
5. **Video drafts** at 720p, takes as above, one variable changed per retry → self-check §2.7 on ≥5 full-res frames per clip, usable in/out marked → 07 shot mode. (~$6.2)
6. **Finals:** keepers at final res; composites (render static/tracked, screen plates, split), moves on stills at native res → handoff to 06.

## 4. Handoff to 06 / 07 (per ad, when built)
Shot list with verified in/out windows · `refs/` · accepted assets named by shot_id · composite recipes: render homography (static: 1B, B2, B3, B4; tracked: 1A, B5a, B5b) and screen-plate key · move parameters: 1A push 100→104% linear centred on the ornament; 1B push 100→104% ease-out centred (540, 860); B3 push 100→106% ease-in-out; B4 render width 1200→1500 px, centre (0.50, 0.53)@(540, 946) → (0.70, 0.55)@(560, 1110), ease-in-out, 0.4 s near-hold at start · caption band 9:16 y 300–500 · frame-1 pack and thumbnail (shotlist O5) · known risks (§5).

## 5. Known risks
| Risk | Shot | Likelihood | Mitigation / fallback |
|---|---|---|---|
| Planar tracking of a hand-held flat sheet with no tracker in the stack | 1A, B5a, B5b | medium-high | free test first; fallback: shorter 1A lift; B5 ornament held still on the palm (already briefed) |
| Ornament spins or shows its back while lifted by the cord | 1A | medium | thumb on the tab; ±15° yaw acceptance; 2.0 s window only; fallback lift |
| Multi-stop finger path not followed | B2 | medium | segmented first/last-frame fallback (budgeted) |
| Green phone screen not uniform / spill on the finger | B2 | low-medium | hand roto ≤12 frames around the tap |
| Young-Grandpa photo does not read as the same man | 1B | medium | edit pass from REF-C1; 07 + cold read at Gate B; arm B has no reserve |
| Photo-to-portrait misread persists in arm B (03 §7.3 S2 flag) | 1B + B2 | open | the phone insert ships in the body (mandatory); Gate D human read |
| Year lower edge in the 9:16 bottom zone | B4 | low | start width 1180 fallback |
| Phone glasses row under the Reels overlay | B2 | certain with the current recording | owner re-record (free) or accept (preview change is in the safe zone; 4:5 shows all) |

## 6. Draft scene-ledger rows (O6 is written at ship, not now)
`setting · cast · presentation · size+move · palette/light · frame1`
- 1A: kitchen table, light oak · C3 hands · box, hero · CU high angle, locked+push · cream/kraft, daylight left · frame1 (arm A)
- 1B: plain cream backdrop split · young C1 photo + print · hero crop · split, push · cream, soft key left · frame1 (arm B)
- B2: same table, top-down · C3 hand · flat-lay with photo + phone · MS locked · daylight left
- B3/B4: same table, box · C3 hands / none · upright · MCU push / CU→ECU push · daylight left
- B5a/B5b: living room, sage-green wall, beige sofa · C1, C2, C3, C4 · in hand · MCU push-in / MS pull-back · daylight left, warm tree bokeh right
Cross-concept check for the Producer: K01 also has an aged Grandpa in round glasses and a living-room box-opening; K04's cast (deep brown skin), room (sage-green wall) and frame 1 differ. Confirm against K01's 05 plan when it lands.


## Reference budget rework (owner ruling 2026-11-25, BRIEF.md item 8) — supersedes the reference rows above
- **Gate B (now):** Grandpa, Grandma, Olivia, Rosie × views 1–3 (NBP) = 12 img $1.68 + scale plate $0.28 + 1B-R plate $0.14 → **$2.10 (≈$2.60)**. Views 1–3 = front · ¾ · profile/full body; a person never gets more than 3 views before Gate B.
- **After Gate B:** views 4–8 Seedream for the 3 people (15 img) $0.60 + identity photos (last year's, young Grandpa; NBP, 2 takes each) $0.56. Views 4–8 only for people with close-ups, on Seedream v5 Pro Edit with views 1–3 as the references (refs = 1–3, never a previous new view). Background people stay at ≤3 views.
- If 07 finds Seedream drifts identity on views 4–8, re-make only the failing views on Nano Banana Pro.
