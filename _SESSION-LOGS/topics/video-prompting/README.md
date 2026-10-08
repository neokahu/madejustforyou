# Topic — Video prompting (Seedance)

**Status:** settled method. Model = **Seedance 2.0** (not 2.5) for all video.

## Current decisions
- **Two named shots** (`Shot 1 / Shot 2`, never timecode), one camera move each, **opening shot moving**. Describe only light + camera; the start frame holds the scene.
- **Pin the product with a constraint naming the exact failure mode** ("The dog stays seated", "Shadow's outline does not change").
- Image-to-video inverts the formula: `subject + movement, background + movement, camera + movement`.
- **Locate action in space**, not just on the body ("beside his own cheek, palm turned away from camera…" + `His palm never faces the camera`).
- **Name the light source as off-screen** and keep it there (unsourced light → lens flare; named panel → model draws it into frame).
- 4–5 assets max, one duty each. Emotion as physical detail, never an adjective.
- Text-sensitive close-ups: **4K still + ffmpeg Ken Burns at native resolution** beats video re-synthesis (no letterform drift; ~0.2 vs ~4 credits).

## Key evidence
| Finding | Evidence | Source |
|---|---|---|
| Two-shot recipe | hook3 8.10 → 14.90, motion 7.63 → 14.96 (same model/frame) | sessions/2026-09-26 §2 |
| Prompt fix, not model weakness | testC 12.11 (morph) → testC3 14.68 PASS; gate ≥8.0 | sessions/2026-09-25 §3 |
| 2.0 beats 2.5 | 2.5: ~half the motion + lens-flare smear | sessions/2026-09-26 §1 |
| Benchmarks | our shipped film hook3 3.59; Macorner (333d live) 18.05 | sessions/2026-09-25 §3 |

## Open items
- Multi-reference identity across independent clips untested — next build = vertical slice S-C1-H1 via AtlasCloud `reference_to_video` with all 8 owner refs (~$2). See [INDEX](../../INDEX.md).

## Detail
- `research/reference/seedance-prompt-method.md` (method, sources)
- `research/reference/image-to-video-prompt-method.md` (THE ONE RULE; draft 720p/2K, batch 3–4)
- `research/reference/RESEARCH-REPORT-2026-10-ad-production.md` (consolidated)
- `research/scripts/motion_qa.py` (motion gate — cannot read text)
- Sessions: [2026-09-25](../../sessions/2026-09-25-topview-evaluated-seedance-method.md) · [2026-09-26](../../sessions/2026-09-26-testing-complete-both-products.md)
