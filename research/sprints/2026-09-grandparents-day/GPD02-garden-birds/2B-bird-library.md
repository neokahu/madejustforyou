# Asset Brief — `GPD02-2B` Grandma's Little Birds · Bird Library + Fixed Frame

> The design deliverable for the **2B** side of the GPD02 A/B (see
> [`brief.md`](brief.md) for the concept, and
> [`2B-bird-layout-spec.md`](2B-bird-layout-spec.md)
> for the per-count layouts). This brief covers **only the reusable art assets** — the bird
> clipart library, the fixed grandma-bird + branch frame, and the Nano-Banana prompts to generate
> them. The *layouts* (how N birds arrange) are the layout spec's job; this is the *art*.

**The one rule that shapes every asset:** in Teeinblue, **reposition/scale is per-clipart-category** —
every bird in the "Birds" category inherits ONE size and ONE anchor. So the whole library must be
built on a **common canvas with a shared anchor**, or birds will perch at different heights/sizes
when the customer swaps them. (Teeinblue guide §4.)

---

## 1. Canvas & anchor spec (applies to EVERY bird — non-negotiable)

| Spec | Value | Why |
|---|---|---|
| Canvas | **520 × 520 px**, transparent PNG | shared box so any picked bird drops into any slot identically |
| Format | 32-bit PNG, alpha, no white halo | Teeinblue places transparent art; it auto-makes the white thumbnail |
| Anchor | **feet on the bottom-center point** — lowest pixels of the grip at **x=260, y≈470** (≈50 px bottom margin) | all birds perch on the branch at the same line, no floaters |
| Facing | **3/4 front, head slightly turned** (LOCKED) | one reused clipart appears at many X-positions and can't be flipped per-slot; a strict side-profile would make a whole row face off-screen |
| Posture | perched, **feet together gripping an implied horizontal perch**; body upright | branch is a *separate* layer beneath — do NOT draw a branch under the bird |
| Visual scale | body fills **~60–70% of canvas height**; **normalize optical weight** so a sparrow and a cardinal read at the same size in a row | prevents "one bird looks tiny / one huge" |
| Content | **single bird only** — no branch, no leaves, no name, no shadow-on-ground, no background | those are separate layers; a baked-in branch would double up |
| Margins | keep art inside a ~40 px safe margin all around | auto-trim tolerance |

