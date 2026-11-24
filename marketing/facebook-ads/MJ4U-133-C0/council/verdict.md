# Council verdict — MJ4U-133 C0 scripts (2026-11-24)

Chairman's synthesis of 5 advisors (Outsider, Contrarian, Executor, Expansionist, First Principles) and 5 peer reviews. Where they disagreed on a fact, I checked the scripts, CRITERIA.md, hooks/03-selection.md §4, product.json and the K02 hero file myself; rulings are stated inline.

## Where the Council Agrees

1. **Every script is fixable. None needs a rewrite.** All six are on-plan, hooks verbatim, budgets mostly clean. The defects sit in three places: shots that won't generate, captions that describe nothing or the wrong thing, and a few locked-rule breaks the scripts' own check reports wrongly passed.
2. **Multi-body action is where the $300 goes.** Five of five flagged the same shots: K10 b7 (Corgi jumps into a hug), K02 5a (dog licks Dad's face in a 4-person hug), K01 b2 (7 matched identities in 2.6s), K06 5a/5b (infant + 3 people + a precise point), K13 b6 (4 actions + tears in 3.9s). Fix pattern: pets still, one action per clip, no AI tears.
3. **K01 beat 2 is the riskiest shot in the round and it is the control.** If the seven aren't readable, H76 fails E28 (script's own conflict #3). Prove it first.
4. **Composited text must never be generated:** DECORATIONS (K10), DAD'S LIST: 1. NOTHING (K02).
5. **K10 "Their first Christmas as three."** reads as a pregnancy announcement (Outsider, Contrarian; nobody defended it).
6. **K01 beat 4 "Grandpa pushed up his glasses."** is a stage direction that also smuggles K04's concept into the control. Every advisor who touched it wanted it gone.
7. **K02 hero file is not a cut-out** (RENDERS.md confirms "on a tree, not transparent"). Beats 1–3 can't be composited cleanly without a re-export.

## Where the Council Clashes

| Clash | Ruling | Why |
|---|---|---|
| K06: make beat 3 (6.0s) a live family (Outsider, Contrarian, Expansionist, First Principles) vs leave as written (Executor, Review 4) | **Not a craft fix → owner question 1.** | K06 is the slate's only PX4 product-hero card (00C-slate) and K01/K06 are kept distinct largely by PX1 vs PX4. Putting a live family at 6s changes the tested axis. |
| K02 READY (Expansionist) vs READY WITH FIXES (everyone else) | **READY WITH FIXES.** | Verified: non-transparent hero (blocker), "Bailey jumps up and licks his face" in a 4-person hug, list text unmarked as composited, copy drops "3D-look". |
| "big wooden numbers" is *false* (Contrarian) vs *imprecise* (Reviews 1, 2, 4) | **Imprecise, still a must-fix.** | F9 = "big 3D-look wooden numbers". Without "3D-look", readers expect raised wood. It's a one-word fix. |
| K13: Mom holds the ornament low and out of sight (Contrarian) | **Dropped.** | The H16 card raises it into lamp light by 1.0s. That's a locked hook frame (03 §4) and it also protects E3. The kids' eyes are on the collar in the hook, so beat 3 is still *their* discovery. |
| K13 b6: wet eyes on Mom only (Expansionist) vs no tears at all (Executor, First Principles) | **No tears.** | AI tears are a known tell. Smiles and the hug carry it. |
| E: show a name or year sharp in every hook frame; K01 H79 raise to VS2 by 0.8s | **Dropped.** | Both change locked 0–2s hook frames (03 §4). |
| E: cut K02 beat 3 to 3.2s | **Dropped.** | Not needed once the grin visibly breaks by 6.5s, and a retime would reopen E32. |
| Executor: K04 1A "two fingers on the edges, not by the string"; K01 H76 "lid out of frame first" | **Dropped as script changes.** | Both are in locked hook frames. 05 handles them as post tracking (round-wide rule 1). |
| K01 b4 caption: "Grandpa counted too" (Expansionist) | **Rejected.** | No shot shows counting (E50). |
| K06 b4 caption: "Mateo's first one. 2026." (Expansionist) | **Rejected.** | Implies a series (K06 line 16: no "every year"). |
| K10 b2: add stacked moving boxes (Outsider) | **Already in the script** | ("moving boxes stacked"). Outsider was wrong. |
| K10 b4: DECORATIONS on a moving flap (Executor) | **Partly wrong.** | Beat 4 has no flap action, but beat 2 does. The rule still applies. |
| K02 b4: lock the pan to start on Bailey (Outsider) | **Already so.** | Verified against the hero file: printed L→R is Bailey · Mary · Jacob · Kobe · Susan · Luna. |
| Proof captions "read the print back" in 5 of 6 (Outsider) | **Partly wrong.** | K13's proof caption is the model line and K04's names no one. The real offenders are K06 b4 and K04 b4 (filler), fixed below. K01's roll call is deliberate: it pays "Seven" muted. |

## Blind Spots the Council Caught

(From the peer reviews and my own checks. No single advisor had these.)

1. **K02 cast table order is wrong; the pan is right.** I checked the hero file. Printed L→R: Bailey · Mary · Jacob · Kobe · Susan · Luna. The cast table header says Jacob first. 05 must block from the print, not the table.
2. **E32 breaks the scripts self-passed:** K04 2a (1.4s), K06 2a (1.6s), and the 0.5s own-ornament shots at 17.0–17.5 in K04 and K06. K10, K13, K02 and K01 already run their last story shot to 17.5 with the ornament in frame, and that satisfies the brief's "own ornament at 17.0–17.5" ruling.
3. **The hook caption runs to 3.2s over the first body shot.** The first body shot must not contradict it. Checked: K10 H15 ("…finally have company" over the bare tree) and K13 H17 ("His bed is empty…" over a no-bed shot) are tolerable for 1.2s. Rule for 05: the first body frame must not visually contradict either hook caption.
4. **E57 vs E60 in full-frame proof beats:** the 9:16 safe zones (no text in the top 14% or bottom 35%) can push the caption band onto the printed names. Nobody placed the bands.
5. **No per-actor live ↔ print match sheet** (skin, hair, glasses, sweater colour). Every hand-off and every "points at his printed self" beat depends on it.
6. **K02 has no mother**, on screen or on the print, and its family is the shared end card in all 12 ads (owner question 2).
7. **K01 copy** "Grey hair, round glasses… for each person" reads as if everyone gets grey hair.
8. **CTA key:** `engine/upload_draft.py:219` reads `content["cta"]`. K01/K02 use `button`, the other four `call_to_action`.

## The Recommendation

All six go to Gate A **READY WITH FIXES**. None is NOT READY. Apply the must-fixes below (one 04 revision pass, captions included). Answer the owner questions. Then before any video spend, prove K01 beat 2 as an image. K02 needs its transparent re-export before 05 can start it.

### K10 — READY WITH FIXES (5 must-fix)
**Must-fix**
1. Beats 2–3 (2.0–6.4s): kraft box tucked under one fold of red tissue, only a Santa hat and the box edge showing (still VS1). In beat 4 she lifts the tissue first.
2. Beat 4 (6.4–9.0s): Daniel's face must read for the last ~0.8s. Do the focus shift box → Daniel in post on a deep-focus plate, so "He watched" is true (E50).
3. Beat 6 (12.2–14.8s): no hanging by the string on camera. Her hand releases an already-hung ornament (post sway). Caption → **"She hung theirs first."** (4 w, 12.7–15.0 = 2.3s, 1.74 w/s), which pays "only hers".
4. Beat 7 (14.8–17.5s): Mochi already sits at their feet, looks up and wags; no jump. Caption → **"First Christmas as two. / Plus Mochi."** (6 w, 15.0–17.5 = 2.5s, 2.40 w/s).
5. 1A/beat 2: "DECORATIONS" composited on a static flap (only the hands move). 1B rack focus done in post on a locked-off plate.

**Optional**
- Beat 4 caption → "He'd hidden it with hers." (5 w, 2.6s, 1.92 w/s): adds motive.
- Beat 5: let the pan rest on Mochi for a beat before settling on 2026.

### K13 — READY WITH FIXES (5 must-fix)
**Must-fix**
1. Caption lag (E50). Retime the picture: beat 2 2.0–4.6, beat 3 4.6–7.6 (still ≤5.0s per 03 §4.1), beat 4 7.6–10.8. Lily is still holding the collar as beat 3 opens. Shot lengths become 2.0 / 2.6 / 3.0 / 3.2 / 2.8 / 3.9, no equal neighbours. Captions unchanged.
2. Beat 3: Mom's palm is already open as she kneels and the push-in does the reveal. No fingers uncovering the composite.
3. Beat 5 (10.8–13.6s): Lily's hand releases the already-hanging ornament (post sway), Noah steadies the branch, Mom's arms round both. That avoids four kid hands on one string. The caption stays true.
4. Beat 6 (13.6–17.5s): open with the collar already on the bed and Lily's hand withdrawing → hug in three-quarter/back view. **No tears.** Printed Biscuit and the collar sit in one sharp vertical line (composite if depth of field fails).
5. Beat 6 caption → **"His collar stays / under his spot."** (6 w, 13.6–17.0 = 3.4s, 1.76 w/s). It echoes H17, and "under him" read as a grave.

**Optional**
- 1B: frame the collar large so it reads in 0.4s (inside the card spec).
- "BISCUIT" on the collar tag, composited (touches the hook prop → owner question 6).

### K04 — READY WITH FIXES (7 must-fix)
**Must-fix**
1. Merge 2a+2b into one shot, 2.0–6.0 (4.0s): fingertip on Grandma in the photo → beside printed Grandma → Grandpa's glasses in the photo → beside the printed glasses. Fixes E32. Caption unchanged.
2. Beats 2–3: camera locked top-down; the finger stops beside each figure and never overlaps the print (R24). Beat 3 changes framing: the photo lifted in her hand beside the ornament.
3. Build "last year's photo" as an image from the locked cast refs before any video. It's a 4th identity surface.
4. Beat 4 (8.8–12.0s) caption → **"Olivia put herself / on it too."** (6 w, 3.2s, 1.88 w/s). It replaces the filler "All four of them. / 2026."
5. Beat 5a (12.0–14.2s): open with the ornament already in Grandpa's hand → glasses tap (big, centred) → laugh. Olivia in frame watching (soft is fine), so the reaction is *to her*.
6. Beat 5b runs to 17.5 with the ornament in frame. Delete the 0.5s own-ornament shot at 17.0–17.5 (E32).
7. Copy: "Every detail picked by hand, one person at a time." → "Every detail chosen, one person at a time." The old line implies hand-painted; F6 is option-picking.

**Optional**
- Beat 5a: direct Grandpa's laugh to match the photo's grin (pays H34's "Same grin" by picture, no claim).
- A 1s insert of the real personalizer screen (screen recording, composited) to kill the "photo-to-portrait" read. Only if 07 flags H33.

### K06 — READY WITH FIXES (5 must-fix; structure → owner question 1)
**Must-fix**
1. Merge 2a+2b into one slide, 2.0–6.0 (4.0s): Sofia → Mom → Dad. Fixes E32. Caption unchanged.
2. H50: confirm the render's baby-figure crop holds at 1080w with ≤1.5× upscale. If not, re-render the K06 artwork larger. The hook frame stays.
3. Beat 4 (8.8–12.0s) caption → **"Mateo got / the end spot."** (5 w, 3.2s, 1.56 w/s). It replaces the spec line and implies no tradition.
4. Beat 5 (12.0–17.5s): ornament already hanging, Sofia's hand letting go (post sway). Mateo swaddled near-still in Mom's arms, face three-quarter. Sofia points *toward* the printed baby, then Mateo, never touching. Dad soft behind.
5. Beat 5b runs to 17.5 with the ornament in frame. Delete the 0.5s shot at 17.0–17.5 (E32).

**Optional**
- Keep beats 3 and 4 visibly different (branch vs full-frame flat), as the script already notes.

### K02 — READY WITH FIXES (8 must-fix; #1 blocks 05)
**Must-fix**
1. Re-export the same cast (Bailey, Mary, Jacob, Kobe, Susan, Luna) from the personalizer as a transparent render before 05. Beats 1–3 can't be composited otherwise.
2. Cast table: reorder to the printed L→R **Bailey · Mary · Jacob · Kobe · Susan · Luna** (verified on the hero file). The pan in beat 4 is already correct.
3. Copy bullet 4 → "A name under each member, plus the year in big 3D-look wooden numbers" (F9). Rename `button` → `cta` at the ad-content.json step.
4. H63: generate a blank sheet. "DAD'S LIST: 1. NOTHING" is composited real lettering and is marked "composited" in the shot brief.
5. Beat 2 (2.0–4.6s): one hand-off only. The box stays flat and open; the cocoa goes down at the frame edge, then he takes the box.
6. Beat 3 (4.6–8.8s): the grin visibly breaks by ~6.5s so it doesn't read as annoyed muted. At ~8.0s he lifts the ornament flat in both hands, not by the hanger.
7. Beat 5a (12.0–14.6s): Bailey's paws and head already on the armrest, pushing in. No jump, no lick.
8. Beat 5b (14.6–17.5s), to pay "His idea.": Mary reaches toward a side branch, Jacob points to the centre, cut to his hand releasing it dead centre (post sway). Caption unchanged.

**Optional**
- 5b: "DAD'S LIST" sheet soft on the side table (composited). It closes H63 visually and is harmless in H61.

### K01 (control) — READY WITH FIXES (6 must-fix; gate condition = beat 2)
**Must-fix**
1. Beat 2 (2.0–4.6s): build the first frame as an image from the locked cast refs, with seven staged in two clear rows. Animate minimal motion. Leo looks and points at the box (drop the shush, which has no logic). Prove it before any other K01 spend.
2. Beat 2 caption → **"Cooper the dog / is on it too."** (7 w, 3.2–6.9 = 3.7s, 1.89 w/s). Strangers read "Cooper" as a man.
3. Beat 4 (6.9–9.0s): ornament held steady in both hands, front-lit, not swung by the hanger toward the lights. Grandpa leans in close with no glasses push. Caption → **"Grandpa needed / a closer look."** (5 w, 2.1s, 2.38 w/s).
4. Beat 6a (12.2–14.8s): over Grandma's shoulder, ornament sharp in the foreground. Leo points at his printed figure, then at himself; the family is soft behind. Caption → **"Everyone found / their spot."** (4 w, 12.7–14.8 = 2.1s, 1.90 w/s).
5. Beat 6b: hand-release on the high branch (post sway), Grandpa's hand on hers. Not hung by the string on camera.
6. Copy: "big wooden numbers" → "big 3D-look wooden numbers". Bullet → "Hair, glasses, sweater and a drink for each person". Rename `button` → `cta`.

**Optional**
- Beat 3: Grandma's fingertip moves figure to figure (beside, never over) and stops at Cooper. This pays H79's "counted every face" by picture.
- Copy: "Grandpa, the kids, the grandkids" → "Grandpa, their kids, the grandkids".

Caption totals after the fixes, all ≤45: K10 38/36 · K13 36/42 · K04 33/32 · K06 28/30 · K02 33/34 · K01 36/37.

## Round-wide rules for 05 (production)

1. **Ornament never spins and is never lifted or hung by its string on camera in the body.** It is either flat in a hand or box, or already hanging, with the sway added in post on the 2D layer. Every "hangs it" becomes a hand-release. Hook frames that do otherwise (K04 H33 string lift, K01 H76 lid, K13 H16 raise) stay as locked; 05 budgets planar tracking for them.
2. **Generated shots:** ≤3 sharp faces, pets still, one action per clip, no AI tears, infants near-still.
3. **First frames are images first**, from locked cast refs, before any video. Identity drift gets caught at image prices.
4. **Before Gate A, write one live ↔ print match sheet per actor** (skin, hair, glasses, sweater colour, drink).
5. **All authored text is composited:** DECORATIONS, DAD'S LIST, any tag text. Focus pulls and blur on a composite are done in post.
6. **Before generation, place the caption band for every proof beat.** It must satisfy E57 safe zones without covering names or the year (E60). If it can't, scale the still smaller in frame; don't move the band mid-ad (E58).
7. **The last story shot runs to 17.5s with the concept's own ornament in frame.** No separate 0.5s shots.
8. **The first body frame (2.0–3.2s) must not visually contradict either hook caption.**
9. **Generate 9:16 with a 4:5-safe centre** and crop the 4:5 from it.
10. **Budget:** ~33 shots ≈ $100–130 at ~3 takes plus ~$20 images. Reserve the headroom for K01 b2, K02 5a and K10 b7. Past 8 takes on any shot, use the fallback above; don't keep re-rolling.
11. **ad-content.json:** normalize the CTA key to `cta` and pass `upload_draft.py --validate-only` (E72).

## Questions for the owner (Gate A)

1. **K06 is 12s of one render with no people (beats 1–4). Make beat 3 (6.0–8.8s) end on Mom holding Mateo soft behind the hung ornament?**
   Recommended: **no, keep as written.** K06 is the slate's only product-hero (PX4) arm; the round exists to learn whether that works, and a live family at 6s blurs it into K01. Its weakness is now a known risk, not a script defect. The 2a merge and the new beat-4 caption reduce the slideshow feel.
2. **Shared end card = the K02 family (Jacob's family, no mother, live-looking Bailey).** It continues K02's own story, puts a stranger's family 0.5s after K13's dog memorial, and is a motherless family in all 12 ads.
   Recommended: **if a neutral 7th render can be made free in the personalizer (a family not used in any concept, two parents), swap the plate. Otherwise keep the ruling and accept the small K02 tilt.** The end card is identical across ads, so the tilt only affects continuity.
3. **K04 H34 "Same glasses. Same grin. Same Grandpa."** No expression option exists (F6), so "Same grin" is an unbacked likeness claim.
   Recommended: **run 07's claim check now, before generation.** If it fails, swap to H35 per 03.
4. **K04 H33 may read as "upload a photo → portrait."**
   Recommended: **keep H33.** Use the copy fix above and a 07 cold read; add the optional personalizer-screen insert only if 07 flags it.
5. **K13 is the only bittersweet concept under one shared music bed (E6).**
   Recommended: **keep one bed. Choose a track whose first ~6s are sparse** and builds later. That is a track choice, not a variant, so E6 holds.
6. **"BISCUIT" on the collar tag** (composited) touches the H16/H17 hook prop.
   Recommended: **yes.** It makes "Biscuit = the dog" read in second one, and it's a prop detail, not a framing change.
7. **K02's motherless family** may read as single or bereaved Dad.
   Recommended: **keep (GATE0 decision).** No caption implies loss, and the comedy carries it.

## The One Thing to Do First

**Generate K01 beat 2 as a still first frame (seven render-matched people + Cooper in two staged rows) before any other spend.** It's the round's control, its riskiest shot, and the shot H76's E28 payment depends on. It costs cents as an image, and if it can't be made, the owner needs to know at Gate A, not after $100 of video.
