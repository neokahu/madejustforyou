# Phase-1 Shooting Scripts + Ad Copy — Dog Memorial Suncatcher

> Product: **6 IN · German Shepherd · "Alex"** — $26.95 · GP $22.34 · BE ROAS 1.21× · target CPA $15.64
> Build plan: `PHASE1-SUNCATCHER-video-build-plan.md` · Framework: plan page §05
> Prompt grammar: `research/reference/seedance-prompt-method.md` (every prompt below obeys it)
> Nothing generates until this document is approved.

---

## What ships

**6 ads = 3 bodies × 2 hooks.** The hook is the only thing that changes between a pair.

| Ad | Concept | Body | Hook clip |
|---|---|---|---|
| S-C1-H1 / S-C1-H2 | 01 · Cá nhân hoá | A | HOOK-1 / HOOK-2 |
| S-C2-H1 / S-C2-H2 | 02 · Phản ứng | B | HOOK-1 / HOOK-2 |
| S-C6-H1 / S-C6-H2 | 06 · Đổi người mua | C | HOOK-1 / HOOK-2 |

**Locked across all six:** 20s · structure A · 9:16 · music bed, no voice · proof = name + breed legible ·
offer bản chuẩn · CTA **"Make one that's only theirs"** · Meta button **Shop Now** · burned captions,
legible sound-off.

---

## Two decisions I made while scripting — flagging both

### 1. The hook pair is shot ONCE and reused across all three bodies — 14 clips, not 18

The build plan budgeted 6 hook clips (2 per body). Shooting the same hook three times means three
slightly different files, and the hook then differs by concept as well as by hook — which is exactly the
confound the plan exists to prevent. **One HOOK-1 file and one HOOK-2 file, dropped in front of all three
bodies,** makes the hook a perfectly controlled variable.

Continuity cost: Body C opens in the owner's window, then cuts to the giver's world. That reads as a cold
open and **bookends** — Body C's last beat returns to that same window. It works.

Saving: 18 clips → **14**. Budget drops ≈$23 → ≈$19.

*If you want per-body hooks instead, say so — it's 4 extra clips and the shot list below just gets
duplicated with per-body room continuity.*

### 2. Bodies A and B get a connection cue, or they break the house rule

Our standing rule: a gift ad shows the **relationship**, never a lone recipient — a person alone reads as
lonely, which is the wrong emotion. Body C satisfies it by construction (a friend gives the gift). Bodies
A and B are one man alone in a house.

Fix, without adding a beat or changing the structure: **a framed photo of the owner with Alex, alive,
sits in shot in beat 2 of both bodies.** The connection is present in frame, the man is not alone in the
story, and it costs nothing — it's a prop in a shot we were already shooting.

---

## Re-timed beat sheet — 5s-native

Seedance generates in fixed lengths. Beats of 2 / 4 / 6 / 5 / 3s meant paying for 5s and throwing most of
it away, or time-stretching the reveal. Re-timed so every clip is generated at 5s and trimmed in ffmpeg:

| Beat | Was | **Now** | Clip |
|---|---|---|---|
| 1 · hook | 0–2s | **0–2s** | 5s generated, 2s used |
| 2 · bối cảnh | 2–6s | **2–6s** | 5s generated, 4s used |
| 3 · sản phẩm lộ ra | 6–12s | **6–11s** | 5s native, full |
| 4 · phản ứng | 12–17s | **11–16s** | 5s native, full |
| 5 · chốt + CTA | 17–20s | **16–20s** | 5s generated, 4s used |

Total still 20s. The reveal still lands at ~30–55% — mid-film, per §05.

---

## Model routing

| Shot type | Model | Status |
|---|---|---|
| Empty room, window, light, product, shadow | **Seedance 2.0** (`seedance-2.0-style`) | ✅ validated — testC3, hook3 14.68 |
| Any shot with a person | **Seedance 2.0** (`seedance-2.0-style`) | ✅ validated 2026-09-26 — testE3, hook3 14.90 / motion 14.96 / cuts 0.21 |

**Settled: one model for the whole build.** Test E refuted the "restricted with people" caveat —
identity, faces and hands all held. Seedance **2.5** lost on both motion (roughly half) and light
(a lens-flare smear instead of a prism band), despite being the platform's preferred model.

