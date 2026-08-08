# Session Handoff — 2026-08-08 · AI Film Studio + MJP-111 finalize

## What was achieved
1. **Finished the MJP-111 emotional film** "Everyone Is Still in Your Garden" (Thai-ad twist). Deliverable: `products/MJP-111-.../ads/film/out/EveryoneStillInYourGarden_v2.mp4` (36s). Real product animated at 00:24, real logo end card, real personalization names (Sophia·Cosmos, Donna·Aster, Sharon·Rose, Helen·Marigold, Sarah·Poppy), crossfades, cool→warm grade, composited text props.
2. **Built the AI Film Studio** (reusable):
   - Bible: `research/reference/ai-film-studio.md` (roster of 6 roles, phased pipeline 0–5 with the **Phase-2 turntable gate**, inputs spec §0, hard rules, real generation cost/time model, **standard folder convention**).
   - Kit: `products/_templates/film-studio/` (`build.sh`, `captions.py`, `props.py`, `endcard.py`, `production.md`, README, folder skeleton + `.gitignore`). Table-driven; syntax-checked.
   - Crew subagents: `.claude/agents/film-{producer,screenwriter,director,art-continuity,editor,qa}.md`; command `.claude/commands/film/new.md` (`/film:new`).
   - Script template: `research/templates/film-script-template.md`.
   - Writer role also produces **ad copy** (`ad-copy.md`) with **5 different-methodology hooks** (not rewordings).
   - Indexed in PROJECT-INDEX + research/README + memory (`ai-film-studio.md`).
3. **Reorganized MJP-111 into the STANDARD layout** (`ads/film/{refs/{cast,product,props},shots,audio,build,out,assets,_scratch}` + `production.md`, `script.md`). Old ad-hoc dirs → `ads/_archive/`; old builds/rejects → `_scratch/`. Nothing deleted. Deliverable intact.
4. **Produced + reconciled MJP-111 ad copy** (`ads/ad-copy.md`) via the `film-screenwriter` agent — first real studio run. It also surfaced a name-drift bug; synced `script.md` ↔ film ↔ copy to the 5 real names.
5. **Corrected the Seedance pricing** (was "$0.09/clip", real ≈ **$0.98/clip @720p**) in `ai-product-review-consistency-method.md` + the studio cost model.
6. **Tracker:** MJP-052 (Snowman family light box) set **live** (URL added, stage/design/live_date/last_updated) in `products/_registry/product-tracker.csv` + re-pushed the Google Sheet.
7. **Saved the real logo** to `library/brand/logo/lockup-horizontal.png` (pulled from the live site).

## Key decision / scope correction
- **Ad economics + testing = FB-advertiser (media-buyer) expertise, NOT the film studio.** Reverted break-even/testing out of `film-producer` (P0/P5) and the bible Phase 5. Studio scope now ends at **delivering creative → hand off to the FB advertiser.**

## ⚠️ TODO — build a separate FB-ADVERTISER domain (own home: `marketing/`, not the film studio)
It should own break-even, the lean testing plan, and kill/scale, backed by sop-docs `Internal-Guidelines/.../Marketing/Facebook-Testing-Scaling-Research.md`. Parking the worked numbers here so they're not lost:

**MJP-111 unit economics (per-product — recompute for every product):**
- In: $50 + $9.99 ship = **$59.99/order**. Out: **$20 POD (all-in, incl. shipping)** + ~$2 fee → **contribution ≈ $38/order (~63% margin).**
- **Break-even CPA ≈ $38 · Break-even ROAS ≈ 1.6×** (order value ~$60).
- Kill/keep: 0 ATC by ~$38 → kill · ATC no sale by ~$76–114 → kill · ≥1 sale ≤ break-even by ~$76 → keep · healthy cost-per-ATC < ~$12.
- Scale: ROAS > ~2.1–2.4× (CPA ≲ $25–29), held 3–4+ days.
- **Lean test (~$160–240 to a validated hook, not $500):** concept probe ~$40–80 (kill dud at ~$38) → 1 DCT ad set for hook discovery ~$120–160.
- **Hook-testing nuance (story film):** for a narrative film the hook = the story's *entry point* — you can't just swap the first 3s. Real variants = re-structured entries (linear-curiosity vs flash-forward-emotional, same footage) + optional separate creatives for DR/UGC. Don't build 5 hooks upfront; probe cheap → expand on signal.

## Other next steps
- Optional: cut the 15s FB version + the 2 story-entry hook variants of MJP-111 (editing, ~$0–1).
- Reconcile `NV984-pajama` to the MJP-NNN scheme (or record as legacy exception). Spell out the ID convention in `products/_registry/README.md`.
- Confirm what **MJP** actually abbreviates (not "Made Just For You" = MJFY).
- `_archive/` + `_scratch/` under MJP-111 hold ~120MB old takes — safe to delete once confirmed.
