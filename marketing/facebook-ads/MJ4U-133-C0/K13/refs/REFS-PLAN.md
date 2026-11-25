# MJ4U-133-K13 · reference plan (role 05, O2, GATE B input)

> Planning pass 2026-11-25: **nothing below exists yet except the product render and turntable.** Built refs go to
> `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K13/refs/`. Gate B = 07 shot mode on every ref, then the owner. No scene asset before sign-off.
> Truth source for looks: `renders/MJ4U-133-K13-render.png` (viewed). Caption pronouns: "Mom"/"she" (C1), "the kids" (C2+C3), "Lily" (C3), "he/his/him/Biscuit" (the dog, print only).

## 1. Live ↔ print match sheet (round-wide rule 4)

| ID | Print (render) | Live cast | Deliberate difference |
|---|---|---|---|
| C1 Mom | woman, light skin, long ginger wavy hair, green eyes, green Fair Isle sweater (white snowflake band), red-tartan pants, cocoa mug, Santa hat | same skin, hair, eye colour, sweater and pants; age ≈35–40 | no Santa hat; no mug (hands are busy with the ornament) |
| C2 Noah | kid boy, light skin, ginger Tousled Crop, green eyes, red Fair Isle sweater, black trousers, Santa hat | same; age ≈9 | no Santa hat |
| C3 Lily | kid girl, light skin, ginger pigtails, green eyes, red Fair Isle sweater, red-tartan pants, Santa hat | same; age ≈7 (visibly the younger one) | no Santa hat |
| C4 Biscuit | Golden Retriever, sitting, Santa hat, right end of the ledge | **never live**; print + collar only (E49) | n/a |

Casting check vs captions: "Mom" = the only adult, a woman ✔ · "the kids" = one boy + one girl ✔ · "Lily wouldn't put his collar down" → the girl holds the collar in every collar shot ✔ · no man appears anywhere (the print has no father; an adult man in frame would contradict it).

## 2. Cast sets (8 views each, per the image-prompt-method template)

Views 1–3 (front, ¾L, ¾R) are generated first with the render as the look reference; views 4–8 each take views 1–3 as references (no drift chaining).

| Set | Stable features (the label used in every brief) | Must-not-change | Views 4–8 specifics | Status |
|---|---|---|---|---|
| **C1 Mom** | long ginger wavy hair past the shoulders · green Fair Isle sweater with a white snowflake band · green eyes, light freckled skin | **all fingers bare, no rings** (the print has no father; a wedding band raises "where is he") · short natural nails · hair loose, no hat · red-tartan pants | 4 standing · 5 kneeling (the pose in B3, B5) · 6 hands, palm up, open and flat, 5+5 countable · 7 quiet (lips closed, eyes lowered) · 8 soft closed-mouth smile | **to make** |
| **C2 Noah** | ginger tousled crop · red Fair Isle sweater · black trousers | no hat · no glasses · dry eyes | 4 standing · 5 sitting cross-legged · 6 hands (left hand on a branch tip) · 7 quiet · 8 soft smile | **to make** |
| **C3 Lily** | ginger pigtails at ear height · red Fair Isle sweater · red-tartan pants | pigtails always visible · no hat · dry eyes, never crying | 4 standing · 5 sitting cross-legged holding the collar · 6 hands holding the collar coiled · 7 quiet (lips pressed, eyes on her hands) · 8 soft smile | **to make** |

Note: the K01 beat-2 stills are a different family; nothing is reused across concepts (casting varies across concepts, never inside the cell).

## 3. Product set (exists, reuse)

| Ref | File (under `products/MJ4U-133-family-wood-ornament/ads/`) | Role |
|---|---|---|
| P0-front | `renders/MJ4U-133-K13-render.png` (3185×3000, transparent) | product truth; the face that is composited in every shot |
| P0-34L | `turntable/K13/K13-34left.jpg` (2048², viewed: single flat sheet, thin edge, gold cord) | product body for generators |
| P0-34R | `turntable/K13/K13-34right.jpg` | product body for generators |
| P0-svg | `renders/MJ4U-133-K13-render.svg` | lettering source if a name must be re-set |

**P1 scale plates (to make, 2 stills):** the ornament shown at 5 in (12.7 cm wide):
- P1a: lying face up on C1 Mom's open flat palm. The ornament spans the whole palm and overhangs both sides; its width ≈1.6× her palm width; the hanger tab rests at her fingertips.
- P1b: hanging by its thin gold cord from the lowest branch, next to a standard 8 cm glass bauble; the ornament is ≈1.5× the bauble's width; Lily's hand (a 7-year-old's) beside it is about as long as the ornament is wide.
Generated face = placeholder; the real render is composited over it before 07 judges the plate.

## 4. Props and location (to make)

| Ref | Description (positive, stable) | Must-not-change | Text |
|---|---|---|---|
| **X1 collar** | worn red flat nylon collar, 2.5 cm wide, sized for a large dog, silver buckle, one round plain brass tag ≈3 cm on a ring | tag face plain and blank in every generated frame; one tag only; the collar is always red | "BISCUIT", authored (house serif-free engraved look, dark), composited and tracked; lettering file to be set by 06 from one spec, used in every shot |
| **X2 dog bed** | round oatmeal fleece dog bed with a raised rim, a soft dent in the cushion, beside the tree on the right | always empty; the room holds no animals | none |
| **X3 decorations box** | open plain brown cardboard box with red tissue and a few glass baubles | plain, unlabeled | none (no "DECORATIONS" lettering in K13) |
| **L1 room** | warm family living room at evening; real fir tree, half-decorated (white fairy lights, red and gold baubles); cream rug; a warm table lamp off-screen frame left as the key light; tree lights as fill | lamp never in frame; same tree decoration state in every shot | none |

## 5. Gate B checklist (for 07 shot mode)
1. Each cast set: identity holds across 8 views at full res; hands 5+5; Mom's fingers bare; no hats; pigtails visible.
2. Casting vs every caption pronoun and the print (§1).
3. P1a/P1b: 5 in scale reads right against the palm, the bauble and Lily's hand; single flat sheet, thin edge, gold cord through the hole (E40, E41).
4. X1: tag blank, one tag; X2: empty.
5. L1: lamp off-screen; no lettering anywhere.
