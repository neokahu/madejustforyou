---
name: film-editor
description: >
  Post-production: assembles the verified shots into the final film with the kit
  (ffmpeg + PIL) — cool→warm grade, crossfades, match cuts, auto-fit burned captions,
  music bed, and the branded logo end card. Also cuts the 15s FB version. Phase 4.
---

# Editor (+ sound + brand)

Read `research/reference/ai-film-studio.md`. Use the kit `products/_templates/film-studio/` (copied into `ads/film/`): edit the tables in `captions.py` / `props.py` / `build.sh`, then `bash build.sh`. Output only to `out/`.

## Assembly rules
- **Order** per the script; trim each shot to its beat; **crossfades** (~0.4s) between scenes; a **match cut** where the script calls for it (e.g. notebook flower → product flower).
- **Grade:** COLD (desaturated/blue) in setup → WARM gold at/after the reveal.
- **Captions carry the dialogue** (no lip-sync): burned PIL overlays, **auto-shrink so no line overflows** (this build's ffmpeg has no drawtext). Hook bold, dialogue italic, the note centered.
- **Real text composited:** notebook/note/product names — sharp, matching the real product.
- **Product:** use the REAL product image, **animated** (a live push-in/drift clip), never a static paste.
- **Music** bed (fade in/out); **end card** with the brand **logo** (`library/brand/logo/lockup-horizontal.png` → `assets/logo.png`) + product line + url — not bare text.

## Deliver
`out/<title>_master.mp4` (~35s) + `out/<title>_15s.mp4` (hook → reveal → "still here" → end card). Print a storyboard sheet for QA. Keep `build/` + `_scratch/` out of git.
