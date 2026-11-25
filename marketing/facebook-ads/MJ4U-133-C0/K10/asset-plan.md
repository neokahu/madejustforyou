# MJ4U-133-K10 · asset plan and budget (role 05, O4) · planning pass

> 2026-11-25. Prices from the 05 brief (AtlasCloud): Nano Banana Pro Edit **$0.14/img** · Seedream v5 Pro Edit **~$0.04/img** · Seedance 2.0 Fast **$0.072/s at 720p** (5 s take = **$0.36**). 4K Nano Banana Pro price not given: estimated $0.24 (check `atlas_get_model_costs` before the B5 keeper). Nothing spent in this pass.

## 1. Reuse vs new, per shot
| shot | reuse | new (paid) | new (local, $0) | post work (06) |
|---|---|---|---|---|
| B1A | K10 render, ¾R turntable | 3 first frames, 3 video takes | DECORATIONS plate | corner-pin DECORATIONS (static); **4-corner track** of the render 0–1.5 s; push-in |
| B1B | render, ¾L | 3 stills | — | 3-layer masks, rack focus, render layer + sway, cord |
| B2 | render (hat crop) | 3 first frames, 3 takes | DECORATIONS, hat crop | static corner-pin, hat crop, pan |
| B3 | hat crop | 3 first frames, 3 takes | — | 2D track of the soft hat crop |
| B4 | render, ¾L | 3 first frames, 3 takes | — | **4-corner track** of the render (soft), static mask on Daniel, rack focus |
| B5 | render, ¾R | 3 stills 2K + 1 keeper 4K | — | flat composite at native res, pull-back (shotlist parameters), E39 measure |
| B6 | render, ¾L | 3 first frames, 3 takes | — | render layer over placeholder, sway on release, drawn cord, push-in |
| B7 | render | 3 first frames, 4 takes (cap 8) | — | render + cord composite, sway, drift |
| B8 | shared end card (06) | — | — | — |
Byte-identical reuse inside the test: B2–B8 shared by both K10 ads (E13, logged at ship). No reuse from other concepts (ledger empty).

## 2. Cost
| block | items | unit | cost |
|---|---|---|---|
| Cast refs | Daniel 8 + 2 extra variants (D6 hands, D7 expr) · Grace 8 + 2 (G6, G7) · Mochi 4 = 24 | $0.14 | $3.36 |
| Props | tree, moving box, kraft box, baubles = 4 | $0.04 | $0.16 |
| Locations | day, evening = 2 | $0.14 | $0.28 |
| Scale plates | palm, branch, each +1 retake = 4 | $0.14 | $0.56 |
| Ref retake allowance | 4 | $0.14 | $0.56 |
| **Gate B subtotal** | 38 images | | **$4.92** |
| First frames | B1A, B2, B3, B4, B6, B7 × 3 = 18 | $0.14 | $2.52 |
| Stills | B1B × 3, B5 × 3 = 6 (+ B5 4K keeper ≈ $0.24) | $0.14 | $1.08 |
| Video | B1A 3 + B2 3 + B3 3 + B4 3 + B6 3 + B7 4 = 19 takes × 5 s | $0.36 | $6.84 |
| **Planned total** | | | **$15.36** |
| Contingency | B7 to the 8-take cap (+4 = $1.44) · B1B fallback as a GEN-VIDEO plate if 07 calls it static (3 = $1.08) · +1 retake on 4 other video shots ($1.44) · 4 first-frame retakes ($0.56) | | $4.52 |
| **Ceiling** | | | **≈ $19.90** |
K10 share of the $300 production cap: **5.1 % planned, 6.6 % at ceiling** (an even 1/6 share is $50). Council rule 10 reserve for K10 b7 is the contingency line above; past 8 takes on B7 → the fallback in the brief, no more re-rolls.
Not budgeted: a 1080p re-render of video keepers (720p keepers are upscaled once to the 1080×1920 delivery, E19).

## 3. Order of work (after the owner tops up)
1. **Local, $0:** `text/DECORATIONS-marker.png`, `text/K10-hat-crop.png` from the render.
2. **Gate B refs ($4.92):** Daniel/Grace views 1–3 → views 4–8 (refs = 1–3) → Mochi M1 → M2–M4 → props → LOC-day → LOC-evening → scale plates.
3. **07 shot mode on refs, then the owner (GATE B)**; owner also rules on shotlist F5 (casting). No scene asset before sign-off.
4. **Riskiest first:** B7 first frame + 2 video takes (multi-body, council reserve) and B1A first frame + 1 take (tracking test for the moving box). If B7 fails 8 takes → fallback first frame.
5. Remaining first frames (3 each) → self-check → video takes → self-check §2.7 on ≥5 full-res frames per clip, mark in/out windows → 07 shot mode.
6. B1B and B5 stills (B5 keeper at 4K), composites, frame-1 pack (`frame1/K10-H01-f0.png`, `K10-H15-f0.png`) and thumbnail → hand to 06.
Back up every new file with `scripts/backup-media.sh`; nothing media goes into git.

## 4. Known risks (carried to 06/07)
| # | risk | where | mitigation |
|---|---|---|---|
| R1 | Tracking the real ornament face on a moving box with our toolchain (no planar tracker) | B1A, B4 | placeholder kept unoccluded, short windows (1.5 s / soft in B4); OpenCV homography on the placeholder's texture; B4 face softened |
| R2 | Multi-body action (turn + embrace + dog) | B7 | one action per subject, Mochi seated, ≤8 takes, fallback first frame in the embrace |
| R3 | Names ≥100 px vs safe zone vs caption band vs E67 | B5 | upper band; one pull-back; 07 ruling on E67 (shotlist F3) |
| R4 | 5 of 6 video prompts generated locked-off need `ACK-OPENMOVE`; post moves on upscaled 720p are slightly soft | B1A, B2, B4, B6, B7 | moves kept small (3–6 %); explain the ACK to the user |
| R5 | Ring drift (gold band appears/disappears, wrong hand) | every hand shot | must-not-change lists; QA every hand at full res |
| R6 | H15 hook is a still with a rack focus: motion gate (E34, report) may read low | B1B | 3-take GEN-VIDEO plate in contingency |
| R7 | Three C0 hooks open on hands + kraft box (K01 H76, K04 H33, K10 H01) | B1A | different setting, cast and framing; 07 checks E16 across the six 05 lists |
| R8 | Generated ornament under the render layer moves (spin) and its cord/edge shows | B6 (placeholder present) | opaque render covers the silhouette; generated cord painted out, cord drawn in post; reject if anything shows |


## Reference budget rework (owner ruling 2026-11-25, BRIEF.md item 8) — supersedes the reference rows above
- **Gate B (now):** Daniel, Grace, Mochi × views 1–3 (NBP) = 9 img $1.26 + 4 props + 2 rooms on Seedream $0.24 + scale plate $0.28 → **$1.78 (≈$2.20)**. Views 1–3 = front · ¾ · profile/full body; a person never gets more than 3 views before Gate B.
- **After Gate B:** views 4–8 Seedream for Daniel, Grace (10 img) $0.40 + Mochi view 4 $0.04. Views 4–8 only for people with close-ups, on Seedream v5 Pro Edit with views 1–3 as the references (refs = 1–3, never a previous new view). Background people stay at ≤3 views.
- If 07 finds Seedream drifts identity on views 4–8, re-make only the failing views on Nano Banana Pro.