⚠️ **Two prompt rules Test E added, and every person shot below must obey them:**
1. **Locate the action in space.** "Raises his right hand into the light" gave a palm held flat at
   camera — a *stop* gesture, eyes closed, in a grief ad. Say where the limb goes relative to body and
   camera, and add `His palm never faces the camera` / `His eyes stay open`.
2. **Name the light source as off-screen — and keep it there.** Unsourced light gave a lens flare. But
   once told about a stained-glass panel, Seedance **invented one in frame**. That is the model drawing
   what we sell. Our panel comes from the start frame or from PIL, never from the model.

---

## References — the hard gate

Nothing shoots until these are locked and approved. Max **4–5 assets per generation, one duty each** —
feeding everything we own makes feature priority ambiguous.

| Ref | What | Duty | Used by |
|---|---|---|---|
| `REF-PANEL` | Real product, 2048×2048 flat artwork | PIL composite texture + scale anchor | every reveal |
| `REF-ROOM` | The living room plate (testA, already generated) | scene tone-setting | A, B, C beat 5 |
| `REF-OWNER` | Owner portrait + ¾-left + ¾-right | character anchoring | A, B, C beat 5 |
| `REF-GIVER` | Sympathy-giver, same treatment | character anchoring | C only |
| `REF-ALEX-PHOTO` | Framed photo: owner + German Shepherd, alive | prop, PIL-composited | A, B beat 2 |

`REF-ALEX-PHOTO` is **composited, not generated** — a generated photo-within-a-photo drifts and the breed
has to read. Build it in PIL from the panel silhouette proportions + a stock-shot German Shepherd.

---

# HOOK CLIPS — shared by all three bodies

## HOOK-1 · name shown
**0–2s · opens ON THE GLASS · 5s generated, 2s used · Seedance 2.0 (no person) ✅**

Start frame: close-up plate of the panel in the window, generated **without lettering**.

```
Use @Image 1 as the first frame.
Define the black dog silhouette panel hanging in the window in @Image 1 as <Panel>.

Shot 1: Slow push-in toward <Panel>. Late afternoon light moves across its surface;
the coloured glass brightens from the left edge inward. <Panel> hangs still.

（solo piano, single sustained note）

Warm late-afternoon light, natural documentary photography, shallow depth of field.
<Panel> geometry and the dog silhouette remain exactly as in @Image 1, unchanged throughout.
The silhouette's outline does not change. No deformation, no morphing.
Continuous natural motion, no stutter or flicker.
Avoid generating any text or lettering on the panel.
```

**Post (PIL):** perspective-warp `REF-PANEL` onto the panel face — "Alex", the silhouette, florals and
heart all exact. This is the shot where the name is read on the glass; it must be the real artwork.

**Burned caption:** `That's not a generic dog.` → `That's his actual breed — and his name.`

## HOOK-2 · relationship
**0–2s · opens on the EMPTY WINDOW, product not visible · 5s generated, 2s used · Seedance 2.0 ✅**

Start frame: the same window, **nothing hanging in it**, sheer curtain, late sun.

```
Use @Image 1 as the first frame.
Define the open window with the pale curtain in @Image 1 as <Window>.

Shot 1: Smooth lateral track past <Window>. The curtain lifts and settles in the draught;
late sun moves slowly across the sill. Nothing else in the room moves.

< distant street sound, very faint >
（solo piano, single sustained note）

Warm late-afternoon light, natural documentary photography.
The room's geometry remains exactly as in @Image 1. No objects appear or disappear.
Continuous natural motion, no stutter or flicker.
Avoid generating any text or subtitles.
```

**Post:** none. The product is deliberately absent — that is the hook.

**Burned caption:** `We still leave the window open for him.`

> ⚠️ Meta Personal Attributes: both hooks are first/third person. Never *"Did you lose your dog?"*

---

# BODY A · Concept 01 — the name is the point

The §05 worked example. The payoff is that the silhouette is *his* breed and the name is *his*.

## A-2 · bối cảnh
**2–6s · 5s generated, 4s used · ⚠️ no person, but the photo prop carries the connection · Seedance 2.0**

Start frame: kitchen corner — a dog bowl on the floor, still in its place; a framed photo on the shelf
above it.

