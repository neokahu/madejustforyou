# Granddaughter blanket — "To My Sweetie Pie" (`MJ4U-012`)

> Product page: https://madejustforyou.net/products/personalized-to-my-granddaughter-blanket-from-grandma
> Real artwork: `assets/product-sweetie-pie-blanket.png` (1500×1500 RGBA)
> Hero variant **L 80×60** — $69.95 · base $39.59 · GP $30.36 · **BE ROAS 2.30×** · target CPA $21.25

## ⚠️ The docs described the wrong product until 2026-09-26

`PHASE1-TOURNAMENT-3-products.md` recorded this blanket's printed line as
*"This old girl will always have your back"* and built **concept B2 entirely on it.** That line is not on
this product. Corrected in the EN doc, the VI doc, the live testing-plan page and the session log.

## What is actually printed

Headline **"To My Sweetie Pie"**, then a ten-line poem:

> I hugged this **SOFT BLANKET** / I SQUEEZED IT REALLY TIGHT / I FILLED IT WITH MY WISHES /
> *Hope and Love and Light* / So when you're feeling low / JUST HOLD IT REALLY TIGHT /
> You'll feel **MY LOVE** within it / MORNING, NOON AND NIGHT / Love, **Grandma**

Pale blue sky, white and blue clouds, small elephants, butterflies, gold stars, two hand-drawn hearts.
**~50 words, four colours, three weights.**

## Personalization — richer than previously recorded

- **Two customizable cartoon figures** — skin tone, hair style and colour, outfit
- **A name under each** (sample: ALICIA, NICOLE)
- **The relationship word** in the signature ("Grandma")

### ⚠️ Casting constraint this creates

Because the figures are customized, **whoever appears on camera must match the figures printed on the
blanket in that shot.** The sample artwork shows a Black grandmother and a Black granddaughter.

**This is not hypothetical — Test D2 produced exactly that failure unprompted:** asked for "a young
woman" holding the blanket, the model cast a white woman against Black cartoon figures. Decide casting
against the artwork before the shoot, or regenerate the artwork to the cast. It is not fixable in QA.

**✅ Confirmed as a rule by the user, 2026-09-26** — reviewing D2: *"the girl using the blanket is not
[ok], it should represent the similar girl on the blanket."* So this is a hard requirement, not a
preference. **Never describe the on-camera person generically.** Name the skin tone, hair texture, hair
colour and style to match the printed figure, every time.

**Age judgement, flagged:** the figure on the blanket is a small child, but the concepts are written for
an **adult** granddaughter (B1's graduation and moving-out beats, B3's *"when life knocks her down"*).
D4 therefore casts a young Black woman with NICOLE's skin tone and curly golden-brown hair — the printed
child, grown up — rather than a child. If the ad should instead show the child at the age printed, the
concepts need rewriting first, because their beats do not fit a small child.

## Test D — 2026-09-26

| Arm | Question | Result |
|---|---|---|
| **D1 · flat on a bed, top-down, 4K** | can ~50 words reproduce at all? | ✅ **word-perfect** |
| **D2 · draped over a woman on a sofa, 4K** | does text survive cloth folds? | ✅ **word-perfect, and the print follows the folds** |
| **D2 · scale** | does 80×60 read as large? | ❌ reads as a throw, not a blanket that wraps |
| **D2 · casting** | — | ❌ white woman against Black figures |
| **D3 · video** | does it survive re-synthesis? | ✅ **text holds** — my initial "corruption" finding was wrong, see below |
| **D4 · casting matched to the artwork** | does a cast-matched shot hold text + figures? | ✅ casting + text · ⚠️ pose became a product display |

### D1 + D2: I was wrong about long text

Verified at 100% on native pixels (`testD1-poem-top.png`, `testD1-poem-bot.png`, `testD2-fold-zoom.png`):
every line, every colour, every weight, the apostrophes in *you're* and *You'll*, the elephants, moons,
stars and hearts, and both characters' faces and hair. **No gibberish anywhere** — which was the failure
mode I had flagged as most dangerous because it ships unnoticed.

**And the cloth case passed too.** I had recorded that *"a flat PIL homography cannot follow cloth — likely
needs mesh warping."* Nano Banana Pro rendered the print following the drape with correct perspective and
shading, unprompted. **The mesh warp is not needed.** That was the last argument for building the
compositing engine, and it is now gone for this product as well.

### What still makes this product VO-led — for a different reason than recorded

The docs said the blanket must be VO-led because *"the product is a wall of text illegible on a phone."*
Half right. The text **renders** fine and is legible in a still. What a viewer cannot do is **read 50
words in a 30-second ad.**

That is an **attention** constraint, not a rendering constraint — and the distinction changes the shot
plan. Skeleton B (grandma reads it aloud) stays correct, but the reason is that the VO delivers the
message faster than reading can, not that the words would come out broken. So:
- Do **not** hold a wide shot of the whole blanket expecting anyone to read it.
- Do let the camera find **one line** — the poem's pivot, *"So when you're feeling low, just hold it
  really tight"* — while the VO carries the rest.
- Legibility being solved means that one line can genuinely be read on screen, which the old plan assumed
  was impossible.

## ✅ D3 — video holds the text. My first reading was wrong.

Seedance 2.0, doc two-shot recipe, 1080, from the D2 still.

```
                         dur  hook3   peak  motion  cuts/s  static%
testD3-video.mp4         4.9  15.60  59.33   18.00    0.21        0
GATE                       —   ≥8.0      —    ≥6.0   ≥0.15      ≤10
```

All gates pass, **and the text is correct.**

### The mistake, recorded because the method error matters more than the call

