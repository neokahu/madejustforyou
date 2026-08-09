# AI Product-Review / UGC — Product Consistency Across Angles (2026 method)

**Purpose:** how to make realistic AI product-review/UGC video where a presenter holds/demos a product at many angles while the product stays consistent. Built 2026-08-06 from a deep-research pass (27 sources → 130 claims → 25 adversarially verified, 12 confirmed / 13 killed). Companion to [[ai-emotional-video-ad-playbook]] + [[image-to-video-prompt-method]].

> **⚠️ PRICING CORRECTION (verified from AtlasCloud billing 2026-08):** Seedance 2.0 Fast Ref-to-Video actually costs **~$0.98 per 5s clip at 720p** (~$0.195/s, token-billed), **~$0.67 at 480p** — NOT the "$0.09" quoted below (that figure was ~10× too low). Seedream edit/t2i ≈ $0.045/image is correct. A clean ~35s film ≈ **$9 (720p) / $6 (480p)**. See `ai-film-studio.md` §4 for the full cost/time model.

> **One line:** build a 4-angle product "turntable" with Nano Banana Pro → multi-reference image-condition it into the scene (Kling 3.0 Omni Elements / Seedance 2.0 multi-ref; on Kie.ai use Nano Banana Pro 8-ref to compose, then i2v) → **composite the real printed names back in post** → minimize/​frame-around hand-holding (still unsolved).

## Confirmed (survived 3-0 adversarial verification)
1. **Multi-reference image-conditioning is the method.** Kling 3.0 Omni "Elements" lets you upload ~3–4 images of a product as a reused **element**; Seedance 2.0 supports up to **12** references. Elements perform best when built from **multiple angle images**, and you can reinforce product identity by re-passing the element per shot.
2. **Generate the 4 angle references first** (turntable/reference sheet) — recommended pipeline is: make the angle set, then feed as references.
3. **Image-to-video from a real/clean product image is recommended** over text-to-video (preserves the actual product).
4. **Nano Banana Pro (Google Gemini image) handles fine product detail** well and is the tool for building the clean angle set.
5. **Multi-view methods (NeRF / Gaussian Splatting)** achieve the best true 360°, **but are impractical for small brands** (capture rig + processing overhead). Skip.

## Killed (refuted — do NOT rely on these)
- "Seedance 2.0 is #1 on leaderboards / clearly best multi-shot consistency" — **0-3**.
- "Veo 3.1 and Kling 3.0 support only single image reference" — **0-3** (false).
- Nano Banana specific text-accuracy %s (94%/85%, char-length curves) — **refuted** (fabricated precision).
- "Structured typography prompt block keeps small printed text sharp" — **0-3**. → **composite the real text instead.**
- "Only Creatify/Higgsfield insert the real product" / "no tool can hands-on demo like a human" — **0-3** as stated, BUT the underlying truth stands: **clean hand-held manipulation is unsolved.**
- Various vendor-blog "X model is best for product fidelity" claims (Seedance, Veo) — **refuted**; treat all vendor benchmarks skeptically.

## Caveats (from verification)
- **Hand-object interaction (holding, rotating, unboxing) is still unsolved** — expect morphing, extra fingers, product warp. Minimize it.
- **Kie.ai's Seedance exposes ONLY first/last-frame** — not the multi-image reference mode. BUT see below: **AtlasCloud exposes the multi-ref mode**, so we DO have it in our stack via Atlas.

## Multi-reference IS available on AtlasCloud (verified 2026-08-06 via Atlas MCP)
Kie.ai can't do multi-ref, but AtlasCloud can:
- **Seedance 2.0 (Fast) Reference-to-Video** (`bytedance/seedance-2.0-fast/reference-to-video`): up to **9 reference images** (+ up to 3 ref videos, 3 audios; multimodal). Reference inputs as "image 1, image 2…" in the prompt. 480p–1440p-SR, 4–15s, native audio. **~$0.98/clip at 720p (see correction banner; "$0.09" was wrong).** ← the video multi-ref mode Kie.ai lacks.
- **Seedance 2.0 Reference-to-Video** (non-fast) + **Mini** variants also exist.
- **Seedream v5.0 Pro Edit** (`bytedance/seedream-v5.0-pro/edit`, IMAGE): up to **10 reference images**, preserves identity/lighting/color. **$0.045/req** (1st image free, +$0.003 each). Good for building the turntable + composing product-into-scene stills.
- Note: "12-ref" from the web research does NOT match Atlas's actual limits (9 video / 10 image). Real ceiling = those.
- Sources are Feb–Aug 2026 vendor blogs cross-checked against primary docs (Kling docs, ByteDance, Google, arXiv, fal.ai).

