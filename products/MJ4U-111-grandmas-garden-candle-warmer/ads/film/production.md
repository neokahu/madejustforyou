# Production — "Everyone Is Still in Your Garden" (MJ4U-111)

**Status:** DELIVERED (v2) · **Cost:** ≈$9 (720p, clean path) · **Res:** 720p · Format: 9:16, ~36s
Pipeline + rules: `research/reference/ai-film-studio.md`. Script: `script.md`. First film built with the studio; reorganized into the STANDARD layout 2026-08-07.

## Product
- Real product photo: `refs/product/real-product.jpg` (hosted `…7a5bf379…`)
- Real personalization on the product (everything on screen matches these): **Sophia·Cosmos, Donna·Aster, Sharon·Rose, Helen·Marigold, Sarah·Poppy** · title "Grandma's Garden — Love Grows Here"

## Cast (turntables — `refs/cast/`)
| Character | Files | Hosted URL |
|---|---|---|
| Grandma | grandma-front.jpg, grandma-34R.jpg | `…cd108f54…` (¾-L) · `…254763c2…` (¾-R) |
| Granddaughter | granddaughter.jpg | `…b35404fd…` |
| Grandpa | grandpa.jpg | `…039dc0a3…` |

## Product turntable (`refs/product/`)
scale-anchored (beside mug) `product-scale-ref.jpg` `…12a759c5…` · lamp-34L/R.jpg

## Scenes (`shots/`, Seedance 2.0 Fast Ref-to-Video, 720p 9:16 5s)
sc1-breakin · sc2-hallway · sc3-notebook · sc4-caught · sc5-note · sc6-reveal · sc7-finds · sc8-hero · product-motion (live real product). 9 clips ≈ $8.8.

## Post
Real text composited (notebook/note/product names); cool→warm grade; crossfades; auto-fit captions; music `audio/music.mp3`; logo end card (`assets/logo.png`).

## Deliverables
- Master: `out/EveryoneStillInYourGarden_v2.mp4` (~36s) ✅
- 15s FB cut: ☐ (optional)
- Tracker `ad_status`: ☐ update when live

## Notes
- **As-built build scripts** are in `_scratch/as-built/` (build_v2.sh, captions.py, props.py, endcard_script.py) — kept for the record. The **canonical reusable build** is the kit `products/_templates/film-studio/`.
- `_scratch/` = old builds, verify frames, the earlier "Her Garden" film. `../_archive/` = obsolete pre-standard dirs (clips, scene-stills, scene-videos, product-turntable, source-images, final). Both are safe to delete once confirmed.
