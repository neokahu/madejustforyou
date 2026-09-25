# Can a model render the product's personalized name? — Test F, 2026-09-26

> Question raised by the user: *why composite the text in PIL, instead of building a gallery of the real
> product from every angle and prompting scenes from that?*
>
> My position going in was "AI cannot render legible text — never ask the model for it," carried into the
> build plan and into memory. **Stage 1 refuted it.** This document replaces that claim with a measured one.

## Where my old claim came from — and why it was bad evidence

The "cannot render text" rule came from **Test C**: a Seedance clip at **720p** where "Alex" ballooned
from small script into a body-spanning word. That is one datapoint, from a **video** model, at the lowest
resolution we use, with the panel small in frame. I generalised it to all models at all resolutions.

## Stage 1 — image models, real product as reference, close-up

Three arms, identical prompt, `image_edit` with `img_1` (the real 2048×2048 product) as reference,
9:16, panel filling the frame.

| Model | Output | "Alex" legible? | Letterform fidelity |
|---|---|---|---|
| **Nano Banana Pro** (`nano_banana2`, 4K) | 3072×5504 | ✅ **yes, cleanly** | ✅ closest to the original thin script |
| **Seedream 5.0 Pro** (2K) | 1440×2560 | ✅ **yes, cleanly** | ✅ close |
| **GPT Image 2.5 Flare** (4K, max) | 2128×3776 | ✅ **yes, cleanly** | ⚠️ legible but a **bolder, different script** |

All three also held the artwork: Van Gogh swirling sky, gold sun, mountains, river, black German Shepherd
silhouette, florals, butterflies and the heart cut-out.

**Conclusion: the user was right for stills.** A 4-letter name, at 2–4K, with the real product supplied as
reference, comes back correct. Do not ask a model to *invent* lettering, but reproducing short lettering
from a reference is within range for current image models.

⚠️ **Legibility ≠ fidelity.** GPT Image rendered a different typeface. On a personalization store the name
should look like what the customer receives, not merely be readable. **Prefer Nano Banana Pro**, and check
the letterform against the real artwork every time, not just whether it spells the name.

⚠️ **Scope.** One product, one 4-letter name, close-up framing. Longer strings are a different problem —
this is exactly what **Test D (fleece blanket, a full printed letter)** exists to answer, and nothing here
should be read as predicting that result.

## Stage 2 — VERDICT: legibility survives video, fidelity does not

Seedance 2.0, doc two-shot recipe, **1080**, start frame = the Nano Banana Pro 4K still, with a
**push-in** so the lettering must be re-synthesized larger — the hardest case.

```
                              dur  hook3   peak  motion  cuts/s  static%
testF2-name-in-video.mp4      4.9  21.61  28.70   24.61    0.21        0
GATE                            —   ≥8.0      —    ≥6.0   ≥0.15      ≤10
```

Best motion numbers of any clip in the project.

**✅ "Alex" stays readable** in every sampled frame, including the final close-up. Test C's total collapse
(small script → body-spanning word) does **not** reproduce when the start frame carries clean, correct
lettering at 4K. Test C's real fault was a bad start frame plus a bad prompt, not the video model.

**❌ The letterform drifts.** First frame: the delicate thin script of the real product. Final frame: a
markedly **bolder, heavier typeface**. The model rewrote the name in a different hand as it scaled it up.
Same word, wrong font, **changing mid-shot**.

### The rule this produces

> A model can write "Alex". It cannot keep writing **our** "Alex".

For a personalization product that distinction is the whole business. A name that changes typeface during
the reveal misrepresents what ships, exactly as a misspelling would — it is just harder to notice.

**So: PIL owns the name in motion.** Not because models cannot render text — they can, and stage 1 proves
it — but because they *re-render* it every frame and it drifts. Where the name is the proof, composite it.

Where a model-rendered name **is** acceptable: wide and medium shots where the name is present but not
being read as proof, and any still. There the drift is invisible and the saving is real.

## Wall-shadow compositing spike — ✅ PASSES on a single frame

Run on `testC3-moving-open.mp4` frame 119, the validated reveal beat.

**The model gets the projection structure right and the lettering wrong.** In the wall shadow, the heart,
florals and butterflies come through correctly — they are simple shapes. The name comes through as an
**illegible cursive squiggle**. Confirmed at 100%: `spike-C3-name-zoom2.png`.

Method that worked, all PIL:
1. Extract the lettering from the real artwork as an alpha mask — source box `(960,1175)-(1125,1248)`,
   threshold luminance 70→190. Excludes the floral petal below; clean glyphs.
2. Cover the model's squiggle with the median shadow tone, Gaussian-feathered 7px.
3. Scale to 118×52, rotate −4°, Gaussian blur 1.6 to match the projection's softness.
4. **Blend as light, not paint** — sample the 85th percentile of the florals' RGB (`134,97,71`) as the
   lit colour and composite at α 0.92 over the shadow tone (`76,56,47`).

Result `spike-before-after.png`: legible, correct script, reads as part of the same projection rather
than a sticker. Tone and softness match the neighbouring florals.

⚠️ **This is one frame. Tracking is not solved and is the remaining work.** The camera pushes in, so the
shadow grows and moves across all 120 frames; a fixed placement will slide. The anchor to track is the
**heart cut-out** — a high-contrast isolated blob inside the shadow — from which per-frame scale and
translation can be derived and applied to the lettering. Template-match the heart, fit scale+offset, warp.

## Stage 2 — original question *(superseded by the verdict above)*

The still is not the deliverable. Test C's failure happened **in video**, so the decisive question is
whether the name holds through image-to-video re-synthesis. Running Seedance 2.0, doc two-shot recipe,
1080, with the Nano Banana Pro 4K still as start frame and a **push-in** — forcing the lettering to be
re-synthesized larger, the hardest case.

Result to be recorded here.

## What this changes in the build

The compositing spike does **not** shrink. Both jobs stay:
- **Close-ups where the name is the proof** — composite, because the letterform drifts in motion.
- **The wall shadow (beat A-3)** — composite, because the model's projected name is illegible squiggle.

What *did* change: **wide and medium shots can use the model's lettering.** It is legible and the drift is
invisible at that size. That is a real saving on shot count, and it came from the user's question.

## What it does not change

The **turntable stays**. It was never an alternative to compositing — it is what makes the model place a
correctly shaped, scaled and lit panel in the scene at all. The two do different jobs.

And the **per-customer economics still favour PIL** for anything beyond this trial: the product changes
breed and name for every order, so a gallery is per-product where a composite is a texture swap. For a
single Phase-1 product that cost is irrelevant; at scale it is not.

Evidence: `products/suncatcher-dog-memorial/tests/testF-*.png`.
