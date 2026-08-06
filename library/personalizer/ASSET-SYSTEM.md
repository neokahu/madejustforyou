# Teeinblue Asset Library System

One taxonomy for **every** customizable asset in Teeinblue — clipart, text/name lists,
fonts, colors/backgrounds, number ranges, photo slots, generators. So any asset has a
predictable home and naming, and new staff never have to guess.

**Teeinblue is the source of truth** staff use daily. This repo is the master-art backup
+ the owner's private index (`asset-registry.csv`). The *rules* below are what everyone
follows inside Teeinblue.

---

## The address of any asset

```
[ASSET TYPE] → Parent Category → Category → Item
```
- **Asset Type** — one of Teeinblue's fixed Asset-menu buckets (below). Never invented.
- **Parent Category / Category** — how we group *inside* a type. Clipart supports multi-level
  parent→sub natively; Additional Options are 1 level only.
- **Item** — the individual asset.

### Teeinblue Asset Types (fixed by the app — verified from docs)

| Teeinblue type | Holds | Category depth | Key fact |
|---|---|---|---|
| **Clipart Categories** | images placed onto a layer (characters, bg images) | multi-level | upload **transparent** → app auto-makes white thumbnail; reposition applies to whole category |
| **Vector Categories** | vector (SVG) cliparts | multi-level | vector variant of clipart |
| **Additional Options** | form choices that add **no layer** (drive conditional) | **1 level** | you upload a **thumbnail per item**; 5 display modes (Thumbnail default) |
| **Color Categories** | colors for a **text layer's color** (not bg) | 1 level | |
| **Font Categories / Upload Fonts** | fonts (Google or uploaded) | 1 level | |
| **Global Options** | an option defined once, reused across artworks | — | |
| **Map Styles** | styles for the Maps feature | — | |

*Internal codes (registry only):* `CLP-` clipart, `AO-` additional option, `FNT-` font, `CLR-` color.
Background swaps live in **Clipart Categories** (bg images) or a base color layer — **not** Color Categories.
Face upload is a **layer option** ("Upload photo"), not an Assets library.

---

## Naming code (every item)

`{TYPE}-{CATCODE}-{NN}[-descriptor]`

- **TYPE** = internal prefix by Teeinblue type (`CLP` clipart, `AO` additional option, `FNT` font, `CLR` color)
- **CATCODE** = short code for the Category (unique within its type)
- **NN** = zero-padded index
- **descriptor** = optional human hint

Examples: `CLP-CRK-01-blue-green` · `AO-TTL-05` (=Papa item) · `AO-KP-15` · `CLP-BGP-02` (=Black bg).

The customer-facing Teeinblue name can stay simple ("Kid 1", "Papa"); the **code** is the
internal handle in the registry.

---

## Worked example — everything the NV984 "Best Dad" pajama needs

| Customer sees | Teeinblue type | Category | Render |
|---|---|---|---|
| Character (per kid) | **Clipart Categories** | Characters → Crayon Kids (`CRK`) | placed on slot (transparent art) |
| Pet | **Clipart Categories** | Characters → Crayon Pets (`CRP`) | placed on slot |
| Title | **Additional Options** | Titles → Dad & Grandpa (`TTL`, item thumbnails) | conditional **Text layers** per preset + Custom text input |
| Number of Kids/Pets | **Additional Options** | Number of Kids/Pets 1–15 (`KP`) | no render — drives conditional (Tile A 1–10 / B 11–15) |
| Background | **Clipart Categories** (bg images) or base layer | Backgrounds (`BGP`) | swaps bg |
| Text color (if offered) | **Color Categories** | — | text color |
| Title font | **Font Categories / Upload Fonts** | Display → Impact (`DISP`) | — |
| Face photo | layer option **Upload photo** | — | cutout into slot |
| Repeats (7 titles etc.) | "Share option with another layer" | — | one pick → all repeats |

Full item list → [`asset-registry.csv`](asset-registry.csv). Config-type details →
the `.md` inside each type folder (`Text/`, `Colors/`, `Numbers/`, `Photo/`).

---

## Folder mirror (matches Teeinblue)

```
library/personalizer/
├── ASSET-SYSTEM.md         these rules
├── asset-registry.csv      owner's private index (all types)
├── Clipart/   <Parent>/<Category>/{png,svg}
├── Fonts/     <Category>/            (font files)
├── Colors/    <Category>.md          (hex lists)
├── Text/      <Category>.md          (word lists)
├── Numbers/   <Category>.md          (ranges + conditional notes)
└── Photo/     <Category>.md          (upload slot + effect spec)
```

---

## How to ADD any asset (new-person checklist)

1. **Pick the Asset Type** (one of the 7 — never invent a new type).
2. **Find the home:** which Parent Category → Category (by *what it is + style/scope*, not
   by product)? Reuse if it exists.
3. **New Category** only if that set truly doesn't exist → pick a free CATCODE.
   **New Parent Category** → sign-off (keep the top level short).
4. **Name it** `{TYPE}-{CATCODE}-{NN}`.
5. **File-based** (CLP/FNT): drop the file in the matching folder. **Config-based**
   (TXT/CLR/NUM/PHO/GEN): add/append its `.md` definition.
6. **Build it in Teeinblue** under the matching Type → Parent → Category.
7. *(owner)* add a row to `asset-registry.csv`.

---

## Why this scales
- **One address scheme** for clipart, text, color, number, photo, font — no per-type invention.
- **Reuse over duplication:** the Title word-list or Background-6 set is built once, reused
  on every product that needs it.
- **Predictable:** "it's a background color" → CLR → Backgrounds → (set). Always.
- **Product-agnostic:** assets live by what they are, so a new product just wires existing
  categories together.
