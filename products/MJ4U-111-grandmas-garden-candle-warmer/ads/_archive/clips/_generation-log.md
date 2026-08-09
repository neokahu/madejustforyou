# MJ4U-111 — Clip Generation Log

Source image (hosted, REAL jpg): https://database.blotato.io/storage/v1/object/public/public_media/c90fc7fd-1d90-479c-ace3-e861dd979111/7a5bf379-9757-4f27-b344-4eb480e71ff5.jpg
Model: Kling 3.0 Turbo (i2v) · 720p drafts · 5s · best-of-3 per shot

> ⚠️ GOTCHA: the source file `..._3.jpg` was actually WebP with a .jpg extension. Kling rejected all 9 (error 400, zero credits — cost_time_ms 1-3). Converted to real JPEG via `sips -s format jpeg` → `hero-real.jpg` (2000×2000) and re-uploaded. Round-1 IDs below are the SUCCESSFUL re-fire.

## Round 1 — 720p drafts (2026-08-06)

| Shot | Draft | taskId | Verdict |
|---|---|---|---|
| A — hero push-in | A1 | da3c95ac76e96b4291473da2090552aa | pending |
| A — hero push-in | A2 | cf4a74d223caf69ac8ac0d345be750ed | pending |
| A — hero push-in | A3 | ba6a5e78b9f80c0240c7c006170ace01 | pending |
| B — ambient + hand | B1 | b814edbf26ad9c66530360c82ef3ad71 | pending |
| B — ambient + hand | B2 | 201dcd44e7ca59151a1e08996a1d7af4 | pending |
| B — ambient + hand | B3 | 588f2c059008874c4afa2d882821b985 | pending |
| C — living still | C1 | 407f2f1418976e8d4c60bcb72a7e76f9 | pending |
| C — living still | C2 | 8658e9ecfe0d281ffd00b6355e9ec5e2 | pending |
| C — living still | C3 | 3ca1edbca5aa2ed17d54ab133578a155 | pending |

Prompts: motion-only, product+names locked (see ai-emotional-video-ad-playbook + image-to-video-prompt-method).
- A: slow dolly-in, glow blooms/pulses, flame flickers, floral bokeh.
- B: locked camera, glow breathes, grandmother's hand enters frame-right, rests beside (not touching).
- C: static locked-off, micro glow-pulse + flicker, names razor-sharp (safest for text).

Kling round-1 verdict (all 9 succeeded): best draft per shot → A1, B2, C2. Text survives even the push-in; A1 softened names slightly (Sharon/Helen).

## Seedance-2-FAST comparison (2026-08-06) — same concepts, 720p, best-of-1
Prompt rewritten to Seedance form (subject+motion, background+motion, camera+motion; negatives→positive locks).
| Shot | taskId | vs Kling |
|---|---|---|
| A — hero | 69ec6745a0bbd704e62d4aa3dd3d1ea7 | Seedance kept names CRISPER; Kling pushed in harder but softened text |
| B — hand | 67112018926b0dae1996ccf997024cc1 | Seedance WINS — rendered a genuinely elderly/wrinkled hand (on-concept) + crisper text |
| C — living still | 87e88b059069c35dd723d17b7e94e2a3 | Tie — both near-perfect; Seedance added nice airborne sparkle |

**Finding: Seedance-2-fast matched/beat Kling 3.0 Turbo on this concept at a lower price tier, even at best-of-1 vs Kling's best-of-3.** Seedance applies gentler camera moves (subtler push-in) — the one edge Kling has if we want a strong dolly-in. Recommended primary = Seedance-fast; keep Kling for shots needing aggressive camera movement.
Clips saved: kling-A1..C3.mp4, seedance-A/B/C.mp4. Review frames in _review/.

## FINALS (2026-08-06) — Seedance-2-fast, 720p (960×960), 5s
NOTE: seedance-2-fast rejects 1080p ("Invalid resolution") — max is 720p on the fast tier. 960×960 plates; will crop to 9:16/4:5 + overlay crisp names in HyperFrames.
| Shot | file | taskId |
|---|---|---|
| A — hero push-in | final-A-hero.mp4 | 345d2354cf9674a6b9fb1b625af7732d |
| B — grandmother's hand | final-B-hand.mp4 | 2464e0af4ef6f20abc7fc9fab2c8bd4b |
| C — living still | final-C-livingstill.mp4 | 73d3bca41a467efe6f05344e59d834d4 |
Text held up well at this framing (hero kept all 5 names legible). Names still get a crisp post-overlay in the edit for guaranteed sharpness + the buyer's real-name reveal.
