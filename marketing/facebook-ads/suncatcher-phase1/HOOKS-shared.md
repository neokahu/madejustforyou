# Suncatcher Phase 1: shared hooks and shared skeleton

> Product: dog memorial suncatcher, **6 IN, German Shepherd, "Alex"** (`products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png`).
> Source of truth: the plan page (https://testing-plan-phase-1.namvu47.workers.dev, text in `_plan-page-text.txt`), §05 / §06 / §07 / §09.
> The plan's placeholder "Max" is replaced with the real name, **Alex**.
> Scripts that use this file: `C1-personalization.md`, `C2-reaction.md`, `C3-buyer-swap.md`.
> Path convention: every path in this folder is repo-relative. Bare `tests/…`, `assets/…`, `ads/…` mean `products/suncatcher-dog-memorial/tests/…` etc. The **BUILD LIST (§10)** always gives the full path.

## Revision 2 — user answers 2026-10-08

Source: the user's answers to `OPEN-QUESTIONS.md`, plus the coordinator's packaging correction (same day). All of them are applied here; the full answer log is in `OPEN-QUESTIONS.md`.

| Answer | What changed in this file |
|---|---|
| **Q1 = YES**: the real panel in direct sun throws a legible "Alex" and a recognisable German Shepherd shape on the wall | Every `⟂ IF / ⟂ ELSE` resolved to the projection-true branch and the ELSE text deleted: §4 B3b (now one shot, `WALL-4K` with the real "Alex"), WALL-4K steps 3–4, §4b third bullet ("his shape lands on the wall"), §8 asset table. |
| **Q2**: offer and delivery window are irrelevant to the video ads | `[STANDARD OFFER — confirm]` removed from the §4b copy block. No shipping, delivery or arrival line anywhere. §9 S6 closed. |
| **Q4/Q5 packaging and gift-buyer features (as corrected by the user)**: show an attractive gift box; no ship-to-recipient or gift-note feature exists | C3 keeps the kraft gift box with white tissue and twine, and the friend's own handwritten card as a styling prop. `F-BOX.png` stays REUSE. No copy claims shipping to the recipient, a gift note or delivery; the friend hand-delivers. (Detail in `C3-buyer-swap.md`.) |
| **Q3**: product page has a breed picker, live name preview and a real photo | Resolved; no change. |
| **Q6** gifter bridge (C2 only) | Concept file only; S10 updated. |
| **Q11 music bed approved** | §6 Voice: `ads/shots/music.mp3` is approved. |
| **Q14 / Q15** (approved defaults) | Concept files only (C2 beat-2 caption; one headline format). Nothing shared changed. |
| Q7, Q8 | Kept as build/read notes (§7, §3 QA). |
| Q9, Q10, Q13 | Parked, not applied. |
| **New: BUILD LIST** | §10: every shot of all 6 ads, one row each, with source, prompts, refs, durations and post steps. |

Re-checks after Revision 2: pronoun/casting check (§5 and each concept file) and the 3-second check (§7 and each concept file) were re-run; both pass.

## Revision 1 — council 2026-10-08

Source: `_council/C1-personalization/verdict.md`, `_council/C2-reaction/verdict.md`, `_council/C3-buyer-swap/verdict.md`.

| Item | Status | What changed in this file |
|---|---|---|
| C2 #10 [SHARED] HOOK-H2 silhouette unmistakable in frame 1 | **Applied** | §3 HOOK-H2 Visual row, start-frame prompt and QA: the panel fills at least a third of the frame width, the ears and muzzle are crisp against the glowing glass, and there is a muted "is this about a dog?" QA before animating. |
| C1 #9 [SHARED] projection-check fallback | Was conditional; **resolved in Revision 2** (Q1 = YES, projection branch) | §4 B3b, WALL-4K steps, §4b. |
| Concept-slot consequences | Updated to match | §2, §6 cut row (C3 beat 4 = 3.0+2.0, beat length unchanged), §5 cast (Alex in a framed photo in C1 beat 4), §8, §9 S9. |

This file defines everything the three concepts share: the two hook clips, the 20s skeleton, the three locked body beats (3, 5 and the music), the cast, the craft spec and the build list. Each concept file adds only its **concept slot** (beats 2 and 4).

---

## 1. The 6 ads

| Ad | Concept | Hook | Hook clip | Body |
|---|---|---|---|---|
| S-C1-H1 | 01 Personalization | H1 name shown | `HOOK-H1` | C1 slot |
| S-C1-H2 | 01 Personalization | H2 relationship | `HOOK-H2` | C1 slot |
| S-C2-H1 | 02 Reaction | H1 | `HOOK-H1` | C2 slot |
| S-C2-H2 | 02 Reaction | H2 | `HOOK-H2` | C2 slot |
| S-C3-H1 | 06 Buyer swap | H1 | `HOOK-H1` | C3 slot |
| S-C3-H2 | 06 Buyer swap | H2 | `HOOK-H2` | C3 slot |

The same two hook files go on all three bodies, byte for byte. Between H1 and H2 of one concept, the only thing that changes is 0.0–2.0s of picture plus the hook caption.

---

## 2. Shared skeleton: structure A, 20s

Beat boundaries come straight from the plan's §05 suncatcher example (0–2 / 2–6 / 6–12 / 12–17 / 17–20).

| Beat | Time | Len | Role (plan §05) | C1 · C2 · C3 | Product on screen |
|---|---|---|---|---|---|
| **1 Hook** | 0.0–2.0 | 2.0 | Opening | **SHARED**: `HOOK-H1` or `HOOK-H2` | ✅ both hooks |
| **2 Context** | 2.0–6.0 | 4.0 | Who, and what happened | **CONCEPT SLOT** | ✅ in every concept |
| **3 Name reveal** | 6.0–12.0 | 6.0 | Name and breed on the wall, legible, held | **SHARED**: `B3a` + `B3b` | ✅ hero |
| **4 Payoff** | 12.0–17.0 | 5.0 | Full reaction | **CONCEPT SLOT** | C1 its shadow · C2 ✅ (its light in the bed) · C3 box, then open box with the panel (3.0+2.0) |
| **5 Close + CTA** | 17.0–20.0 | 3.0 | Close-up of the panel in the window + CTA | **SHARED**: `B5` | ✅ hero |

**The one thing that changes between concepts** is who or what the camera follows in beats 2 and 4:

| | Beat 2 follows | Beat 4 follows |
|---|---|---|
| **C1 · Personalization** | the object world: Alex's engraved ALEX tag, his empty bowl, panel in the window | his shadow on the wall, with the owner holding a framed photo of the living Alex beside it (face not featured) |
| **C2 · Reaction** | the owner's face *before* the light, his empty dog bed sharp beside him | the owner's face *as* the light lands: Alex's German Shepherd-shaped light lying in the empty bed, his gaze lowered to it |
| **C3 · Buyer swap** | the friend (the buyer) lowering it into the gift box | the friend handing it to the owner, then the open box in his hands |

Everything else is locked across all six: beat 1 clips, beats 3 and 5 (picture and captions), length, music, grade, caption style, CTA and button. (The offer is not in the creative; it is handled outside it, plan Phase 2.)

---

## 3. Shared hook clips

### HOOK-H1 · name shown (control)

| | |
|---|---|
| **On-screen text** | **That's not a generic dog.** / **That's his actual breed — and his name.** |
| **Caption timing** | Line 1 from 0.0s. Line 2 added under it at 1.0s. Both hold until **3.0s** (1.0s into beat 2, which carries no caption before 3.0s in any concept). 12 words over 3.0s. |
| **Visual** | `PANEL-4K` = **REUSE** `products/suncatcher-dog-memorial/tests/testF-nanobananapro.png` (3072×5504, the real panel hanging in a sunlit window, "Alex" legible). |
| **Camera** | One move: **Ken Burns pull-out**. Frame 1 = a 1300px-wide crop centred on the silhouette, so "Alex" is ~140px wide in the 1080px output and the ears, muzzle and tail are sharp. By 2.0s = a 2600px-wide crop showing the whole panel, cords and the bright window behind. Ease-out, native resolution, motion starts on frame 1. Exact crop path in §10 row 1. |
| **Sound** | Shared music bed starts on frame 1. |
| **Product** | ✅ Frame 1. Name and breed in the first second; by 2.0s it reads as a hanging suncatcher. |
| **Why this framing** | §07 Hook 1 = "show the name on screen in the first second". The pull-out puts the name first and the object type second, inside 2s. |

### HOOK-H2 · relationship (variant)

| | |
|---|---|
| **On-screen text** | **We still leave the window open for him.** |
| **Caption timing** | 0.0–3.0s, one line (two if it wraps). 8 words over 3.0s. |
| **Visual** | **NEW** clip. The owner stands at an open window. The panel hangs in the window beside his face, backlit, sharp and **at least a third of the frame width**. Coloured light falls on his cheek. The name is not featured (that is Hook 1's job), but the black German Shepherd silhouette must be **unmistakable in frame 1**: crisp erect ears and long muzzle, dark against evenly glowing glass, never washed out by the backlight (council C2 #10). A cold viewer must read "a dog" before reading "a man". |
| **Camera** | Shot 1 of the clip only: slow push-in. Trimmed 0.0–2.0s. |
| **Sound** | Shared music bed from frame 1. |
| **Product** | ✅ Frame 1. A dog-silhouette stained-glass panel in a window, and a man looking past it. |
| **Why this framing** | §07 Hook 2 = name the relationship, not the name. The plan's §05 opening ("close-up of the owner standing still by the window") plus §09's rule that the gift must show within 3s. Putting the panel in the frame from the first frame satisfies both. |

The HOOK-H2 start-frame prompt, video prompt and QA are in §10 row 2 (single source, so the build list and the script cannot drift apart).

QA before animating (C2 #10 / build note Q7, do this first):
1. **Muted cold read.** Show frame 1 alone at phone size (about 360px wide) to someone who has not seen the script, sound off, for 2 seconds. Ask "is this about a dog?". Anything but an immediate yes means regenerate. Reading it as a man grieving a person is a fail.
2. **Measure** the panel's width on frame 1: at least 1/3 of 1080px (≥360px in the master).
3. **Silhouette:** both ears and the muzzle have a clean dark edge against the glass, with no bloom or flare eating into the outline.

Then: the panel matches the product (frame shape, corner spirals, dog facing left, heart cut-out). If the model wrote a name other than "Alex" on the silhouette (the `owner-v2` failure wrote "Allie"), paste the real "Alex" lettering (`ALEX-lettering.png`, §10 prep P1) in PIL, as was done for `F-BOX.png`. Hands: 5 + 5 at full resolution, no ring.

---

## 4. Shared body beats

### B3 · Name reveal, 6.0–12.0 (identical in all three concepts)

| Shot | Time | Len | Source | Camera | On-screen text | Sound |
|---|---|---|---|---|---|---|
| **B3a** | 6.0–9.0 | 3.0 | **REUSE** `tests/testC3-moving-open.mp4`, in-point 1.9s → 4.9s (sun through the panel, coloured light on the floor, push toward the German Shepherd shadow on the wall; passed QA, hook3 14.68) | push-in (as generated) | **Every afternoon, he's back on the wall.** | bed swells at 6.0 |
| **B3b** | 9.0–12.0 | 3.0 | **NEW still** `WALL-4K`: the German Shepherd shadow on the wall with the real "Alex" glowing inside it (steps below) | slow Ken Burns push-in toward "Alex" | **His breed. His name. In the light.** (9.0–12.0, 7 words) | bed |

Revision 2: the user confirmed the real 6" panel in direct sun throws a legible "Alex" and a recognisable German Shepherd shape on the wall (Q1 = YES), so the proof beat reads name + breed off the wall, as the plan's C1 role says.

Product rule: the name is never read off a generated video frame. Test F showed the typeface drifts in video, so the legible read is a 4K still with a Ken Burns move (script-method R22).

**WALL-4K**: built from testC3's last frame, with the real lettering.
1. Extract the frame (prep P3 in §10).
2. Nano Banana Pro edit, 4K, 9:16 (prompt in §10 row 4). Save the result unpasted as `WALL-4K-clean.png`: C1-B4 uses it as its shadow-outline reference, so that reference carries no lettering for the model to copy.
3. PIL: paste the real "Alex" script (`ALEX-lettering.png`) into the shadow in a soft warm glow (pale gold, 1–2px Gaussian blur, matched scale and angle), the same method used for `F-BOX.png`. Save as `WALL-4K.png`.
4. QA: the outline reads as a German Shepherd; read "Alex" by eye on at least 5 frames of the finished Ken Burns (R23).

### 4b · Shared ad-copy block (identical in all three concepts)

Each concept writes its own opening lines and headline (its copy concept slot). Everything from the bullets down is this block, byte for byte:

```
• his actual breed, in silhouette
• his name, set inside it
• hang it where the afternoon sun comes in — his shape lands on the wall

6 in · stained-glass-style panel · ready to hang

Make one that's only theirs.
```
**Description** (shared): `Choose the breed. Add the name.` · **Button:** Shop Now

No offer, shipping, delivery or arrival line (Revision 2, Q2: the offer is handled outside the creative). No line claims a gift note or shipping to the recipient.

### B5 · Close + CTA, 17.0–20.0 (identical in all three concepts)

| | |
|---|---|
| **Source** | **REUSE** `PANEL-4K` (`tests/testF-nanobananapro.png`) |
| **Camera** | Ken Burns **slow push-in**, opposite direction to HOOK-H1: start at a 2900px-wide crop (whole window, panel in the upper half) and end at a 2000px-wide crop on the panel. The last frame is still moving (R12). Exact crop path in §10 row 5. |
| **On-screen text** | **Make one that's only theirs** (17.2s on), with the small MadeJustForYou logo at the bottom-centre over the moving shot. No static end card. |
| **Sound** | Bed resolves on the last bar. |
| **Meta button** | Shop Now |

---

## 5. Cast: names every trait so captions and pictures agree

| Role | Who | Locked reference | Pronoun in captions |
|---|---|---|---|
| **Alex** | German Shepherd, male. Appears as the panel silhouette, its shadow and the name, plus **one** exception (Revision 1, C1 #5): in C1 beat 4 the owner holds a small framed photo of the living Alex (`ads/frames/F-PHOTO.png`). Never a living dog moving on screen in any beat. | product artwork; F-PHOTO for the photo | he / his / him |
| **Owner** | Man, about 70, light skin, wire-rimmed glasses, short grey beard, heavy grey brows, thinning grey hair swept back. Grey-green plaid flannel shirt over a white crew-neck tee, blue jeans, brown leather shoes. No ring. | `assets/turntable-owner/` (8 images) | he / his. The same man in **all three** concepts. |
| **Friend (C3 only)** | Woman, early 50s, light olive skin, dark brown chin-length bob with a side part, small gold stud earrings. Moss-green knit cardigan over a cream crew-neck top, dark trousers. | `ads/frames/giver-front-v1.png`, `giver-34L.png`, `giver-34R.png` | I / me (her captions are first person) |

Not usable in this build: `ads/frames/handoff2-v1.png` and `ads/shots/handoff.mp4` cast the owner as a silver-haired **woman**. These scripts use one owner, the man, across all three concepts, so that footage would contradict the "he" captions. `handoff2-v1.png` is used only as the composition base for C3 beat 4a, with the woman replaced.

**Shared pronoun/casting check (re-run, Revision 2).** Shared captions: H1 "his actual breed — and his name" sits on the dog silhouette; H2 "for him" is Alex (dog cue enforced by the muted QA, §3); B3a "he's back on the wall" and B3b "His breed. His name." have no person in frame; B5 has no pronoun. The shared copy block's "his" is always Alex. Revision 2 changed no shared caption. ✅

---

## 6. Craft spec (locked, all 6 ads)

| Field | Spec |
|---|---|
| Aspect / size | 9:16, 1080×1920 master |
| Length | 20.0s |
| Structure | A, beats as in §2 |
| Cut | Hard cuts only. Beat lengths 2.0 / 4.0 / 6.0 (3.0+3.0) / 5.0 / 3.0. Inside the concept slot, C3's beat 4 is 3.0+2.0 (Revision 1, C3 #5); the beat length is unchanged. |
| Voice | **Music bed, no voice.** One shared bed for all 6 ads: sparse solo piano, no percussion, starts on frame 1, lifts at 6.0s, resolves at 20.0s. **`products/suncatcher-dog-memorial/ads/shots/music.mp3`, approved by the user 2026-10-08.** |
| Grade | No imposed grade. The product already runs cool to warm. Beats before 6.0s are naturally cooler and flatter; the reveal brings the gold. |
| Captions | Burned in, US English, legible with sound off. White bold sans, ~64px cap height at 1080w, soft 30% black shadow, max 2 lines, centred. Keep inside the Reels safe zone: no text above 14% or below 65% of frame height, 6% side margins. Each caption holds at least 0.33s per word. |
| Logo | Beat 5 only, small, over moving footage |
| Generation | Seedance 2.0 i2v, 5s, 720p, no audio. Every clip is trimmed to its beat; the generated length is never the edit length. Stills via Nano Banana Pro (AtlasCloud `google/nano-banana-pro/edit`). |

## 7. Pre-shoot 3-second check (the hooks alone), re-run after Revision 2

Mute it, watch 0–3s, and ask whether you know what gift is being sold.

| Hook | 0–2.0s on its own | Pass? |
|---|---|---|
| H1 | ECU of a black German Shepherd silhouette with "Alex" in white script, pulling back to a stained-glass panel hanging on cords in a sunny window. Caption: "his actual breed — and his name." | ✅ A personalized dog-silhouette suncatcher with the dog's name. |
| H2 | A man at an open window. A stained-glass panel at least a third of the frame wide, with a crisp black German Shepherd silhouette (ears and muzzle sharp), hangs at his eye level, glowing, and coloured light falls on his face. Caption: "We still leave the window open for him." | ✅ A dog memorial suncatcher, **provided** the muted "is this about a dog?" QA in §3 passes on frame 1. The name and personalization are not yet shown; the object and the dog are. Build note (Q7): the council's cold read took "him" as a dead husband or son when the dog was not obvious; that QA is the gate. |

Revision 2 changed no hook picture or caption, so the hook-alone result is unchanged. The 2.0–3.0s second belongs to each concept's beat 2; each concept file confirms the product stays in frame there (all three re-run: ✅).

Read note (Q8): the concept is judged across the 3 products per plan §04, not on this product's 6 cells alone; don't call H1 vs H2 from one concept.

## 8. Asset status (whole build)

| ID | Used in | REUSE / NEW |
|---|---|---|
| `PANEL-4K` | H1, B5 | REUSE `tests/testF-nanobananapro.png` |
| `HOOK-H2` | H2 | NEW frame + clip |
| `B3a` | all | REUSE `tests/testC3-moving-open.mp4` |
| `WALL-4K` | B3b in all 6 ads; the clean (unpasted) version is C1-B4's shadow reference | NEW still (edit + PIL "Alex") |
| C1-B2 tag + empty bowl | C1 | NEW frame (+ PIL "ALEX" on the tag) + clip |
| C1-B4 photo beside the shadow | C1 | NEW frame (refs: owner, `C3-room-first.png`, `WALL-4K-clean`, F-PHOTO) + clip, 3 takes |
| C2-B2 face before, bed sharp | C2 | NEW two-pass edit of `owner-v1.png` (3 tries per pass) + clip |
| C2-B4 Alex's light in the bed | C2 | NEW edit **of the finished C2-B2 still** + clip, 3 takes |
| C3-B2 lowering it into the box | C3 | REUSE `ads/frames/F-BOX.png` + PIL handwritten card (still, Ken Burns pull-out) |
| C3-B4a hand-off | C3 | NEW single-subject edit of `handoff2-v1.png` + clip, 3 takes |
| C3-B4b open box in his hands | C3 | NEW still (edit + PIL "Alex"), Ken Burns |

New generation: 6 Seedance clips = 12 generations (1 take each for HOOK-H2, C1-B2 and C2-B2; 3 takes each for C1-B4, C2-B4 and C3-B4a), about $12. Stills: HOOK-H2, WALL-4K, C1-B2, C1-B4, C2-B2 (2 passes × 3 tries), C2-B4, C3-B4a, C3-B4b, about 13 calls, about $2. With a ~30% reshoot allowance, about **$18**.

---

## 9. Conflicts flagged: shared by all three concepts

Wherever the plan page conflicts with another source, the scripts follow the plan. Each concept file adds its own conflicts after these.

| ID | Conflict | What the scripts do |
|---|---|---|
| **S1** | **Structure A vs Hook 1.** In §05, structure A is "the first second is the recipient's face as they open the gift". §06/§07 Hook 1 is "show the name on screen in the first second". Both can't be true of frame 1. | H1 opens on the name (follows §07). H2 opens on the owner's face with the panel in frame, so only H2 also meets structure A. |
| **S2** | **§05 suncatcher example vs §09.** The example's 0–2s ("close-up of the owner standing still by the window") does not show the product, but §09 requires the gift to be identifiable within 3s. | H2 keeps the owner at the window and puts the panel in frame from frame 1. |
| **S3** | **Pacing.** The plan locks "~5s per scene". script-method R11 says vary shot length 2–5s and never use uniform 5s beats. | The plan's beat boundaries are kept exactly (2/4/6/5/3). Beat 3 is two 3.0s shots (one scene). Hard cuts throughout. |
| **S4** | **Proof choice.** §07 locks proof as "name + breed clearly visible" (rank 2), but §05 says cold traffic should lead with rank 1 (real reaction) or rank 3 (volume). | Rank 2 is used for all three concepts, as locked. |
| **S5** | **Hook caption length.** H1 is 12 words; 2s isn't enough for 12 words. | Both hook captions hold until 3.0s, running 1.0s into beat 2 (which has no caption before 3.0s in any concept). |
| **S6** | ~~Standard offer is not defined.~~ **Closed (Revision 2, Q2).** | The offer is handled outside the creative (plan Phase 2). No offer, shipping or delivery line in any video or primary text. |
| **S7** | **CTA wording.** R8 (MODERATE) prefers a create verb plus "today". The plan locks "Make one that's only theirs". | Locked CTA used unchanged. |
| **S8** | **Number of hooks.** The decomposition doc says at least 3 openers per concept. The plan hard-locks 2. | 2 hooks. |
| **S9** | **"Lonely giftee" house rule** vs C1 and C2, where the plan's own wording puts the owner alone on screen. | C1 beat 4 has him holding `F-PHOTO` (him hugging the living Alex) beside the shadow; C2 beat 4 lands Alex's light in Alex's own bed. The adult-child "second hand" variant (Q9) is **parked**. |
| **S10** | **Buyer list.** §05's buyer list has no "self / owner", yet §07 C3 implies C1/C2's buyer is the owner. | C1 buyer = the grieving owner buying for himself. C2 buyer = the owner, with a gifter bridge line in the primary text (Revision 2, Q6). C3 buyer = sympathy-giver. |
| **S11** | **Prior build is non-conformant.** `PHASE1-SUNCATCHER-shooting-scripts.md` (superseded) and `ads/out/S-C1.mp4` / `S-C6.mp4` changed the CTA, dropped C2 and H2, and cast a woman owner. | None of that is reused except the assets listed as REUSE above. |
| **S12** | **Compositing.** The topic README says "compositing engine removed", but these scripts need PIL pastes of real lettering (WALL-4K, C1-B2 tag, C3-B4b, HOOK-H2 if needed). | One-still PIL paste, the method already used for `F-BOX.png`. No perspective-warp engine. |

---

## 10. BUILD LIST (all 6 ads, every shot)

Run top to bottom. Nothing here has been generated yet.

### Conventions

- `P/` = `products/suncatcher-dog-memorial/`. New stills go to `P/ads/frames/phase1/`, new clips to `P/ads/shots/phase1/`. Create both folders first.
- **Stills:** AtlasCloud `atlas_generate_image`, model `google/nano-banana-pro/edit`, aspect 9:16, resolution as listed. Upload each local reference with `atlas_upload_media` first and pass the URLs **in the Image order given** (Image 1 = first URL). Check the param names with `atlas_get_model_info` once.
- **Videos:** Seedance 2.0 image-to-video, kie.ai `seedance_2_video`: `image_url` = the uploaded start frame (Image 1), `duration` 5, `resolution` "720p", `aspect_ratio` "9:16", `generate_audio` false, `fast` false. The prompt is the `prompt-video` block, sent as written. (Equivalent AtlasCloud Seedance 2.0 i2v is fine; look up its exact model id with `atlas_list_models`, never guess it.)
- **Prompt guard:** every `prompt-image` and `prompt-video` block below was run through `~/.claude/hooks/generation-prompt-guard.py` on 2026-10-08 and passes, except the one deliberate exception flagged in row 8.
- **Ken Burns** paths are in source pixels: `(cx, cy, crop_width)` start → end; crop height = width × 16/9; output 1080×1920 at 25fps, ease-out, motion from frame 1; render with `kb_segment()` in `P/ads/build_v2.py` (add the keys to its `KB` dict).
- **Captions** are burned in at assembly (shared spec, §6), never generated.
- **"Alex" read:** read it by eye at full size on at least 5 frames of any finished Ken Burns segment that shows it (R23).

### Prep (no generation)

| ID | Output | Command / step |
|---|---|---|
| P1 | `P/ads/frames/phase1/ALEX-lettering.png` | PIL: crop `P/assets/product-alex-german-shepherd.png` to box (970, 1185, 1105, 1255) (the white "Alex" script on the silhouette; check the box contains the whole word and widen by a few px if needed). Make an RGBA cut-out: alpha = luminance > 200, 1px feather. This is the only source of the name for every paste. |
| P2 | `P/ads/frames/phase1/C3-room-first.png` | `ffmpeg -ss 0.1 -i products/suncatcher-dog-memorial/tests/testC3-moving-open.mp4 -frames:v 1 products/suncatcher-dog-memorial/ads/frames/phase1/C3-room-first.png` |
| P3 | `P/ads/frames/phase1/C3-wall-last.png` | `ffmpeg -ss 4.8 -i products/suncatcher-dog-memorial/tests/testC3-moving-open.mp4 -frames:v 1 products/suncatcher-dog-memorial/ads/frames/phase1/C3-wall-last.png` |

### Shots

| # | Shot | Used in | Source | Duration / in-point | Post step |
|---|---|---|---|---|---|
| 1 | HOOK-H1 | S-C1-H1, S-C2-H1, S-C3-H1 | **REUSE** `products/suncatcher-dog-memorial/tests/testF-nanobananapro.png` | 2.0s Ken Burns | KB pull-out `(1480, 2820, 1300)` → `(1500, 2640, 2600)`. Check "Alex" ≈140px wide on frame 1. Caption per §3. |
| 2 | HOOK-H2 | S-C1-H2, S-C2-H2, S-C3-H2 | **NEW still** `P/ads/frames/phase1/H2-start.png` + **NEW video** `P/ads/shots/phase1/H2.mp4` (1 take) | in 0.0 → out 2.0 | §3 QA on the still before animating (muted cold read, panel ≥360px, crisp ears). PIL "Alex" (P1) only if the model wrote another name. |
| 3 | B3a | all 6 | **REUSE** `products/suncatcher-dog-memorial/tests/testC3-moving-open.mp4` | in 1.9 → out 4.9 (3.0s) | Upscale 720→1080 width at assembly. Caption "Every afternoon, he's back on the wall." |
| 4 | B3b | all 6 | **NEW still** `P/ads/frames/phase1/WALL-4K-clean.png` → `P/ads/frames/phase1/WALL-4K.png` | 3.0s Ken Burns | PIL: paste P1 into the shadow (pale-gold glow, 1–2px blur, matched scale/angle) → `WALL-4K.png`. KB slow push-in: start a 2600px-wide crop centred on the shadow, end a 1500px-wide crop centred on the pasted "Alex" (set both centres from the paste position). "Alex" ≥100px wide at the end crop. Read "Alex" on 5 frames. |
| 5 | B5 | all 6 | **REUSE** `products/suncatcher-dog-memorial/tests/testF-nanobananapro.png` | 3.0s Ken Burns | KB push-in `(1536, 2900, 2900)` → `(1500, 2640, 2000)`; last frame still moving. Caption "Make one that's only theirs" from 17.2s + small logo bottom-centre. |
| 6 | C1-B2 | S-C1-H1, S-C1-H2 | **NEW still** `P/ads/frames/phase1/C1-B2.png` (4K) + **NEW video** `P/ads/shots/phase1/C1-B2.mp4` (1 take) | in 0.0 → out 4.0 | PIL on the still **before** animating: engrave "ALEX" on the tag (capital serif, dark recessed fill, 1px warm highlight on the lower edge, ~40% of tag diameter, matched perspective) → animate the pasted still. Read "ALEX" at clip 0.0/0.5/1.0s. **Fallback** if the letters drift: KB vertical pan on the 4K still from the tag (bottom) to the panel (top), 4.0s. |
| 7 | C1-B4 | S-C1-H1, S-C1-H2 | **NEW still** `P/ads/frames/phase1/C1-B4.png` + **NEW video** `P/ads/shots/phase1/C1-B4-t{1,2,3}.mp4` (3 takes) | in 0.0 → out 5.0 | Pick the best take on the C1-B4 QA (C1 file). No lettering in frame. |
| 8 | C2-B2 | S-C2-H1, S-C2-H2 | **NEW still** pass 1 `P/ads/frames/phase1/C2-B2-p1.png` (3 tries) → pass 2 `P/ads/frames/phase1/C2-B2.png` (3 tries) + **NEW video** `P/ads/shots/phase1/C2-B2.mp4` (1 take) | in 0.0 → out 4.0 | ⚠️ **Guard exception:** Shot 1 is a fixed camera on purpose (council C2 #4, so B2 and B4 open on one framing), and the guard's `OPENMOVE` rule blocks it. kie.ai `seedance_2_video` has no `commandId` field to carry `ACK-OPENMOVE`, so tell the user before running it. If they decline, use the alternative prompt in row 8b, which keeps the framing at frame 1. |
| 9 | C2-B4 | S-C2-H1, S-C2-H2 | **NEW still** `P/ads/frames/phase1/C2-B4.png` (edit of `C2-B2.png`) + **NEW video** `P/ads/shots/phase1/C2-B4-t{1,2,3}.mp4` (3 takes) | in 0.0 → out 5.0 | Overlay the C2-B4 still on `C2-B2.png` at 50%: chair, window and bed must line up. Reach check on the still picks REACH-A or REACH-B prompt. |
| 10 | C3-B2 | S-C3-H1, S-C3-H2 | **REUSE** `products/suncatcher-dog-memorial/ads/frames/F-BOX.png` (kraft gift box, white tissue, her moss-green cuffs, real "Alex" already pasted) | 4.0s Ken Burns | PIL: add the friend's small cream handwritten card with a twine loop on the white tissue at the upper right of the box, about (2450, 1350), dark ink: "For you — and Alex.", matched to the tissue's angle and light → `P/ads/frames/phase1/F-BOX-card.png`. KB pull-out `(1628, 2968, 1300)` → `(1536, 2752, 2600)`. Check "Alex" is legible through clip 0.0–1.0s and the card reads at the end crop. |
| 11 | C3-B4a | S-C3-H1, S-C3-H2 | **NEW still** `P/ads/frames/phase1/C3-B4a.png` + **NEW video** `P/ads/shots/phase1/C3-B4a-t{1,2,3}.mp4` (3 takes) | in 0.0 → out 3.0 (slide later only if the window still opens with the box in his hands) | Box stays closed; no product in frame. |
| 12 | C3-B4b | S-C3-H1, S-C3-H2 | **NEW still** `P/ads/frames/phase1/C3-B4b.png` (4K) | 2.0s Ken Burns | PIL: paste P1 onto the silhouette over whatever the model wrote. KB slow push-in toward the panel; end crop chosen so "Alex" ≥100px wide in 1080 output. Read "Alex" on 5 frames. If QA fails: drop 4b and run C3-B4a 0.0–5.0 as one shot. |

**Counts:** 12 shots. **REUSE 4** (HOOK-H1, B3a, B5, C3-B2). **NEW stills 8** final stills (H2-start, WALL-4K, C1-B2, C1-B4, C2-B2 [2 passes], C2-B4, C3-B4a, C3-B4b) = about 13 still calls with tries. **NEW videos 6** clips (H2, C1-B2, C1-B4, C2-B2, C2-B4, C3-B4a) = 12 generations with takes. Plus 3 prep files (no generation).

**Order of work:** P1–P3 → stills for rows 2, 4, 6, 7 (needs `WALL-4K-clean`), 8, 11 → QA → row 9 still (needs `C2-B2.png`) and row 12 still (needs the chosen C3-B4a take's last frame) → all videos → QA → assembly with `music.mp3`.

### Row 2 · HOOK-H2

Still: Nano Banana Pro edit, 2K. Image 1 = `products/suncatcher-dog-memorial/assets/turntable-owner/owner-front.png`, Image 2 = `products/suncatcher-dog-memorial/assets/turntable-owner/owner-34left.png`, Image 3 = `products/suncatcher-dog-memorial/assets/turntable-owner/owner-34right.png` (character), Image 4 = `products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png` (exact product).

```prompt-image
Use Images 1, 2 and 3 as the character reference for this man; keep his wire-rimmed glasses, short grey beard, heavy brows, thinning grey hair swept back, and grey-green plaid flannel shirt over a white tee identical. Use Image 4 as the exact product, front face toward camera, its black frame, stained-glass artwork and seated dog silhouette unchanged. Waist-up medium shot, vertical 9:16: he stands at a tall living-room window with the lower sash raised open, a thin white curtain edge at the right of frame. The product hangs on a dark cord inside the window at the left third of the frame, at his eye level, filling a full third of the frame width. Low sun comes from the upper right of the window, so the glass glows evenly in blues and golds and the black seated German Shepherd silhouette stands out dark and crisp against it, its two erect pointed ears and long muzzle sharply outlined. He stands at the right third, body turned three-quarters toward the window. His left hand rests flat on the window sill and his right arm hangs relaxed, the hand resting against the side of his right thigh. He looks out through the open window past the product, lips closed, eyes open and soft. A faint band of blue and gold light falls across his left cheek. Late-afternoon sun, warm interior. Shot on a 35mm lens at f/5.6 so his face and the product are both in focus, natural colour, photographic realism.
```

Video: Image 1 = `P/ads/frames/phase1/H2-start.png`.

```prompt-video
Use @Image 1 as the first frame.
Define the man with the grey beard, wire-rimmed glasses and green plaid flannel shirt in @Image 1 as <Owner>.
Define the black-framed stained-glass panel with the dog silhouette hanging in the window in @Image 1 as <Panel>.

Shot 1: Slow push-in toward <Owner> and <Panel>. The thin white curtain at the right edge stirs in a
light breeze. <Owner> stays at the window, looking out past <Panel>.
Shot 2: Fixed medium framing. <Owner> lowers his gaze slightly toward <Panel>, and his shoulders drop
as he lets out a long breath. His left hand stays flat on the window sill.

（solo piano, sparse, no percussion）

<Owner>'s face, glasses, beard and clothing remain exactly as in @Image 1, unchanged throughout.
<Panel> hangs still on its cord; its frame, artwork and the seated dog silhouette remain exactly as in
@Image 1. His eyes stay open. Hands have five fingers each, correctly formed.
Movements are continuous and natural, no stutter or flicker.
```

### Row 4 · WALL-4K (B3b)

Still: Nano Banana Pro edit, **4K**. Image 1 = `P/ads/frames/phase1/C3-wall-last.png` (composition), Image 2 = `products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png` (shadow shape).

```prompt-image
Recreate Image 1 at higher resolution. Use Image 1 as the composition reference and keep the wall, the window light and the dog-shaped shadow exactly the same. Use Image 2 as the shape structure reference for the shadow: a seated German Shepherd facing left, two erect pointed ears, long muzzle, bushy tail curled at its base, the small heart cut-out at the shoulder and the floral sprigs on the lower body.
```

Save the output as `WALL-4K-clean.png`; then the PIL paste (row 4 post) makes `WALL-4K.png`.

### Row 6 · C1-B2

Still: Nano Banana Pro edit, **4K**. Image 1 = `P/ads/frames/phase1/C3-room-first.png` (room), Image 2 = `products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png` (exact product).

```prompt-image
Use Image 1 as the room and background reference: the same window, wooden floorboards, pale wall and grey round dog bed. Use Image 2 as the exact product, hanging on a dark cord in the window, front face toward the room. Low-angle close shot at floor level, vertical 9:16. In the sharp foreground a brown leather leash lies coiled on the floorboards, with a small round polished brass tag hanging from its clip, the tag's smooth flat face turned toward camera, about a fifth of the frame width. Just behind the leash sits an empty, dry stainless-steel dog bowl. Behind the bowl the grey round dog bed sits empty against the wall. The window fills the top quarter of the frame with the product from Image 2 hanging in it, small and softly out of focus, its black seated-dog silhouette still readable. Soft, even, overcast cool daylight; the floor and the wall are evenly lit in flat grey-blue tones. Shot on a 35mm lens at f/4, focus on the tag, natural colour, photographic realism.
```

Video: Image 1 = `P/ads/frames/phase1/C1-B2.png` **after** the PIL "ALEX" engraving.

```prompt-video
Use @Image 1 as the first frame.
Define the small brass tag engraved ALEX on the coiled leather leash in @Image 1 as <Tag>.
Define the black-framed panel with the dog silhouette hanging in the window in @Image 1 as <Panel>.

Shot 1: Slow tilt up from <Tag> and the empty bowl to the window and <Panel>. The leash, the bowl
and the empty dog bed lie still.

（solo piano, sparse, no percussion）

The letters ALEX on <Tag> stay exactly as in @Image 1.
<Panel> hangs still; its frame, artwork and seated dog silhouette remain exactly as in @Image 1.
The light stays soft, even and cool throughout.
Movements are continuous and natural, no stutter or flicker.
```

### Row 7 · C1-B4

Still: Nano Banana Pro edit, 2K. Image 1 = `products/suncatcher-dog-memorial/assets/turntable-owner/owner-front.png`, Image 2 = `products/suncatcher-dog-memorial/assets/turntable-owner/owner-34left.png`, Image 3 = `products/suncatcher-dog-memorial/assets/turntable-owner/owner-34right.png` (character), Image 4 = `P/ads/frames/phase1/C3-room-first.png` (room and scale), Image 5 = `P/ads/frames/phase1/WALL-4K-clean.png` (shadow outline; the unpasted version, so there is no lettering to copy), Image 6 = `products/suncatcher-dog-memorial/ads/frames/F-PHOTO.png` (the framed photo he holds).

```prompt-image
Use Images 1, 2 and 3 as the character reference for this man; keep his thinning grey hair swept back, short grey beard, wire-rimmed glasses and grey-green plaid flannel shirt over a white tee identical. Use Image 4 as the room and background reference: the same pale wall, wooden floorboards and window. Use Image 5 as the exact shape structure of the seated German Shepherd shadow on the wall. Use Image 6 as the exact framed photo he holds. Medium shot from just behind his left shoulder, vertical 9:16: he sits on the front edge of a beige armchair beside the wall and leans forward toward it, seen three-quarters from behind so his ear, the arm of his glasses and the edge of his beard show. The shadow on the wall is about knee height. His right hand holds the framed photo by its lower edge at chest height, a hand's width below and to the left of the shadow's muzzle, on the plain shaded part of the wall, the picture turned toward camera and the back of his hand toward camera. His left forearm rests on his left thigh, the hand relaxed over his knee. Low late-afternoon sun from the window at the right of frame throws the blue and gold light and the shadow onto the wall. Shot on a 35mm lens, shallow depth of field, focus on the photo and the shadow, photographic realism.
```

Video: Image 1 = `P/ads/frames/phase1/C1-B4.png`. 3 takes.

```prompt-video
Use @Image 1 as the first frame.
Define the man with grey hair, wire-rimmed glasses and green plaid flannel shirt in @Image 1 as <Owner>.
Define the dog-shaped shadow on the wall in @Image 1 as <Shadow>.
Define the small oak-framed photo in <Owner>'s right hand in @Image 1 as <Photo>.

Shot 1: Slow push-in toward <Photo> and <Shadow>'s head. <Owner> slowly raises his right hand until
<Photo> sits level with <Shadow>'s head, just to the left of its muzzle, the back of his hand toward
camera. His head tilts slightly toward the wall.

（solo piano, warming, no percussion）

<Shadow>'s outline, ears and heart cut-out do not change, and it stays in place on the wall.
<Photo>'s frame and picture remain exactly as in @Image 1.
<Owner>'s hair, glasses, beard and clothing remain exactly as in @Image 1; his face stays turned away
three-quarters. His right hand has five fingers, correctly formed, and his palm never faces the camera.
Movements are continuous and natural, no stutter or flicker.
```

### Row 8 · C2-B2

Pass 1 still: Nano Banana Pro edit, 2K, 3 tries. Image 1 = `products/suncatcher-dog-memorial/ads/frames/owner-v1.png` (composition).

```prompt-image
Edit Image 1, using it as the composition reference. Relight the whole scene with soft, even, overcast daylight, so his face and skin are evenly lit in natural tones. The panel in the window keeps a faint, muted glow of blue and gold. Keep the man, his pose, his glasses, beard and plaid flannel shirt, his right hand resting on the armrest, the armchair, the window and the hanging panel exactly the same.
```

Pass 2 still: Nano Banana Pro edit, 2K, 3 tries. Image 1 = the chosen `P/ads/frames/phase1/C2-B2-p1.png` (composition).

```prompt-image
Edit Image 1, using it as the composition reference. Add an empty grey round dog bed on the wooden floor at the lower left of frame, beside the armchair, fully in frame and in sharp focus. Keep everything else exactly the same.
```

Video: Image 1 = `P/ads/frames/phase1/C2-B2.png`. Row 8a (as approved by the council; needs the OPENMOVE exception):

```prompt-video
Use @Image 1 as the first frame.
Define the man with the grey beard, wire-rimmed glasses and green plaid flannel shirt in @Image 1 as <Owner>.
Define the empty grey round dog bed on the floor in @Image 1 as <Bed>.
Define the black-framed panel with the dog silhouette hanging in the window in @Image 1 as <Panel>.

Shot 1: Fixed camera, medium-close framing. <Owner> sits in the armchair, his right hand resting on the
armrest, and slowly lowers his gaze down and to his right toward <Bed>, then slowly lifts it back up
to the window and <Panel>.

（solo piano, sparse, no percussion）

<Owner>'s face, glasses, beard and body proportions remain exactly as in @Image 1, unchanged throughout.
<Bed> stays in place and in focus. <Panel> hangs still; its frame, artwork and seated dog silhouette
remain exactly as in @Image 1. His eyes stay open. His right hand stays on the armrest and has five
fingers, correctly formed. Movements are continuous and natural, no stutter or flicker.
```

Row 8b (guard-clean alternative, only if the user declines the exception; frame 1 still equals the B4 start framing, and B3 sits between B2 and B4 in the cut, so the match holds):

```prompt-video
Use @Image 1 as the first frame.
Define the man with the grey beard, wire-rimmed glasses and green plaid flannel shirt in @Image 1 as <Owner>.
Define the empty grey round dog bed on the floor in @Image 1 as <Bed>.
Define the black-framed panel with the dog silhouette hanging in the window in @Image 1 as <Panel>.

Shot 1: Very slow, slight push-in toward <Owner>. <Owner> sits in the armchair, his right hand resting
on the armrest, and slowly lowers his gaze down and to his right toward <Bed>, then slowly lifts it
back up to the window and <Panel>.

（solo piano, sparse, no percussion）

<Owner>'s face, glasses, beard and body proportions remain exactly as in @Image 1, unchanged throughout.
<Bed> stays in place and in focus. <Panel> hangs still; its frame, artwork and seated dog silhouette
remain exactly as in @Image 1. His eyes stay open. His right hand stays on the armrest and has five
fingers, correctly formed. Movements are continuous and natural, no stutter or flicker.
```

### Row 9 · C2-B4

Still: Nano Banana Pro edit, 2K. Image 1 = `P/ads/frames/phase1/C2-B2.png` (composition), Image 2 = `products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png` (outline of the light patch).

```prompt-image
Edit Image 1, using it as the composition reference. Use Image 2 as the shape structure reference for the light patch. Change the light to low gold late-afternoon sun coming through the panel in the window behind him. Lay a band of blue and gold light from the panel across his left cheek and glasses. Lay a soft patch of blue and gold light inside the empty dog bed, shaped like the seated German Shepherd in Image 2, with two erect pointed ears and a long muzzle, plain coloured light with a soft edge. Keep the man, his pose, his right hand on the armrest, the armchair, the bed, the window and the panel exactly the same.
```

Reach check on this still: can his right hand reach the bed rim without leaving the frame or crossing his body? Yes → REACH-A. No → REACH-B (expected, since in `owner-v1` the hand is on the frame-right armrest and the bed is at frame-left).

Video: Image 1 = `P/ads/frames/phase1/C2-B4.png`. 3 takes. REACH-B (default):

```prompt-video
Use @Image 1 as the first frame.
Define the man with the grey beard, wire-rimmed glasses and green plaid flannel shirt in @Image 1 as <Owner>.
Define the empty grey round dog bed with the patch of coloured light in it in @Image 1 as <Bed>.
Define the black-framed panel with the dog silhouette hanging in the window in @Image 1 as <Panel>.

Shot 1: Slow, slight push-in that keeps <Owner>'s face and <Bed> in frame. The coloured light from
<Panel> slowly brightens and warms. <Owner> slowly lowers his gaze to <Bed>, lets out a long breath,
and his shoulders drop. His right hand stays resting on the armrest.

（solo piano, swelling gently）

<Owner>'s face, glasses, beard and body proportions remain exactly as in @Image 1, unchanged throughout.
His eyes stay open. The patch of light in <Bed> keeps its shape and place.
<Panel> hangs still; its frame, artwork and seated dog silhouette remain exactly as in @Image 1.
His right hand has five fingers, correctly formed, and his palm never faces the camera.
Movements are continuous and natural, no stutter or flicker.
```

REACH-A: the same prompt with the sentence "His right hand stays resting on the armrest." replaced by "His right hand slides off the armrest and comes to rest on the rim of <Bed>, the back of his hand toward camera."

### Row 11 · C3-B4a

Still: Nano Banana Pro edit, 2K. Image 1 = `products/suncatcher-dog-memorial/ads/frames/handoff2-v1.png` (composition, and the woman in the foreground), Image 2 = `products/suncatcher-dog-memorial/assets/turntable-owner/owner-front.png`, Image 3 = `products/suncatcher-dog-memorial/assets/turntable-owner/owner-34left.png`, Image 4 = `products/suncatcher-dog-memorial/assets/turntable-owner/owner-34right.png` (character: the man who replaces the woman in the doorway).

```prompt-image
Edit Image 1, using it as the composition reference. Replace the silver-haired woman in the doorway with the man from Images 2, 3 and 4, used as the character reference; keep his wire-rimmed glasses, short grey beard, heavy grey brows, thinning grey hair swept back, and grey-green plaid flannel shirt over a white tee identical. He stands in the doorway holding the closed kraft gift box tied with twine with both hands from below at chest height, his eyes lowered to the box, lips pressed together. The woman in the foreground keeps her right hand resting lightly on the near edge of the box. Keep the woman, her hair and green cardigan, the doorway, the light and the box exactly the same.
```

Video: Image 1 = `P/ads/frames/phase1/C3-B4a.png`. 3 takes.

```prompt-video
Use @Image 1 as the first frame.
Define the man with the grey beard, wire-rimmed glasses and green plaid flannel shirt in the doorway in @Image 1 as <Owner>.
Define the woman with the dark bob and moss-green cardigan in the foreground in @Image 1 as <Friend>.
Define the closed kraft gift box tied with twine in @Image 1 as <Box>.

Shot 1: Slow push-in past <Friend>'s shoulder toward <Owner>. <Friend>'s right hand lifts away from
<Box> and lowers to her side. <Owner> slowly draws <Box> in against his chest with both hands, lets
out a long breath, then lifts his eyes to <Friend>, and a faint closed-mouth smile appears.

（solo piano, warming）

<Owner>'s and <Friend>'s faces, hair and clothing remain exactly as in @Image 1, unchanged throughout.
<Box> stays closed and keeps its shape and twine bow. His eyes stay open.
Hands have five fingers each, correctly formed. Movements are continuous and natural, no stutter or flicker.
```

### Row 12 · C3-B4b

Prep: `ffmpeg -sseof -0.05 -i products/suncatcher-dog-memorial/ads/shots/phase1/C3-B4a-tN.mp4 -frames:v 1 products/suncatcher-dog-memorial/ads/frames/phase1/C3-B4a-last.png` (N = the chosen take).

Still: Nano Banana Pro edit, **4K**. Image 1 = `P/ads/frames/phase1/C3-B4a-last.png` (character and lighting), Image 2 = `products/suncatcher-dog-memorial/assets/product-alex-german-shepherd.png` (exact product), Image 3 = `products/suncatcher-dog-memorial/ads/frames/F-BOX.png` (texture and colour of the kraft gift box and white tissue).

```prompt-image
Use Image 1 as the character and lighting reference: the same man, his grey beard and grey-green plaid flannel shirt, and the same warm doorway light. Use Image 2 as the exact product: its black frame, stained-glass artwork and seated dog silhouette unchanged. Use Image 3 as the texture and colour reference for the kraft gift box and white tissue. Close shot, vertical 9:16, framed from his beard down to his waist: he holds the open kraft gift box in both hands at chest height, his thumbs on the box's near rim and his fingers under its base, the lid tipped back against his left forearm. The product from Image 2 lies face up on white tissue inside the box, front face toward camera, filling about half the frame width. Warm late-afternoon light from camera left. Shot on a 50mm lens, shallow depth of field, focus on the product, photographic realism.
```
