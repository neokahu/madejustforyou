# Role 05 brief — MJ4U-133 C0 (2026-11-25, Producer)

Gate A is approved (BRIEF.md). Each 05 agent takes ONE concept folder `<K>/` and produces the visual plan. **Planning pass only: no paid generation in this pass** (AtlasCloud balance ≈ $15; the owner tops up before Gate B). Reference lock = GATE B: 07 shot mode, then the owner.

## Read first
- `<K>/script.md` (revised after council; the beat table is authority for words/timing)
- `BRIEF.md` (all rulings incl. Gate A, council questions, **E37 amended**), `CRITERIA.md` (E37 amended, E40 shape, E41 scale, E32 shot lengths, E57/E60 safe zones)
- `council/verdict.md` § "Round-wide rules for 05" (all 11 rules apply)
- `RENDERS.md`: renders, turntables, K01 test-clip lessons, K01 beat-2 proof, K04 recording
- `research/reference/video-team/role-research/05-visual-director.md` and the adapters (`research/reference/video-team/adapters/README.md` → seedance-prompt-method.md, image-prompt-method.md, image-to-video-prompt-method.md, ai-product-review-consistency-method.md)

## What changed since the 05 spec was written (overrides the spec's "generator never draws the product")
- **E37 amended (user, 2026-11-24):** the generator MAY draw the ornament's physical body from the concept's turntable refs (front render + `<K>-34left.jpg` + `<K>-34right.jpg`), for physical holds, hanging, scale and light. Its generated face is a placeholder: the real render is composited and tracked over it in post. No shipped frame shows generated figures, names or year.
- **Tested (K01, Seedance 2.0 Fast ref-to-video):** hand + ornament hanging from a branch by its gold cord = PASS; a free-hanging ornament left alone SPINS 360° and shows an invented back = FAIL. Rule: the ornament faces camera throughout; a shot never relies on a free-hanging ornament staying still (cut before, or sway added in post on the real artwork). Round-wide rule 1 ("never hung by the string on camera") is relaxed to: hand-release onto a branch is allowed; the spin rule above applies.
- Cord is **thin gold metallic**. Product = one flat 3 mm plywood sheet, printed one side, blank back (E40).
- Image-first: every generated video shot starts from an image first frame (Nano Banana Pro Edit or Seedream Edit), cast-matched, before any video.

## Assets on disk (media, gitignored, Drive-backed) — `products/MJ4U-133-family-wood-ornament/ads/`
- `renders/MJ4U-133-<K>-render.{png,svg}` (transparent 3185×3000, real artwork; all six incl. K02)
- `turntable/<K>/<K>-34left.jpg`, `<K>-34right.jpg` (K01 also `K01-front-flat.jpg`, `K01-test-hang-seedance.mp4`)
- `stills/K01/K01-b2-take{1,2}.png` (beat-2 proof; take 2 preferred; may seed K01 cast refs)
- `screen-recordings/K04-personalizer-circle-glasses.mov` (use clean frames 0–1s and ~8–10s only; label is "Circle Glasses")
- `source-images/hero-family-2026-tree.png` (shared end-card plate unless the neutral render is made)
- New media from this role goes under `products/MJ4U-133-family-wood-ornament/ads/MJ4U-133-C0/<K>/`.

## Deliver in `<K>/` (this pass)
- **O1 `shotlist.md`** (full spec columns; serves-first; E32; round-wide rules; frame-1 interrupt for EACH hook arm)
- **O2 `refs/REFS-PLAN.md`**: per recurring person: 2–3 stable features + must-not-change list, matched to the printed render and caption pronouns; which refs exist vs must be made; the product ref set (render + turntable) and the scale anchor (4/5/7 in vs hand/branch).
- **O3 `briefs/`**: one tool-agnostic brief per generated asset (template §4.1), every field filled or "n/a". Do NOT call any generation tool.
- **O4 `asset-plan.md`**: reuse vs new, image first frames, video clips, takes, cost at current Atlas prices (Nano Banana Pro Edit $0.14/img; Seedream v5 Pro Edit ~$0.04/img; Seedance 2.0 Fast ref-to-video $0.072/s at 720p), and the concept's share of the $300 cap.
- **O5** frame-1 plan per hook arm + thumbnail still plan (in shotlist or a short file).
- Flag anything that changes *what* a beat shows, its duration or words → back to 04/owner; do not change it yourself.
Do not commit. Do not edit other concepts' folders.

## Cost logging (2026-11-25, owner request) — mandatory
Every generated asset is logged in `marketing/facebook-ads/media-cost-ledger.csv` (charged price from the AtlasCloud API + width/height/duration/fps/bytes + product/test/concept/purpose + kept/rejected/test). `scripts/atlas_poll.sh` logs automatically on download; for anything downloaded another way run `python3 scripts/media_ledger.py log <prediction_id> <file> --purpose <p> --status <kept|rejected|test>`. Totals: `python3 scripts/media_ledger.py sum --by concept --test MJ4U-133-C0`.
**Real charged prices (2026-11-24/25):** Seedream v5 Pro Edit 2048² = **$0.072**/img (not $0.04); Nano Banana Pro Edit 2k = $0.14; Seedance 2.0 Fast ref-to-video 5s 720p with 3 reference images = **$0.78** (≈$0.156/s, not $0.072/s). Budget with these.
