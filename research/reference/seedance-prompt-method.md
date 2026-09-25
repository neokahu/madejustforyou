# Seedance prompt method — image-to-video

> Sources: BytePlus official *Dreamina Seedance 2.0 series prompt guide* (docs.byteplus.com/en/docs/modelark/2222480) ·
> ByteDance Seed *Introducing Seedance 2.5* · TopView plugin `references/seedance-2.5.md` (vendor contract) ·
> Seedance 1.0 Lite prompt guide (aimlapi) · RunDiffusion Seedance 2.0 guide · Flick Seedance 2.5 guide.
> Written 2026-09-25 after our own Test C failed in a way the official guide predicts exactly.

## The model's own mental model

Seedance decomposes a prompt into a **spatial layer** (what is in the frame) and a **temporal layer**
(how it changes). So a prompt is an *engineering instruction*, not ad copy: who, where, doing what, how
the camera moves, in what order. Copy-style prose gets copy-style results.

## Formula

```
precise subject + action details + scene/environment + lighting & colour tone
+ camera movement + visual style + image quality + constraints
```

**For image-to-video specifically the rule inverts:**

```
subject + movement, background + movement, camera + movement
```

> "Minimise static descriptions. Since the graphic video already has a scene, focus on describing the
> moving parts."

The start frame already carries the room, the palette, the product. Re-describing them wastes the prompt
and invites the model to re-render — which is how a product drifts.

## The seven rules that matter most

**1 · One camera movement per shot.** Official, verbatim: *"Try to specify only 1 type of camera movement
in a single shot. Do not require push, pull, pan, and move at the same time, as this will increase image
instability."* The model knows standard grammar — `medium shot`, `close-up`, `wide shot`, `slow push-in`,
`smooth lateral tracking`, `fixed shot`. Pick one.

**2 · Define subjects explicitly, then reuse the label.**
`Define [2–3 stable static features] in @Image N as <Subject>` — then refer to `<Subject>` every single
time. Two or three features, not ten; they must uniquely identify, not exhaustively describe.

**3 · Storyboard by shot, not by timecode.** Organise as `Shot 1 / Shot 2 / Shot 3`, each as:
camera move → subject action/expression → position change → audio. **Do not force timings** — *"support
for precise timing (such as 0–3 seconds) is unstable, and forcibly limiting duration may lead to abnormal
generation results."* This contradicts the second-by-second beat sheets in our own build plan: those are
for *us*, and must be converted to named shots before they reach the model.

**4 · Actions: body-part specific, quantified, gentle.** Name the part and the degree — `slowly raise a
hand`, `slightly lower the head`. Prefer *"slow, gentle, coherent subtle movements"* and avoid big
dynamic action. Add the transition between actions (`use the inertia of turning to naturally raise a
hand`) so motion is continuous rather than cut-up.

**5 · Emotion as physical detail, never as an adjective.** Not "very sad". The guide's own table:

| Emotion | Write instead |
|---|---|
| Sadness | lowering the head, shoulders trembling slightly, eyes reddening, fingers clutching the corner of clothing, tears welling but not falling |
| Relief | letting out a long breath, tense shoulders relaxing, a long-lost faint smile, looking up toward the distance |

Directly usable for our memorial work.

**6 · Constraint words are not optional.** *"Constraint words are very important. They can effectively
avoid visual flaws, deformities, breakdowns."* Standard set: `characters' faces and body proportions
remain stable without deformation`, `movements are continuous and natural, no stutter or flicker`,
`avoid generating any text or subtitles`, `do not generate a logo`, `do not generate a watermark`.

⚠️ **Conflict with the TopView contract:** TopView says *"do not add generic quality boilerplate,
negative prompts, watermark bans, or subtitle bans that the user did not request."* BytePlus says
constraints are essential. **Resolution: keep constraints that protect the specific thing we are selling**
(pose, identity, product geometry) and drop generic boilerplate. A constraint naming *our* failure mode is
not boilerplate.

**7 · Symbols carry meaning.**

| Type | Symbol | Example |
|---|---|---|
| Music | `（）` | （soft piano, no percussion） |
| Sound effect | `<>` | `< a dog's collar tag chimes somewhere off-screen >` |
| Dialogue | `{}` | `{I still leave the window open}` |
| Subtitle | `【】` | `【Made just for them】` |

## Asset strategy