**Grandma-bird is the ONE exception** to scale (it's intentionally larger) but shares the same
520-wide canvas conventions — see §3.

---

## 2. The bird library (8 to start)

All 8 share the §1 canvas/anchor. Aesthetic (all): **warm watercolor + subtle hand-embroidered
texture**, soft edges, brand palette accents, storybook-not-clip-art. Each bird keeps its **true
species colors** but pulled toward the brand's warm register (avoid cold/neon).

| # | Bird | Signature marks (must read at a glance) | Palette lean |
|---|---|---|---|
| 1 | **Robin** (American) | warm orange-red breast, brown-grey back, thin beak | clay/honey — brand-core |
| 2 | **Bluebird** (Eastern) | blue back & wings, rust-orange breast, white belly | muted blue + rust |
| 3 | **Cardinal** (male) | all-red body, black face mask, pointed crest | clay-red |
| 4 | **Chickadee** | black cap + bib, white cheeks, soft grey wings | warm grey |
| 5 | **Sparrow** | brown streaked back, pale chest, stubby beak | tan/sand |
| 6 | **Dove** | soft dove-grey → cream, gentle round head, small | cream/grey |
| 7 | **Goldfinch** | bright yellow body, black cap & wing bars | honey-yellow |
| 8 | **Owl** (small, round) | round face disc, big soft eyes, brown mottled | warm brown |

> Owl appears twice on purpose: a **small owl** in the library (a customer can pick it for a
> grandkid) and a **larger owl** as the fixed grandma-bird (§3) — same species, different size/role.

**Expansion slots (later, if 2B wins):** blue jay, wren, hummingbird, penguin (novelty), swallow —
add to the same category on the same canvas; layouts don't change.

---

## 3. Fixed frame (renders at EVERY count — solves "1 bird looks empty")

These are NOT customer-picked; they're always-on layers the designer builds once.

### 3a. Grandma-bird — **plump owl on a small nest** (LOCKED: no props)
- Slightly **larger** than library birds (≈1.4× optical weight) — reads as "the matriarch" by
  size + top-center placement alone. **No glasses, no shawl** (keeps it timeless, avoids clip-art).
- Sits on / just above a **small woven nest**. Warm-brown owl, round, soft eyes, content expression.
- Own canvas: **720 × 720 px**, transparent, **nest base on bottom-center anchor** (perches on the
  top branch). Kept as a fixed layer, not in the "Birds" category.

### 3b. Branch — the perch
- **Two stacked horizontal branches** (a top branch under the grandma-bird zone, a lower branch for
  the single-row counts 1–5). Drawn so either reads on its own.
- Spans **~90% of print width**, gentle organic curve, a few watercolor leaves (brand honey/sage),
  small stubs where feet grip. Transparent PNG sized to the **full print canvas** (~3600 px wide),
  NOT the 520 box.
- Deliver as **one asset containing both branches** + optionally each branch alone, so low counts
  can hide the top branch if it looks bare.

### 3c. Title (text layer, not art)
- "**{Nickname}'s Little Birds**" — headline in **Playfair Display**; optional warm sub-line
  "*the whole flock loves you*" in **Caveat**. Nickname: Grandma / Nana / Mimi / Gigi / Grammy /
  Oma / Abuela. (Built in Teeinblue per layout spec §4, not baked into art.)

### 3d. Name tags (text layer, not art)
- Small script name under each bird, **Caveat**, auto-scale on, ~12-char limit, one warm-ink color.
  Optional tiny hanging-tag shape behind the text (separate transparent PNG, reused per slot).

---

## 4. Palette (brand-core — hex, all assets)

| Role | Hex |
|---|---|
| Cream ground | `#FBF6EE` |
| Clay | `#C15F3C` |
| Honey | `#E0A458` |
| Soft Rose | `#D98E85` |
| Sage (leaves) | pull a muted warm green ~`#8CA07A` |
| Warm Ink (text) | `#2E2822` |

Species colors stay accurate but **desaturate toward this register** — no neon yellow, no cold
electric blue. Cardinal red = clay-red, not fire-engine.

---

## 5. Nano-Banana prompts

**Pipeline per asset:** `nano_banana_pro_image` (1:1, 2K, png) → **background-remove**
(`recraft_remove_background`) → transparent PNG → **trim + place on the 520×520 canvas** (720 for
grandma owl) with **feet/nest on the bottom-center anchor** → hand to Teeinblue "Birds" clipart
category. Generate 1:1 large, then downscale — do NOT ask the model for 520 px directly.

### 5a. Shared style block (prepend to every bird prompt) — **VALIDATED v3, 2026-07-31**
> Test-generated all 8 birds + owls + branch (see `bird-gen/`). This wording is the
> one that survived 3 rounds — see §5e for the two failure modes it fixes. **Use it verbatim.**
```
A single {BIRD}, warm hand-painted watercolor illustration with a subtle hand-embroidered thread
texture, soft feathered edges, storybook children's-book quality — NOT flat clip-art. POSE: faces
the viewer almost head-on — breast and rounded belly toward the camera, both eyes visible, plump
and upright, only a slight turn of the head. A symmetric FRONT-FACING portrait, NOT a side profile.
Both feet planted flat and together at the very bottom-center — the feet rest on EMPTY white space:
absolutely NO branch, NO perch, NO twig, NO stick, NO wire under or near the feet. Short tail
tucked UP behind the body, NOT hanging down below the feet. Single subject, perfectly centered,
floating on a flat digital pure-white background (#FFFFFF) that bleeds off all four edges — it is
NOT a sheet of watercolor paper: NO paper edge, NO rectangular border, NO frame, NO deckled edge,
no leaves, no text, no ground shadow. Warm cozy palette (cream #FBF6EE, clay #C15F3C, honey
#E0A458), species colors accurate but gently muted/warm — no neon, no cold electric tones. Even
soft lighting, print quality, high resolution, square 1:1. Distinguishing detail: {DETAIL}.
```

### 5b. Per-bird subject line (swap into `{BIRD}` + append its marks)
| # | Bird | `{BIRD}` + distinguishing detail to append |
|---|---|---|
| 1 | Robin | `American robin` — "warm orange-red breast, brown-grey back and wings, slim beak, round belly" |
| 2 | Bluebird | `Eastern bluebird` — "soft muted-blue back and wings, rust-orange breast, cream belly" |
| 3 | Cardinal | `male cardinal` — "warm clay-red all over (not fire-engine), small black face mask, pointed head crest" |
| 4 | Chickadee | `chickadee` — "black cap and bib, white cheeks, soft warm-grey wings, tiny and round" |
| 5 | Sparrow | `house sparrow` — "brown-streaked back, pale tan chest, short stubby beak, plump" |
| 6 | Dove | `mourning dove` — "gentle dove-grey fading to cream, small round head, soft and calm" |
| 7 | Goldfinch | `American goldfinch` — "honey-yellow body (muted, not neon), black cap and black-and-white wing bars" |
| 8 | Owl (small) | `small round owlet` — "warm mottled brown, big soft friendly eyes, round face disc, fluffy" |

### 5c. Grandma-bird (owl on nest) — standalone prompt
```
A plump, motherly owl perched on a small woven twig nest, warm hand-painted watercolor with subtle
hand-embroidered thread texture, soft feathered edges, storybook quality. Warm mottled-brown owl,
round soft face disc, big gentle contented eyes, slightly larger and cozier than a normal songbird
— reads as the wise matriarch. NO glasses, NO shawl, no accessories. 3/4 front view, symmetric,
sitting calmly on the nest, nest base at the bottom-center of the frame. Single subject centered,
solid white background, no branch, no text, no other birds. Warm palette (cream #FBF6EE, clay
#C15F3C, honey #E0A458, warm brown). Even soft lighting, print quality, high resolution, 1:1.
```

### 5d. Branch — standalone prompt (generate wide, not square)
```
A single slender tree branch spanning left to right, warm hand-painted watercolor with subtle
hand-embroidered texture, gentle organic curve, a few small watercolor leaves in muted sage-green
and honey, a couple of tiny twig stubs where a bird could perch. Horizontal, thin, elegant — like a
delicate perch for small birds. Solid white background, no birds, no text, nothing else. Warm cozy
palette (sage green, honey #E0A458, warm brown bark). Print quality, high resolution, wide 16:9.
```
(Generate at 16:9, background-remove, then place/duplicate into the top + lower branch positions on
the full print canvas.)

### 5e. Consistency guardrails + validated failure modes (2026-07-31 test)
Two failure modes were found and fixed across 3 rounds — the §5a wording defends against both:
1. **Side-profile drift.** Slim songbirds (bluebird, chickadee, sparrow, dove, goldfinch) default to
   a classic side-on perched pose; round birds (robin, owls) obey "front" easily. Fix = the emphatic
   "faces the viewer almost head-on … NOT a side profile" (v2 fixed this).
2. **Phantom perch + paper border + hanging tail.** "gripping a thin perch" made the model draw a
   real branch under the feet; "solid white background" sometimes rendered a deckled watercolor-paper
   border (cardinal, goldfinch); long-tailed birds dropped the tail *below* the feet as a 2nd anchor.
   Fix (v3) = "feet rest on EMPTY white space, NO branch/perch/twig" + "flat digital pure-white
   #FFFFFF, NOT a sheet of paper, no border/frame/deckled edge" + "tail tucked UP, not below feet."
- Trade-off: v3 birds sit at a gentle **3/4 angle** rather than dead-front — natural, both eyes
  visible, feet centered. Acceptable.
- **JPEG fallback:** one run (sparrow) returned a `.jpeg` (no alpha) from the kie ggc endpoint —
  re-run if you get one, since Teeinblue needs a transparent PNG.
- Run **all birds in one batch, same style block** so texture/lighting/scale match — a mismatched
  flock is the real #1 quality risk.
- After generation, **eyeball side-by-side at equal height**; re-scale outliers on the 520 canvas.
- Confirm every bird's **feet land on y≈470** before handing to Teeinblue — misaligned = floaters.

### 5f. Validated test renders (2026-07-31)
Location: [`bird-gen/raw/`](bird-gen/raw/) · recipe + taskIds:
[`bird-gen/_BATCH-RECIPE.md`](bird-gen/_BATCH-RECIPE.md).
Keepers: robin / small-owl / grandma-owl / branch = **v1**; bluebird, cardinal, chickadee, sparrow,
dove, goldfinch = **v3**. (v1 = original prompt, v2 = facing fix, v3 = perch/border/tail fix.)
Still RAW — not yet background-removed or placed on the 520 anchor canvas (that's the next step).

---

## 6. Deliverables checklist
- [ ] 8 bird PNGs (robin, bluebird, cardinal, chickadee, sparrow, dove, goldfinch, small owl) —
      520×520, transparent, feet on bottom-center anchor, optically matched scale
- [ ] Grandma-owl-on-nest PNG — 720×720, transparent, nest on anchor
- [ ] Branch asset — full-width transparent PNG (both branches + each alone)
- [ ] Optional name-tag shape PNG (reused per slot)
- [ ] Upload the 8 birds as Teeinblue Clipart Category **"Birds"** (bulk ZIP ≤512 MB, guide §4);
      set reposition on the first → all inherit
- [ ] Verify swap test: pick each bird into slot 1 → all perch identically (proves the anchor)

## 7. Handoff order (matches layout spec §5)
1. Build the **fixed frame** first (branch + grandma owl + title) — validates the "1 bird" case.
2. Generate + normalize the **8-bird library** (this brief).
3. Then the designer wires the **N=1–10 layouts** (layout spec §3) using these assets.
4. Mock **N=3** with real names (Ava, Liam, Noah) for the Tier-1 test post.

---
*Parallel 2A asset spec (birth-flower library, so the A/B has matched asset sets):*
[`2A-flower-library.md`](2A-flower-library.md)
