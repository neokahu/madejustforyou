# MJ4U-133-C0 · product renders (real personalizer output, 2026-11-23)

Made by the Producer in the live store personalizer (madejustforyou.net product 9776740696421), exported as the personalizer's own SVG
(Teeinblue artwork layers + names in the store font Chewy), rendered locally to transparent PNG 3185×3000 (headless Chrome, crop of the
artwork viewBox to the ornament + hanger). **This is the product truth for every shot: never redraw it with a generator.**
Files (media, gitignored → Drive): `products/MJ4U-133-family-wood-ornament/ads/renders/MJ4U-133-<K>-render.{svg,png}`.

| Concept | Members left→right as printed | Notes vs the 00A render spec |
|---|---|---|
| K10 | Daniel (man, light, black Messy Crop, green sweater, black coffee) · Grace (woman, light, black Long Straight, red sweater, red-tartan pants, hot chocolate) · Mochi (Pembroke Welsh Corgi) | all Santa hats |
| K13 | Mom (woman, light, ginger Long Waves, green sweater) · Noah (kid boy, ginger, Tousled Crop, red sweater) · Lily (kid girl, ginger Pigtails, red sweater) · Biscuit (Golden Retriever) | Noah's hairstyle = Tousled Crop (Messy Crop not offered for kids) |
| K04 | Grandpa (aged man, dark, grey Short Taper, **circle glasses**, green sweater) · Grandma (aged woman, dark, grey Short Curls, red sweater, black tea) · Olivia (young woman, dark, black Box Braids, white sweater, latte) · Rosie (Beagle) | **Grandpa/Grandma without Santa hats** so the grey hair reads (hats hid it); Olivia keeps her hat; Rosie has no hat (the dog accessory did not take; the render is the truth) |
| K01 | Grandpa (aged, grey, circle glasses, no hat) · Grandma (aged, grey Top Bun, no hat) · Emma (kid girl, blonde pigtails) · Michael (navy reindeer sweater) · Cooper (Golden Retriever) · Sarah (blonde Long Waves) · Leo (kid boy) | **7 members print in two rows**: Emma and Cooper sit on an upper ledge; printed name order is Grandpa, Grandma, Emma, Michael, Cooper, Sarah, Leo. Grandparents hatless as in K04 |
| K06 | Dad (man, tan, black Short Taper, red sweater) · Mom (woman, tan, brown Long Straight, green sweater) · Sofia (kid girl, black High Ponytail, red sweater + red-tartan pants) · Mateo (baby, Wispy Tuft, white sweater, baby bottle) | printed "Mom" (US store), not "Mum" |
| K02 | Bailey (white Pit Bull, Santa) · Mary (kid girl, **Brown** skin, brown Classic Bob, Cherry Red sweater, Violet Xmas pants, Santa) · Jacob (young man, brown skin, Buzz Cut, brown Full Beard, **Circle Glasses**, Jet Black sweater, Cherry Red Xmas pants, Santa) · Kobe (kid boy, **Brown** skin, brown Fluffy Curls, Pine Green sweater, Red Tartan pants, Santa) · Susan (kid girl, **Brown** skin, brown Cuffed Locs, Red Tartan top, Buffalo Check pants, Santa) · Luna (Persian cat, white with maroon head, Hazel-Yellow eyes, Santa); Jacob's drink Latte Macchiato | **Re-exported 2026-11-24, v2 2026-11-25** (v1 had the kids too light (Tan) and Luna's eyes blue; flagged by K02's 05; v1 in `_superseded/`) from the personalizer to `MJ4U-133-K02-render.{svg,png}` (transparent). Matches the hero `hero-family-2026-tree.png` except small details: drinks (mugs vs glasses) and Susan's locs have gold cuffs and are shorter. Single row of six on the ledge. |

Personalizer facts confirmed while building (feed 04/05): age ranges Young/Aged for adults; hair colors incl. Grey and Salt & Pepper; glasses
No/Sunglasses/Square/Circle; kid, baby, dog (100+ breeds, 8 groups) and cat characters; accessories No/Santa/Reindeer/Tree(/Bow); drinks by
category (coffee/tea/cocoa, juice, soft drink, beer, wine…; baby bottle/milk for babies); up to 10 members. Site banner: "Order by Dec 11 for Christmas delivery".

