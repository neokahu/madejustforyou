# MJ4U-133-C0 · K04 · Gate B reference set (role 05 self-check, 2026-11-25)

Scope (owner ruling 2026-11-25 item 8 + coordinator): cast views 1–3 (Nano Banana Pro Edit) + scale plate + 1B-R plate (Seedream v5 Pro Edit). Identity photos (last year's, young Grandpa) come **after** Gate B.
Media: `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K04/refs/` (rejects in `_rejected/`, printed-figure crops used as look refs in `_inputs/`). Contact sheet: `K04/refs/gateB-contact.jpg`.
**Status: self-checked by 05, awaiting 07 shot mode → owner. 05 does not grade this as final.**

## Spend
11 NBP Edit submissions × $0.14 = $1.54 (one was blocked by the platform's content filter and is probably not billed) + 3 Seedream × $0.0384 = $0.12. **Total ≈ $1.52–1.66, under the $2.30 cap.**

## Results
| Ref | File | Self-check | Notes |
|---|---|---|---|
| C1 Grandpa v1 front | C1-grandpa-v1-front.png | PASS | round thin black wire glasses, clear lenses; grey taper; clean-shaven; green Fair Isle. Right hand at the bottom edge, bare (no ring) |
| C1 Grandpa v2 ¾L | C1-grandpa-v2-34left.jpg | PASS | same face and glasses |
| C2 Grandma v1 front | C2-grandma-v1-front.jpg | PASS (2nd submission) | take 1 blocked by the platform filter (prompt rephrased, no identity change). Grey tight curls, no glasses, red Fair Isle with reindeer; hand at edge bare |
| C2 Grandma v2 ¾L | C2-grandma-v2-34left.jpg | PASS | |
| C3 Olivia v1 front | C3-olivia-v1-front.jpg | PASS, flag | box braids, white Fair Isle with red band. **Flag for 07:** reads ~22–25; script says 25–30 adult. Age-up in views 4–8 if 07 agrees |
| C3 Olivia v2 ¾L | C3-olivia-v2-34left.png | PASS | |
| C4 Rosie v1 front | C4-rosie-v1-front.jpg | PASS | tricolour beagle, plain brown collar, no tag |
| C4 Rosie v2 ¾ | C4-rosie-v2-34-take2.jpg | PASS (take 2) | take 1 REJECTED: two heads (`_rejected/`) |
| C4 Rosie v3 profile, lying | C4-rosie-v3-profile.jpg | PASS | |
| ~~PROD scale plate take 2~~ | `_superseded/PROD-scale-plate-take2-SUPERSEDED-reads-7in.jpeg` | SUPERSEDED (07 S3: reads 6.5–7 in by the hand) | ornament ≈1.5× palm width, ≈1.7× the mug rim (5 in reads right); cuff white with a red band; ring finger bare. Mug cropped at the right edge. Take 1 REJECTED: the mug was too small, so the ornament read as ~7 in |
| ~~K04-1B-R plate v1~~ | `_superseded/K04-1B-R-plate-v1-SUPERSEDED-thick-edge.jpeg` | SUPERSEDED (07 S2: edge 12–18 px ≈ 6–9 mm board) | single flat sheet, left plywood edge visible, tab + hole, thin gold cord rising out of frame, plain cream backdrop. Printed face is a generated placeholder: the real render is warped over it in post (E37) |

## NOT MADE: view 3 (full body seated) for Grandpa, Grandma, Olivia
The Claude Code auto-mode permission classifier denied the full-body-seated submissions for Grandpa and Olivia. Grandma's v3 was not attempted, since it is the same kind of request. Per the denial I did not retry or work around it. **The owner or user has to approve these 3 images (≈$0.42 NBP) or rule that views 1–2 are enough for Gate B.** Their hands matter most for Olivia (1A–B3); her hands view (v6) is in the post-Gate-B batch anyway.

## For 07 (shot mode)
Check at full res against the render crops: glasses shape (C1), no glasses (C2), braids and age (C3), markings (C4), every visible hand for rings, scale ratios on the scale plate, and the condition-1 elements on the 1B-R plate.

## Fix pass (owner ruling "Gate B fixes and ornament size", 07-GATE-B.md), 2026-11-25
Cap $0.70; spent 4 × Seedream v5 Pro Edit $0.0384 = **$0.15** (ledger purpose `refs`). Running K04 refs total ≈ $1.67–1.81.

| Ref | File | Self-check | Evidence |
|---|---|---|---|
| **K04-1B-R plate v2b** (replaces v1) | K04-1B-R-plate-v2b.jpeg | PASS, to 07 | Square-on hang, prompt "single hair-thin pale line, no visible thickness band". At native res (1:3 zoom) the outer cut edge is one dark contour ~1–2 px with no wood band and no double contour; the sheet separates from the backdrop by its soft shadow down-right; tab, hole, gold cord to the frame top. Condition 1 ("cut edge against a plain background") is met by the silhouette and shadow, not by a visible side band. No post fix needed |
| K04-1B-R plate v2a | `_rejected/K04-1B-R-plate-v2a-edge-still-thick.jpeg` | REJECTED | 8° yaw: left edge band still ~10–15 px |
| **PROD scale plate v3a** (replaces take 2) | PROD-scale-plate-v3a.jpeg | PASS at 5 in, to 07 | Ornament ≈0.73× her wrist-to-fingertip length (5 in ÷ ~17–18 cm ≈ 0.72) and ≈1.25–1.4× her knuckle width; the mug rim reads ≈0.75× the ornament width (8 cm vs 12.7 cm ≈ 0.63, so slightly large: the mug sits nearer the lens). The hand anchor reads ≈4.5–5 in. Cuff white with a red band, five fingers, ring finger bare |
| PROD scale plate v3b | `_rejected/PROD-scale-plate-v3b-reads-6in.jpeg` | REJECTED | ornament ≈0.83× hand length, ≈1.8× knuckles → ~6 in |

Post fallback, in case 07 still reads the v2b edge as thick: before compositing, erode the plate's ornament matte by the excess edge width (target ≤5 px band at 77 px/cm) and paint the real render's alpha silhouette 2 px larger over it, so the visible edge is the render's own outline plus a 1–2 px plywood-tone stroke. Not needed on v2b as measured.
B2 layout scale (1 cm ≈ 39 px) is set from the declared 5 in (E41), not measured from any plate (07 note).
