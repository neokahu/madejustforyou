> ⛔ **SUPERSEDED 2026-10-08 — do not build from this file.** It deviated from the approved plan
> (https://testing-plan-phase-1.namvu47.workers.dev): dropped concept C2 and the hook pair, changed the locked CTA.
> The plan-conformant scripts are in `marketing/facebook-ads/suncatcher-phase1/` (C1 / C2 / C3 × Hook 1 / Hook 2),
> written by the screenwriter agent and reviewed by LLM council per case. Kept only as a record of the deviation.

# Phase-1 Shooting Scripts v2 + Ad Copy — Dog Memorial Suncatcher

> Product: **6 IN · German Shepherd · "Alex"** — $26.95 · GP $22.34 · BE ROAS 1.21× · target CPA $15.64
> Rules: `research/reference/script-method.md` · prompts: `seedance-prompt-method.md`, `image-prompt-method.md`
> Decision record: LLM council 2026-10-08 — `research/councils/council-transcript-2026-10-08-suncatcher-script.md`
> v1 (6 ads = 3 bodies × 2 hooks, Hook 2 product-absent) is in git history. **Superseded.**

## What changed from v1, and why

| v1 | v2 | Why |
|---|---|---|
| 6 ads (3 bodies × 2 hooks) | **3 ads: 2 videos + 1 static** | At $15.64 CPA, 6 cells need ~$300 before any reads. |
| Hook 2 opens on an empty window | **Cut.** Every ad shows the panel, name legible, in frame 1 | R1 (STRONG). Council: unanimous. A late-reveal test (T1) waits for a converting control. |
| Body C one of three | **Body C leads** (S-C6) | Only body that shows the buyer's moment. |
| Bodies A + B: man alone | A becomes the product-hero cut (S-C1), anchored by the photo of him *with* Alex. B parked. | R17 lonely-giftee rule. |
| Uniform 5s beats, crossfades | **Varied 1.8–4.6s shots, hard cuts** | R11. MJ4U-111 lost on this. |
| Frozen end card | CTA + small logo **over a moving panel shot** | R12. |
| CTA "Make one that's only theirs" | **"Make their dog's suncatcher"** | Names the object (council, Outsider). |
| Owner in "grey sweater" | **Grey-green plaid flannel over white tee** | Matches the locked REF-OWNER set. |
| testE3 owner shot | **Reshoot** with our real panel in the start frame | testE3 invented a church window = model drew the product. |

Checkout is verified working (real orders, 2026-10-08), so these ads are read on add-to-cart **and** purchase.

**Locked across both videos:** 20s · 9:16 · music bed, no VO · burned captions (sound-off legible, inside Reels safe zone) · product on screen by 1s · hard cuts · Meta button **Shop Now** · copy states delivery time.

---

## Assets — what exists, what gets made

| ID | What | Method | State |
|---|---|---|---|
| `PANEL-4K` | Nano Banana Pro 4K still, panel in a sunlit window, "Alex" correct | `tests/testF-nanobananapro.png` | ✅ have |
| `WALL` | Panel in window → coloured light → German Shepherd shadow on wall, 2 named shots | `tests/testC3-moving-open.mp4` (hook3 14.68) | ✅ have |
| `REF-OWNER` | 8-image set | `assets/turntable-owner/` | ✅ fixed 2026-10-08 |
| `REF-ALEX-PHOTO` | Owner + living German Shepherd | `assets/REF-ALEX-PHOTO.png` | ✅ have |
| `REF-GIVER` | The friend: front + ¾L + ¾R | Nano Banana Pro | 🔨 make |
| `F-PHONE`, `F-FLORIST`, `F-HANDOFF`, `F-OWNER` | Video start frames | Nano Banana Pro, refs assigned roles | 🔨 make |
| `F-BOX`, `F-PHOTO` | Stills for Ken Burns (rigid product text = still, R22) | Nano Banana Pro | 🔨 make |

**REF-GIVER:** a woman in her early 50s, light olive skin, dark brown chin-length bob, small gold stud
earrings, moss-green knit cardigan over a cream top. Distinct from the owner at a glance (colour, hair, gender).

---

# AD 1 · S-C6 · "What to send" — the buyer is the friend (LEAD)

| # | Time | Len | Shot | Camera | On-screen text | Sound | Product |
|---|---|---|---|---|---|---|---|
| 1 | 0.0–1.8 | 1.8 | `PANEL-4K` Ken Burns, frame 1 = whole panel, "Alex" legible | push-in | **Her dog died on Tuesday.** | piano starts frame 1 | ✅ hero |
| 2 | 1.8–4.4 | 2.6 | Friend at her kitchen table reads her phone, goes still, lowers it | slow push-in | I didn't know what to send. | piano | — |
| 3 | 4.4–7.2 | 2.8 | Florist buckets: she reaches toward the flowers, stops, lowers her hand | lateral track | Flowers felt wrong. They die too. | piano | — (1 beat away) |
| 4 | 7.2–11.0 | 3.8 | `F-BOX` her hands (green cardigan cuffs) hold the panel above tissue in a kraft box | Ken Burns push to the name | So I sent him. His breed. His name. | piano lifts | ✅ name read |
| 5 | 11.2–14.6 | 3.4 | Over her shoulder at the owner's door: **the grieving owner (a woman, silver hair) hugs the box**; the friend's hand rests on her arm; tears → faint smile | slow push-in | — | piano | box |
| 6 | 13.4–16.6 | 3.2 | `WALL` shot 2: push to the German Shepherd shadow on the wall | push-in | Now the room goes gold at four o'clock. | swell | ✅ payoff |
| 7 | 16.6–20.0 | 3.4 | `PANEL-4K` Ken Burns, different crop, moving | push-in | **Make their dog's suncatcher** + small logo | resolve | ✅ CTA |

Shot lengths (rev. 2026-10-08): 1.8 / 2.4 / 2.6 / 3.6 / 3.4 / 2.8 / 3.4. Hand-off payoff at 11.2s = 56%.
**Owner in S-C6 is a woman** ("her dog"). The plaid-shirt man is S-C1's owner only — an earlier hands-only hand-off used his cuffs and read as "the owner giving a gift to another man" (user, 2026-10-08). Story-film taste lives in beats 4–6, not the open.
Connection (R17): beat 5 shows giver → receiver. Grandma/age rules N/A. Policy (R6): all third/first person.

### Prompts

**REF-GIVER front** — Nano Banana Pro, 2K, 3:4, text-to-image:
> Photograph a woman in her early 50s with light olive skin, a dark brown chin-length bob with a side part, and small gold stud earrings. She wears a moss-green knit cardigan over a cream crew-neck top. Head and shoulders, facing camera, eye level, calm neutral expression with lips closed. Her arms rest at her sides, hands below the frame against her hips. Plain warm-grey wall behind her. Soft window light from camera left. Shot on a 50mm lens, shallow depth of field, natural colour, photographic realism.

**REF-GIVER ¾ left / ¾ right** — Image 1 = front as character reference:
> Use Image 1 as the character reference for this woman. Keep her face, chin-length dark bob, gold stud earrings, moss-green knit cardigan and cream top identical. Three-quarter view, head turned 35 degrees to her [left/right], eyes toward the same direction. Her arms rest at her sides, hands below the frame against her hips. Plain warm-grey wall. Soft window light from camera left. 50mm lens, shallow depth of field, photographic realism.

**F-PHONE** (9:16) — Images 1–3 = character:
> Use Images 1, 2 and 3 as the character reference for this woman; keep her face, hair, earrings and moss-green cardigan identical. Medium shot: she sits at a small wooden kitchen table in morning light, holding a phone in both hands at chest height, screen facing her and away from camera, elbows resting on the table. A mug of coffee sits by her right elbow. Soft morning window light from camera right, muted cool tones. 35mm lens, shallow depth of field, photographic realism.

**F-PHONE → video** (Seedance 2.0 i2v, 5s, 720p, no audio):
```
Use @Image 1 as the first frame.
Define the woman with the dark bob and moss-green cardigan in @Image 1 as <Giver>.

Shot 1: Slow push-in toward <Giver>. <Giver> reads the phone held in both hands, then goes still.
Shot 2: Fixed medium framing. <Giver> slowly lowers the phone flat onto the table, both hands staying
on it, and her head tilts forward slightly. Her eyes stay open.

（solo piano, single sustained note）

<Giver>'s face, hair and body proportions remain exactly as in @Image 1, unchanged throughout.
Her hands have five fingers each, correctly formed. The phone screen faces away from camera throughout.
Movements are continuous and natural, no stutter or flicker.
```

**F-FLORIST** (9:16) — Images 1–3 = character:
> Use Images 1, 2 and 3 as the character reference; keep her face, hair, earrings and moss-green cardigan identical. Medium shot inside a small flower shop: she stands in front of galvanised buckets of mixed flowers, her right hand raised halfway toward a bunch of white lilies, fingers open, not yet touching. Her left hand rests at her side against her thigh. Soft daylight from the shop window behind camera. 35mm lens, shallow depth of field, photographic realism.

**F-FLORIST → video:**
```
Use @Image 1 as the first frame.
Define the woman with the dark bob and moss-green cardigan in @Image 1 as <Giver>.

Shot 1: Smooth lateral track past the flower buckets toward <Giver>. <Giver>'s raised right hand
stops short of the lilies.
Shot 2: Slow push-in on <Giver>. She lowers her right hand slowly back to her side and shakes her
head once, very slightly. Her eyes stay on the flowers.

（solo piano, sparse）

<Giver>'s face, hair and body proportions remain exactly as in @Image 1, unchanged throughout.
Her hands have five fingers each, correctly formed. The flowers stay in their buckets.
Movements are continuous and natural, no stutter or flicker.
```

**F-BOX** (still, 9:16, 4K) — Image 1 = product, Image 2 = character (sleeves only):
> Using Image 1 as the exact product and Image 2 for the woman's moss-green cardigan sleeves: overhead close-up of an open kraft gift box lined with white tissue paper on a wooden table. Her two hands, in moss-green knit cuffs, hold the product from Image 1 by its left and right edges, lifted slightly above the tissue, front face toward camera and fully visible. Thumbs on the front edge of the black frame, fingers behind it. Soft window light from the top left. 50mm lens, natural colour, photographic realism.

**F-HANDOFF** (9:16) — Images 1–3 = the friend (REF-GIVER):
> Use Images 1, 2 and 3 as the character reference for the woman with the dark chin-length bob and moss-green knit cardigan; keep her hair and cardigan identical. Over-the-shoulder shot from just behind her left shoulder at an open front door: the back of her head and her shoulder fill the left foreground, softly out of focus. Both of her hands hold out a closed kraft gift box tied with twine toward a woman in her mid-60s standing in the doorway, with short silver hair, light skin, a soft dusty-blue cardigan and a pearl stud in each ear. The older woman's two hands are on the sides of the box from below, receiving it, her eyes lowered to the box, lips pressed together, eyes glistening. Warm late-afternoon light falls on the older woman's face from camera left. 50mm lens, shallow depth of field, photographic realism.

**F-HANDOFF → video:**
```
Use @Image 1 as the first frame.
Define the silver-haired woman in the dusty-blue cardigan in the doorway in @Image 1 as <Owner>.
Define the woman with the dark bob and moss-green cardigan in the foreground in @Image 1 as <Friend>.
Define the kraft gift box tied with twine in @Image 1 as <Box>.

Shot 1: Slow push-in past <Friend>'s shoulder toward <Owner>. <Owner> takes <Box> into both hands and
slowly draws it in against her chest. <Friend>'s hands release <Box>.
Shot 2: Fixed medium-close framing on <Owner>. <Friend>'s right hand rests gently on <Owner>'s forearm.
<Owner> lets out a long breath, her shoulders relax, and a faint smile appears while her eyes stay wet.

（solo piano, warming）

<Owner>'s and <Friend>'s faces, hair and clothing remain exactly as in @Image 1, unchanged throughout.
<Box> keeps its shape and twine bow. Hands have five fingers each, correctly formed.
Movements are continuous and natural, no stutter or flicker.
```

---

# AD 2 · S-C1 · "His breed. His name." — product hero

| # | Time | Len | Shot | Camera | On-screen text | Product |
|---|---|---|---|---|---|---|
| 1 | 0.0–2.0 | 2.0 | `PANEL-4K` Ken Burns, "Alex" legible frame 1 | push-in | **Made with his breed. And his name.** | ✅ |
| 2 | 2.0–4.6 | 2.6 | `WALL` shot 1: lateral track, coloured light on the floor | lateral | Hang it where the afternoon sun comes in | ✅ |
| 3 | 4.6–7.6 | 3.0 | `WALL` shot 2: push to the shadow on the wall | push-in | and his shape lands on the wall. | ✅ |
| 4 | 7.6–11.2 | 3.6 | `F-PHOTO` the owner with Alex, framed, coloured light across the glass | Ken Burns | Choose the breed. Add the name. | — (prop) |
| 5 | 11.2–15.8 | 4.6 | `F-OWNER` the owner in the armchair, our panel in the window behind him, hand rising into the band of light | slow push-in | Every afternoon at four. | ✅ in frame |
| 6 | 15.8–20.0 | 4.2 | `PANEL-4K` Ken Burns, moving | push-in | **Make their dog's suncatcher** + small logo | ✅ CTA |

Connection: beat 4 (him with living Alex) keeps beat 5 from reading as a man alone.

**F-PHOTO** (still, 9:16) — Image 1 = the photograph:
> Using Image 1 as the exact photograph: place it in a simple oak picture frame standing on a white-painted windowsill. A band of blue and gold light from a coloured-glass panel off-screen above falls diagonally across the frame's glass. Close-up, frame filling two-thirds of the image, slightly angled. Soft late-afternoon light. 50mm lens, shallow depth of field, photographic realism.

**F-OWNER** (9:16) — Images 1–2 = character, Image 3 = product:
> Use Images 1 and 2 as the character reference for this man; keep his wire-rimmed glasses, short grey beard, thinning grey hair, and grey-green plaid flannel shirt over a white tee identical. Use Image 3 as the exact product: it hangs on a cord in the window behind him at the left of frame, small, front face toward camera. Medium shot: he sits in a beige armchair beside the window, both forearms on the armrests, hands resting on the armrest ends. A band of blue and gold light from the product falls across his left cheek. Late-afternoon sun, wooden floor. 35mm lens, shallow depth of field, photographic realism.

**F-OWNER → video:**
```
Use @Image 1 as the first frame.
Define the man with the grey beard, wire-rimmed glasses and green plaid flannel shirt in @Image 1 as <Owner>.
Define the coloured-glass panel hanging in the window in @Image 1 as <Panel>.

Shot 1: Slow push-in toward <Owner>. The band of blue and gold light from <Panel> moves slowly
across his cheek.
Shot 2: Fixed medium-close framing. <Owner> raises his right hand from the armrest to beside his
own cheek, palm turned away from camera toward the window, so the coloured band falls across the
back of his hand. His shoulders drop as he lets out a long breath.

（solo piano, sparse, no percussion）

<Owner>'s face, glasses, beard and body proportions remain exactly as in @Image 1, unchanged
throughout. <Panel> geometry and artwork remain exactly as in @Image 1; it hangs still. His palm
never faces the camera. His eyes stay open. Hands have five fingers each, correctly formed.
Movements are continuous and natural, no stutter or flicker.
```

---

# AD 3 · S-STATIC — baseline image ad (4:5, 1080×1350)

`PANEL-4K` cropped to the panel + window light, headline set in PIL on a dark band at the bottom:
**His breed. His name. In the light.** · sub-line *Personalized memorial suncatcher · 6 in* · small logo.
Zero generation cost. It tells us whether the product sells before the film does any work.

---

# Ad copy

Line breaks and bullets are mandatory (`engine/upload_draft.py` enforces it). Every line first or third person.
Delivery: **made to order, ships in 3–5 days** — confirm the arrival window on the product page matches before upload.

## S-C6 · What to send
**Primary text**
```
Her dog died on Tuesday. I didn't know what to send.

Flowers felt wrong — they die too.

So I sent her this:
• his breed, cut in silhouette
• his name, inside it
• made to hang in the window he used to sit by

She says the room goes gold at four o'clock now.

Made to order · ships in 3–5 days.
```
**Headline:** `What to send when flowers feel wrong` · **Description:** `Choose the breed, add the name.` · **Button:** Shop Now

## S-C1 · His breed. His name.
**Primary text**
```
Not a clipart dog. His breed — and his name.

Hang it where the afternoon sun comes in:
• the room fills with blue and gold
• his shape lands on the wall
• his name sits inside it

6 inches · ready to hang
Made to order · ships in 3–5 days.
```
**Headline:** `His breed. His name. In the light.` · **Description:** `Choose the breed, add the name.` · **Button:** Shop Now

## S-STATIC
Primary text = S-C1. Headline = `A memorial that catches the light`.

---

# Build + QA

1. REF-GIVER (3 stills) → QA identity across the 3.
2. Six start frames/stills → QA: identity, hands (count fingers at full res), product = Image 1 exactly, "Alex" legible in F-BOX.
3. Four Seedance clips (5s, 720p, `generate_audio:false`) → `motion_qa.py` + eyes on ≥5 frames each.
4. Assemble with hard cuts (`ads/build_v2.py`), captions inside the Reels safe zone, piano bed, CTA over moving shot.
5. Export 1080×1920 masters + the 4:5 static → `products/suncatcher-dog-memorial/ads/out/`.

Budget: ~$0.6 stills + ~$2–4 video (best-of-2 on people shots) ≈ **$5**.

# Parked (not deleted)
- Body B (reaction on the face) and Hook 2 (empty window) → T1 late-reveal test after a control converts.
- Breed-swap variants (council, Expansionist) → after a winner.
- Who buys (owner vs friend) → pull pet-memorial suncatcher ads from the Meta Ad Library before scaling.
