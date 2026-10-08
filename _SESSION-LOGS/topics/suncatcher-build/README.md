# Topic — Suncatcher build (dog memorial, German Shepherd "Alex")

**Status:** testing done; build waits on script revision + REF-OWNER fixes + REF-GIVER set.

## Product
Printed acrylic panel — stained-glass landscape, solid black silhouette, name in small white script *inside* the silhouette. The name/florals are the panel's **most translucent** areas → read as bright script inside the shadow on the wall. Artwork already runs cool→warm.

## Current decisions
- Beat 3: room floods blue-and-gold, Alex's shadow falls across the wall with his name glowing inside it.
- Close-up = 4K still (REF-PANEL-SCENE) + ffmpeg Ken Burns at native res; compositing engine removed.
- One video model for the whole build: Seedance 2.0. Video now via AtlasCloud (see [platforms-and-cost](../platforms-and-cost/README.md)).
- Shared hook pair across three bodies (14 clips → 12).

## Test results
A scale ✅ · B identity ✅ · C motion+fidelity ✅ (after prompt fix) · E people ✅ (hook3 14.90 / motion 14.96) · F name rendering ✅ stills / ⚠️ video drifts typeface.

## Open items
1. Revise `PHASE1-SUNCATCHER-shooting-scripts.md` per `script-method.md` §4a (Hook 2, Body C) — not yet edited.
2. Regenerate `owner-hands` + `owner-expr-relief` — see [character-references](../character-references/README.md).
3. Build REF-GIVER set (blocks clips 6–11).
4. Vertical slice S-C1-H1 on AtlasCloud `reference_to_video`, all 8 owner refs (~$2).

## Assets
- Committed (force-added): `products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png`, `REF-ALEX-PHOTO.png`.
- Local only: `assets/turntable-owner/*` and 12 clips in `tests/`.

## Detail
- `marketing/facebook-ads/PHASE1-SUNCATCHER-video-build-plan.md` · `PHASE1-SUNCATCHER-shooting-scripts.md`
- Sessions: [2026-09-25](../../sessions/2026-09-25-topview-evaluated-seedance-method.md) · [2026-09-26](../../sessions/2026-09-26-testing-complete-both-products.md) · [2026-10-08](../../sessions/2026-10-08-research-consolidated-handoff.md)
