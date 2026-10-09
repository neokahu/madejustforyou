# Topic — Suncatcher build (dog memorial, German Shepherd "Alex")

**Status:** ✅ 3 ads BUILT 2026-10-08 (S-C6 video, S-C1 video, S-STATIC) — awaiting user review + upload.

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
1. User: listen to music bed · confirm delivery promise · approve upload (review: https://claude.ai/artifact/QHgZNZfk24WQzCb376NSFz).
2. Extend `engine/upload_draft.py` (2 videos + 1 image), write `ads/ad-content.json`, upload PAUSED.
3. Parked: Body B, Hook 2 (late-reveal T1 test), breed-swap variants, who-buys check (Ad Library).

## Build (2026-10-08)
Revisions after user review: S-C6 hand-off recast (friend → grieving woman); S-C1 framed photo regenerated (old one was a face-swap). kie.ai is out of credits — use AtlasCloud `google/nano-banana-pro/edit`.

Script v2 = `PHASE1-SUNCATCHER-shooting-scripts.md` (council-shaped). `ads/build_v2.py` rebuilds everything from
`ads/frames/` + `ads/shots/`. Both videos pass motion_qa gate (hook3 17.3 / 16.2). Name in every read beat is real artwork.

## Assets
- Committed (force-added): `products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png`, `REF-ALEX-PHOTO.png`.
- Media is gitignored and backed up to `gdrive:madejustforyou/repo/products/suncatcher-dog-memorial/` (scripts/backup-media.sh).

## Detail
- `marketing/facebook-ads/PHASE1-SUNCATCHER-video-build-plan.md` · `PHASE1-SUNCATCHER-shooting-scripts.md`
- Sessions: [2026-09-25](../../sessions/2026-09-25-topview-evaluated-seedance-method.md) · [2026-09-26](../../sessions/2026-09-26-testing-complete-both-products.md) · [2026-10-08](../../sessions/2026-10-08-research-consolidated-handoff.md) · [2026-10-08b](../../sessions/2026-10-08b-suncatcher-ads-built.md)
