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

## Stage 2 — does it survive video? *(running)*

The still is not the deliverable. Test C's failure happened **in video**, so the decisive question is
whether the name holds through image-to-video re-synthesis. Running Seedance 2.0, doc two-shot recipe,
1080, with the Nano Banana Pro 4K still as start frame and a **push-in** — forcing the lettering to be
re-synthesized larger, the hardest case.

Result to be recorded here.

## What this changes if Stage 2 also passes

The **compositing spike shrinks**: close-ups of the panel would no longer need a PIL warp, leaving only
the **wall-shadow shot** (beat A-3), where "Alex" must appear as pale script inside the dark dog shape —
a projection no model has been asked for yet.

## What it does not change

The **turntable stays**. It was never an alternative to compositing — it is what makes the model place a
correctly shaped, scaled and lit panel in the scene at all. The two do different jobs.

And the **per-customer economics still favour PIL** for anything beyond this trial: the product changes
breed and name for every order, so a gallery is per-product where a composite is a texture swap. For a
single Phase-1 product that cost is irrelevant; at scale it is not.

Evidence: `products/suncatcher-dog-memorial/tests/testF-*.png`.