## ✅ VERIFIED on our stack (2026-08-06, MJ4U-111 test)
Ran the pipeline 1-by-1 to confirm before scaling spend:
1. **Turntable angles** — Seedream v5.0 Pro Edit (Atlas), from the single front lamp photo → clean-background **¾-left** and **¾-right** angles, product on-model (shade/gold arc/base/candle/floral design preserved; ¾-right kept all 5 names legible). ~$0.045/image, ~2 min each (thinking mode on).
2. **Multi-ref video** — fed front + ¾-left + ¾-right as 3 `reference_images` into **Seedance 2.0 Fast Reference-to-Video** (Atlas) with a slow-orbit prompt → the camera orbits AROUND the lamp and the product stays consistent, sharp, undistorted across all frames (true 3D-consistent motion, not a flat zoom). **$0.09**, ~1 min. This is the capability Kie.ai's first/last-frame i2v cannot do.
3. **KOL holds product** — fed [grandma face, lamp front, lamp ¾-right] into Seedance 2.0 Fast Ref-to-Video; prompt = she picks up the lamp and turns it to camera. Result: **hands read natural (no obvious extra-finger morph), product stays on-model, face consistent.** The hand-object shot the web research called "unsolved" worked on the first take via multi-ref. $0.09. → `kol-holds.mp4`, `_frames/hold-strip.jpg`.
Files: `products/MJ4U-111-.../ads/product-turntable/` (lamp-34left.jpg, lamp-34right.jpg, refvid-orbit.mp4, kol-holds.mp4, _frames/).
Still true: printed names go soft → overlay in post. Verify hands at full-frame before finalizing any hold shot; holding a lit warmer is slightly unphysical (prefer "hand resting on it" for realism).
4. **Integrated emotional scene (payoff)** — [grandma face, lamp front, lamp ¾-right] → Seedance 2.0 Fast Ref-to-Video; prompt = seated, gazes at the glowing lamp on the side table, hand to chest. Result: **lamp integrates naturally (realistic tabletop scale, room-matched warm glow, grounded shadow) — solves the earlier "pasted-in" problem** from Nano-Banana-still compositing; grandma tears up, hand to chest = genuine emotional peak. $0.09. → `ads/scene-videos/payoff-refvid.mp4`.

**KEY TAKEAWAY:** for emotional human+product scenes, generate the scene DIRECTLY as multi-ref Ref-to-Video (character ref + product angle refs) instead of Nano-Banana still → i2v. The multi-ref video builds the product INTO the scene with correct scale/light/shadow. This replaces the earlier compose-then-animate path. Total validation spend ~$0.40.

## Our pipeline (mapped to the Kie.ai / Nano Banana stack)
1. **Build the product turntable** — Nano Banana Pro: from the real product photo, generate a clean **4-angle set on blank background** (front, ¾-left, ¾-right, back or top) + a straight-on **name-panel close-up**. Remove background (Recraft) / sharpen (Topaz) as needed. Reusable per product.
2. **Compose scenes with multi-ref** — Nano Banana Pro accepts up to **8 image refs**: pass character ref + the correct-angle product ref → generate the scene with the lamp already in the right perspective/lighting (avoids the "pasted-in" look). This is our substitute for Kling Omni Elements (check if Kie.ai ever exposes Omni; if so, prefer it for video-native multi-ref).
3. **Animate** — i2v the composed still (Kling 3.0 Turbo / Seedance-fast), gentle motion, best-of-N, cull morphs. Never text-to-video.
4. **Names** — **composite the real printed name-panel back in post** (HyperFrames overlay). Do not trust any model to render the small personalized text. The buyer's real-name reveal is an edit-side motion graphic anyway.
5. **Hand-holding** — frame as **product-on-surface + hand near/resting** (not full manipulation). If a hold is required: first+last frame, restrained motion, best-of-N, expect to discard several.

## Sources (selected)
Kling 3.0 Omni user guide (kling.ai), invideo Kling Omni Elements, ByteDance Seedance, fal.ai image-conditioned-vs-NeRF, 4dpipeline photogrammetry-vs-3DGS, higgsfield ai-video hands/faces, seedance first-last-frame guide, aivid.video text-changes-between-frames, mindstudio Seedance-vs-Veo, layer3labs UGC tools. Full list in session research notes (deep-research run wf_e44d6670).