## K04 personalizer screen recording (user, 2026-11-24)
`products/MJ4U-133-family-wood-ornament/ads/screen-recordings/K04-personalizer-circle-glasses.mov` (402×812, 60 fps, 10.4s; Drive-backed).
Live store UI in a phone viewport with the K04 family set; Grandpa's glasses go No Glasses → Square Glasses → **Circle Glasses** (the real option label; the script's "Circle" = "Circle Glasses").
Use for the K04 phone insert: **clean before frame 0–1s** (No Glasses, no cursor) and **clean after frame ~8–10s** (Circle Glasses selected). The middle (~1.5–7.5s) shows a desktop cursor and hover tooltips: do not use it. Build the tap in post (before → composited fingertip tap → after, ~1.5s).

## Turntable pipeline test, K01 (2026-11-24) — E37 amendment
Files: `products/MJ4U-133-family-wood-ornament/ads/turntable/K01/` (Drive-backed). Seedream v5.0 Pro Edit (Atlas) from the flat render: `K01-34left.jpg` (v2 + cord-colour edit), `K01-34right.jpg` (v3). Rejected takes in `_rejected/`.
- Prompt lessons: say **"ONE single flat sheet… printed on that one flat front surface… one continuous edge around the outer outline only"**, or figures come out as stacked layers (breaks E40). The cord is **thin gold metallic** (the listing photos), not red. Back view invented wrong interior holes: not needed, skip.
- Listing photos are all mockups (flat art on a tree): there is no real physical-sample photo.
- Test clip `K01-test-hang-seedance.mp4` (Seedance 2.0 Fast ref-to-video, refs = front + both ¾ views, 9:16, 5s, $0.36): **shot 1 PASS** (hangs by gold cord from a branch, natural hand with a green cuff lowering away, physical scale, room light). **Shot 2 FAIL**: free-hanging ornament spun 360°, showing an invented back and thicker edge. Fix: the ornament faces camera throughout (no free-hang shot on its own; any sway is added in post on the real artwork), one shot per clip.

## Turntables, all six concepts (2026-11-24)
`products/MJ4U-133-family-wood-ornament/ads/turntable/<K>/<K>-34left.jpg`, `<K>-34right.jpg` (+ the flat render as front). Seedream v5.0 Pro Edit, prompt as in the K01 test (single flat sheet, coin-thin edge, hanger tab named, gold cord). Re-rolled: K10 both (first left too thick; first right lost the hanger tab), K06 left (too thick). Rejected takes in `_rejected/`. Printed faces are placeholders (E37): the real render is composited over them in post.

## K01 beat 2 proof still (2026-11-24) — the council's "prove it first" shot
`products/MJ4U-133-family-wood-ornament/ads/stills/K01/K01-b2-take{1,2}.png` (Nano Banana Pro Edit, 9:16 2k, the K01 render as character-look reference only). **Both takes PASS the core risk:** all seven read in one frame (Grandpa circle glasses + red sweater, Grandma grey bun + green sweater with the box on her lap, Emma hugging her from behind, Michael navy reindeer sweater, Sarah long blonde waves, Leo pointing at the box, Cooper's nose at the box), two clear rows, red tissue covers the box contents (ornament composited later).
Gaps for 05/07 (shot gate, not blockers): Grandma and Grandpa wear jeans (cast table: red-tartan / dark trousers); Emma's pigtails are not visible under the hat; Grandpa sits beside the chair, not on the armrest; Michael's sweater has one big cartoon reindeer rather than a Fair Isle band. Take 2 is the stronger frame (all faces turned to the box, Leo's face visible). These are first frames, not the cast reference set: 05 still locks cast refs, and this still can seed them.
Spend today: turntables ~$0.55, K01 test clip $0.36, beat-2 stills $0.28 (AtlasCloud balance $15.11).

## Planar-tracking test (2026-11-25, free) — owner ruling 5
`scripts/track_composite_test.py` (OpenCV 4.14 in `~/.local/share/rea-video/.venv`): manual ornament box on frame 0 → KLT feature tracking on the generated placeholder face → RANSAC homography per frame → the real render warped and alpha-composited. Run on `K01-test-hang-seedance.mp4` frames 0–59. Output: `turntable/K01/K01-tracking-test-opencv.mp4` (side by side) + `K01-tracking-test-sheet.jpg`.
- **PASS within a shot:** frames 0, 20 and 40 of shot 1 (slow push-in, hand under the hanging ornament) hold the real artwork locked on the moving ornament; names and faces sharp; 167–400 inliers per frame.
- **Breaks across the cut** into shot 2 (the spinning ornament): expected. Tracking resets per shot, and spinning shots are already ruled out.
- To do in 06: per-shot manual first-frame quad (or corner refinement), a light grade on the composite to match scene light, and a soft edge/shadow. The method holds for 1A/B5a/B5b-type shots that keep the ornament facing camera with slow motion.