Four functional roles: **character anchoring · scene tone-setting · camera-movement reference · rhythmic
atmosphere.** Recommended total **4–5 assets**: 1–2 character images + 1 scene image + 1 camera-movement
video + 1 audio clip.

> *"It is not recommended to use the full asset limit. Too many assets will make it difficult for the
> model to judge feature priorities."*

So our instinct to feed every reference we own is wrong. One duty per reference, few references.

## Mode, and what belongs in parameters

Per the TopView contract, `auto` / `edit` / `extend` goes in **structured parameters**
(`omniReferenceTaskType`), never in prose. Same for aspect ratio, duration, resolution. `edit` and
`extend` both require a real `reference_video`; a video used only for style/motion/camera stays `auto`.

## ⚠️ Model caveat: people — ✅ RESOLVED 2026-09-26, see Test E below

**Superseded.** Test E ran people on Seedance 2.0 and identity, faces and hands all held. Use 2.0 for
people; 2.5 underperformed it. The original concern, kept for provenance:

RunDiffusion's guide states Seedance 2.0 is **restricted with people** and recommends Seedance 1.5 Pro,
Kling or Veo 3.1 for human subjects, with 2.0 best for scenes and architecture. Our ads are people-heavy
(owner, granddaughter, sympathy-giver). **Verify per model before committing a human-centred body to
Seedance 2.0.** Our Test B identity hold was GPT Image 2.5 for stills — it says nothing about video.

---

## Post-mortem: why our Test C morphed

Prompt used (Wan 3.0, 5s, from the Test A still):

> *The reveal beat. Camera pushes in steadily toward the wall as the sun drops: the coloured light sweeps
> visibly across the floorboards, and the German Shepherd shadow slides and sharpens on the wall until the
> name glowing inside it resolves. The suncatcher turns gently on its cords, throwing moving blue and gold
> light. Dust motes drift through the sunbeam. Continuous motion throughout, no static hold, no cuts.*

It scored well (`hook3 12.11`) and the dog changed from sitting to standing. Against the guide:

| Rule | What I did |
|---|---|
| One camera movement per shot | **Four simultaneous motions** — camera push, light sweep, panel rotation, dust drift. The documented cause of instability |
| I2V: describe only what moves | Re-described the panel and its artwork, which the start frame already held |
| Constraint words | **None.** Nothing said *preserve the sitting pose* or *product geometry unchanged* |
| No unrequested negatives in prose | "no static hold, no cuts" written as prose instruction |
| Shot structure | One run-on sentence, no `Shot 1 / Shot 2` |
| Verb choice | *"slides and sharpens… until the name resolves"* — transformation verbs invite redrawing. A shadow that is asked to *change* will be redrawn, and a redrawn dog is a new dog |

The morph was not bad luck. It was four documented rule violations, and the fix is mechanical.

## Our template for a product-reveal beat

```
Use @Image 1 as the first frame.
Define the black German Shepherd silhouette panel hanging in the window in @Image 1 as <Panel>.

Shot 1: Fixed camera, wide. The low sun moves; the coloured light cast by <Panel> travels slowly
across the wooden floor. <Panel> hangs still.
Shot 2: Slow push-in toward the wall. The shadow cast by <Panel> grows larger in frame as the
camera approaches. The shadow's shape does not change.

< faint chime of a collar tag somewhere off-screen >
（soft piano, sparse, no percussion）

Warm late-afternoon light, natural documentary photography, cinematic texture.
<Panel> geometry, artwork and the seated pose of the dog remain exactly as in @Image 1, unchanged
throughout. No deformation, no morphing. Continuous natural motion, no stutter or flicker.
Avoid generating any text or subtitles. Do not generate a logo or watermark.
```

The load-bearing line is *"The shadow's shape does not change"* plus the explicit pose constraint. Motion
comes from **camera and light** — things allowed to change — while the **product is pinned**.

---

## Verified 2026-09-25 — the corrected prompt, same start frame, same 5s/720

Re-ran the reveal beat on **Seedance 2.0** (`seedance-2.0-style`) with the template above. Only the
prompt changed.

```
                                dur  hook3   peak  motion  cuts/s  static%
testC  (Wan 3.0, bad prompt)    4.9  12.11  18.87   11.83     0.0        0
testC2 (Seedance, corrected)    4.9   5.87  36.24    9.82    0.21        0
GATE                              —   ≥8.0      —    ≥6.0   ≥0.15      ≤10
```

