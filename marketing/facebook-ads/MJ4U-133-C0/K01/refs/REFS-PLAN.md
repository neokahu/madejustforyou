# MJ4U-133-K01 · reference plan (O2, GATE B) · role 05, 2026-11-25

**Gate B = this set locked:** 07 shot mode checks identity, scale and on-model, then the owner signs. **No scene asset (FF-*, video, B2 re-stage) is made before sign-off.**
Media path for everything new: `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K01/refs/` (gitignored, Drive-backed via `scripts/backup-media.sh`).
Source of truth for looks: the printed figures in `renders/MJ4U-133-K01-render.png` (read by eye 2026-11-25, crop of the figure rows). Pronouns: "she/her" = Grandma only; everyone else is named.

## 1 · Live ↔ print match sheet (round-wide rule 4)

| ID | Printed figure (render) | Live cast | Skin | Hair | Glasses | Sweater | Trousers | Hat (live) | Drink | Caption word |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 Grandma | aged woman | woman ~70 | light | grey, high top bun | none | green Fair Isle, white snowflake + reindeer band | red tartan | none | (cocoa on print; not shown live) | she / her / Grandma |
| C2 Grandpa | aged man | man ~72 | light | short grey, side-parted | **round thin-rimmed circle glasses** | red Fair Isle, white reindeer + snowflake band | **black** | none | (cocoa) | Grandpa (always named) |
| C3 Emma | kid girl | girl ~7 | light | blonde, **two low pigtails** | none | red Fair Isle | red tartan | Santa hat | (cocoa) | Emma |
| C4 Michael | young man | man ~35 | light | short brown | none | **cream Fair Isle with a navy reindeer band and red trim** | **black** | Santa hat | (coffee mug) | Michael |
| C5 Cooper | Golden Retriever | adult Golden Retriever, light gold coat | — | — | — | — | — | **none** (red collar) | — | Cooper / the dog |
| C6 Sarah | young woman | woman ~33 | light | long blonde waves | none | red Fair Isle | red tartan | Santa hat | (cocoa) | Sarah |
| C7 Leo | kid boy | boy ~5 | light | short brown | none | green Fair Isle | black | Santa hat | (cocoa) | Leo |

**For 04 (minor, no words change):** the script's cast table says Michael wears red-tartan trousers; the render shows **black**. The render wins (E44 is about the printed figure). The cast table also calls his sweater "navy reindeer Fair Isle"; on the print it is cream with a navy reindeer band.

## 2 · Stable features + must-not-change (the labels every brief reuses)

| Label | 2–3 stable features | Must not change |
|---|---|---|
| `<Grandma>` | grey high top bun · green Fair Isle sweater · light skin, ~70 | no hat; no glasses; **fingers bare, no rings, no nail polish**; red-tartan trousers; never in tears |
| `<Grandpa>` | round thin-rimmed circle glasses · short grey hair · red Fair Isle sweater | glasses always on, lenses round (not square); clean-shaven; no hat; bare fingers; black trousers; never pushes or removes the glasses |
| `<Emma>` | two low blonde pigtails below a Santa hat · red Fair Isle sweater · girl ~7 | both pigtails visible; hat on; red-tartan trousers |
| `<Michael>` | short brown hair · cream Fair Isle with a navy reindeer band · Santa hat | no beard; black trousers; one plain sweater pattern (no cartoon reindeer face) |
| `<Sarah>` | long blonde waves · red Fair Isle · Santa hat | red-tartan trousers |
| `<Leo>` | short brown hair under a Santa hat · green Fair Isle sweater · boy ~5 | five fingers on the pointing hand; black trousers |
| `<Cooper>` | adult Golden Retriever · light gold coat · red collar | stays seated or lying; no hat; mouth closed or soft pant (no barking pose) |
| `<Ornament>` | one flat 3 mm plywood sheet cut to the outline · hanger tab with a hole at top · thin gold metallic cord | printed on the front only; coin-thin edge, no layered relief; back blank; faces camera; never spins |

## 3 · What exists vs what must be made