I inspected **the final frame only**, read *"So when you're ceeling low"*, and concluded the video had
corrupted the print — writing it up as the project's most important quality finding.

**It was occlusion, not corruption.** Checked across frames 60 / 80 / 95 / 105 / 115 / 119
(`d3-f-check.png`): frames 80 and 95 show **"feeling"** with a complete `f`, ascender and crossbar
intact. In the later frames the word rides up toward the blanket's top edge as she pulls it, and a fold
crops the ascender — leaving a shape that reads as `c` in a still frame. The apparent line-break shift
has the same cause: perspective and drape, not re-lettering.

**Rule this produces: never judge printed text from a single frame.** A fold, an edge or a highlight can
remove a stroke. Sample across the clip and confirm the glyph reappears. One frame is an anecdote.

Credit where due — the user caught this: *"the text is fine. the reason is that when the girl pulls up
the blanket, it creates wrinkles that cover the F and you mistook it as C."* Correct, and verified.

## D4 — casting matched

`testD4-cast-matched.png`. Cast to NICOLE grown up: same warm brown skin, same curly golden-brown puffs.

- ✅ **Casting reads correctly** — she is recognisably the printed granddaughter, twenty years on
- ✅ **Text word-perfect** again in stills
- ⚠️ **The pose drifted to a product display.** Prompted for the blanket *wrapped around her shoulders and
  pooling across her lap*, the model had her **hold it up flat like a catalogue board**, face half hidden
  behind the top edge. Legible, but it is a packshot, not an emotional beat — and this product's whole
  structure is emotional. Re-prompt with the pose as the load-bearing instruction and the text incidental.

## ✅ D5 — pose and scale both solved, by fixing the prompt not the model

Three variants, each **~50 words, pose-led, and describing the product NOT AT ALL**, per
`image-to-video-prompt-method.md`. Drafted at 2K per the doc, batched 3 per the best-of-N rule.

| Variant | Shot | Result |
|---|---|---|
| **D5a · wrapped** | fully wrapped on a sofa, falling past her lap to the floor | ✅ pose fixed, scale reads large — **the emotional beat** |
| **D5b · arm-span** | held open at full arm span, still reaching the floor | ✅ **strongest scale cue** — the 80×60 claim is finally visible. Hero/packshot |
| **D5c · two people** | grandma + granddaughter under it together | ✅ scale via two bodies, **and** the relationship the product is about |

Casting correct in all three; D5c matches **both** printed figures (grey bun = ALICIA, curly puffs =
NICOLE). Text fully legible in all three.

### The finding that matters

**I described the product not at all, and the print came back correct anyway** — because the reference
image already carries it. Deleting ~140 words of product description is what let the pose instruction
land. D4's packshot drift was never a model limitation; it was my prompt making the print outrank the pose.

This is THE ONE RULE demonstrated rather than quoted: *"the image already defines the product,
composition, and text… never re-describe the product."* A `PreToolUse` hook now blocks prompts that
break it — `research/reference/generation-prompt-guard.md`.

### Shot assignment for the build

- **Emotional beat / reaction** → D5a framing
- **Product hero + size proof** → D5b framing
- **Relationship beat (house rule)** → D5c framing

## Open

- **Child vs adult granddaughter** — the printed figure is a small child; the concepts (B1 graduation,
  B3 *"when life knocks her down"*) are written for an adult. D4/D5 cast her as an adult. Blocks nothing,
  but if the ad should show a child, the concepts need rewriting first.


## D6 / D7 — the hand, fixed in two passes (2026-09-26)

The user rejected D5a twice: *"the hand looks like it's punching a hole through the blanket"*, then
*"just keep both of her hands in the blanket."*

| | Prompt | Result |
|---|---|---|
| **D5a** | *"Only her face and one hand show"* | ❌ no real hand; an ambiguous shape at the blanket's top edge |
| **D6** | right hand located — *"rests on the top edge near her collarbone, fingers relaxed and fully visible"* | ⚠️ natural hand, but still read as intrusive |
| **D7** | *"Both her hands stay wrapped inside the blanket, held against her chest beneath the fabric, so the blanket's printed front face stays smooth and unbroken"* | ✅ **accepted shape** — no hand in frame, front face unbroken |

**The lesson is not "locate the limb" — it is "the simplest correct answer may be to remove it."** D6
followed the doc and was still wrong for the shot. Stating the *surface* we want protected ("printed
front face stays smooth and unbroken") did what describing the hand could not.

⚠️ Text is cropped at the left and right edges where the blanket wraps. Inherent to this framing and
acceptable — the poem is read in the flat D1 / D5b framings, not here.

Assets: `D6-limb-rule.png`, `D7-hands-inside.png` (use **D7**), `compare-D5a-vs-D6.png`.

---

## ▶️ Before production — recommended next step

**One vertical slice, not more component tests.** Build **S-C1-H1 end to end** (5 clips → assemble →
grade → captions → music → score). Untested today and all exercised at once by that single build:

1. **Identity across multiple clips** — the biggest gap. Test B proved identity in ONE still and ONE
   camera change. Four clips of the same person have never been compared side by side. This is rule #2's
   actual risk and the MJ4U-111 failure mode.
2. **Assembly** — no full 20s cut exists. Grade continuity across separately-generated clips, structure-A
   timing, caption legibility sound-off, music bed, end card.
3. **Meta 9:16 safe areas** — feed UI crops top and bottom; CTA/end-card placement unchecked.
4. **kie.ai cost visibility** — its balance endpoint returns no number; we are spending blind there.

≈$2 on AtlasCloud. A grade mismatch found after one ad costs one ad; after twelve it costs twelve.
