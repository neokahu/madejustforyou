# Image prompt method — GPT Image 2/2.5 · Nano Banana 2/Pro · Seedream 5.0

> Sources: **OpenAI** *Image prompting* guide (developers.openai.com/api/docs/guides/image-prompting) +
> openai-cookbook `image-gen-models-prompting-guide` · **Google Cloud** *The ultimate Nano Banana
> prompting guide* (2026-03-05) + blog.google Nano Banana Pro tips · **ByteDance Seed** Seedream 5.0 Pro
> launch + **BytePlus ModelArk** image-generation tutorial + Replicate *How to prompt Seedream 5.0*.
> Written 2026-09-26 after the user rejected a render: *"the hand looks like it's punching a hole
> through the blanket, not natural. Do research on the best way to prompt for these models."*
>
> Companion to [[image-to-video-prompt-method]] (i2v) and [[seedance-prompt-method]] (video).
> **This doc covers the IMAGE models. It did not exist before, which is why image prompting was guesswork.**

## Why this doc exists — the failure it explains

Two of my renders failed on the same thing, and the cause was documented all along.

`testD5a` prompt contained: *"Only her face and one hand show."* Result: a hand at an arbitrary position
that reads as coming **through** the fabric.

**Google's best-practice #2, verbatim:** *"Use positive framing: describe what you want, not what you
don't want (e.g. 'empty street' instead of 'no cars')."*

*"Only her face and one hand show"* is an exclusion. It never says **where the hand is** or **what it is
touching**. This is the image-side twin of the video-side rule I added after Test E — *locate the action
in space* — and it generalises:

> **THE LIMB RULE: never describe a body part by what is hidden. Say where it is and what it touches.**
> ❌ "Only her face and one hand show"
> ✅ "Her right hand rests on top of the blanket at her collarbone, fingers relaxed and visible"

---

## Per-model prompt structure — they are NOT the same

### GPT Image 2 / 2.5 — the "Golden Order"

```
Background / Environment → Subject → Specific details → Constraints
```

*"Always move from wide context to narrow specifics. This mirrors how the model's reasoning engine parses
intent."*

**OpenAI's six rules:**
1. Structure consistently — background → subject → details → constraints
2. Be specific about **materials and textures** — *"brushed aluminium"*, not *"shiny metal"*
3. Use **explicit constraints** — state what to preserve **and** what to change
4. Put literal text in **quotes or ALL CAPS**, with font, size, placement
5. **Iterate with small changes** — do not overload one prompt
6. Reference multi-image inputs **by index and role**

**Editing style is different from generating — direct commands, terse:**

> ❌ *"Transform this beautiful image by artistically changing the background to create a more dramatic atmosphere"*
> ✅ *"Change background to sunset beach. Keep subject unchanged."*

No flowery language, no justifications. **This is the opposite of how I have been writing prompts.**

**Multi-reference format — assign every reference a role:**

```
Use Image 1 (man in suit) as character reference.
Use Image 2 (neon city) as background/style reference.
Place character in scene with cinematic rim lighting.
```
Role types: `style · character · pose · composition · background`.
Also: `input_fidelity="high"` on edits when detail must survive.

### Nano Banana 2 / Pro (Gemini 3) — a *thinking* model

> *"It doesn't just match keywords; it understands intent, physics, and composition. Stop using 'tag
> soups' and start acting like a Creative Director."*

**Text-to-image, no references:**
```
[Subject] + [Action] + [Location/context] + [Composition] + [Style]
```

**With references — the one we use:**
```
[Reference images] + [Relationship instruction] + [New scenario]
```
Google's own example: *"Using the attached napkin sketch as the **structure** and the attached fabric
sample as the **texture**, transform this into a high-fidelity 3D armchair render. Place it in a
sun-drenched, minimalist living room."*

Note the shape: **each reference is given a job** ("structure", "texture"), then the relationship, then
the new scene. My prompts named no relationship at all.

**Four best practices:** be specific · **positive framing** · control the camera with photographic terms ·
iterate conversationally.
**Start the prompt with a strong verb** naming the primary operation.

**Editing:** *"Be explicit about what to keep exactly the same."* Semantic masking works — you can define
a mask in words. **If an image is 80% right, refine it; do not regenerate from scratch.**

**Creative-Director controls** (all four are levers I have never used):
- **Lighting** — *"three-point softbox setup"*, *"chiaroscuro, harsh high contrast"*, *"golden-hour backlighting creating long shadows"*
- **Camera / lens** — name the body and the lens: *GoPro* for distorted action, *Fujifilm* for colour science, *disposable camera* for nostalgic flash; *"low angle, shallow depth of field (f/1.8)"*, *"wide-angle"*, *"macro"*
- **Colour grade / film stock** — *"as if on 1980s colour film, slightly grainy"*, *"muted teal"*
- **Materiality** — *"navy blue tweed"*, not *"a suit jacket"*

