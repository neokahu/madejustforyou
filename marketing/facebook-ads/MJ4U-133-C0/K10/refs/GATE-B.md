# MJ4U-133-K10 · Gate B reference set (role 05 build, 2026-11-25)

> Built under BRIEF.md "User rulings 2026-11-25" item 8 (views 1–3, props and rooms on Seedream, scale plates) with a $2.00 hard cap. Casting approved by the owner: an East Asian-American couple with gold wedding bands.
> Media: `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K10/refs/` (gitignored, Drive-backed). Contact sheet: `K10/refs/gateB-contact.jpg`.
> **Status: built and self-checked by 05; next 07 shot mode, then the owner.** No scene asset has been made.

## Spend
| item | model | n | cost |
|---|---|---|---|
| D1, G1, M1 | Nano Banana Pro Edit, 2K | 3 | $0.42 |
| D2, G2, M2, M3, SCALE-palm | Nano Banana Pro Edit, 2K | 5 | $0.70 |
| 4 props (tree, moving box, baubles, kraft) | Seedream v5 Pro Edit | 4 | ≈$0.15 |
| LOC-day, LOC-evening, SCALE-branch | Seedream v5 Pro Edit | 3 | $0.151 |
| **Total** | | **15** | **≈$1.42 / $2.00 cap** |
Re-rolls: none were needed. Two generations were **not run**: D3 (Daniel, full body, leaning on a door frame) and G3 (Grace, full body standing). The permission layer denied both calls. They were not retried, and the decision is left to the user. Inputs uploaded for the generations: the K10 render on white (`_render-white.jpg`), a plain grey canvas (`_canvas-grey.jpg`), and the ¾ turntables.

## Per-image check (05 self-check, full resolution)
| file | role | verdict | notes for 07 |
|---|---|---|---|
| K10-D1-front.jpg | Daniel view 1 | PASS | East Asian-American man, late 20s, short black messy crop, green Fair Isle sweater with snowflakes + reindeer band (matches the print); clean-shaven, no glasses. |
| K10-D2-34left.jpg | Daniel view 2 | PASS | Same face, hair and sweater as D1. |
| (D3 full body) | Daniel view 3 | NOT MADE | Denied by the permission layer; needed for B4 (doorway lean) and to check the ring. |
| K10-G1-front.jpg | Grace view 1 | PASS | Long straight black hair, centre part, no fringe, gold studs, red Fair Isle sweater with white band (matches the print). |
| K10-G2-34back.jpg | Grace view 2 | PASS | Back-¾: the hair length and sweater read, which is what B4's over-the-shoulder shot needs. Face only in partial profile. |
| (G3 full body) | Grace view 3 | NOT MADE | Denied by the permission layer; tartan trousers and the ring are not yet shown on any view. |
| K10-M1-front.jpg | Mochi view 1 | PASS | Pembroke, red-and-white, white blaze, white chest and front legs, upright ears, full tail, plain red collar (a metal D-ring, no tag text). Seated, both front paws down. |
| K10-M2-34up.jpg | Mochi view 2 | PASS (minor) | Seated, head tilted up (the B7 pose). A white curtain/window shows at the left edge: background only, but do not pass it on to scene frames. |
| K10-M3-side.png | Mochi view 3 | PASS (minor) | Asked for a profile, got a front-¾ facing left with the tail on the floor. Identity is consistent with M1 and M2. |
| K10-PROP-tree.jpeg | tree | PASS | Small real fir in a woven basket, bare, no lights. |
| K10-PROP-movingbox.jpeg | DECORATIONS box | PASS | Far flap upright and blank (corner-pin target), plain cardboard, red tissue. The near flap is open rather than folded over; fine as a prop reference. |
| K10-PROP-kraft.jpeg | kraft box + ornament | PASS | The ornament reads as one flat sheet, face-up, tab to the far side. The generated print is a placeholder (E37). Box is about ornament size plus a margin. |
| K10-PROP-baubles.jpeg | childhood baubles | PASS | 4 worn glass baubles (red, gold, pale blue, silver), scuffed, no text. |
| K10-LOC-day.jpeg | room, day | PASS (minor) | Tree on the right on a rug, boxes stacked against the back wall, doorway at back right. A sliver of the window frame shows on the left wall: scene first frames must keep the window off-screen. |
| K10-LOC-evening.jpeg | room, night (H15) | PASS (minor) | Same layout, warm lamp light from the right, blue window light from the left, open box with tissue. **The lamp and window edges show in frame**: H15 is a close-up on the tree, so crop them out there. |
| K10-SCALE-palm.png | scale anchor, hand | PASS | Measured on the image: ornament width ≈0.63× hand length (target 0.67) and wider than the palm, overhanging both sides. Left hand (the thumb side is correct) with a gold band on the ring finger. The palm is shown fingers-up rather than flat top-down; the scale relation is what this plate must lock. Generated print = placeholder. |
| K10-SCALE-branch.jpeg | scale anchor, branch | PASS | Ornament width ≈1.7× the bauble diameter (target ≈1.6). Hangs face-on by a thin gold cord. Flat single sheet. |
Product truth: the face on every generated ornament is a placeholder. Only `renders/MJ4U-133-K10-render.png` ships (E37). The props and plates carry no other legible text.

## Open before Gate B sign-off
1. **D3 and G3 (full-body views) were not generated** because of the permission denial. Each is about $0.14 on Nano Banana Pro, or about $0.04 on Seedream, using views 1–2 as references. The user or Producer decides whether to run them now or with views 4–8 after Gate B.
2. The ring state is visible only on SCALE-palm (Grace). Daniel's band shows on no reference yet (D3 or view 6, hands).
3. Mochi has no fully side-on profile (M3 is a front-¾). It is enough for B7 (high-angle ¾).
4. The window and lamp edges in the LOC plates are acceptable on reference plates, but must stay off-screen in scene frames.

## Fix pass after 07 (2026-11-25, owner ruling "Gate B fixes and ornament size")
| file | role | verdict | cost |
|---|---|---|---|
| K10-G2b-34left-face.png | Grace ¾ face view (closes 07 S2, E46) | PASS: same face, centre part, no fringe, gold studs, red Fair Isle with the white band, all matching G1. Made from G1 only (no chained drift); her face is turned toward frame-left. | $0.14 (NBP, ledger purpose `refs`) |
- **Ornament size, K10 = 5 in (E41).** 07 measured SCALE-palm at ≈4.6–5 in and SCALE-branch at ≈5.5 in. Both are within plausible 5 in, so no re-take (07 did not flag them).
- Grace now has 2 face views (G1, G2b) plus the back-of-head view (G2) for B4.
- Still open (07 S3, not in this pass): D3 (Daniel full body), a view showing Daniel's ring (both needed before B4), and G3 (Grace full body, needed before B2). Room-plate edges must stay out of scene frames.
- Gate B spend total ≈ $1.56 (first pass $1.42 + fix $0.14). Contact sheet rebuilt with G2b.
