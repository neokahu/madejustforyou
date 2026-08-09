# Image-to-Video Prompt Method — animating a provided product image

**Use when:** you have a finished product photo (with the printed names/photo already on it) and want a short motion clip for an ad. The AI **only animates your image** — it never generates the product, names, or logo. Companion to [[ai-emotional-video-ad-playbook]]. Built 2026-08-05 from web research (official model docs + prompt guides).

> **THE ONE RULE:** the image already defines the product, composition, and text. The prompt's only job is **what moves** — camera, one subtle action, lighting shift, timing. **Never re-describe the product** ("a green candle warmer with names…"). Re-describing what's already in the image is the #1 cause of warping/morphing, because the model starts *re-drawing* it instead of moving it. Refer to it generically ("the lamp", "the subject").

---

## 1. Universal i2v prompt template
```
[ONE camera move] as [the subject] [ONE subtle action].
[Ambient motion on secondary elements only]. [Lighting/mood]. [Speed = slow/steady].
[Positive lock: product stays sharp, fixed, undistorted]. [Short negative block if model supports it].
```
- **Lead with the camera move** — models weight the first ~5 words most; a buried camera instruction gets ignored.
- **One move, one action.** "Slow push-in as the glow blooms" — NOT "push in while orbiting while a hand pours while it rotates." Compound motion = morphing.
- **20–50 words.** Tight wins; quality fragments past ~80–100 words.
- **Assign motion to secondary elements** (steam, glow, bokeh, sunlight, a hand) and explicitly keep the **product fixed**.

## 2. The control levers (dials for "close to expected")
| Lever | Setting for predictable product shots |
|---|---|
| **Clip length** | 3–5s. Drift compounds with length — draft at 5s. |
| **Motion amount** | LOW. Say "slow, subtle, minimal motion"; where exposed, motion-strength ~0.6–0.8. |
| **Camera** | ONE clean move, or locked. Positive phrasing for static ("locked-off camera, perfectly still"), never "no camera movement". |
| **Subject + background lock** | Positive: "product stays centered, keeps its shape, firmly rests on the surface; background holds steady." Unpinned backgrounds warp and drag the product. |
| **First + last frame** | The most predictable control: give both endpoints, model interpolates. For near-static, feed the **same image to both** (a "living still"). |
| **Negative prompt** | Only on models that support it (Kling/Veo/Wan) — 3–5 targeted stability terms, not generic "bad quality". |
| **Seed** | Once a clip is ~90% right, **lock the seed** and change one word. Document winning seeds. |
| **Best-of-N** | Product i2v is probabilistic — batch 3–4 per prompt, pick the cleanest. Plan for *selection*, not one-shot. |
| **Resolution** | Draft 720p to find the shot cheap, re-run the keeper at 1080p. |

## 2.5 How many product images? (we have multiple shots)
**Per clip = 1 image. Across the ad = use all of them.** i2v animates ONE start frame — feeding many angles into a single generation does NOT give 3D understanding; it just needs one clean first frame. Since an ad is 3–6 clips, use a **different shot per clip** for variety with zero morph risk (you feed real angles instead of asking the model to invent them).

| Shot | Use this photo |
|---|---|
| Glow / hero push-in | clean front beauty shot |
| Detail — engraved names (living still) | macro / close-up of the engraving |
| Ambient / lifestyle | staged in-context / angled shot |
| CTA hero | sharpest straight-on shot |

- **Pro move — first + last frame:** if two shots form a natural motion (wide → close, front → angled), feed them as the two endpoints and let the model interpolate. Most predictable control there is, and the product stays true at BOTH ends because both are your real photos (no mid-drift). Ideal for "pull in to the names."
- **Optional multi-reference for fidelity:** Kling elements / Seedance `@image1,@image2` / Veo "ingredients" accept a couple of angles to hold the product consistent (most-important first). Nice-to-have, not required.
- **Caution:** mismatched lighting/backgrounds across shots make the cut feel disjointed — color-grade to match in CapCut.

## 3. Per-model cheat sheet (our stack)
| Model | Prompt structure | Camera control | Product fidelity lever | Negatives | Clip |
|---|---|---|---|---|---|
| **Kling** (best product fidelity) | Subject → its motion → camera in *second half* of sentence | Natural language ("slow push-in"); default the camera selector | **Relevance slider ~0.9** for max prompt loyalty; Pro/Professional mode for 1080p | Dedicated field — use **stability** terms: "camera drift, handheld, sudden zoom, morphing, warping" | 5/10s |
| **Veo 3 / 3.1** (cinematic + audio) | Google 5-part: `[Cinematography]+[Subject]+[Action]+[Context]+[Style & audio]` | Named moves (dolly, crane, arc) | Prompt *only* motion/camera/audio; "ingredients"/first-last frame for consistency | Natural-language exclusions (no bracket field) | 6–8s |
| **Seedance** | `subject+motion, background+motion, camera+motion` | Cinematography verbs; **toggle Fixed-Camera OFF** to honor moves | i2v preserves the reference image well; put product as `@image1 as first frame` | Steer via positive constraints | 5/10s |
| **Hailuo / MiniMax** (only formal camera syntax) | Plain scene + **[bracket] camera commands** at the exact point | `[Push in] [Pan left] [Tilt up] [Zoom in] [Static shot] [Tracking shot]` — combine ≤3 in one bracket | `first_frame_image` = start; set `prompt_optimizer=false` for precise control | Positive phrasing only | 6/10s |
| **Wan** (cheap/volume) | 4-part: primary motion → camera → environment → speed/intensity | Explicit terms + explicit speed+direction ("slowly toward camera"); dolly-in reliable, dolly-out weak | Only animate what's in the image; under-specified → invents extra people | Field exists but **weak at CFG=1** → also phrase limits as positive constraints | ≤5s |