**Text rendering:** quotes around the words, **name the font** (*"bold white sans-serif"*, *"Century
Gothic"*), and the **text-first trick** — settle the wording in conversation, then ask for the image.
Up to **14 reference images**; 1K/2K/4K.

### Seedream 5.0 — quotes and visual markers

- **Double quotation marks around any text to be rendered.** Quote it, place it, keep it short — long
  fine print falls apart (ByteDance admits this).
- **Visual markers beat description for placement:** draw arrows, boxes or coloured regions **on the input
  image**, then reference them — *"Place a large painting where the red rectangle is on the wall."*
  ⚠️ **We should be doing this.** It is deterministic placement without TopView's AnyShoot, and it is the
  answer to "prompt exactly what appears where".
- **Keep prompts under ~600 words** — *"very long prompts may scatter the information, causing the model to
  overlook details."*
- Realism comes from **imperfection**: sensor noise, handheld softness, "no beauty filters" — not from "8K".
- Resolution words in the prompt do nothing; **set size in parameters**. Pro caps at 2048×2048 total pixels.
- Has **automatic prompt optimisation** — terse prompts get rewritten before generation, so a short prompt
  is not necessarily the prompt that ran. `optimize_prompt_options.mode` controls it.
- Multi-image by index: *"Combine the people from Images 2 to 6 referencing the positioning in Image 1."*

---

## Our unified checklist

1. **Positive framing, always.** Never "only X shows", "no Y", "without Z".
2. **THE LIMB RULE** — every hand, arm and gaze gets a position and a contact point.
3. **Assign a role to every reference** — character / style / pose / composition / background / texture.
4. **State the relationship** between references, then the new scenario.
5. **Never re-describe what the reference carries** (also THE ONE RULE in [[image-to-video-prompt-method]]).
6. **Text:** double quotes + font + placement. Keep it short.
7. **Editing = terse commands.** What changes, what stays. No prose.
8. **Use the director levers** — lighting, camera/lens, grade, materiality.
9. **Refine, don't regenerate,** when it is 80% right.
10. **Draft low-res, batch 3–4, select.**

## Model routing for our work

| Need | Model | Why |
|---|---|---|
| Product artwork / printed text must be exact | **Nano Banana Pro** | measured best text fidelity — carried the whole blanket result |
| Deterministic placement of an element | **Seedream 5.0** + visual markers on the input | replaces AnyShoot's coordinate control |
| Identity-preserving edit with several references | **GPT Image 2.5** + `input_fidelity="high"` + role-labelled refs | strongest documented multi-ref role system |
| Avoid | GPT Image at 4K/max for artwork | 4× the cost of Nano Banana Pro and it rendered the **wrong typeface** |

## Rewrite of the prompt that failed

**Before** (produced the punched-through hand):
> Wide shot, soft window light. A young Black woman with curly golden-brown hair in two puffs sits on a
> sofa completely wrapped in the blanket from @Image 1 — it covers both shoulders, falls past her knees
> and pools on the floor. **Only her face and one hand show.** She looks down, calm.

**After** — reference given a role, limb located, positive framing throughout:
> Use Image 1 as the blanket's **pattern and texture** reference.
> A warm living room, soft window light from the left. A young Black woman in her twenties with curly
> golden-brown hair in two puffs sits on a sofa, the blanket drawn around both shoulders and falling
> across her knees to pool on the floor. **Her right hand rests on the blanket's top edge near her
> collarbone, fingers relaxed and fully visible; her left arm stays inside the blanket.** She looks down
> at the fabric, calm.
> Keep the blanket's printed design exactly as in Image 1. Photographic, shallow depth of field.


---

## ✅ Verified 2026-09-26 — the rewrite fixed it

Ran the "After" prompt above on Nano Banana Pro, 2K, same reference.
Evidence: `products/blanket-granddaughter/tests/compare-D5a-vs-D6.png`.

| | Before (`kieai-nbpro-D5a.png`) | After (`D6-limb-rule.png`) |
|---|---|---|
| Hand | ❌ no real hand; an ambiguous shape at the blanket's top edge | ✅ right hand resting flat near the collarbone, five fingers, clearly on top of the fabric |
| Printed text | legible | legible |
| Casting | matches NICOLE | matches NICOLE |
| Headline occlusion | less | ⚠️ slightly more — hand and forearm sit higher |

**The limb fix is real. The cost is a little more occlusion of "My Sweetie Pie"** — acceptable for the
emotional beat, since the poem is read in the flat D1/D5b framings, but it is a trade not a free win.

Also added `Shot on a Fujifilm camera, 50mm lens, shallow depth of field` — the director levers from the
Google guide. Warmer, more filmic than the earlier renders.

## ⚠️ The hook had a hole, found only by testing it

`nano_banana`, `gpt_image`, `seedream`, `flux2_image`, `imagen4`, `ideogram_v3` and `wan_image` were
**never in the guard's tool list**. Every kie.ai image call went through **unguarded** — including the one
that produced the bad hand. Fixed in the tool list and in `.claude/settings.json`'s matcher.

Two further guard corrections, both surfaced by it blocking correct work:
- **Image word cap was 100**, inherited from the i2v doc which is about *animating* an existing image.
  Image *generation* formulas are structurally longer; Seedream's own limit is ~600. Image cap is now 250.
- **REFROLE regex** missed `as the blanket's pattern and texture reference` because of the possessive.

New image checks the guard now enforces: `NEGFRAME` (exclusionary framing), `LIMB` (a limb named but
never located), `REFROLE` (a reference with no assigned role).
