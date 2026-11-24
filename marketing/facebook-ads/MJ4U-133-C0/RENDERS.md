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
| K02 | existing hero artwork (Bailey · Mary · Jacob · Kobe · Susan · Luna) | `ads/source-images/hero-family-2026-tree.png` (on a tree, not transparent) |

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
