# Asset Brief — `GPD02-2A` Grandma's Garden · Birth-Flower Library + Fixed Frame

> The **2A** side of the GPD02 A/B — the *proven* metaphor (birth-flower garden) that competitors
> own. Built to be **structurally identical** to the 2B bird library
> ([`2B-bird-library.md`](2B-bird-library.md)) so the head-to-head
> test isolates **metaphor** (flowers vs birds), not build quality. Same Roster mechanic, same
> layouts, same fixed-frame + title + name-tag pattern — **only the motif and its anchor change.**

**Key difference from 2B:** a bird is *freely picked* from a library; a birth flower is
**determined by the grandchild's birth month**. So the "library" is a fixed **12-flower set (one per
month)**, and the customer's input is a **month per grandchild** → the matching flower renders. Same
per-category anchor rule applies: all 12 flowers must share ONE canvas/anchor.

---

## 0. Print targets (products)

| Product | Physical | Design px @ 300 DPI | Notes |
|---|---|---|---|
| **Lamp** (LOCKED 2026-07-31) | full wrap **31 × 5 cm** · one side 9 × 5 cm | **3661 × 591** (build **3675 × 600**, round up) | **Continuous wrap** — flowers flow across the side seams; design as ONE 31 cm garden border, do NOT group per 9 cm panel. |
| Sweatshirt | ~portrait center chest | ~3600 × 4200 | per [`brief.md`](brief.md), DTG |

**Lamp layout consequences (5 cm-tall strip):**
- **Single horizontal row only** — at 591 px tall you can't stack rows. Flowers run in one line along
  the wrap like a flower bed. (Fits the garden metaphor better than the birds' 2-branch layout.)
- **Name legibility is the constraint here.** After the bloom takes ~65% of 591 px, the name band is
  only ~180 px (~4 mm text). Enlarge names vs the v1 mockup. **Test the worst case first:** 10 flowers
  across 31 cm ≈ 3 cm each — likely too cramped, so the **lamp may cap at fewer grandkids than the
  sweatshirt**. Confirm the max count the lamp supports before building.
- Continuous wrap = a flower **may straddle a seam**; that's fine, plan the border as one strip.
- Colors: sRGB PNG (confirm supplier); add ~2 mm bleed per edge only if the supplier asks.
- Flower assets have ample resolution (generated ~2048 px) → downscaling into the ~410 px slot is
  lossless; the 520×520 stem-base anchor still applies, just confirm stems plant on the lamp baseline.

---

## 1. Canvas & anchor spec (EVERY flower — mirrors 2B §1)

| Spec | Value | Note |
|---|---|---|
| Canvas | **520 × 520 px**, transparent PNG | shared box, same as birds |
| Anchor | **stem base at bottom-center** — lowest stem pixels at **x=260, y≈480** | flowers "plant" into the soil/branch line at the same height |
| Facing | **3/4 front bloom, upright stem** | symmetric; sits at any X-position (same reused-clipart constraint as birds) |
| Content | **single flower on a short stem + 1–2 leaves**, nothing else | no soil, no name, no background |
| Visual scale | bloom fills **~55–65% of canvas height**; **normalize optical weight** across all 12 | a rose and a lily-of-the-valley must read at similar size in a row |
| Format | 32-bit transparent PNG, no white halo | Teeinblue auto-thumbnails |

---

## 2. The birth-flower library (12 — one per month, US convention)

All 12 share §1 canvas/anchor and the **warm watercolor botanical** look + brand palette (§4 of the
bird brief). Keep blooms **botanically recognizable** but painterly, not clip-art.

| Month | Birth flower | Signature read | Palette lean |
|---|---|---|---|
| Jan | **Carnation** | ruffled layered petals | soft rose `#D98E85` |
| Feb | **Violet** | small five-petal, heart leaves | muted violet + sage |
| Mar | **Daffodil** | trumpet center, star petals | honey `#E0A458` |
| Apr | **Daisy** | white petals, yellow center | cream + honey |
| May | **Lily of the Valley** | tiny white bells on a stem | cream + sage |
| Jun | **Rose** | classic layered bloom | clay `#C15F3C` |
| Jul | **Larkspur** | tall spike of small blooms | muted blue |
| Aug | **Gladiolus** | tall ruffled spike | soft rose/clay |
| Sep | **Aster** | many thin petals, round center | muted lavender |
| Oct | **Marigold** | dense ruffled pom | clay/honey |
| Nov | **Chrysanthemum** | full layered mum | honey/clay |
| Dec | **Narcissus** | paperwhite, cupped center | cream + honey |

> Standard US birth-flower set. If a month has a common alt (Feb=Iris, Jul=Water Lily, Dec=Holly),
> keep the one above for consistency unless testing shows a recognition issue.

---

## 3. Fixed frame (renders at every count — mirrors 2B §3)

- **3a. Anchor motif** — instead of a grandma-owl: a slightly **larger "grandma" bloom or a small
  watering-can / garden marker** at top-center as the fixed focal point. *Recommend the larger
  bloom* (keeps it botanical, lowest style risk) — one oversized rose or peony, ≈1.4× scale, on its
  own **720×720** canvas, stem base on anchor.
- **3b. Ground line** — the "soil / garden bed" equivalent of the birds' branch: a soft watercolor
  **soil/grass line** (two stacked beds for 1–5 vs 6–10 rows), full print width (~3600 px), muted
  sage/earth. Same two-row logic as the branch so **layouts are shared 1:1** with 2B.
- **3c. Title** — "**{Nickname}'s Garden**" — Playfair headline + Caveat sub-line "*a little garden
  that keeps growing*". Same nickname set.
- **3d. Name tags** — script name under/on each stem, Caveat, auto-scale, ~12-char. (Note the 2A
  fix from mockups README: names render small on stems — **enlarge/space so 1–10 stay legible**.)

---

## 4. Personalization mechanic (Teeinblue)

| Customer sees | Teeinblue type | Renders |
|---|---|---|
| Number of grandkids (1–10) | **Additional Option** 1–10 | no render — drives conditional layout (same as 2B) |
| Birth **month** per grandchild | **Additional Option** (Jan–Dec) OR a **Clipart Category "Birth Flowers"** picker labeled by month | selects which of the 12 flowers renders in that slot |
| Name per grandchild | **Text layer** (Caveat, ~12-char, auto-scale) | name on/under the stem |
| Nickname | Additional Option / Text | title line |

- Simplest build = **Clipart Category "Birth Flowers"** with the 12 blooms, customer picks per
  grandchild (item labels = "January – Carnation", etc.). Mechanically identical to the bird picker,
  so the **layout groups (N=1–10) are reused** from the layout spec §3 — swap the branch for the
  soil line, the bird slots for flower slots.
- Layer budget mirrors 2B: ~55 flower slots + 55 name tags across counts 1–10.

---

## 5. Nano-Banana prompts

Same pipeline as 2B §5 (generate 1:1 2K → `recraft_remove_background` → place on 520×520 with
**stem base on bottom-center anchor**). Batch all 12 in one style pass for a matched set.

### 5a. Shared style block
```
A single {FLOWER} on a short stem with one or two small leaves, warm hand-painted watercolor
botanical illustration with a subtle hand-embroidered thread texture, soft edges, storybook quality
— NOT flat clip-art. 3/4 front view of the bloom, upright symmetric stem, stem base at the very
bottom-center of the frame. Single flower, perfectly centered, solid white background, no soil, no
pot, no text, no ground shadow, nothing else. Warm cozy palette (cream #FBF6EE, clay #C15F3C, honey
#E0A458, soft rose #D98E85, muted sage leaves), colors accurate but gently muted/warm — no neon, no
cold tones. Even soft lighting, print quality, high resolution, square 1:1.
```
Swap `{FLOWER}` = the month's bloom from §2 + append its signature read (e.g. Jun →
`a classic layered garden rose, warm clay-red, a few open petals`).

