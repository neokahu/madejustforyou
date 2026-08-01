# Design Files & Personalization Spec — Grandparents Day

## ⚠️ Read first: what these files are (and aren't)

The `*-4k.png` files here are **high-resolution (4K) concept artwork** — they show the intended
look, palette, and layout **with sample names baked in** (Ava/Liam/Noah). They are a **visual
brief for the designer**, not production print files. Two reasons they can't ship as-is:

1. **The text is baked in.** You need it **customer-customizable** — names typed on the website,
   merged into the design per order. A flat PNG can't do that.
2. **No transparent background + raster text.** These exported as **RGB (no alpha)**, and the text
   is pixels, not fonts. Apparel DTG needs a transparent knockout, and text should be live vector
   for crisp print and to be the *editable* layer.

> AI image-gen gives you **concept art fast**. Production needs a **template**, which is a
> designer + app build (below). Use these files to brief that build.

---

## The right model: two layers, text merged at order time

A personalized product is **not one image** — it's a **fixed base + a dynamic layer**:

```
   FIXED BASE ART                 DYNAMIC LAYER (per order)
   ┌────────────────┐            ┌────────────────────────┐
   │ "Grandma's     │            │ nickname → "Grandma"    │
   │  Garden" title │     +      │ name 1  → "Ava"         │  →  print-ready
   │  flowers/birds │            │ name 2  → "Liam"        │      file for POD
   │  branch/ribbon │            │ name 3  → "Noah"        │
   └────────────────┘            └────────────────────────┘
      designed once                 customer types on site
```

The customer fills a form on the product page → a **personalizer app** renders a live preview and,
on purchase, **generates the print file** with their text → sent to the **POD/print partner**.

### The count-variability twist — why this needs a designer, not AI
"One flower/bird/star **per grandchild**" means the **number of motifs must equal the number of
children the customer enters** (3 kids = exactly 3 flowers, 6 kids = 6). AI generation **cannot
guarantee this** — proof: our `…-BASE-no-names.png` reference drew a *random 5-flower* bouquet with
no relation to any count. For deep customization you need a **designer-built component library**
where every motif is **visually consistent** (same style, weight, palette) so any 1–10 can be
assembled cleanly:

- **Designer builds once:** a consistent set — 12 birth-month flowers (for Garden), a bird, a star,
  the ribbon, the headline lockup — all matching, as transparent PNG/vector.
- **App assembles per order:** a **dynamic template** (**Teeinblue** or **Customily** — POD-
  personalization specialists: "add a person → adds one matching motif + name"; birth-month →
  the right flower) lays out exactly N components for N children, plus each name.
- **AI's role = reference only:** it sets the look/style for the designer to match — it does **not**
  produce the count-accurate, consistent components or the live template.

**Zakeke / Kickflip** are strong general live-preview customizers if you don't need per-child motif
assembly (e.g. a fixed layout with just a variable name row, like the Crew mug).

---

## The Shopify stack to make text customizable
| Layer | Options | Job |
|-------|---------|-----|
| **Personalizer app** | **Teeinblue**, **Customily** (best for per-name motif assembly) · Zakeke · Kickflip | form fields + live preview + generate print file |
| **POD / fulfillment** | Printful · Printify · a dedicated personalized-POD supplier | print the generated file, ship |
| **Fonts** | Playfair Display + Caveat (licensed for print) | the live text layer |

Customer customizes → app outputs print file → POD prints. That's the whole loop.

---

## What the designer must build (the actual "design file")
For each concept, deliver a **template**, not a flat image:
1. **Component art** (clean, transparent PNG or vector): headline lockup, each of the 12 birth-month
   flowers, bird/star motifs, ribbon.
2. **Personalization fields** (per design — see below): nickname dropdown, name inputs, count 1–10.
3. **Type spec:** font (Playfair headline / Caveat names), size, color (`warm ink #2E2822`),
   position, alignment; **curved text** for mugs; **max characters** per field; safe print area.
4. **Assembly rule:** N motifs for N names; birth-month → flower mapping (for Garden).
5. **Production-ready output:** transparent background (apparel), correct **DPI at physical print
   size** (e.g. 12×14 in @ 300 DPI = 3600×4200 px — our 4K refs are in range).

### Per-design field spec
| Design | Customer inputs | Motif logic | Font |
|--------|-----------------|-------------|------|
| Grandma's Garden (2A) | nickname · 1–10 × {name, birth month} | 1 flower/kid (by birth month) | Playfair + Caveat names |
| Grandma's Little Birds (2B) | nickname · 1–10 × name | 1 bird/kid | Playfair + Caveat names |
| Grandma's Night Sky (2C) | nickname · 1–10 × name | 1 star/kid | Playfair + Caveat names |
| Grandma's Crew (1A) mug | nickname · 1–10 names | names in a roster row | Playfair + ink |
| Grandma's Recipe (3A) | grandma's name · recipe title · ingredient lines (or photo upload of handwriting) | text block | Caveat handwriting |
| First Dad Now Grandpa (4A) | nickname · est. year · 1–10 names | names row | serif/varsity |

---

## Concept files in this folder (the visual brief)
| File | Concept | Size | Mode |
|------|---------|------|------|
| `GPD02-2A-grandmas-garden-4k.png` | Grandma's Garden | 3712×4608 | RGB (needs knockout) |
| `GPD02-2B-grandmas-little-birds-4k.png` | Grandma's Little Birds | 3712×4608 | RGB |
| `GPD02-2C-grandmas-night-sky-4k.png` | Grandma's Night Sky | 3712×4608 | RGB |
| `GPD01-1A-grandmas-crew-4k.png` | Grandma's Crew mug | 4096×4096 | RGB |
| `GPD15-3A-grandmas-recipe-4k.png` | Grandma's Recipe | 3584×4800 | RGB |
| `GPD07-4A-first-dad-now-grandpa-4k.png` | First Dad, Now Grandpa | 4096×4096 | RGB |
| `GPD02-2A-grandmas-garden-BASE-no-names.png` | Garden **base** (fixed layer, names removed) | 2K | RGB |

> The BASE file shows the *fixed layer* — the reusable art with the name zone empty. In production
> that empty zone is where the app renders the customer's names.

## Bottom line
- Keep these as the **look-and-feel brief**.
- Ship customization via **Teeinblue/Customily + POD**, with a designer building the **component
  art + template** and licensed **Playfair/Caveat** fonts.
- The names are **never** baked into the art — they're a live layer the customer fills.