**✅ The morph is fixed.** The dog stays **seated** through all four sampled frames. The first attempt had
it standing by frame 3. Heart, florals and panel geometry all hold. "Alex" appears at roughly the right
scale instead of ballooning into a body-spanning word. The load-bearing lines were *"Shadow's outline does
not change"* and *"The dog stays seated"* — a constraint naming the specific failure mode.

**✅ Shot grammar works, and buys a cut.** `cuts/s 0.21` — Seedance honoured `Shot 1` / `Shot 2` and cut
between them inside a single 5s generation. That clears the 0.15 cut gate, which a single continuous clip
normally cannot. Named-shot storyboarding is therefore worth using even within one clip.

**❌ `hook3` dropped to 5.87 and fails — my error, not the method's.** I made Shot 1 a **fixed camera**,
and `hook3` measures the first three seconds. *One camera movement per shot does not mean no movement.*

**Rule to add: the opening shot must carry its own single camera move.** Reserve `fixed camera` for later
shots. For the reveal beat, Shot 1 should be a slow push-in or a slow lateral track, with Shot 2 taking a
different single move — not stillness followed by motion.

Evidence: `products/suncatcher-dog-memorial/tests/testC2-seedance-corrected.mp4`, `testC2-frames.png`.

### Third run — the fix, and the trade-off it exposes

Only change from run 2: Shot 1 became a **smooth lateral track** instead of `fixed camera`.

```
                                dur  hook3   peak  motion  cuts/s  static%
testC  Wan 3.0, bad prompt      4.9  12.11  18.87   11.83     0.0        0   dog morphed
testC2 Seedance, fixed open     4.9   5.87  36.24    9.82    0.21        0   hook3 fail
testC3 Seedance, moving open    4.9  14.68  18.49   14.72     0.0        0   ✅ PASS
GATE                              —   ≥8.0      —    ≥6.0   ≥0.15      ≤10
Macorner (333 days live)        17.7  18.05      —   12.62    0.40        3
```

`hook3` **14.68** clears the gate and is **4× our shipped film's 3.59**; `motion` **14.72** exceeds the
competitor winner's 12.62; `static 0%`. The dog stays seated in every sampled frame, with heart, florals
and butterflies consistent and "Alex" legible at true scale.

**Trade-off:** `cuts/s` fell to 0. The cut in run 2 existed *because* Shot 1 was static and Shot 2 moved —
the frame-differencer reads that contrast as a cut. Two moving shots blend into one continuous move.

**This does not matter, and knowing why is the point:** the cut gate applies to the **assembled** film,
where cuts come from beat-to-beat editing in ffmpeg. Within a single clip, prefer motion over a
manufactured cut. Only reach for a static→moving contrast when a clip must stand alone.

**Settled recipe for a product-reveal beat:** two named shots, each with its own single camera move, the
opening shot moving; describe only light and camera; pin the product with a constraint that names the
exact failure mode.

---

## ⚠️ Scope of this document — read before reusing these prompts elsewhere

Everything above is **Seedance-specific**, sourced from BytePlus's own guide and the TopView vendor
contract. MiniMax H3, Wan 3.0, Kling and Veo have their own prompt conventions.

Running a Seedance-grammar prompt on another model is a **confound**: if that model performs worse, you
cannot tell whether it is worse at the task or worse at this grammar. When comparing models, either
(a) write each arm in its own grammar and accept that the prompt is no longer controlled, or
(b) keep the prompt identical, and report the non-Seedance arms as **indicative only**.

Test E (2026-09-26) took option (b) deliberately.

## Prompt audit — Test E, people in video

Written before the run, audited against the rules above. Two deviations found, both mine:

| Rule | Verdict |
|---|---|
| One camera movement per shot | ✅ `Slow push-in` only |
| Define subject by 2–3 stable features, reuse label | ✅ `<Owner>` — grey beard, wire-rimmed glasses, green plaid flannel |
| Named shots, not timecodes | ✅ `Shot 1` |
| Actions body-part specific, quantified, gentle | ✅ "slowly raises his right hand", "fingers opening slightly" |
| Emotion as physical detail | ✅ "shoulders drop as he lets out a long breath" — the guide's own *Relief* row |
| Constraints naming **our** failure mode | ✅ face/glasses/beard unchanged; five fingers |
| Symbol grammar | ✅ `（soft piano, sparse, no percussion）` |
| **I2V — describe only what moves** | ✅ *(I first marked this ❌ — wrong. The doc's own shipped template carries the same short lighting/style line, so keeping it is following the method, not breaking it. The rule bans re-describing the **subject and product**, not a one-line grade cue.)* |
| **No generic boilerplate** | ❌ "Avoid generating any text or subtitles" — no text exists in this shot; this is the boilerplate the TopView contract bans |
| **Two named shots, opening shot moving** | ❌ **the real miss.** The settled recipe is two shots with one camera move each. I wrote one shot — which is also why both arms returned `cuts/s 0.0` |

Neither deviation plausibly causes identity drift, and the prompt was **identical across all four arms**,
so Test E remains a controlled model comparison. But the corrected form is what ships:

```
Use @Image 1 as the first frame.
Define the man with the grey beard, wire-rimmed glasses and green plaid flannel shirt
in @Image 1 as <Owner>.

Shot 1: Slow push-in toward <Owner>. A band of blue and gold light moves slowly across
his face from left to right. <Owner> slowly raises his right hand into the band of light
and holds it there, fingers opening slightly. His shoulders drop as he lets out a long
breath. He does not turn his head.

（soft piano, sparse, no percussion）

<Owner>'s face, glasses, beard and body proportions remain exactly as in @Image 1,
unchanged throughout. His clothing does not change. Hands have five fingers each,
correctly formed. Movements are continuous and natural, no stutter or flicker.
```

**The general lesson:** the lighting/style block belongs in the **text-to-image** prompt that makes the
start frame, not in the image-to-video prompt that animates it. Saying it twice invites a re-render, and
a re-rendered subject is a new subject — the same mechanism that morphed the dog in Test C.

---

## Verified 2026-09-26 — Test E, people. The recipe holds for human subjects.

Four runs, same start frame (`img_3`, owner reference), varying model and prompt structure.

```
                                dur  hook3   peak  motion  cuts/s  static%
testE  2.0, one shot            4.9   8.10  15.10    7.63    0.00        0
testE  2.5, one shot            4.9   4.64   6.04    4.54    0.00        0
testE2 2.5, anchored one shot   4.9   6.88   9.85    6.35    0.00        0
testE3 2.0, doc two-shot        4.9  14.90  43.27   14.96    0.21        0   ✅ ALL GATES
GATE                              —   ≥8.0      —    ≥6.0   ≥0.15      ≤10
Macorner (333 days live)       17.7  18.05      —   12.62    0.40        3
```

**1 · The "Seedance 2.0 is restricted with people" caveat is refuted.** Identity held in every run —
beard, wire-rimmed glasses, heavy brows, plaid over white tee — and hands came back with five correctly
formed fingers each. Delete the warning from the model caveat section for 2.0.

**2 · Use Seedance 2.0 for people, not 2.5.** 2.5 is the platform's *preferred* model and lost on both
measures: roughly half the motion, and it rendered a **lens-flare smear** where 2.0 rendered an actual
blue-and-gold prism band across the face. Preferred ≠ better for our shot.

**3 · The two-shot recipe is not reveal-specific — it is the recipe.** Switching from one shot to two
(lateral track → push-in) took hook3 8.10 → 14.90 and motion 7.63 → 14.96 on the same model, and bought
`cuts/s 0.21` exactly as testC2 did. **One shot leaves `cuts/s` at 0.**

**4 · New rule — locate the action in space, not just on the body.** Rule 4 says actions must be
body-part specific and quantified. That is not sufficient. *"Raises his right hand into the band of
light, fingers opening slightly"* produced a **palm held flat toward camera** — a "stop" gesture, with
eyes closed, in a grief ad. The model has to be told where the limb goes relative to the body and the
camera. What worked:

> *"raises his right hand beside his own cheek, **palm turned away from camera toward the window on his
> left**, so the coloured band falls across the back of his hand"*

plus the constraints *"His eyes stay open"* and *"His palm never faces the camera."*

**5 · Name the light source or the model invents one.** *"A band of blue and gold moves across his face"*
with no source gave a lens flare. *"Sunlight through a stained-glass panel off-screen to his left"* gave a
correct prism band on cheek and palm.

**⚠️ 6 · The corollary, and it matters more than the rest.** Once told there is a stained-glass panel
off-screen, Seedance **built one into frame** — a leaded church window it invented. It looks good and it
is wrong: that is the model rendering the product, the thing our division of labour forbids. Name the
light source **as off-screen** and keep it off-screen, or put our real panel in the start frame. Never
let the model draw what we sell.

Evidence: `products/suncatcher-dog-memorial/tests/testE*.mp4`, `testE3-frames.png`.