```
Use @Image 1 as the first frame.
Define the metal dog bowl on the floor in @Image 1 as <Bowl>.
Define the framed photograph on the shelf in @Image 1 as <Photo>.

Shot 1: Slow push-in from the floor toward the shelf, rising. <Bowl> passes out of the bottom
of frame as the camera rises; <Photo> grows in frame. Dust drifts in the light.
Nothing in the room moves.

（solo piano, sparse）

Soft indirect afternoon light, natural documentary photography, shallow depth of field.
<Bowl> and <Photo> remain exactly as in @Image 1, unchanged throughout.
Their positions and contents do not change. No deformation, no morphing.
Continuous natural motion, no stutter or flicker.
Avoid generating any text, lettering or photographs inside the frame.
```

**Post (PIL):** composite `REF-ALEX-PHOTO` into the picture frame, perspective-warped. The owner and a
living German Shepherd, together. **This is the connection cue — it is not optional.**

**Burned caption:** `The bowl is still where he left it.`

## A-3 · sản phẩm lộ ra — THE REVEAL
**6–11s · 5s native · Seedance 2.0 ✅ this is the validated testC3 shot**

Start frame: `REF-ROOM` wide — panel in the window, empty wall camera-right.

```
Use @Image 1 as the first frame.
Define the black German Shepherd silhouette panel hanging in the window in @Image 1 as <Panel>.

Shot 1: Smooth lateral track across the room. The low sun moves; the coloured light cast by
<Panel> travels slowly across the wooden floor, blue and gold. <Panel> hangs still.
Shot 2: Slow push-in toward the wall. The dog-shaped shadow cast by <Panel> grows larger in
frame as the camera approaches. The shadow's outline does not change.

< a collar tag chimes faintly, off-screen >
（solo piano, sparse, no percussion）

Warm late-afternoon light, natural documentary photography, cinematic texture.
<Panel> geometry, artwork and the seated pose of the dog remain exactly as in @Image 1,
unchanged throughout. The shadow's outline does not change. The dog stays seated.
No deformation, no morphing. Continuous natural motion, no stutter or flicker.
Avoid generating any text or lettering, on the panel or on the wall.
```

**Post:** none. ⚠️ **Revised 2026-09-26** — the wall shadow proves the **breed**, not the name. The model
renders the shadow's heart, florals and butterflies correctly but the name as illegible squiggle, and
compositing it in was proven possible yet made unnecessary: the name is read in the stills close-up
instead. Do not caption this beat as if the name were readable here.

**Burned caption:** `That shape on the wall is his actual breed.`

**Gate:** `motion_qa.py` — hook3 ≥8.0 · motion ≥6.0 · static ≤10. testC3 scored 14.68 / 14.72 / 0%.
**Then look at the frames.** A passing number on a misrepresented product is the trap this shot already
sprung once.

## A-4 · phản ứng
**11–16s · 5s native · ⚠️ PERSON — model TBD**

Start frame: the owner sitting on the floor, side-on, the band of coloured light falling across him.

```
Use @Image 1 as the first frame.
Define the seated man in the grey sweater in @Image 1 as <Owner>.

Shot 1: Slow push-in toward <Owner>. <Owner> slowly raises his right hand into the band of
coloured light and holds it there; his fingers open slightly. His shoulders drop as he lets
out a long breath. He does not turn his head.

（solo piano, sparse）

Warm late-afternoon light, natural documentary photography, shallow depth of field.
<Owner>'s face and body proportions remain stable without deformation.
His clothing and the room remain exactly as in @Image 1.
Hands have five fingers, correctly formed.
Movements are continuous and natural, no stutter or flicker.
Avoid generating any text or subtitles.
```

Emotion written as physical detail per the guide's table — *long breath out, shoulders dropping* is
relief, not "sad man". Never write the adjective.

**Burned caption:** *(none — let the shot breathe)*

## A-5 · chốt + CTA
**16–20s · 5s generated, 4s used · Seedance 2.0 ✅**

Start frame: medium-close on the panel in the window, sun lower and warmer.

```
Use @Image 1 as the first frame.
Define the black dog silhouette panel hanging in the window in @Image 1 as <Panel>.

Shot 1: Slow push-in toward <Panel>. The light behind it deepens from gold to amber as the
sun drops. <Panel> turns a few degrees on its cord and settles.

（solo piano, resolving）

Warm low-angle light, natural documentary photography.
<Panel> geometry and the dog silhouette remain exactly as in @Image 1, unchanged throughout.
The silhouette's outline does not change. No deformation, no morphing.
Continuous natural motion, no stutter or flicker.
Avoid generating any text or lettering on the panel.
```

