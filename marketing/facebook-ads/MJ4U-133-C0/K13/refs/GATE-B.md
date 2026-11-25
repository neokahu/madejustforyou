# MJ4U-133-K13 · Gate B reference set (role 05, 2026-11-25)

> Built under the owner's ruling (BRIEF "User rulings 2026-11-25" item 8). The hard cap was $1.90; **$1.69 was spent** (11 × Nano Banana Pro Edit at $0.14 = $1.54, plus 4 × Seedream v5 Pro Edit = $0.15). The AtlasCloud balance was $15.11 at the start; it is a shared balance.
> Media: `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/K13/refs/` (gitignored; back it up with `scripts/backup-media.sh`). Contact sheet: `K13/refs/gateB-contact.jpg`.
> Self-checked by 05 at full resolution. **Not final:** 07 shot mode, then the owner.

## Method
- **Look references:** each character was cropped from `renders/MJ4U-133-K13-render.png` above the printed names, so no lettering reaches the model (`refs/_inputs/look-*.jpg`). Each crop was used only for hair, eye colour and wardrobe; the cartoon style was not copied.
- **View 1 (front):** made from the look crop. **Views 2 and 3:** made with view 1 as the identity reference, plus the look crop for the trousers in view 3. No view was chained from another new view.
- **Prompts:** positive framing, every hand placed, every reference given a role (image-prompt-method.md); all calls passed the prompt guard.
- **Rulings applied:** no Santa hats on the live cast; Mom's fingers bare.

## Results

| File | Model | Verdict | Notes |
|---|---|---|---|
| C1-mom-v1-front.jpg | NBP | PASS | long ginger waves, green eyes, freckles, green Fair Isle snowflake sweater, bare-headed; reads as late 30s |
| C1-mom-v2-34L.png | NBP | PASS | same face; head at ¾ |
| C1-mom-v3-full.jpg | NBP | PASS | kneeling on her heels; red-tartan trousers; checked at full res: **all fingers bare, no ring**; thumbs tucked under the hands (07: count 4+thumb on each hand) |
| C2-noah-v1-front.jpg | NBP | PASS | ginger tousled crop, red sweater; reads as about 9 |
| C2-noah-v2-34L.jpg | NBP | PASS | same face |
| C2-noah-v3-full.jpg | NBP | PASS | cross-legged, black trousers, 5+5 fingers |
| C3-lily-v1-front.png | NBP | PASS | two ginger pigtails, red snowflake sweater; visibly younger than Noah |
| C3-lily-v2-34L.png | NBP | PASS | same face; pigtail tie visible |
| C3-lily-v3-full.jpg | NBP | PASS | cross-legged, red-tartan trousers, 5+5 fingers |
| L1-room.jpeg | Seedream | PASS, with a note | half-decorated tree (lowest branches bare), open plain box on the left, empty oatmeal bed with a dent on the right, cream rug, no animals, no lettering. **Note:** the lamp shade shows at the left edge. It is a location ref only; scene first frames keep the lamp off-screen. |
| X1-collar.jpeg | Seedream | PASS | worn red flat collar sized for a large dog, one blank round brass tag. The buckle has a second keeper loop beside it: an acceptable real-collar detail. |
| X2-bed-collar-v2.jpeg | Seedream (refine) | PASS | empty bed with the X1-style collar coiled on it and the tag blank; the H17 frame-1 look. Take v1 was rejected: its collar was small and closed-loop, which didn't match X1 (`_rejected/`). |
| P1a-scale-palm-v2.png | NBP (refine) | PASS | 5 in scale: the ornament lies flat on Mom's open palm, overhangs both sides (≈1.7× palm width) and has the gold cord through the tab hole; single flat sheet, coin-thin edge. The face is a generated **placeholder**: its printed names and figures are invented and must never ship (E37). Take v1 was rejected: it had no cord and a tighter overhang. |

Not made in this pass (per the ruling): views 4–8 (on Seedream after Gate B, only for close-up people) and the P1b branch plate. The hanging scale is to be checked against the K01 hang test, or P1b made after Gate B if 07 asks for it.

## For 07 (shot mode) and the owner
1. Identity across views 1–3 per person; casting vs the captions ("Mom", "the kids", "Lily … his collar").
2. Mom's fingers at full res in v3 and P1a.
3. P1a: is the scale plausible for 5 in (E41), and is the build a single flat sheet (E40)?
4. L1: the lamp shade sits at the edge (acceptable for a location ref?).
