# MJ4U-111 product-reveal VIDEO — state for the next session (ChatCut)

**Goal:** a ~15–20s vertical (9:16, 1080×1920) product-reveal video. Direction (locked, from competitor teardown):
- **Focal hook** — open on an extreme macro of the lit lampshade (names + birth-flowers fill frame), then reveal.
- **Real motion** — push-ins, candle-flame flicker, glow breathing (NOT a static slideshow).
- **Text animates in over the clip** (kinetic captions), never a static text panel.
- Warm, emotional, product-as-hero, **no discount**. Copy voice: "A warm glow. A forever garden."

## Assets ready to feed ChatCut
- `clips/hook-macro.mp4` — 5s, **the hook**: AI motion (AtlasCloud Seedance) push-in on the lit shade, flame flickers, print stays sharp ("Alice · Grace · Jade"). 1080×1920.
- `out/hook-demo.mp4` — the hook clip WITH animated captions + music (proof of the format; ffmpeg).
- Scene stills (AtlasCloud Flux.2 Flex Edit — product un-pasted into real scenes, print preserved), in `../src/`:
  `scene-gift.jpg` (gift table, best), `01-scene-flux.jpg` (bedside), `scene-livingroom.jpg`, `scene-daytime.jpg` (has a "Bruce" name drift — re-roll).
- `hookframes/hook-gift-macro.jpg` — the focal crop used for the hook.
- Music: `../../film/audio/music.mp3`. Logo: `../../film/assets/logo.png`.
- Prior real-motion clips (optional): `../film/shots/product-motion.mp4`, `../../_archive/product-turntable/kol-holds.mp4`.

## ChatCut = full AI video editor (not just assembly)
Timeline editor driven by prompt; Claude plugin `plugin:chatcut:chatcut`. Native: AI editing (highlights/cuts), **AI motion graphics from a sentence** (lower-thirds, typing/emphasis = the "text animating on the clip"), auto captions (100+ langs, styles), AI video gen (Seedance 2.5/2.0, Kling 3.0), AI image gen (GPT Image 2, Nano Banana 2), AI voiceover + royalty-free music, transcript editing, export. Credit-based (free tier + paid). Cloud/project-based → must IMPORT our assets into a ChatCut project.

## What to ask ChatCut (in a NEW session — Claude drives it)
1. Create/open a ChatCut project (9:16, 1080×1920).
2. **Import our real product assets** (its AI doesn't know the personalized lamp — feed the real ones): `clips/hook-macro.mp4` (the hook), the in-scene stills in `../src/` (`scene-gift.jpg` best, `01-scene-flux.jpg`, `scene-livingroom.jpg`), `../../film/assets/logo.png`.
3. Let ChatCut **animate the remaining stills** (Seedance/Kling image-to-video, subtle push-ins), **add kinetic captions / motion-graphic lower-thirds** timed to the beats, **generate a warm music bed** (and optional soft VO), warm grade.
4. Structure: focal hook (macro of names) → reveal (gift scene) → glow (bedside) → CTA card "Grandma's Garden — Love Grows Here / Personalize hers → madejustforyou.net". Warm, product-as-hero, **no discount**.
5. Export the 9:16 mp4.
Copy voice: "A warm glow. A forever garden." Headlines/body in `../README.md`.

## Fallback (no ChatCut): the ffmpeg pipeline works
`build_video.sh` (older, used the grey turntable — replace with the new in-scene clips) + `make_layers.py`. The hook-demo proves captions-over-motion via PNG overlays + `fade` (this ffmpeg has NO `drawtext`/freetype — use PNG caption layers).
