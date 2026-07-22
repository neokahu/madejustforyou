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

### 1. Get the REAL print size (blocker for everything)
- [ ] Import pajama **product base** from fulfillment provider (Teeinblue → Product Base → import).
- [ ] Record **Printarea Key + Size (px) @ 300 DPI**. All-over pajama = large (seamless tile OR cut-sew panel). Write it here: `________ × ________ px`.

### 2. QC the 16 AI characters
- [ ] Open `05-ai-recreate-test/` — check EACH: single-line limbs (not filled), **headless**, colors/pose match.
- [ ] Confirm char10 & char11 fixed. Regenerate any bad one from `_BATCH-RECIPE.md` (reuse limb-fix prompt).

### 3. Prep characters → transparent PNG (TASK-MKT-010)
- [ ] Background-remove each of the 16 (Recraft remove-bg or Photoshop) → transparent PNG.
- [ ] Align each character's head/neck to ONE common **face-slot anchor** (so 1 face-slot fits all 12).

### 4. Rebuild the design in Photoshop AT CORRECT SIZE (Claude can do this)
- [ ] Rebuild base at the imported printarea size: background color (6 variants) + navy stars + palm silhouettes + title.
- [ ] Title: reserve width for LONGEST word ("POP POP" / 15-char custom); BEST/EVER static; middle word is a placeholder (real text = Teeinblue layer).
- [ ] Mark head-anchored face-slots + character positions for BOTH layouts: **Tile A (1–10)** and **Tile B (11–15)**.
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
