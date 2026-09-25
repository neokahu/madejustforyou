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

---

## ✅ RESOLUTION — the compositor is NOT needed for the suncatcher

Prompted by the user asking whether the compositing engine was necessary at all, or whether Seedance
could do the job. The answer is neither: a **third option beats both**.

**The letterform drift comes from video re-synthesis. A stills-based camera move has none.** We already
hold a Nano Banana Pro 4K still where "Alex" is correct. Push on that still in ffmpeg and nothing is
redrawn — no model, no PIL warp, no tracking.

```
                              dur  hook3   peak  motion  cuts/s  static%
kenburns-native.mp4           4.9  11.02  14.14   10.73    0.00        0   ✅ clears the gate
testF2-name-in-video.mp4      4.9  21.61  28.70   24.61    0.21        0   ✅ gate, ❌ product
GATE                            —   ≥8.0      —    ≥6.0   ≥0.15      ≤10
```

**⚠️ Build the zoom on native resolution.** My first attempt did `scale=1080` *before* `zoompan`, which
upsamples and softens exactly the lettering being protected. Correct order — crop to aspect at native
size, zoom, and let `zoompan`'s `s=` do the only downscale:

```
crop=3072:5461:0:0,
zoompan=z='1+0.45*on/125':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=25
```

`0.45` over 125 frames passes the gate; `0.25` passes motion but is marginal, `0.12` fails both.

**Side-by-side verdict** (`compare-kenburns-vs-seedance.png`), same start frame, same final moment:

| | Stills Ken Burns | Seedance video |
|---|---|---|
| Letterform | ✅ correct delicate script | ❌ bold, heavy, wrong typeface |
| Silhouette outline | ✅ true | ❌ wavy, bulging |
| Ornate black frame | ✅ present | ❌ gone from frame |
| Glass texture | ✅ crisp | ⚠️ softened, restyled |
| Gate | ✅ pass | ✅ pass |
| Cost | ~0.2 cr (the still) | ~4 cr |

Seedance's close-up is worse than "wrong font" — **the panel geometry deforms too.** Cheaper, sharper and
more faithful all point the same way.

### Settled shot policy for the suncatcher

| Shot | Method |
|---|---|
| Wide / medium, name present but not read | **Seedance 2.0** — model lettering is fine, drift invisible |
| Close-up where the name **is** the proof | **4K still + ffmpeg Ken Burns at native res** |
| Wall shadow (beat A-3) | **Seedance 2.0**, and the shadow proves the **breed**, not the name |

The shadow already does its real job: Hook 1 claims *"that's his actual breed"*, and the silhouette —
erect ears, long muzzle, bushy tail, plus heart, florals and butterflies — carries that perfectly. Only
the name fails there, and the name is read in the close-up instead. This is the fallback the build plan
already specified; it is now the plan.

### The compositor is deferred, not cancelled

Still possibly needed for the **fleece blanket**, whose text is a long printed line on **cloth** — a mesh
warp, not a homography, and unproven. That decision waits on the blanket image. **Do not build the engine
speculatively:** the suncatcher no longer needs it, and the blanket may be answered instead by its
**Skeleton B (VO-led)** structure, where grandma reads the letter aloud precisely because on-camera text
cannot be relied on.

**What this removes from the build:** the compositing engine, per-frame shadow tracking, the heart-anchor
template match, and the wall-shadow name composite. Replaced by one still and six lines of ffmpeg.


---

## Test D — the blanket, 2026-09-26. Long text, and a failure the gate cannot see.

Product: **"To My Sweetie Pie"** (`MJ4U-012`) — a ten-line, ~50-word poem in four colours and three
weights, plus two customizable figures and two names. Full writeup:
`products/blanket-granddaughter/README.md`.

**Stills: long text reproduces word-perfect, and cloth does not need a mesh warp.**
Nano Banana Pro at 4K held every line, colour, weight and apostrophe — flat on a bed *and* draped over a
person, with the print following the folds in correct perspective. This kills two of my recorded rules at
once: that ~50 words would come back as plausible gibberish, and that *"a flat PIL homography cannot
follow cloth — likely needs mesh warping."* Neither held.

**Video: the text holds.**

```
                         dur  hook3   peak  motion  cuts/s  static%
testD3-video.mp4         4.9  15.60  59.33   18.00    0.21        0    ← all gates pass, text correct
```

⚠️ **I first reported this clip as corrupting the text** — reading *"ceeling"* for *"feeling"* in the
final frame and writing it up as the project's most important quality finding. **That was wrong.**
Sampling frames 60–119 shows a complete `f` at frames 80 and 95; in the later frames the word rides up to
the blanket's edge and a fold crops the ascender. Occlusion, not re-lettering.

**Rule: never judge printed text from a single frame.** Folds, edges and highlights remove strokes. Sample
across the clip and confirm the glyph reappears before calling a defect.

### What still stands, and what does not

**Does not stand:** "video corrupts long text." The blanket's 50 words survived image-to-video intact.

**Still stands, on its own evidence:** the **suncatcher's letterform drift**. There the name stayed
correctly spelled but was redrawn in a markedly bolder typeface *and the panel geometry deformed* — the
silhouette went wavy and the ornate frame vanished. Those are visible across the clip, not one frame.

### Revised rule

| Shot | Method |
|---|---|
| Text read on screen **and** the product is a rigid object being pushed in on | stills Ken Burns — the suncatcher case, where geometry deforms |
| Text read on screen on **cloth**, moderate camera move | Seedance 2.0 is acceptable — verified on the blanket |
| Text present, not read | Seedance 2.0 |

The honest summary is narrower than my earlier one: **video is not a blanket disqualifier for text.**
Verify per shot, across frames.

### The process rule survives, for a different reason
**Never let `motion_qa.py` stand in for reading the words** — it measures motion and cannot read. But
read them **across frames**, which is the part I got wrong. testC (the morphing dog) remains a real case
of the gate passing a misrepresented product; testD3 does not.