### 5b. Grandma bloom (anchor) — standalone
```
One oversized, full watercolor rose (or peony) — the centerpiece bloom, slightly larger and more
detailed than the others, warm clay-and-rose tones, hand-painted with subtle embroidered texture,
upright on a short stem, stem base at bottom-center. Solid white background, single subject centered,
no text, no pot. Warm brand palette. Print quality, high resolution, 1:1.
```

### 5c. Soil/garden-bed line — standalone (wide)
```
A soft watercolor garden soil-and-grass bed spanning left to right, muted sage green and warm earth
tones, gentle organic edge, a few tiny sprigs — a delicate planting line for small flowers. Solid
white background, no flowers, no text. Warm palette. Print quality, high resolution, wide 16:9.
```

### 5d. Consistency guardrails
- One batch, one style block, matched scale — a mismatched garden is the #1 failure mode (same as
  the flock). Eyeball all 12 at equal height; re-scale outliers on their 520 canvas.
- Confirm every flower's **stem base lands on y≈480** before upload.

---

## 6. Deliverables checklist
- [ ] 12 birth-flower PNGs — 520×520, transparent, stem base on anchor, optically matched
- [ ] Grandma-bloom anchor PNG — 720×720, transparent
- [ ] Soil/garden-bed line — full-width transparent PNG (two beds + each alone)
- [ ] Name-tag treatment (enlarged vs the v1 mockup — legibility fix)
- [ ] Upload 12 as Teeinblue Clipart Category **"Birth Flowers"**, labeled by month; set reposition
      on the first → all inherit
- [ ] Swap test: each flower into slot 1 → all plant identically

## 7. A/B parity check (why this matters)
2A and 2B must differ **only** in metaphor. Before the Tier-1 post, confirm both share: same product
(sweatshirt), same nickname set, same layout positions (N=1–10), same title/name-tag fonts (Playfair
+ Caveat), same palette, same 3-kid mock (Ava, Liam, Noah). Then the winner = the *metaphor*, which
is the whole point of the test (per [`brief.md`](brief.md)).
