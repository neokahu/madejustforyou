# K06 · O2 reference plan (GATE B, not yet built) · role 05, 2026-11-25

Media path for everything below: `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K06/refs/` (gitignored, Drive-backed).
Gate sequence: build these refs (≈$6.5) → 07 shot mode (identity, on-model vs the render, scale) → owner. **No first frame (P1, F5a, F5b) and no video before sign-off.**

## A · Live ↔ print match sheet (round-wide rule 4)

Printed source: `renders/MJ4U-133-K06-render.png`, left to right Dad, Mom, Sofia, Mateo. Pronouns: "he" = Mateo only, "she/her" = Sofia only (script cast sheet).

| ID | Story role | Stable features (the label reused in every brief) | Must-not-change list | Match to the print |
|---|---|---|---|---|
| **C1 Dad** | father, early 30s; soft-focus in beat 5 only | light-tan skin · short black tapered hair, clean-shaven · red Fair Isle sweater | no glasses · no beard or stubble · sweater red with white Fair Isle band · no Santa hat · no ring on the right hand (left hand on Sofia's shoulder: plain gold band allowed, the same in every frame) | skin, hair colour and cut, sweater colour = print. Coffee cup: none live (hands busy) |
| **C2 Mom** | mother, early 30s; holds Mateo | light-tan skin · long straight brown hair past the shoulders, centre part · green Fair Isle sweater | no glasses · hair loose, never tied up · sweater green with white/red band · both arms wrap Mateo in every frame · no Santa hat · plain gold band on her left ring finger (her only jewellery) | skin, hair, sweater = print. Red tartan trousers: wear them, mostly out of frame |
| **C3 Sofia** | big sister, age 6–7, lead action | light-tan skin · black high ponytail with a red hair tie · red Fair Isle sweater | no glasses · ponytail high, not braided, no fringe change · red tartan trousers · no Santa hat · no jewellery · 5 fingers, nails bare | skin, hair, sweater and trousers = print |
| **C4 Mateo** | baby, 4–6 months, his first Christmas | light-tan skin · wispy dark hair tuft · white Fair Isle sweater collar showing above a cream knit swaddle blanket | near-still in every frame · eyes open and calm, or a slow blink · upright against Mom's chest, head on her shoulder side facing camera ¾ · no dummy, no hat · hands inside the swaddle | skin, hair (Wispy Tuft), white sweater = print. Bottle: not shown live |

Casting check against the captions: "Sofia showed Mateo / where he sits.": Sofia is a girl, the one doing the showing. Mateo is "he", an infant, and the one shown. Mom and Dad are named by title only, and each is clearly an adult man or woman. Four live people match the four printed ones (IC5), with no pet. Casting follows the story role and the artwork, not demographics.
**Santa hats: none live (05 decision, owner may overrule).** The hats would hide Sofia's ponytail and Mom's hair, which are both stable features, and they drift between takes. The sweaters carry the match to the print.

## B · Character reference sets (8 separate full-res images each, never a sheet; image-prompt-method §8-slot)

Generate views 1–3 first, then views 4–8 each from views 1–3 (no drift chaining). Model: Nano Banana Pro Edit, 2K, 1 image per call. Start view 1 from text plus the render crop of that figure as the **look reference only** (colours, hair shape), not as a style. Output is photoreal.

| Slot | C1 Dad | C2 Mom | C3 Sofia | C4 Mateo (adapted to an infant) |
|---|---|---|---|---|
| 1 | front, chest-up | front, chest-up | front, chest-up | front, face and swaddle, held upright (adult arms in a neutral grey sweater as a stand-in, cropped) |
| 2 | ¾ left | ¾ left | ¾ left | ¾ left |
| 3 | ¾ right | ¾ right | ¾ right | ¾ right |
| 4 | full body, standing | full body, standing | full body, standing | in Mom's arms (uses C2 views 1–3 too): the beat-5 hold |
| 5 | standing behind a child-height shoulder, left hand resting on it | standing, holding a swaddled infant upright, both arms wrapped | standing, right arm extended at chest height, fingertips at a small object | lying in a bassinet, top-down |
| 6 | hands close-up | hands close-up (the ring) | hands close-up: right index pointing, thumb tucked | hands, curled, at the swaddle edge |
| 7 | expression: soft smile, eyes down | expression: closed-mouth smile, gaze down | expression: open delighted smile | expression: calm, eyes open |
| 8 | expression: warm smile, eyes to camera-left | expression: soft laugh | expression: proud, eyebrows raised, looking aside | expression: slow-blink, eyes half-closed |

Files: `refs/C1-dad-01-front.png` … `refs/C4-mateo-08-blink.png`. Contact sheet for 07: `refs/K06-cast-contact.jpg`.
Existing refs to reuse: **none** (no locked set for this family. The K01 beat-2 stills are a different family).

## C · Product reference set (exists, except the scale plate)

| ID | File | Role | Status |
|---|---|---|---|
| PR-front | `renders/MJ4U-133-K06-render.png` (+ `.svg`) | product face: the only printed truth composited into every frame. Also the front view for generator body refs | **exists** |
| PR-34L | `turntable/K06/K06-34left.jpg` | product body (edge, cut outline, hanger tab, gold cord) | **exists** (re-rolled once for thickness; 07 to confirm "coin-thin" edge) |
| PR-34R | `turntable/K06/K06-34right.jpg` | product body | **exists** |
| **SA1** | `refs/K06-SA1-scale.png` | **scale anchor**: 5 in ornament on a fir branch beside a standard 3 in (7.6 cm) red glass ball, with an adult hand (palm ≈8.5 cm) open just below it | **to make** (brief `briefs/K06-SA1.md`) |
| Lettering | names and year are vector text inside the SVG (Chewy / Fredoka One), always carried by PR-front. No separate cut-out needed | text truth | exists (inside the render) |

**Scale rule (E41):** the hero size in every K06 scene is **5 in** (≈12.7 cm, roughly square).
- Next to an adult palm, it is about 1.5 palm widths.
- Next to Sofia's palm (≈6 cm), it is about 2 palm widths.
- Next to a 3 in glass ball, it is about 1.7 balls.
- On the tree it covers about 3–4 needle-tuft spacings.
- In beat 5 it hangs at Sofia's chest height, about 95 cm off the floor.

07 checks P1, F5a and F5b against SA1.

## D · Set reference (made at Gate C, after this gate)

**P1** (tree plate) is a first frame, not a reference. It is made after sign-off, and F5a/F5b reuse its tree and lights as the light/style reference. That keeps the hook, body and beat 5 in one room.
