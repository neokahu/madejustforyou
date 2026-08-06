# Teeinblue — Assets & Personalization Mechanics (verified)

**What this is:** the authoritative reference for how Teeinblue's Assets and layer
personalization actually work — so builds and SOPs stop guessing. Every claim below is
verified against the official docs (support.teeinblue.com) + the store's own portal, July 2026.

Companion files:
- Asset library (files + owner index): [`/library/personalizer/`](../../library/personalizer/ASSET-SYSTEM.md)
- Tool fit / verdict: [`teeinblue.md`](teeinblue.md)
- SOPs (separate `sop-docs` repo): TASK-MKT-007 (prep), TASK-MKT-008 (campaign),
  TASK-MKT-012 (organize/name), TASK-MKT-013 (upload + image-option→text)

---

## 1. Asset Types (fixed by the app)

The **Assets** menu has these types. "Category" is grouping *inside* a type.

| Teeinblue Asset Type | Holds | Category depth | Key facts |
|---|---|---|---|
| **Clipart Categories** | images **placed onto** a layer (characters, background images) | **multi-level** (parent → sub) | Upload **transparent** art → app **auto-generates a white-bg thumbnail**. Original is never shown on storefront (only used to render the order file). **Reposition applies to the whole category** → pre-size/anchor in Photoshop before upload. |
| **Vector Categories** | vector (SVG) cliparts | multi-level | vector variant of clipart |
| **Additional Options** | form choices that **add NO layer**; drive **conditional logic** | **1 level only** | You **upload a thumbnail per item**. 5 display modes: Thumbnail Images (default), Dropdown Option Name, Dropdown + Thumbnail, Inline Radio Button, Radio (+ "show name on hover"). |
| **Color Categories** | a set of colors for a **TEXT layer's color** | 1 level | **NOT** for backgrounds. |
| **Font Categories** + **Upload Fonts** | fonts (Google or uploaded) | 1 level | Needed to let a customer change font. |
| **Global Options** | an option defined **once, reused across artworks/layers** | — | central library; edit in one place. |
| **Map Styles** | styles for the Maps feature | — | |

**Backgrounds** are **not** Color Categories → use a **Clipart Category of background images**
(the docs' own example) or a base color layer.
**Face photo** is **not** an Asset → it's the **"Upload photo"** option on a layer.

---

## 2. How a layer becomes personalizable

Click the pencil on a layer → pick one option:
1. No personalization
2. **1 Clipart category**
3. **1 Group of clipart categories** (parent + sub-categories → multi-level picker)
4. **Upload photo** (customer photo; supports face cutout via Cutout.pro etc.)
5. Maps · 6. Star Maps
7. **Share option with another layer** — for **repeated-pattern products (socks, shoes, all-over
   pajamas)**: link layers so the customer chooses once and it applies to every repeat.
8. Toggle show/hide layer

Plus, separately: **Text personalization** and **Additional Options**.

---

## 3. The "image picker but renders text" pattern (Title)

An Additional Option **renders nothing**. A Text layer **cannot** populate from an Additional
Option (auto-populate only pulls from Maps / Star maps / Song / Moon / Custom-text `{{value}}`).
So there are two documented ways:

**Route A — live text (matches competitor; custom works cleanly):**
1. Additional Option `Titles`, display = **Thumbnail Images**, each item (`Dad`, `Papa`…) gets a
   **thumbnail** = the white square word tile.
2. In the artwork, add **one Text layer per preset word** (font Impact, auto-scale max width,
   char limit 15), each with **Conditional = `Titles` equals that item**.
3. Add **one Custom Text layer** (Allow personalized = input), Conditional = `Titles` = `Custom`.
4. Enable **Show on first load** on exactly one.
5. Repeats (7 title positions) → **Share option with another layer**.
- Cost: ~9 conditional text layers per title slot (once, then shared).

**Route B — placed images (fewer layers):**
- Presets = a **Clipart Category** of transparent word-images (placed on the slot; auto-thumbnails)
  + one conditional Custom Text layer. Presets are images, not live text.

---

## 4. Clipart specifics
- Multi-level hierarchy: set a **Parent Category** to nest; "1 Group of clipart categories" shows
  sub-categories as a two-step pick on the form.
- **Upload transparent PNG**; app auto-trims + makes a white thumbnail. You *can* override the
  thumbnail per clipart.
- **Reposition is per-category** — you edit the first clipart and all others inherit it → so all
  members must share size/shape/anchor. Pre-arrange in Photoshop (esp. face-slot: all bodies'
  head/neck at one common anchor).
- **Upload limits:** ≤64 MB and ≤64 megapixels per file (rec <32 MB). **Bulk upload = ZIP ≤512 MB,
  max 2 zips at a time.**

## 5. Additional Options specifics
- "An extra selection only shown on the form; adds no layer." Used to ask a question and to
  **drive conditional layers** (e.g. Number of people, choose pet dog/cat, hair color → hairstyle).
- **One level only** (no sub-categories) — unlike Clipart.
- Create: `Assets → Additional Options → New Category` → add items via **Item name → +Add new**.
- In artwork: `+ → Additional Option` → link the category, set Title, default value, Mark required.
- Then add image/text layers with **Conditional Settings** keyed to the option's items.

## 6. Text layer capabilities
- Default text, color (**Color Picker** or **Color Category**), font (**Font Category** for choice).
- **Auto scale when text too long** (set max frame-width; ~500–600px suggested for names).
- **Input type:** all characters / numbers / date picker / custom rules (allow/block char sets).
- Input case, **character limit**, prefix/suffix, stroke, letter spacing, alignment.
- **Populate values from other options:** only Maps `{{place_name}}`, Star maps, Song `{{title}}`,
  Moon `{{date...}}`, and Custom-text `{{value}}` / `{{value.Xchar}}`.
- **PSD text imports** and converts to a Teeinblue text layer (re-check font after).
- **Paragraph** text = fixed container, wraps + auto-scales down to fit.

---

## 7. NV984 "Best Dad" pajama → mapping

| Customer sees | Teeinblue type | Category | Render |
|---|---|---|---|
| Character (per kid) | Clipart Categories | Characters → Crayon Kids / Crayon Pets | placed (transparent) |
| Title | Additional Options | Titles → Dad & Grandpa (item thumbnails) | Route A: conditional Text layers + Custom input |
| Number of Kids/Pets | Additional Options | Number of Kids/Pets 1–15 | drives conditional (Tile A 1–10 / B 11–15); no render |
| Background | Clipart Categories (bg images) or base layer | Backgrounds | swaps bg |
| Font | Font Categories / Upload Fonts | Display → Impact | — |
| Face photo | layer "Upload photo" | — | cutout into head slot |
| 7 title repeats + figures | "Share option with another layer" | — | one pick → all repeats |

---

## 8. Sources
support.teeinblue.com articles: `upload-and-edit-cliparts`, `hierarchy-of-clipart-categories`,
`display-settings-of-clipart-category`, `in-depth-guide-regarding-additional-option-feature`,
`personalization-options-for-layers-in-artwork`, `add-text-text-personalization`,
`auto-populate-values-from-other-options-maps-star-maps`, `color-categories`,
`global-options-reuse-options-across-artworks`, `about-fonts`. Portal-confirmed: Additional Option
display modes + 1-level categories (screenshot, Jul 2026).
