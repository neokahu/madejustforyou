# NEXT SESSION — Checklist (NV984 pajama clone)

Status: clipart recreated; design skeleton built at DEMO size only. Next session = correct size → finish design → Teeinblue build.

## What's already done
- `01-reference/` — scraped product data, mockups, listing URL
- `02-photoshop-build/` — Tile A skeleton (⚠️ **2400×2400 @300 = 8"×8", DEMO SIZE ONLY**)
- `03-clipart-candidates/` — style research (crayon-doodle matches)
- `04-competitor-cliparts/` — 16 competitor previews (100px ref only) + contact sheet
- `05-ai-recreate-test/` — **16 AI-recreated characters @2K** (char01–12 + Cat1-2 + Dog1-2) + `_BATCH-RECIPE.md` (prompts + taskIds)
- SOP: `sop-docs` → WF-MKT-005 + TASK-MKT-007/008/009/010/011 + Teeinblue.md

## DO NEXT (in order)

### 1. Get the REAL print size (blocker for everything) ✅ DONE (2026-07-22)
- [x] Imported pajama **product base** from Teeinblue → confirmed **cut-and-sew, 2 panels** per pair: `left_leg` + `right_leg` (identical dims, mirror).
- [x] **Printarea size @ 300 DPI, per size** (left_leg = right_leg):
  - XS `5939×6616` · S `6001×6684` · M `6123×6821` · L `6221×6930` · XL `6288×7004` · **2XL/3XL/4XL `6335×7057`**
  - **MASTER = `6335 × 7057 px @ 300 DPI` (21.1"×23.5", the 4XL max)** → build here, scales down for smaller sizes.
  - NOT a seamless tile → all-over scattered repeat fitted per leg panel with safe margin. Current PS skeleton (2400×2400 square, DEMO) must be rebuilt to this tall portrait panel.

### 2. QC the 16 AI characters
- [ ] Open `05-ai-recreate-test/` — check EACH: single-line limbs (not filled), **headless**, colors/pose match.
- [ ] Confirm char10 & char11 fixed. Regenerate any bad one from `_BATCH-RECIPE.md` (reuse limb-fix prompt).

### 3. Prep characters → transparent PNG (TASK-MKT-010)
- [x] Background-removed all 16 → **transparent PNG** in `05-ai-recreate-test/` … → `06-bodies-transparent/` (rembg u2net, local venv `/tmp/rembg-venv`, post_process_mask + tight autocrop). 12 kid bodies = clean & solid.
- [x] ⚠️ **Line-art pets solidified:** Cat-1/2, Dog-1/2 + char-03 interiors flood-filled white (scipy binary_fill_holes, gap-bridged) → solid white body + black outline, verified on black bg. Neckline notches stay open. Pre-fill hollow versions backed up in `06-bodies-transparent/_pre-fill-backup/`.
- [ ] Align each character's head/neck to ONE common **face-slot anchor** (so 1 face-slot fits all 12) — done at Teeinblue placement.
- [x] **Vector clipart set** → `07-vector-cliparts/` (svg + png, transparent, named `kid-01..11` + `pet-01..04`, `_manifest.txt`). Sourced from `04-…/vectorized/` traces: bg rect stripped, rendered @2000px, hollow pet-02 flood-filled white. Scalable alt to the raster `06-bodies-transparent/` set.

### 4. Rebuild the design in Photoshop AT CORRECT SIZE (Claude can do this) — 🟡 IN PROGRESS (2026-07-22)
- [x] **Tile A base rebuilt at real leg size** → `02-photoshop-build/leg-master-1to10.psd` (6335×7057 @300, portrait).
  - Layers: `BG_Color` (white, swappable) · `Palms` (8× real palm silhouette PNG, Multiply blend — asset: `02-photoshop-build/assets/palm-silhouette.png`, AI-gen'd) · `Stars`→`StarField` (50 navy stars, irregular + random rotation) · `Titles` (7× BEST / `TITLE_var(max15)` / EVER navy Impact + navy `Crowns` layer) · `FaceSlots` (10 numbered circles, gray fill + red ring + red number).
  - Built via `photoshop_execute_script` (ExtendScript). ⚠️ GOTCHA: that tool wraps code in an IIFE — **NO `#target` line, always `return`** or it fails silently. Raw `execute_script` DOM works; adobe-photoshop MCP server is NOT connected (only `mcp__photoshop__*`).
- [x] Crown added above each title (raised for clear gap) · real palm silhouettes placed (Multiply) · star field re-scattered irregular.
- [x] **Title = Teeinblue variable.** Middle word layers renamed `TITLE_var(max15)`, center-justified. Presets: Dad/Abuelo/Daddy/Father/Grandpa/Papa/Pop Pop/Pops + **Custom (0–15 chars)**. Teeinblue text option = auto-resize to **reserved max width ≈ 1500px** (long customs shrink, short stay large, always centered). BEST/EVER stay static. NOT baked in PS.
- [ ] **Polish still optional:** swap Impact → heavier condensed *distressed* font to match reference grunge; add subtle distress texture.
- [ ] Build **Tile B (11–15)** layout variant.
- [ ] Note: variable text + characters + faces are **Teeinblue layers, NOT baked into PS**. PS = fixed base + slot positions only.

### 5. Build Teeinblue campaign (TASK-MKT-008 + TASK-MKT-011)
- [ ] Clipart Category: 12 characters (+ Cat1-2, Dog1-2), uniform anchor.
- [ ] Additional Option "Number of Kids/Pets" 1–15 → conditional layer-groups: **1–10 = Tile A, 11–15 = Tile B**; Linked Layers to cycle faces.
- [ ] Additional Option "Title" (Dad/Daddy/Abuelo/Father/Grandpa/Papa/Pop Pop/Pops/Custom) → Text layer, **auto-scale max width**, char limit 15, conditional custom-text field.
- [ ] Additional Option "Background Color" (White/Black/Blue/Grey/Green/Red).
- [ ] Upload photo layer per figure → Photo Enhancer + Cutout.pro face cutout + min size, at face-slot anchor.
- [ ] Variants: 9 sizes, tiered price $33.95→$42.95.

### 6. QC + launch (TASK-MKT-009)
- [ ] Test Number = 1 / mid / 15; title longest word; all bg colors; cutout render; print-file full res.

## Open loops (whole project)
- [ ] **Margin numbers** (AOV / POD base / ship) → lock break-even ROAS in the FB/TikTok/Google testing docs.
- [ ] **Vectorize method** test → fill in TASK-MKT-010 Cách 1.
- [ ] Decide: recreate per-product vs build only validated winners (spy tools).

## Key facts to remember
- Competitor previews = 100px, print-res 403-blocked → must recreate (AI-recreate validated: Nano Banana Pro, 2K, headless prompt in `_BATCH-RECIPE.md`).
- Personalizer = Teeinblue; competitor uses buildyou.io.
- Clipart license (if buying): Creative Fabrica (Full POD, uncapped) primary; Vexels = design platform (not element seller).
