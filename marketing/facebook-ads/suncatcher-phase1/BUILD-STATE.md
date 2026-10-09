# Suncatcher Phase-1 build — live state (update after every step)

Build list = `HOOKS-shared.md` §10. Frames: `products/suncatcher-dog-memorial/ads/frames/phase1/`, clips: `.../ads/shots/phase1/`.
Tools: images + video on **AtlasCloud** (kie.ai out of credits): stills `google/nano-banana-pro/edit` ($0.14),
video `bytedance/seedance-2.0/image-to-video` (720p, 5s, ratio 9:16, generate_audio false, ~$0.98).
Download helper: `products/suncatcher-dog-memorial/ads/tools/atlas_fetch.sh <pred_id> <out> ...`.
Decisions: C2-B2 video uses **row 8b** (slow push-in, guard-clean), not 8a.

| Row | Shot | State | Final file |
|---|---|---|---|
| P1–P3 | prep | ✅ | ALEX-lettering.png (soft alpha), C3-room-first.png, C3-wall-last.png |
| 1 | HOOK-H1 | REUSE (KB on tests/testF-nanobananapro.png) | — |
| 2 | HOOK-H2 still | ✅ (v2 + ring removed by edit) | H2-start-FINAL.png · video ⏳ |
| 3 | B3a | REUSE tests/testC3-moving-open.mp4 1.9–4.9 | — |
| 4 | B3b WALL-4K | ✅ model name erased → real "Alex" pasted (soft, 400px wide, centre 2137,3118) | WALL-4K.png (clean ref: WALL-4K-clean.png) |
| 5 | B5 | REUSE (KB on testF) | — |
| 6 | C1-B2 still | ✅ ALEX engraved (Georgia Bold, recessed) | C1-B2.png · video in flight 9e5a1cd190d24f59b9c19cba9eb6664c → shots/phase1/C1-B2.mp4 |
| 7 | C1-B4 still | ✅ v2 (photo beside shadow head) | C1-B4.png · video ⏳ (3 takes) |
| 8 | C2-B2 still | ✅ p1 relit → v1 bed added | C2-B2.png · video ⏳ (row 8b) |
| 9 | C2-B4 still | ⏳ edit of C2-B2.png (needs upload) | — |
| 10 | C3-B2 | ✅ card pasted | frames/phase1/F-BOX-card.png (KB at assembly) |
| 11 | C3-B4a still | ✅ v1 | C3-B4a.png · video ⏳ (3 takes) |
| 12 | C3-B4b still | ⏳ needs chosen C3-B4a take's last frame | — |
| — | assembly | ⏳ extend ads/build_v2.py with 6 phase-1 ads; captions per HOOKS-shared §6; music.mp3 | ads/out/phase1/ |

QA lessons this build: the model keeps adding a **gold wedding ring** to the owner — zoom every hand; it writes its own
name on product/shadow — always replace with ALEX-lettering.png.

## In flight (AtlasCloud prediction IDs → target file)
- 45e8caf8d7754f7d8604c2bd7b464c3f → shots/phase1/H2.mp4
- 9149360b1eb144a3a2fd6eadb47189b3 / d2fffb8b6a7e48f8b842800d921e2ece / ddcd705288f94ba5ae6c6d72f11ba2d2 → shots/phase1/C1-B4-t1/t2/t3.mp4
- 7ceb98cf97834551a2a2cdee33f02ea9 → shots/phase1/C2-B2.mp4 (row 8b)
- 8d0f8738a0cc4159a8cfa527dd12f627 / d14f0a23372e49eabc4f219763b07d09 / 49e5bf833a6c4885b4edfe7ca850dece → shots/phase1/C3-B4a-t1/t2/t3.mp4
- 70ffafdcfbd547a096a69b648a9ed7b4 → frames/phase1/C2-B4.png (still)
Re-fetch any with: products/suncatcher-dog-memorial/ads/tools/atlas_fetch.sh <id> <out>
- C2-B4 still: v1 REJECTED (model swapped the man + redrew panel when product was a ref) → v2 ✅ (no product ref, light described in words) = frames/phase1/C2-B4.png
- C2-B4 video takes in flight: 105daa644569465e8902b015885efaa0 / 154397206a0f496abe1dfd79d7fc909f / 131ab43ff5ae4a1abb5be4ea6a7f151a → shots/phase1/C2-B4-t1/t2/t3.mp4
- C1-B2 video ✅ shots/phase1/C1-B2.mp4 (tag ALEX legible at 0.1s, panel true)
- QA batch 1: H2 ✅ ONLY 0.0–2.0s (by 3.0s model rewrites name as "Kloe" + silhouette drifts — never extend) · C1-B4 pick **t1** · C2-B2 ✅ · C3-B4a pick **t1** (ends on faint smile, friend in frame)
- C3-B4b stills in flight: d802258b902d45239d379d20fce39c91 / 00b1d72e724548ec8f7e3e8c27b76891 → frames/phase1/C3-B4b-v1/v2.png (then paste ALEX-lettering)

## ✅ ALL SHOTS READY (2026-10-08) — final picks for assembly
| Shot | File | Use |
|---|---|---|
| HOOK-H1 | KB on products/suncatcher-dog-memorial/tests/testF-nanobananapro.png (row 1 path) | 0–2.0 |
| HOOK-H2 | shots/phase1/H2.mp4 | 0.0–2.0 ONLY |
| B3a | tests/testC3-moving-open.mp4 | 1.9–4.9 |
| B3b | KB on frames/phase1/WALL-4K.png (real "Alex" centre ≈ 2137,3118, ~400px wide) | 3.0s |
| B5 | KB on testF-nanobananapro.png (row 5 path) | 3.0s + CTA/logo |
| C1-B2 | shots/phase1/C1-B2.mp4 | 0.0–4.0 |
| C1-B4 | shots/phase1/C1-B4-t1.mp4 | 0.0–5.0 |
| C2-B2 | shots/phase1/C2-B2.mp4 | 0.0–4.0 |
| C2-B4 | shots/phase1/C2-B4-t2.mp4 | 0.0–5.0 |
| C3-B2 | KB on frames/phase1/F-BOX-card.png (row 10 path) | 4.0s |
| C3-B4a | shots/phase1/C3-B4a-t1.mp4 | 0.0–3.0 |
| C3-B4b | KB on frames/phase1/C3-B4b.png (real "Alex" centre ≈ 1619,3670, ~118px wide in 4K → push so ≥100px at 1080 out) | 2.0s |
Music: products/suncatcher-dog-memorial/ads/shots/music.mp3 (approved).
