# Film Studio — reusable build kit

Copy this folder into a product's ads dir to build an emotional short-film ad:
```
cp -r products/_templates/film-studio products/<ID>/ads/film
```
Full method + roles + rules + cost model: `research/reference/ai-film-studio.md`.
Script template: `research/templates/film-script-template.md`.

## STANDARD folder layout (one film per product — do NOT invent new folders)
```
ads/film/                 # one production. Multiple films → film-<slug>/
├─ production.md          # control doc: config · cast · scenes · budget · state
├─ script.md             # the shooting script
├─ refs/                 # Phase 2 — LOCKED inputs (turntables)
│  ├─ cast/              #   <char>-front.jpg, <char>-34L.jpg, <char>-34R.jpg
│  ├─ product/           #   real-product.jpg, product-scale-ref.jpg, product-34*.jpg
│  └─ props/             #   source stills for text props / wall photos
├─ shots/                # Phase 3 — raw scene clips: sc01-<slug>.mp4 …  (WINNERS ONLY)
├─ audio/                # music.mp3, vo.mp3
├─ build.sh captions.py props.py endcard.py   # the kit (edit the tables)
├─ build/                # Phase 4 — EPHEMERAL intermediates (caps/props/segments). gitignored
├─ out/                  # deliverables: <title>_master.mp4, <title>_15s.mp4, variants
├─ assets/               # logo.png, shared brand bits
└─ _scratch/             # verify frames + REJECTED takes. gitignored
```
**Rules:** winners live in `shots/`; every reject/verify frame goes to `_scratch/` (never clutter `shots/`). `build/` + `_scratch/` are regenerable → gitignored. Deliverables ONLY in `out/`. Flow reads left-to-right: **refs → shots → build → out**.

**Deprecated ad-hoc folders → where they map** (the old MJ4U-111 mess): `source-images/`→`refs/product/` · `product-turntable/`→`refs/product/` (+ winners to `shots/`) · `scene-videos/` & `clips/`→`shots/` (winners) + `_scratch/` (rejects) · `scene-stills/`→`_scratch/` · `final/`→`out/` (+ `audio/`).

## Files
- `production.md` — per-film config + live state/budget (fill this first).
- `captions.py` — burned dialogue/hook captions (edit the `CAPTIONS` table). Auto-shrinks to never overflow.
- `props.py` — real text-prop inserts: notebook page + handwritten note (edit `NOTEBOOK` / `NOTE`).
- `endcard.py` — branded end card (uses `assets/logo.png` + brand palette).
- `build.sh` — trims + cool/warm grade + timed captions + crossfades + inserts + music + end card. Edit the `SCENES` table.
- `assets/` — put `logo.png` (from `library/brand/logo/lockup-horizontal.png`) and `music.mp3` here.

## Workflow (step-gated)
1. **Phase 2 first** — build + host the character turntable (locked ref + ¾ angles) and the **scale-anchored product ref** (product beside a mug). Get sign-off BEFORE any scene. Do NOT skip.
2. **Phase 3** — after sign-off, batch-generate all scenes (Seedance ref-to-video, feed the locked refs), then QA together. Set each scene's `duration` from its beat length.
3. **Phase 4** — drop clips in `script-shots/`, edit the tables in `captions.py`/`props.py`/`build.sh`, run `bash build.sh`.
4. Verify the storyboard sheet the build prints, then ship + a 15s cut.

## Cost/time (720p): ~$0.98/clip · ~$9 clean film · ~8 min parallel shoot. See the bible.