| Ref | Exists? | Source / how it is made | Views | Est. images |
|---|---|---|---|---|
| **REF-P1** product front | ✅ `renders/MJ4U-133-K01-render.png` (3185×3000, transparent) + `.svg` | real artwork | front | 0 |
| **REF-P2** ¾ left | ✅ `turntable/K01/K01-34left.jpg` | Seedream, accepted 2026-11-24 | ¾L | 0 |
| **REF-P3** ¾ right | ✅ `turntable/K01/K01-34right.jpg` | Seedream, accepted | ¾R | 0 |
| REF-P4 front, flat on grey | ✅ `turntable/K01/K01-front-flat.jpg` | — | front | 0 |
| **REF-P5 scale-anchored plate** | ❌ make | Image edit from P1+P2: the 5 in ornament held flat in two adult hands (`<Grandma>` hands ref), and a second frame of it lying in the ~6 × 6 × 2 in kraft box on red tissue. Real face composited after. | 2 | 2 (+1 retake) |
| REF-P6 hang scale | ✅ (evidence) `turntable/K01/K01-test-hang-seedance.mp4` shot 1 (PASS: hangs by the gold cord from a branch, hand lowering away) | test clip | — | 0 |
| Lettering | ✅ the names and "2026" are inside the SVG as text in the store font Chewy; for B5 re-render the SVG at 2× (6370 px wide) | `render_svg.sh` (scratchpad, see RENDERS.md) | — | 0 |
| **L1 location** | ⚠️ partial: `stills/K01/K01-b2-take2.png` (room, tree, chair, lamp, fireplace) | Use take 2 as the location/composition ref. One empty-room plate (no people) for B5's bokeh and as an FF background ref | 1 | 1 |
| **C1 Grandma** | ❌ make (seed: take-2 crop) | 8 views | front, ¾L, ¾R, full seated (armchair), full standing, hands (both, five fingers each, bare), smile, moved (hand to mouth, eyes bright, no tears) | 8 |
| **C2 Grandpa** | ❌ make (seed: take-2 crop) | 8 views | front, ¾L, ¾R, full seated, leaning-in profile, hands (bare, red cuffs), smile, warm look down | 8 |
| **C3 Emma** | ❌ make (seed: take-2 crop; fix the pigtails) | 8 views | front, ¾L, ¾R, full standing, leaning over a chair back, hands, smile, hugging-pose upper body | 8 |
| **C7 Leo** | ❌ make (seed: take-2 crop) | 8 views | front, ¾L, ¾R, full standing, kneeling, pointing hand (index out, five fingers), grin, profile | 8 |
| C4 Michael | ❌ make (seed: take-2 crop; fix the sweater) | 3 views (deviation: appears only in the B2 still and soft in B6a) | front, ¾L, full standing | 3 |
| C6 Sarah | ❌ make (seed: take-2 crop) | 3 views (same deviation) | front, ¾R, full standing | 3 |
| C5 Cooper | ❌ make (seed: take-2 crop) | 3 views (dog: sitting front, sitting side, head close-up) | — | 3 |

Total new reference images: **45** (8×4 + 3×3 + 2 product + 1 location + ~3 retakes). The 3-view deviation for Michael, Sarah and Cooper is deliberate: they appear only in a still (B2) or soft in the background (B6a), so 8 views add cost without protecting a generated shot. 07 may require the full 8.

### How the people refs are made (image-prompt-method § Character reference set)
1. **Seed = a crop of take 2**, upscaled, as identity reference, plus the matching render figure as the trait reference (hair, glasses, sweater colours). Faces in take 2 are ~100–120 px wide, so view 1 (front) is the first canonical identity; check it against take 2 by eye before going on.
2. Views 1–3 first. Views 4–8 each take views 1–3 as references (no drift chaining).
3. One view per call, 2K, plain warm-grey background, soft window light from camera-left, 50 mm look. Every limb placed (LIMB RULE): e.g. "both hands resting on her thighs, fingers slightly apart so five show on each hand".
4. **QA every hand at full resolution** (rings appear unasked: 2026-10-08 owner set).

### Gate B checklist for 07
- [ ] Each person matches the match sheet row (skin, hair, glasses, sweater, trousers, hat) and the printed figure.
- [ ] Grandpa's glasses are round in every view; no ring on any hand; 5 fingers per visible hand.
- [ ] Emma's two pigtails visible under the hat; Michael's sweater is cream with a navy reindeer band.
- [ ] Faces in views 1–3 are the same person across views and match take 2 closely enough that the B2 re-stage can use either.
- [ ] REF-P5: the ornament reads as 5 in against the hands and the box; single flat sheet, thin edge, gold cord.
- [ ] No legible text in any ref.
