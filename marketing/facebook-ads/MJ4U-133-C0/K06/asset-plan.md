# K06 · O4 asset plan and budget (role 05, planning pass, 2026-11-25)

Prices are the producer's current Atlas list: Nano Banana Pro Edit **$0.14/img** · Seedream v5 Pro Edit ≈$0.04/img · Seedance 2.0 Fast ref-to-video **$0.072/s at 720p**. Two prices are not verified: the NBP 4K output price (budgeted at $0.24) and Seedance 1080p (not budgeted). The Atlas MCP has no price-list call, only past spend.

## Per shot: reuse vs new

| Shot | Source | REUSE | NEW (generated) | Post-only work (06) |
|---|---|---|---|---|
| A-1 | STILL+MOVE | render · turntables | P1 (shared) | 2-layer comp, push, bokeh twinkle |
| B-1 | STILL+MOVE | render · P1 | — | ECU → snap pull, defocus ramp, sync hit |
| 2 | STILL+MOVE | render · P1 | — | lateral slide, defocus |
| 3 | GEN-VIDEO plate | render · P1 · turntables | V3 | reverse, planar track of the render |
| 4 | STILL+MOVE | render · P1 | — | push, defocus |
| 5a | GEN-VIDEO | turntables · render · cast refs | F5a, V5a | track + fingertip roto + post sway on the render |
| 5b | GEN-VIDEO | turntables · render · cast refs | F5b, V5b | track the render |
| 6 | shared end card | round asset | — (round-level) | — |
| refs | — | render, turntables (exist) | C1–C4 ×8, SA1 | contact sheet |

Of the 17.5 s of K06-only picture, 9.2 s (hook, 2 and 4) costs only P1. Beats 1–4 add one video plate (V3, 2.8 s).

## Generation count and cost

| Asset | Model | Units × takes | Est. |
|---|---|---|---|
| Cast refs C1–C4 (8 views each) | NBP Edit 2K | 32 + 8 re-rolls = 40 img | $5.60 |
| SA1 scale plate | NBP Edit 2K | 2 img | $0.28 |
| P1 tree plate | NBP Edit 2K drafts + 4K final | 3 × $0.14 + 1 × $0.24 | $0.66 |
| F5a first frame | NBP Edit 2K | 4 img | $0.56 |
| F5b first frame | NBP Edit 2K | 4 img | $0.56 |
| V3 parallax plate | Seedance 2.0 Fast r2v 720p | 5 s × 3 | $1.08 |
| V5a | Seedance 2.0 Fast r2v 720p | 5 s × 4 | $1.44 |
| V5b | Seedance 2.0 Fast r2v 720p | 5 s × 4 | $1.44 |
| **Planned total** | | 53 images · 55 s video | **≈ $11.6** |
| Re-roll reserve (rule 10: stop at 8 takes per shot) | +4 takes each on V5a/V5b, +2 on V3, +6 images | | +$4.0 |
| **Ceiling** | | | **≈ $15.6** |
| Optional | P1-clean (post sway on hanging shots) $0.14 · Seedance 1080p for 5a/5b (unpriced) | | — |

**Share of the $300 cap:** ≈ $12 planned (4%), $16 ceiling (5%). That is well under 1/6 of the round's ~$150 generation budget (rule 10), which leaves headroom for K01 b2, K02 5a and K10 b7.

## Order of work (each step gated by its check)

1. **Cast views 1–3** for Sofia, Mom, Mateo and Dad ($1.7) → 07 identity and print-match check → views 4–8 ($3.9).
2. **SA1** ($0.28).
3. **GATE B**: 07 shot mode on refs/ → owner sign-off.
4. **P1** in 2K drafts → keeper → 4K. 06 tests the 4-point registration of the render before anything else uses P1.
5. **Product beats in post** (A-1, B-1, 2, 4) at $0. They give the owner a viewable 0–12 s animatic before any video spend.
6. **V3** → window and track check. Fallback is the free 2.5D pull-back.
7. **F5a → V5a**, then **F5b → V5b**: image first, 07 shot check on the first frame, then video.
8. Final pass: composite the render over V3, V5a and V5b. Export the frame-1 pack and the thumbnail (shotlist §4).

## Takes policy

Images: draft 2K, select from N, change one variable per retry. Video: 720p is both draft and final, because Seedance is not seed-reproducible at a new resolution, so the first frame is the cheap gate. Past 8 takes on any shot, use the named fallback (V3: 2.5D still; V5b: head-turn variant, which needs 04's OK). Don't keep re-rolling.