**Post:** `REF-PANEL` warped on. Then end card: `Make one that's only theirs` + logo.

**Burned caption:** `Make one that's only theirs`

---

# BODY B · Concept 02 — the reaction is the point

Same house, same owner, same reveal moment. **The camera stays on the face, not the glass.** The product
is legible but never the subject. This is the whole difference — do not let it drift into Body A.

## B-2 · bối cảnh
**2–6s · 5s generated, 4s used · ⚠️ PERSON — model TBD**

Start frame: the owner at the kitchen sink, side-on, ordinary afternoon; the framed photo on the shelf
behind him, out of focus.

```
Use @Image 1 as the first frame.
Define the man in the grey sweater at the sink in @Image 1 as <Owner>.
Define the framed photograph on the shelf behind him in @Image 1 as <Photo>.

Shot 1: Slow lateral track behind <Owner>. <Owner> washes a single cup, slowly, without
looking up. <Photo> stays in soft focus behind him and does not move.

（solo piano, sparse）

Soft indirect afternoon light, natural documentary photography, shallow depth of field.
<Owner>'s face and body proportions remain stable without deformation.
Hands have five fingers, correctly formed.
<Photo> remains exactly as in @Image 1; its contents do not change.
Movements are continuous and natural, no stutter or flicker.
Avoid generating any text, lettering or photographs inside the frame.
```

**Post (PIL):** `REF-ALEX-PHOTO` into the frame. Soft-focused, but the breed still reads.

**Burned caption:** `Same cup. Same time every day.`

## B-3 · sản phẩm lộ ra — held on the face
**6–11s · 5s native · ⚠️ PERSON — model TBD**

Start frame: medium-close on the owner's face, three-quarter, neutral light.

```
Use @Image 1 as the first frame.
Define the man in the grey sweater in @Image 1 as <Owner>.

Shot 1: Fixed medium-close framing on <Owner>. A band of blue and gold light moves slowly
across his face from left to right. <Owner> stops moving. His eyes track the light. His jaw
loosens; he stops mid-breath.
Shot 2: Slow push-in on <Owner>. His eyes redden slightly. He does not blink.

（solo piano, sparse, no percussion）

Warm late-afternoon light, natural documentary photography, shallow depth of field.
<Owner>'s face and body proportions remain stable without deformation.
His clothing remains exactly as in @Image 1.
Movements are continuous and natural, no stutter or flicker.
Avoid generating any text or subtitles.
```

> ⚠️ **Rule exception, deliberate.** Shot 1 is fixed. The opening-shot-must-move rule exists to protect
> `hook3` — but this clip starts at second 6, not second 0, so it is not measured by `hook3`. The
> *light* moves, which the differencer reads. If motion scores below 6.0, change Shot 1 to a very slow
> push-in — **not** to a bigger performance from the actor.

**Post:** none — the product is out of frame by design.

**Burned caption:** `The room does this at four o'clock.`

## B-4 · phản ứng
**11–16s · 5s native · ⚠️ PERSON — model TBD**

Start frame: wider — the owner in the room, the panel visible camera-left, small in frame.

```
Use @Image 1 as the first frame.
Define the man in the grey sweater in @Image 1 as <Owner>.
Define the black dog silhouette panel in the window in @Image 1 as <Panel>.

Shot 1: Slow pull-back from <Owner>. <Owner> turns his head toward <Panel> and holds there.
His shoulders drop as he lets out a long breath. <Panel> hangs still.

（solo piano, sparse）

Warm late-afternoon light, natural documentary photography.
<Owner>'s face and body proportions remain stable without deformation.
<Panel> geometry and the dog silhouette remain exactly as in @Image 1, unchanged throughout.
The silhouette's outline does not change.
Movements are continuous and natural, no stutter or flicker.
Avoid generating any text or lettering on the panel.
```

**Post (PIL):** `REF-PANEL` warped on — small in frame, but it must still be the real artwork.

**Burned caption:** *(none)*

## B-5 · chốt + CTA
**16–20s · 5s generated, 4s used · Seedance 2.0 ✅**

**Identical setup to A-5.** Reuse the same clip if the grade matches — it is the product close and there
is no reason for it to differ between bodies. Saves one clip: **14 → 13.**

**Burned caption:** `Make one that's only theirs`

---

