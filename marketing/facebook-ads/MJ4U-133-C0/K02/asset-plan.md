# MJ4U-133-K02 · asset plan and budget (role 05, O4)

Planning pass 2026-11-25: **$0 spent.** Prices (AtlasCloud, Producer brief): Nano Banana Pro Edit **$0.14/img** · Seedream v5 Pro Edit ~$0.04/img · Seedance 2.0 Fast ref-to-video **$0.072/s at 720p** (K01 test: 5s = $0.36). Video takes are made at 720p and the keeper is the final (a Seedance re-render at another resolution is a different clip); keepers are upscaled in post.

## Reuse vs new

| Asset | Status | Source |
|---|---|---|
| K02 printed face (all beats) | **REUSE** | `renders/MJ4U-133-K02-render.png` (real personalizer export) |
| Ornament body refs | **REUSE** | `turntable/K02/K02-34left.jpg`, `K02-34right.jpg` |
| Beat 4 proof (STILL+MOVE) | **REUSE**, $0 | the render + a blurred frame of the B3 keeper |
| End card 17.5–20.0 | **SHARED** (not K02's cost) | round plate (hero on the tree) |
| "DAD'S LIST" lettering | **NEW, $0** | PIL handwriting font or an owner phone photo (composited) |
| Cast refs C1–C6 | **NEW** | 40 images (Nano Banana Pro Edit) |
| Scale plate | **NEW** | 1 image (+1) |
| First frames (6 shots) | **NEW** | Nano Banana Pro Edit |
| Video (6 shots) | **NEW** | Seedance 2.0 Fast ref-to-video |
| K01 beat-2 stills | not reusable | different cast |

Scene ledger: K02 body is reused byte-identical across H61/H63 (controlled test, E13, log as deliberate). No cross-concept reuse planned. Rows go into `marketing/facebook-ads/_ledgers/scene-ledger.csv` when the ads ship (O6).

## Cost

| Line | Count | Unit | Cost |
|---|---|---|---|
| Cast refs (Jacob, Mary, Kobe, Susan × 8; Bailey, Luna × 4) | 40 | $0.14 | $5.60 |
| Scale plate | 2 | $0.14 | $0.28 |
| Ref re-rolls (~30%) | 12 | $0.14 | $1.68 |
| **Refs subtotal (Gate B)** | | | **$7.56** |
| First frames: H61 3 · H63 2 · B2 3 · B3 3 · B5a 4 · B5b 3 | 18 | $0.14 | $2.52 |
| Video H61: 3 takes × 5s | 15 s | $0.072 | $1.08 |
| Video H63: 2 × 5s | 10 s | $0.072 | $0.72 |
| Video B2: 4 × 5s | 20 s | $0.072 | $1.44 |
| Video B3: 3 × 6s | 18 s | $0.072 | $1.30 |
| Video B5a: 4 × 5s | 20 s | $0.072 | $1.44 |
| Video B5b: 4 × 5s | 20 s | $0.072 | $1.44 |
| **Scenes subtotal** | 103 s video + 18 stills | | **$9.94** |
| **K02 planned total** | | | **≈ $17.50** |
| Contingency: B2, B5a, B5b to the 8-take cap (+4 takes × 5s each, +4 first frames total) | 60 s + 4 | | +$4.88 |
| **K02 ceiling** | | | **≈ $22.40** |

Share of the $300 production cap: **≈ 5.8% planned, ≈ 7.5% at the ceiling** (an even split of six concepts is $50; council estimate for the round ≈ $120–150). AtlasCloud balance is ≈ $15 today: K02's Gate B refs ($7.56) fit, the scene work needs the owner's top-up.

Cheaper option (not recommended for faces): views 4–8 of each person on Seedream ($0.04) instead of Nano Banana Pro saves ≈ $2.50, at an identity-drift risk on hands and expressions.

## Order of work (each step gated)

1. Owner: skin-tone decision (re-export the render, free) → `refs/REFS-PLAN.md`.
2. Refs C1–C6 + scale plate ($7.56) → contact sheet → **07 shot mode → owner = Gate B.**
3. First frames for all six generated shots ($2.52) → 07 (identity drift is caught at image prices).
4. Video drafts, hardest first: B5a, B2, B5b, then B3, H61, H63; change one variable per retry; stop at 8 takes per shot and use the fallback.
5. Self-check §2.7 on ≥5 full-res frames per take; mark usable in/out windows → 07 shot mode.
6. Post: planar-track the render onto the placeholder (H61, B2, B3, B5a, B5b; 2D track for H63), composite the lettering, build the B4 pan, upscale keepers → handoff to 06.

## Post work 05 hands to 06 (no generation cost)
- Corner-pin tracking of the K02 render on 5 moving shots + 1 top-down 2D track (R3 in the shot list).
- B4 move parameters (shot list): scale 0.70, centre x 900→2300 source px, names at frame y 1150–1230, cubic ease, 3.2s; 4:5 variant.
- H63 post push-in 100→110% centred (540, 900) and the lettering plate at x 250–830, y 560–880.
- B5b optional sway on the 2D layer (≤3°, damped).
