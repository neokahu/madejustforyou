**K10 — READY WITH FIXES · ~7 generated shots → ~20–24 clips w/ retakes**
- Beat 7 (14.8–17.5): "Mochi jumps up between them" — live corgi doing a cued action during a 2-person hug is the 5+-retake shot. Fix: Mochi already sitting between their feet, looks up and wags as they turn into the hug. Same meaning (the three of them).
- Beat 6 (12.2–14.8): "hangs the ornament by its string" — hand+string+small object = tangles/warp, and the composite must track a spinning ornament. Fix: her hand enters; cut to the ornament already hanging on an empty-generated branch, sway added in post on the 2D layer.
- Beat 1B (0–2.0): rack focus across a composited ornament. Fix: generate a locked-off plate with no focus pull; do the rack in post by blurring the composite layer.
- Beats 1A/4: "DECORATIONS" on a moving flap. Fix: box and flap static, only hands move → lettering composites flat.

**K13 — READY WITH FIXES · ~7 shots → ~20–24 clips** (no live dog = big saving)
- 1A (0.3–1.0s): Mom raises the ornament into lamp light = composite on a moving hand through changing light. Fix: she holds it still at frame edge; a camera push does the "raise".
- Beat 3 (4.2–7.0): she "opens her hand" to reveal it = fingers uncovering a composite = frame-by-frame matte. Fix: palm already open as she kneels; push-in reveals.
- Beat 5 (10.8–13.6): two kids hang it together, "both hands on it" = 4 kid hands on one string, the worst hand case of the round. Fix: Lily's hand releases an already-hanging ornament (post sway), Noah's hand steadies the branch, Mom's arms around both.
- Beat 6 (13.6–17.5): 4 actions in 3.9s (lays collar, looks up, turns, hug with wet eyes). Fix: open with collar already on the bed, her hand withdrawing → hug. Drop "wet eyes" — AI tears look over-acted; smiles are enough.

**K04 — READY WITH FIXES · ~5 shots + 1 photo still → ~14–16 clips**
- 2a–3 (2.0–8.8): fingertip "rests on" tiny printed figures on a 5-in ornament = hand over composite needing a precise per-frame matte. Fix: finger touches the photo (generated anyway) then stops beside each printed figure, never over the ornament outline (R24 already asks this). Lock camera top-down so the composite is static.
- The "last year's photo" is a 4th identity surface — Grandpa/Grandma/Rosie must match live cast in 5a/5b. Fix: build the photo from the same locked cast refs, as an image (cents), before any video.
- 5a (12.0–14.2): lift from box + look + tap glasses + laugh in 2.2s. Fix: open with the ornament already in his hand → glasses tap → laugh.
- 1A: "lifts it out by the string" → swing. Fix: two fingers on the edges, face-on.

**K06 — READY · ~2 shots → ~6–8 clips. Cheapest script.** Beats 1–4 are render moves + a static branch plate (post only).
- 5a/5b (12.0–17.0): 4 live people incl. an infant; babies drift and flail. Fix: Mateo swaddled on Mom, face three-quarter turned, near-still; Sofia points toward (not touching) the already-hanging ornament (post sway); "lift onto tree" → her hand letting go.

**K02 — READY WITH FIXES · ~6 shots → ~22–26 clips**
- H63: handwritten "DAD'S LIST: 1. NOTHING" will garble if generated. Fix: generate a blank sheet, handwriting in post; the box slides beside the text (as the script says).
- Beat 2 (2.0–4.6): two hand-offs (box into his hands, cocoa down) with 3 kids watching. Fix: cocoa already on the side table; one hand-off of a box that stays flat and open.
- 5a (12.0–14.6): "Bailey jumps up and licks his face" + 3-kid hug = live pet cued action on top of 4-person identity; 2nd-riskiest shot of the round. Fix: Bailey's paws and head already on the armrest, pushing in. Same warmth.
- Hero file not transparent (conflict #5). Fix before Gate A: re-export the same cast from the personalizer — free, and beats 1–3 can't be cleanly composited without it.

**K01 — READY WITH FIXES · ~6 shots → ~26–32 clips. Where the money goes.**
- Beat 2 (2.0–4.6): 7 readable cast members matching the render + a dog, 3 acting = riskiest shot of all 12 ads; failing it breaks E28 for H76. Fix: lock the first frame with an image model first (~$0.10/try, many tries), then animate with minimal motion (Leo's shush + Cooper's nose only). Prove this shot before spending anything else on K01.
- 6a (12.2–14.8): 7 people each acting (wave/cheer/laugh/bark). Fix: over Grandma's shoulder, ornament sharp in foreground, family soft behind; use the script's own fallback "Everyone waved. Even Cooper." (tail reads; bark doesn't).
- Beat 4 (6.9–9.0): held "toward the tree lights" by its hanger → spin + backlight. Fix: held steady in both hands, front-lit.
- H76 (0.3s): lid comes off over the composite. Fix: lid lifts up and out of frame before the ornament face shows; box stays still.

**Across all six**
- **Budget:** ~33 generated shots, all ≤5s. At ~3 takes avg ≈ 100–130 clips ≈ $100–130, plus ~$15–25 first frames + cast sheets. Fits the $300 cap with ~$150 headroom — reserve it for K01 b2, K02 5a, K10 b7. If any passes 8 takes, use the fallback above, not another roll.
- **One rule for every ornament shot:** the ornament never spins and is never lifted/hung by its string on camera. Either flat in a hand/box, or hanging on an empty-generated branch with post sway on the 2D layer. Every "hang it on the tree" becomes hand-release + settle. Removes most composite tracking.
- **Frame once:** generate 9:16 with a 4:5-safe centre and crop the 4:5. Generate first frames as images before video so identity drift is caught at image prices.
