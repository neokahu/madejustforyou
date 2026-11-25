# Gate C prep — views 4–8 + image first frames (2026-11-25, Producer)

Gate B is approved (BRIEF.md). For your concept only:
1. **Views 4–8** for people with close-ups only (your asset plan's rework section), on `bytedance/seedream-v5.0-pro/edit` at size ≤2.61 MP (e.g. "1776*2368" bills ≈$0.077; "1536*1536" or smaller ≈$0.036), refs = that person's approved views 1–3 (never a newer view). Plus any extra view 07 listed as "needed before shot X" in `<K>/refs/07-GATE-B.md` (full body, hands, ring).
2. **Image first frames** for every generated video shot in your shotlist (and the stills that ship as still + move), using the approved cast refs + the turntable views for the ornament body (E37 amended: generated ornament face is a placeholder). Nano Banana Pro Edit 2k, 9:16, 4:5-safe centre. ≤2 takes per frame unless it fails.
3. **No video.** Video waits for the owner's top-up.
Rules: prompt-method docs + guard; download only via `scripts/atlas_poll.sh` with `LEDGER_PURPOSE=refs` (views) or `LEDGER_PURPOSE=first-frames` so every job lands in the cost ledger; self-check every image at full res (identity vs refs and print, hands, casting vs captions, ornament face-on, scale per BRIEF: K01 7 in, others 5 in); contact sheet `<K>/first-frames/contact.jpg` and notes `<K>/first-frames/FIRST-FRAMES.md`. Media under `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/<K>/`. Do not commit.

## Re-take round (2026-11-25, after 07 first-frames review) — checklist 05 must apply before calling a frame PASS
07 failed ~24 frames that 05 self-passed. Check every take for these before keeping it:
1. **Rings:** only where ruled (K10 couple gold bands). Everyone else, including K13 Mom, has bare fingers.
2. **Ornament scale** vs the hand/branch: K01 = 7 in, all others = 5 in. Size is fixed in the first frame; rescaling a moving shot in post is not allowed.
3. **Trousers** match the cast table (tartan where printed); no default jeans/khakis.
4. ≤3 sharp faces; ornament outline = the turntable (no plank, bauble or plaque); casting/skin tone vs the approved refs.
Read `<K>/first-frames/07-SHOT.md` and `first-frames-07-SUMMARY.md` and re-take only what 07 lists.

## Ornament-free plate method (2026-11-26)
For a shot where the model will not hold the ornament's size: prompt the same scene with the ornament absent (the branch tip empty with the gold cord's hook point visible, or the hands cupped/posed around an empty 5 in (K01: 7 in) gap at the right height), keep everything else identical. 06 composites the real render at the scale anchored by the hand/branch, adds a contact shadow and (if hanging) a gentle sway on the 2D layer. Video is generated from the ornament-free plate; the composite is tracked per shot (`scripts/track_composite_test.py` method).