# BODY C · Concept 06 — the buyer swaps

The person on screen is **the friend who sends it**, not the owner. This is the only body that satisfies
the giving-relationship rule by construction.

## C-2 · she hears the news
**2–6s · 5s generated, 4s used · ⚠️ PERSON — model TBD**

Start frame: a woman at a table, phone in hand, in the middle of an ordinary morning.

```
Use @Image 1 as the first frame.
Define the woman with the dark bob and the green cardigan in @Image 1 as <Giver>.

Shot 1: Slow push-in toward <Giver>. <Giver> reads her phone, then goes still. She lowers the
phone slowly to the table. Her head tilts forward slightly.

（solo piano, single note）

Soft morning light, natural documentary photography, shallow depth of field.
<Giver>'s face and body proportions remain stable without deformation.
Hands have five fingers, correctly formed. Her clothing remains exactly as in @Image 1.
Movements are continuous and natural, no stutter or flicker.
Avoid generating any text, lettering or screen content on the phone.
```

**Post (PIL):** leave the phone screen dark or composite a plain message bubble. **Never let the model
write text.**

**Burned caption:** `Her dog died on Tuesday.`

## C-3 · she doesn't know what to send
**6–11s · 5s native · ⚠️ PERSON — model TBD**

Start frame: the woman standing in front of a florist's bucket display, hand half-raised.

```
Use @Image 1 as the first frame.
Define the woman with the dark bob and the green cardigan in @Image 1 as <Giver>.

Shot 1: Slow lateral track past <Giver>. <Giver> reaches toward the flowers, stops, and lowers
her hand again. She shakes her head once, very slightly.

（solo piano, sparse）

Soft daylight, natural documentary photography, shallow depth of field.
<Giver>'s face and body proportions remain stable without deformation.
Hands have five fingers, correctly formed.
Movements are continuous and natural, no stutter or flicker.
Avoid generating any text or subtitles.
```

**Burned caption:** `Flowers felt wrong. They die too.`

## C-4 · she chooses this
**11–16s · 5s native · ⚠️ PERSON — model TBD**

Start frame: close on her hands at a table, the panel face-down in tissue paper, box open.

```
Use @Image 1 as the first frame.
Define the pair of hands in the green cardigan sleeves in @Image 1 as <Hands>.
Define the panel lying in the tissue paper in @Image 1 as <Panel>.

Shot 1: Slow push-in toward <Panel>. <Hands> turn <Panel> face-up and hold it steady,
then fold the tissue paper over one edge.

（solo piano, warming）

Soft indirect light, natural documentary photography, shallow depth of field.
<Hands> have five fingers each, correctly formed, without deformation.
<Panel> geometry and the dog silhouette remain exactly as in @Image 1, unchanged throughout.
The silhouette's outline does not change. No deformation, no morphing.
Movements are continuous and natural, no stutter or flicker.
Avoid generating any text or lettering on the panel.
```

**Post (PIL):** `REF-PANEL` warped onto the panel face — held flat and still, this is the **easiest and
cleanest composite in the build.** The name is read here, in her hands, at the moment of giving. That is
the strongest possible placement for concept 06.

**Burned caption:** `His breed. His name. Not a generic sympathy card.`

## C-5 · the owner's window — bookend
**16–20s · 5s generated, 4s used · Seedance 2.0 ✅**

**Same setup as A-5 / B-5** — and it now closes the loop opened by the hook clip, which was this same
window. That is why the shared hook works for Body C.

**Burned caption:** `Make one that's only theirs`

---

# Clip inventory

| # | Clip | Person? | Model | Post |
|---|---|---|---|---|
| 1 | HOOK-1 | no | Seedance 2.0 ✅ | panel warp |
| 2 | HOOK-2 | no | Seedance 2.0 ✅ | — |
| 3 | A-2 | no | Seedance 2.0 ✅ | photo prop |
| 4 | A-3 reveal | no | Seedance 2.0 ✅ | panel + **name in shadow** |
| 5 | A-4 | ⚠️ yes | TBD | — |
| 6 | B-2 | ⚠️ yes | TBD | photo prop |
| 7 | B-3 | ⚠️ yes | TBD | — |
| 8 | B-4 | ⚠️ yes | TBD | panel warp |
| 9 | C-2 | ⚠️ yes | TBD | phone screen |
| 10 | C-3 | ⚠️ yes | TBD | — |
| 11 | C-4 | ⚠️ yes | TBD | panel warp |
| 12 | SHARED-CLOSE (A-5 = B-5 = C-5) | no | Seedance 2.0 ✅ | panel warp + end card |

