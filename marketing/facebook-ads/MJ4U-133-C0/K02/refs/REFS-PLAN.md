# MJ4U-133-K02 · reference plan (role 05, O2) · GATE B

Status: **planned, nothing generated** (2026-11-25). Gate B = 07 shot mode on every ref, then the owner. **No scene asset is made before sign-off.**
Ref media goes to `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K02/refs/` (gitignored, Drive-backed).
Printed truth = `renders/MJ4U-133-K02-render.png` (L→R Bailey · Mary · Jacob · Kobe · Susan · Luna). Live cast is blocked from this print.

## Decision needed before refs (owner) — skin tone

The re-exported render and the hero file disagree on the kids:

| | Render (shipped in beats 1–5, composited) | Hero (shared end card 17.5–20.0) |
|---|---|---|
| Mary, Kobe, Susan skin | light tan (clearly lighter than Jacob) | brown, close to Jacob |
| Susan's locs | shoulder length, gold cuffs | longer, no cuffs |
| Drinks | mugs | glasses with whipped cream |

E44 says the live cast matches the printed figure, and the viewer sees both files inside 9 seconds of each other.
**Recommended (free, ~10 min):** re-export the K02 render from the personalizer with the three kids' skin set to the same tone as the hero (and Susan's locs without cuffs if the option exists), then cast the kids brown-skinned as the script's cast table already says. **Fallback:** keep the render as is, cast the kids light tan, and accept that the end card shows a darker version of the same named kids (07 to judge; it goes away if the neutral end-card render is made).
The match sheet below is written for the **recommended** option; the fallback changes only the kids' skin line.

## Live ↔ print match sheet (round-wide rule 4)

Labels below are the **2–3 stable features** reused verbatim in every brief. Must-not-change lists are positive.

### C1 · Jacob · "he / him / his" · the dad (giftee and the one who hangs it)
| Trait | Print (render) | Live |
|---|---|---|
| character | young man | man, ~35–40 |
| skin | medium brown | medium brown |
| hair | Buzz Cut (under a Santa hat on the print) | buzz cut, dark, bareheaded on screen |
| beard | brown Full Beard, grey-brown cast | full, neatly trimmed, brown with grey-brown cast |
| glasses | Circle Glasses | round thin black wire frames |
| sweater | Jet Black Fair Isle, white snowflake/reindeer band | black knit Fair Isle sweater, white snowflake band across chest |
| trousers | Cherry Red | cherry-red lounge trousers |
| drink | mug (render) / whipped-cream glass (hero) | cocoa mug with whipped cream (prop; drink is not an identity trait) |
- **Label:** `Jacob := round thin black glasses · full brown beard · black Fair Isle sweater`
- **Must not change:** glasses round and black in every shot · beard full · sweater black with the white band · hands bare, ring finger bare · head bare (buzz cut).

### C2 · Mary · in "the kids / them" · kid girl
| Trait | Print | Live |
|---|---|---|
| character | kid girl | girl ~7–8 |
| skin | see decision (render: light tan) | brown (recommended) |
| hair | brown Classic Bob | chin-length brown bob with fringe |
| sweater | Cherry Red Fair Isle (white band) | red Fair Isle sweater, white band |
| trousers | Violet Xmas pants | purple pyjama trousers |
| accessory | Santa hat | Santa hat |
- **Label:** `Mary := brown chin-length bob · red Fair Isle sweater · purple trousers`
- **Must not change:** bob length at the chin · Santa hat on · red sweater · purple trousers.

### C3 · Kobe · in "the kids / them" · kid boy (gives the box; green cuff = his hand)
| Trait | Print | Live |
|---|---|---|
| character | kid boy | boy ~6–7 |
| skin | see decision | brown (recommended) |
| hair | brown Fluffy Curls | full curly brown hair spilling out under the hat |
| sweater | Pine Green Fair Isle | pine-green sweater with white Fair Isle band (green cuffs) |
| trousers | Red Tartan | red tartan pyjama trousers |
| accessory | Santa hat | Santa hat |
- **Label:** `Kobe := full brown curls · pine-green sweater · red tartan trousers`
- **Must not change:** green cuffs on both wrists (his hands identify him in H61/H63) · curls visible below the hat · tartan trousers.

### C4 · Susan · in "the kids / them" · kid girl
| Trait | Print | Live |
|---|---|---|
| character | kid girl | girl ~8–9 |
| skin | see decision | brown (recommended) |
| hair | brown Cuffed Locs (gold cuffs, shoulder length) | shoulder-length brown locs with small gold cuffs |
| top | Red Tartan pyjama top | red tartan pyjama shirt |
| trousers | Buffalo Check | red-and-black buffalo-check pyjama trousers |
| accessory | Santa hat | Santa hat |
- **Label:** `Susan := shoulder-length brown locs with gold cuffs · red tartan pyjama shirt · buffalo-check trousers`
- **Must not change:** locs shoulder length with gold cuffs · tartan top and check trousers (two different reds patterns).

