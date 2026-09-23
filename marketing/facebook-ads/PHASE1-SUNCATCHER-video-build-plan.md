# Phase-1 Video Build — Dog Memorial Suncatcher (Vòng Concept)

> Product: [personalized-dog-memorial-suncatcher-breed-name](https://madejustforyou.net/products/personalized-dog-memorial-suncatcher-breed-name)
> Hero variant **6 IN** — $26.95 · GP $22.34 · **BE ROAS 1.21×** · target CPA $15.64
> Plan source of truth: **https://testing-plan-phase-1.namvu47.workers.dev** (§05 khung dựng, §07 ráp lại)
> Pipeline: `research/reference/ai-film-studio.md` · kit `products/_templates/film-studio/`

## What ships — 6 ads, not 6 films

3 concepts × 2 hooks. **The hook is the only thing that changes between the pair** — same body, same
grade, same music, same CTA. That is what makes the hook a clean OFAT test.

| Ad | Concept | Body |
|---|---|---|
| S-C1-H1 / S-C1-H2 | **01 · Cá nhân hoá** — name + breed is the payoff | Body A |
| S-C2-H1 / S-C2-H2 | **02 · Phản ứng** — the owner's face when the room fills | Body B |
| S-C6-H1 / S-C6-H2 | **06 · Đổi người mua** — a sympathy-giver buys it, not the owner | Body C |

**Locked across all six** (change any of these and the comparison dies):
length **20s** · structure **A · Mở bằng phản ứng** · pacing **~5s/scene** · voice **nhạc nền, không lời**
· proof **tên + giống chó hiện rõ** · offer **bản chuẩn** · CTA **"Make one that's only theirs"** ·
Meta button **Shop Now** · 9:16 · burned captions, legible sound-off.

**The two hooks** (0–2s: opening frame + on-screen text):

- **Hook 1 · name shown** — *"That's not a generic dog. That's his actual breed — and his name."*
  Open **on the glass**, name and breed silhouette sharp in frame 1.
- **Hook 2 · relationship** — *"We still leave the window open for him."*
  Open **on the empty window**, product not yet visible.

⚠️ **Meta Personal Attributes policy.** Every grief hook stays first/third person. *"Did you lose your
dog?"* gets rejected; *"We still leave the window open for him"* does not. This applies to the ad copy too.

## The three bodies

Beat 1 is the hook and is shot twice. Beats 2–5 are the body and are shot once.

**Body A · concept 01 — the name is the point** (this is the §05 worked example)

| Beat | | |
|---|---|---|
| 1 · hook | 0–2s | *swappable — see above* |
| 2 · bối cảnh | 2–6s | Empty house, Max's food bowl still in its place |
| 3 · sản phẩm lộ ra | 6–12s | Sun through the glass — **his name and breed land on the wall** |
| 4 · phản ứng | 12–17s | The owner sits down, reaches into the band of light |
| 5 · chốt + CTA | 17–20s | Close on the suncatcher in the window |

**Body B · concept 02 — the reaction is the point**
Same house, same owner. The camera stays on **the face**, not the glass: the room turns colour and he goes
still. Product legible but never the subject. Reveal still lands at ~60%.

**Body C · concept 06 — the buyer swaps**
The person on screen is **the friend who sends it**, not the owner. Beats: she hears the news → doesn't
know what to send → chooses this → *then* the owner's window. Satisfies the house rule that a gift ad
shows the giving relationship, never a lone recipient.

## Hard gate — lock these before a single scene is generated

This gate exists because identity drift, product-scale jumps and pasted-in props each cost a full
reshoot (~$1/clip) versus ~$0.05 to fix at the reference stage.

1. **Owner** — one locked portrait + ¾-left / ¾-right. Used in Bodies A, B and the last beat of C.
2. **Sympathy-giver** — second person, same treatment. Body C only.
3. **Max** — the dog's look must be **one fixed breed**, because the product's selling point is that the
   silhouette is *his actual breed*. Breed on the glass and dog in any photo prop must match exactly.
4. **Product turntable from the REAL store photo** — scale-anchored (suncatcher beside a mug at true
   size) + front/¾. Keep the product in close/medium framing; a bare crop has no scale cue and the model
   oversizes it in wides.
5. **Text props** — name + breed silhouette rendered sharp in PIL.

### The one real production risk

**The money shot is text projected on a wall, and AI cannot render legible text.** Beat 3 of every body
depends on the name being readable. Do not ask the model for it.

Generate the plate — sun, window, band of colour on the wall, no lettering — then **composite the name
and breed silhouette in post with PIL**, warped to the wall's perspective and tracked across the beat.
Same for the lettering on the glass itself. This is the existing `products/_templates/film-studio/` kit
plus the perspective-warp approach proven in the cartoon POC (`products/MJ4U-111-…/ads/cartoon-poc/`).

If a beat can't be composited convincingly, reframe so the name is read in close-up on the glass rather
than projected — do not ship a blurred approximation of the thing being sold.

## Budget

| | Count | Unit | |
|---|---|---|---|
| Body clips | 4 × 3 bodies = 12 | $0.98 | $11.76 |
| Hook clips | 2 × 3 bodies = 6 | $0.98 | $5.88 |
| Reference images | ~8 | $0.045 | $0.36 |
| Music bed | 1 (shared) | $0.15 | $0.15 |
| Reshoot allowance | ~30% | | ~$5.30 |
| | | **Total** | **≈ $23** |

720p. 480p halves it if the first pass is exploratory. Set each clip's `duration` to its beat length —
rendering a blanket 5s for a 3s beat throws away ~$0.40 each.

Against $360 of media spend and a $15.64 target CPA, production cost is not the constraint. **Quality of
the reveal is.**

## Order of work

1. **Script all three bodies** scene-by-scene before generating anything — visual, camera, on-screen text,
   sound. Plus ad copy: primary text ×3, headline ×3.
2. **Build and approve the turntables.** ← hard gate, nothing shoots before this
3. **Batch-generate all 18 clips in parallel** once refs are locked (~5–8 min wall clock, not 25–30).
4. **QA every shot together** — identity, product scale, hands/morphs, mood, and "shows connection, not a
   lonely giftee". Reshoot only failures.
5. **Post** — composite name/breed, cool→warm grade at the reveal, captions, music, end card.
6. **Ship 6 ads + copy** to the ad account; media buying, kill lines and scaling are out of studio scope.

## ⚠️ Conflict to resolve before scripting

`PHASE1-TOURNAMENT-3-products.md` gives suncatcher **a different hook pair per concept** (A1/A2/A3 each
with their own H1/H2). The approved page gives **one hook pair shared by all three concepts**.

**The page wins** — per-concept hooks would confound concept with hook and destroy the whole test. But the
tournament doc still reads as authoritative and will mislead whoever builds from it, so it needs a note
pointing at the page. Its unused lines are still good material for **Vòng Hook** later:

- *"The sun hits it at 4pm and the whole room turns into him."*
- *"Anyone can hang a rainbow. This one has his name on it."*
- *"Her dog died on Tuesday. I didn't know what to send."*
- *"Flowers wilt in a week. This catches the light every morning."*

## Out of scope

Blanket and magnet builds (same structure, different skeletons — B is VO-led, not a reveal) · media
buying · anything in Vòng Hook / Craft / Format, which only start after a winner exists.
