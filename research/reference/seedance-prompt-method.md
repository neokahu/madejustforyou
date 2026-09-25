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

## ⚠️ Model caveat: people

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