### C5 · Bailey · dog (named in a caption)
- Print: white Pit Bull, open-mouth smile, Santa hat. Live: **white short-coat American Pit Bull Terrier, black nose, dark eyes, no hat** (a dog in a hat on the armrest is a second action risk); plain brown collar, no tag text.
- **Label:** `Bailey := white short-coat pit bull · black nose`
- **Must not change:** coat pure white, short · stays still with paws and head on the armrest · mouth closed in 5a (no lick).

### C6 · Luna · cat (named in a caption)
- Print: Persian, long white body fur, dark maroon-brown head and ears, Santa hat. Live: **long-haired Persian, white body, dark maroon-brown face mask and ears, flat face, no hat**.
- **Label:** `Luna := long-haired Persian · white body · dark maroon-brown head`
- **Must not change:** coat pattern (white body, dark head) · seated under the tree, head tilted up, still.

Pronoun check: "he / him / his" → Jacob only (every captioned shot shows him); "the kids / them" → Mary, Kobe, Susan; names Bailey and Luna → the pets. No mother on screen or in captions (GATE0). PASS on paper; 07 re-checks per shot.

## Reference sets to make (none exist yet for K02)

8 separate full-resolution views per person (image-prompt-method § Character reference set): 1 front · 2 ¾-left · 3 ¾-right · 4 full standing · 5 full seated · 6 hands · 7 expression A · 8 expression B. Views 1 from the printed figure (render crop as character-look reference only) + the label; views 2–3 from view 1; views 4–8 each from views 1–3 (no drift chaining). Neutral grey background, soft window light from camera-left, 2K, 9:16 for full-body views, 1:1 for heads/hands.

| Set | Views | Expressions (7 / 8) | Brief |
|---|---|---|---|
| C1 Jacob | 8 | 7 lips pressed, trying to look unimpressed · 8 broad grin, eyes crinkled | `briefs/B-REF-C1-Jacob.md` |
| C2 Mary | 8 | 7 watchful half-smile · 8 open laugh | `briefs/B-REF-C2-Mary.md` |
| C3 Kobe | 8 (view 6 = both hands with green cuffs, holding a small box flat) | 7 hopeful · 8 laugh | `briefs/B-REF-C3-Kobe.md` |
| C4 Susan | 8 | 7 watchful smile · 8 laugh | `briefs/B-REF-C4-Susan.md` |
| C5 Bailey | 4: front · ¾-left · side seated · paws-on-armrest | n/a | `briefs/B-REF-C5-Bailey.md` |
| C6 Luna | 4: front · ¾-left · side seated · seated looking up | n/a | `briefs/B-REF-C6-Luna.md` |
| Scale plate | 1 (+1 re-roll) | n/a | `briefs/B-REF-SCALE-plate.md` |

Total 41 images planned (+ ~30% re-rolls). Cost in `../asset-plan.md`.

## Product reference set (exists)

| Ref | File | Role in briefs |
|---|---|---|
| P0 front (truth) | `renders/MJ4U-133-K02-render.png` | composite source only; may be a body-shape reference in top-down H63 |
| P1 ¾-left | `turntable/K02/K02-34left.jpg` | product body (thickness, edge, cord) |
| P2 ¾-right | `turntable/K02/K02-34right.jpg` | product body |
| Hero | `source-images/hero-family-2026-tree.png` | end card only (shared); not used as a K02 ref (see decision) |

Product must-not-change: one flat 3 mm sheet cut to the outline, printed on the front only, blank back, coin-thin edge, hanger tab at the top centre with one hole, thin gold metallic cord (E40). Faces in generated frames are placeholders (E37).

## Scale anchor (E41) · 5 in variant

Ornament: longest side 5 in = **12.7 cm** (near-square, ~12.4 × 12.7 cm incl. the tab). *Assumption:* the listed size is the longest side; Producer to confirm with the supplier spec.
| Anchor | Relation the plate and every shot must show |
|---|---|
| adult man's hand (Jacob, ~19 cm long, palm ~8.5 cm wide) | the ornament spans about one and a half palm widths; held in two hands, thumbs on the side rims, it is a little narrower than his two spread hands |
| kid's hand (~7 yrs, ~13 cm long) | the ornament is about one kid hand-length wide |
| cocoa mug (9.5 cm tall) | the ornament is about 1.3 mug-heights tall |
| kraft gift box | inner 15 × 15 cm, 5 cm deep: the ornament lies flat with ~1 cm margin each side |
| tree branch | hangs from one branch tip by a ~10 cm gold cord loop; about as wide as three needle clusters |
The scale plate (`B-REF-SCALE-plate`) shows the ornament (placeholder face) lying flat in the open kraft box, beside the cocoa mug, with an adult hand resting on the box rim: one image that pins box, mug, hand and ornament together. 07 checks every generated shot against it.

## Props that carry text or identity
- "DAD'S LIST: / 1. NOTHING" lettering plate (H63): composited, never generated (round-wide rule 5). Built in post (handwriting font in PIL, blue ballpoint) or from an owner phone photo; spec in `../shotlist.md` H63.
- No other legible text in any K02 frame (mug plain, box plain kraft, no tags).

## Gate B packet (to 07, then owner)
All 41 refs + contact sheet at full res, this match sheet, and the scale plate with the K02 render composited on the placeholder. 07 checks: identity vs label, print match (E44), pronouns (E45), five fingers in hands views, scale plate vs the anchor table.
