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
| **D3 · video** | does it survive re-synthesis? | ❌ **CORRUPTS THE TEXT** — *feeling* → *ceeling* |
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

## ⛔ D3 — video corrupts the text, and every gate passed anyway

Seedance 2.0, doc two-shot recipe, 1080, from the D2 still.

```
                         dur  hook3   peak  motion  cuts/s  static%
testD3-video.mp4         4.9  15.60  59.33   18.00    0.21        0
GATE                       —   ≥8.0      —    ≥6.0   ≥0.15      ≤10
```

**All four gates pass. The clip misspells the product.**

At 100% (`d3-text-zoom.png`): *"So when you're **ceeling** low"* — the `f` in *feeling* has become a `c`.
Line breaks have also shifted and *"and Light"* is displaced from its line.

**This is the failure mode flagged at the start of Test D as the dangerous one** — not obvious garbage,
which gets caught, but text that reads correctly at thumbnail size and is wrong when you look. It shipped
past `motion_qa.py` with a hook3 of 15.6. **The gate cannot detect this. Only reading the words can.**

⚠️ One corruption was found by inspection; there may be more. Any video frame where the poem is visible
must be read, not scanned.

### The rule

| Shot | Method |
|---|---|
| Text is read on screen | **Stills + ffmpeg Ken Burns at native resolution.** Never video. |
| Text present but not read (wide, over-shoulder, background) | Seedance 2.0 is fine |

Same conclusion as the suncatcher, but a grade worse. There the name stayed correctly spelled and only
changed typeface. Here the word is **misspelled** — on a personalization product, indistinguishable from
printing the customer's name wrong.

## D4 — casting matched

`testD4-cast-matched.png`. Cast to NICOLE grown up: same warm brown skin, same curly golden-brown puffs.

- ✅ **Casting reads correctly** — she is recognisably the printed granddaughter, twenty years on
- ✅ **Text word-perfect** again in stills
- ⚠️ **The pose drifted to a product display.** Prompted for the blanket *wrapped around her shoulders and
  pooling across her lap*, the model had her **hold it up flat like a catalogue board**, face half hidden
  behind the top edge. Legible, but it is a packshot, not an emotional beat — and this product's whole
  structure is emotional. Re-prompt with the pose as the load-bearing instruction and the text incidental.

## Open

- **Scale.** No arm has established 80×60. Held up or draped on a lap it reads as a throw. Needs a human
  scale cue — fully wrapped around the shoulders, or two people under it — before the size claim is
  credible.
- **Pose.** D4 needs a re-run that holds the wrapped pose.
- **Child vs adult granddaughter** — see the casting note above; blocks nothing but changes the concepts.