Quick pick: **Kling** = the default for "make my product move cleanly." **Veo/Seedance** = one cinematic hero shot (glow/reaction, native audio). **Hailuo/Wan** = cheap b-roll volume for variant testing.

## 4. Copy-paste shot templates
Prepend your uploaded image; replace only the bracketed mood.

**(a) Slow push-in hero**
```
Slow, steady dolly-in toward the product, cinematic precision. Soft key light,
gentle specular highlights shift as the camera nears. The product stays pin-sharp,
centered, and undistorted; locked, no camera shake. Shallow depth of field,
background blurs to bokeh. [warm golden-hour mood]. 5s.
Negative: warping, morphing, text distortion, camera shake, flicker.
```
**(b) Ambient lifestyle (product still, world alive)** — best for emotional gifts
```
Locked camera. The product rests still and unchanged on the surface. Gentle ambient
life only: [soft warm glow slowly blooming / sunlight drifting through it casting moving
light / faint bokeh breathing]. Near the end a single hand enters slowly from frame-right,
natural fingers, and rests beside the product without touching it. Product stays perfectly
fixed, sharp, identical to source. 5s.
Negative: product warping, extra hands, extra fingers, text distortion, flicker.
```
**(c) Living still / cinemagraph (near-zero motion, safest)**
```
Static, locked-off camera. Product completely fixed and identical to the source.
Only micro-motion: barely perceptible [glow pulse / light drift / particle float].
No camera movement, no product movement, no warping. Minimal, elegant, premium. 3s.
```
**(d) Constrained orbit reveal** (keep angle <90° so unseen sides aren't invented)
```
Smooth slow 60-degree arc around the product on a clean surface. Product stays centered
and locked while the camera arcs; reflections track the move. Soft studio light. Product
crisp and undistorted, stable motion. 5s.
Negative: morphing, warping, distorted product, camera shake.
```

## 5. Failure → fix
| Symptom | Fix |
|---|---|
| Product warps/morphs | Shorten to 3–5s · slow the move · "product keeps its shape, undistorted" · orbit <90° |
| **Printed names / photo scramble** | Keep motion restrained + camera near the text; **don't describe the text in the prompt**; if it still flickers, generate a clean motion plate and **composite the real printed area back in post** (CapCut/AE) |
| Extra hands/objects appear | Negative "extra hands, extra fingers, duplicated objects"; specify "single hand" or "no hands" |
| Jittery / too fast | "slow, smooth, stable, locked camera"; lower motion strength; "no exaggerated motion, no flicker" |
| Background melts | Camera near-static · "background holds steady, no background distortion" · simpler bg · shorter clip |
| Product slides / floats | "firmly rests on the surface, does not move or float, gravity intact"; lock camera |

## 6. Keeping OUR personalized products readable
Our products have printed names/photos — the thing that must survive the motion.
- **Treat the printed area as fixed** — never let the model re-render it. Restrained/locked motion near it; **no orbit or whip-pan across the names.**
- If the personalization must stay razor-sharp: keep clip **≤3s, camera locked**, add "text stays sharp and unchanged, no letter warping."
- Safest of all: animate a **clean motion plate** (glow/ambient) with the product mostly static, then **overlay the crisp real product/name area in post**. Overlays can't fix warp — the plate must be restrained first.
- In the source frame, keep the personalization **large and centered**; thin/tiny text flickers first.

## 7. The dial-in loop
1. Upload the clean product still (no blur/motion cues in it — a bad still gets worse animated).
2. Start with template (c) or (b) — lowest motion, highest predictability.
3. Generate **3–4 at once (720p)**, pick the cleanest.
4. **Change ONE variable per iteration** so you know what caused a warp.
5. Random one-off glitch → **reroll** (new seed, same prompt). Consistent problem (always warps text) → **reduce motion / reprompt.**
6. Once ~90% right → **lock the seed**, tweak one word, render final at 1080p.

## Worked example — candle warmer (MJ4U-111), "love growing at home"
Source: the finished candle-warmer photo with engraved grandchildren's names. Angle: warm glow (from §1 of the playbook).
```
Locked-off camera, perfectly still. The lamp rests unchanged on a dusk windowsill.
A warm amber glow slowly blooms and breathes across the engraved surface; faint bokeh
drifts behind. Near the end a grandmother's hand enters softly from frame-right and
rests beside it, not touching. Product and engraved names stay sharp, fixed, identical
to source. Cozy nostalgic film grade, soft golden light. 5s.
Negative: text warping, product morphing, extra hands, flicker, background distortion.
```
Then: burn captions + ElevenLabs VO + gentle piano in CapCut; if the names shimmer at all, overlay the real engraved area back in post.

## Sources
Runway Gen-4 / i2v prompting guides · Google Veo 3.1 prompting guide (Cloud) · Kling camera-control + relevance-slider docs · MiniMax/Hailuo director bracket-command docs · Wan 2.2 prompt guides + HuggingFace Wan thread · fal.ai/Replicate model pages (Seedance, Kling, Hailuo) · masonry.so product-model fidelity test · artlist / LTX negative-prompt guides · aivid.video text-consistency fix. Full URLs in session research notes.