**12 clips** — down from 18, by sharing the hook pair and the product close. ≈$12 of generation plus a
30% reshoot allowance ≈ **$16**.

**5 clips are shootable today.** 7 wait on the people test.

---

# Ad copy

Primary text and headline differ **by concept** (concept is the variable being tested). Within each hook
pair they are **identical** — only the video's first 2 seconds change.

Line breaks and bullets are mandatory: FB primary text must be scannable, never a paragraph.

## S-C1 · concept 01 · personalization

**Primary text**
```
His name is on it. So is his breed.

Not a clipart dog — a German Shepherd, because that's what he was.

We cut the silhouette to the breed you choose and set the name inside it in white script.

Hang it where the afternoon sun comes in:

• the room fills with blue and gold
• his shape lands on the wall
• his name sits inside the shadow

6 inches. Ready to hang. Made to order.
```
**Headline:** `His breed. His name. In the light.`
**Description:** `Choose the breed, add the name. Ships in 3–5 days.`
**Button:** Shop Now

## S-C2 · concept 02 · the reaction

**Primary text**
```
The room changes at about four o'clock.

That's when the sun comes through it — everything goes blue and gold, and his shape lands on the wall.

After the first week you stop looking at the glass.

You look at the wall.

• Your dog's breed, in silhouette
• His name, in the light
• 6 inches, fits any window

Made just for him.
```
**Headline:** `At four o'clock the whole room turns into him.`
**Description:** `Choose the breed, add the name. Ships in 3–5 days.`
**Button:** Shop Now

## S-C6 · concept 06 · the buyer swaps

**Primary text**
```
Her dog died on Tuesday. I didn't know what to send.

Flowers felt wrong — they die too.

So I sent her this: his breed in silhouette, his name inside it, cut to hang in her kitchen window.

She told me the room goes gold at four o'clock now.

• Choose the breed and the name
• 6 inches, ready to hang
• Made to order, ships in 3–5 days
```
**Headline:** `What to send when flowers feel wrong.`
**Description:** `Choose the breed, add the name. Ships in 3–5 days.`
**Button:** Shop Now

> ⚠️ **Meta Personal Attributes.** Every line is first or third person. Never *"Did you lose your dog?"*,
> never *"Are you grieving?"* — second-person grief gets the ad rejected and can flag the account.

---

# Pre-flight check — §05 step 9

Mute the first 3 seconds of each cut. **Can you tell what gift is being sold?**

- **HOOK-1** → yes, the panel is in frame 1.
- **HOOK-2** → **no, by design.** The product is not visible until second 6.

That is the test. Hook 2 trades 3-second clarity for emotional pull, and if it loses on link CTR while
holding on hook rate, we have learnt something specific: on this product, showing the object beats
naming the relationship. Do not "fix" Hook 2 by putting the product in it — that deletes the experiment.

# Order of work from here

1. ✅ Scripts + copy — this document. **Needs approval.**
2. ✅ **People test — DONE 2026-09-26.** Seedance 2.0 for every clip. See the model routing table above.
3. ✅ **Compositing — RESOLVED 2026-09-26, and the engine is not needed.** The name-reading close-up
   becomes a **4K still + ffmpeg Ken Burns at native resolution** (`hook3 11.02 / motion 10.73`, clears
   the gate, ~0.2 cr). It beats Seedance on letterform, silhouette, frame and sharpness at a twentieth
   of the cost, because nothing is re-synthesized. The wall shadow keeps Seedance and proves the
   **breed**, not the name. Full evidence: `research/reference/product-text-fidelity-2026.md`.
   ⚠️ Zoom on native resolution — scaling to 1080 before `zoompan` softens the lettering. — PIL perspective-warp of `REF-PANEL` onto the panel face and into the wall
   shadow. If the wall-shadow name can't be made convincing, A-3's caption moves to the glass close-up
   and the build still ships.
4. **Turntables** — REF-OWNER, REF-GIVER, REF-ALEX-PHOTO. Hard gate.
5. **Batch-generate 12 clips.**
6. **QA every shot** — `motion_qa.py`, then eyes on frames.
7. **Post** → 6 ads + copy to the ad account.
