# MJ4U-133-K13 · asset plan and budget (role 05, O4)

> Planning pass 2026-11-25; no spend. Prices are the Producer's current Atlas figures: Nano Banana Pro Edit $0.14/img, Seedream v5 Pro Edit ~$0.04/img, Seedance 2.0 Fast ref-to-video $0.072/s at 720p. The 1080p final rate is **not given**: estimated at $0.16/s; confirm with `atlas_get_model_costs` before Gate C.
> Seedance clips are budgeted at 5 s each (the K01 test length); each edit window is trimmed from inside the verified window.

## 1. Reuse vs new, per shot

| shot | source | reuse | new assets |
|---|---|---|---|
| 1A (H16) | GEN-VIDEO from image | render, turntable | first frame ×3, clip ×4 |
| 1Ba (H17) | STILL+MOVE | render, turntable, B6 set | still ×3 |
| 1Bb (H17) | STILL+MOVE | render, turntable | plate ×3 |
| B2 | GEN-VIDEO from image | render, turntable | first frame ×3, clip ×3 |
| B3 | GEN-VIDEO from image | render, turntable | first frame ×3, clip ×3 |
| B4 | STILL+MOVE (real artwork) | **render (no generation)**; background = blurred B5 plate | none |
| B5 | GEN-VIDEO from image | render, turntable | first frame ×3, clip ×3 |
| B6 | GEN-VIDEO from image | render, turntable | first frame ×3, clip ×4 |
| B7 | shared end card | **REUSE** (round-wide, not K13's spend) | none |
| refs | cast C1–C3, P1, X1, L1 | render, turntable | see §2 |

Body (2.0–20.0) is built once and shared by both ads (E13): no duplicate generation.

## 2. Cost estimate

| Item | Count | Model | Unit | Cost |
|---|---|---|---|---|
| Cast sets C1–C3, 8 views × 2 variants | 48 img | NB Pro Edit | $0.14 | $6.72 |
| Scale plates P1a, P1b × 2 | 4 img | NB Pro Edit | $0.14 | $0.56 |
| Collar X1 + room L1 × 2 | 4 img | NB Pro Edit | $0.14 | $0.56 |
| First frames 1A, B2, B3, B5, B6 × 3 | 15 img | NB Pro Edit | $0.14 | $2.10 |
| H17 stills 1Ba, 1Bb × 3 | 6 img | NB Pro Edit | $0.14 | $0.84 |
| **Images subtotal** | 77 | | | **$10.78** |
| Video drafts (17 takes × 5 s, 720p) | 85 s | Seedance 2.0 Fast | $0.072/s | $6.12 |
| Finals (5 keepers × 5 s, 1080p) | 25 s | Seedance 2.0 Fast | ~$0.16/s (est.) | ~$4.00 |
| **Video subtotal** | | | | **~$10.12** |
| **Planned total** | | | | **≈ $20.90** |
| Contingency: 1A and B6 up to the 8-take cap (+8 × $0.36), image retries (~$2) | | | | ≈ $4.90 |
| **Ceiling for K13** | | | | **≈ $26** (≈ 9% of the $300 cap) |

Savings option: views 4–8 of the cast sets on Seedream v5 Pro Edit instead of NB Pro (30 img × $0.10 less) saves ≈$3, at some identity risk; only if 07 passes Seedream identity on view 4 first.

Current AtlasCloud balance ≈ $15: K13 alone exceeds it once video starts. The owner top-up is needed before Gate B work begins.

## 3. Order of work (each step gated)
1. L1 room master, X1 collar (cheap; fixes the set). 
2. C1–C3 views 1–3 → 07 check → views 4–8. P1a/P1b with the real render composited.
3. **Gate B:** 07 shot mode on all refs, then the owner.
4. FF-B6 (set master) → 1Ba, 1Bb stills from it (same bed, collar, branch).
5. FF-1A, FF-B2, FF-B3, FF-B5 → 07 image check (identity drift caught at image prices).
6. Video drafts at 720p, one variable changed per retry; self-check §2.7 on ≥5 frames per clip; mark usable windows → 07 shot mode.
7. Finals of the keepers; composite the real render (planar tracks: 1A raising hand, B2 edge, B3 palm, B5 ¾ hanging, B6 hanging); composite "BISCUIT" on the tag (1A, 1Ba, B2, B6); B4 pan and 1Ba/1Bb moves built at native resolution.
8. Thumbnail still from B6 ≈17.3 s; frame-1 pack per arm (shotlist §2).

## 4. Post work that 06 must budget (time, not money)
Planar tracking on 5 generated clips, one of them a moving hand-held raise (1A, rule 1 exception); tag-text tracking on a swinging tag (1A) and a turning collar (B2); 2D sway on 1Bb and B5; a depth composite in B6 if the plate's depth of field fails.
