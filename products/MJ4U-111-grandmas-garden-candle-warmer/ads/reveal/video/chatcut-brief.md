# ChatCut Director's Brief — MJ4U-111 "Grandma's Garden" reveal ad
*(Claude drafts this; ChatCut builds it. Feed this whole brief to ChatCut in a NEW session.)*

## Deliverable
- **9:16, 1080×1920, ~18–20s**, warm, premium, emotional. Product-reveal ad (no actors, no story).
- Platform: Facebook/Instagram Reels + feed. **No discount, no urgency** — full-price gift positioning.

## HARD guardrails (do not violate)
1. **Never regenerate or alter the personalized lamp or its printed text.** Use our supplied product assets AS-IS. The printed "GRANDMA'S GARDEN / Love Grows Here" and the names **Alice · Grace · Jade** + birth-flowers must stay pixel-accurate. If you animate a still, use image-to-video that preserves the product; do not repaint it.
2. **Keep captions OFF the printed lampshade** — place text in clean areas (lower third / negative space) so it never fights the product's own text.
3. Warm, unified color grade across all shots so it feels like one film.

## Assets to import — ALL PREPARED & 9:16-READY in `sources/`
*(Claude already prepped these — native 9:16, product + names accurate. See `sources/MANIFEST.md`.)*
- `sources/hook-macro.mp4` — 5s motion HOOK (macro of lit shade, flame flicker, names sharp). **Use as-is.**
- `sources/scene-gift-9x16.jpg` — gift-table scene (1072×1920) → animate for the REVEAL beat.
- `sources/scene-bedside-9x16.jpg` — bedside scene (1072×1920) → animate for the GLOW beat.
- `sources/logo.png` — MadeJustForYou wordmark for the end card.
- `sources/music-reference.mp3` — mood reference (or let ChatCut generate a warm bed).

## Timeline (beats, timing, motion, text)
1. **HOOK · 0:00–0:04** — `hook-macro.mp4`. Caption fades up ~1.2s: **"One flower for every grandchild"** (elegant serif, white, lower third). Sub ~2.8s: *"her whole family, on one little lamp"* (italic, smaller).
2. **REVEAL · 0:04–0:09** — animate `sources/scene-gift-9x16.jpg` (slow gentle push/pull, candle flicker, bokeh shimmer). Lower-third motion graphic: **"Grandma's Garden — Love Grows Here."**
3. **GLOW · 0:09–0:13** — animate `sources/scene-bedside-9x16.jpg` (bedside, subtle motion). Caption: **"A warm glow, every evening."**
4. **CTA · 0:13–0:19** — end card: `logo.png` + script **"Love Grows Here"** + button-style **"Personalize hers →"** + **madejustforyou.net**. Motion-graphic build-on (fade/scale), hold ~3s.

## Captions / motion-graphics style
- **Elegant & premium** (warm serif, soft fade/rise). **NOT** TikTok-pop/bounce — this is a heartfelt gift, not a hype product.
- Kinetic but restrained: fade + slight rise; the CTA can scale/build on.

## Music
- Generate a **warm, tender, cinematic/ambient** bed (~80–95 BPM), royalty-free, cut to exact length, soft (music under, no VO needed — optional gentle female VO reading: *"A warm glow. A forever garden. One flower for every grandchild she's watched grow."*).

## Copy voice (for any text)
"A warm glow. A forever garden." · locked title **"Grandma's Garden — Love Grows Here."** Full headlines/body in `../README.md`.

## Export
- 1080×1920 mp4, H.264, high bitrate. Save back and tell me the path/URL so I can review frames.

## Success = better than our ffmpeg version if:
- Motion graphics/captions look more polished & animated than PIL-PNG fades, AND
- Product print stays accurate, AND
- It's faster than hand-building. If not, we keep the AtlasCloud+ffmpeg pipeline.
