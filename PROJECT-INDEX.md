# MadeJustForYou — Project Index

Map of everything in this repo and how it connects. **Start here.** When something moves or a new
area is added, update this file.

MadeJustForYou = Shopify print-on-demand **personalized-gift** store. The live site/theme is handled
by a freelancer; this repo is the **research, design/asset production, and personalizer-build**
workspace. Personalizer app = **Teeinblue**. Fulfillment = POD providers via Teeinblue.

---

## Top-level map

| Path | What it is |
|---|---|
| **`PROJECT-INDEX.md`** | this file — the map |
| **`README.md`** | short repo note |
| **`research/`** | the core: idea research system, occasion calendar, sprints, tool guides |
| **`teeinblue-assets/`** | production-ready personalizer assets + the library system (mirrors Teeinblue) |
| **`product-clone/`** | per-product build pipelines (reference → design → clipart → Teeinblue) |
| **`product-tracker/`** | ops tracker: each product's pipeline status (design → freelancer → live → ads) |
| **`sample-products/`** | one-off sample design mockups |
| **`category-covers/`** | storefront category cover images |
| **`assets/`** | brand/social assets (e.g. `assets/social/` Facebook cover, welcome post) |
| **`_SESSION-LOGS/`** | session handoffs (latest working state) — **read before resuming** |
| **`handoffs/`** | older session handoffs (pre-`_SESSION-LOGS` convention) |
| **`MadeJustForYou_design_system.html`** | exported brand/design-system reference |
| **`Grandparents-Day-Checklist.md`** | campaign checklist |
| **`THEME-REPO.md`** | 👉 pointer — the Shopify **theme code** lives in a **separate repo** (`~/Desktop/projects/madejustforyou-theme/shopify-theme-1/`), not here |

**Brand palette** (from theme repo `config/settings_data.json`): terracotta `#C15F3C`, gold `#E0A458`, dusty rose `#D98E85`,
cream `#FBF6EE`, sand `#EFE4D4`, espresso `#2E2822`, taupe `#8A7E70`. Fonts: Playfair Display
(heading), DM Sans (body), Caveat (script).

---

## `research/` — idea research & testing system

The real priority: a systematic engine to find + validate design ideas before building.

Structure: stable **playbook** (`method/ reference/ templates/ scripts/ calendar/`) is separated
from **living sprint work** (`sprints/`). See `research/README.md` for the folder map.

| Path | Purpose |
|---|---|
| `research/README.md` | how the research system works + folder map |
| `research/method/0-foundation…4-validate.md` | the methodology, filenames = pipeline stages (0 dimensions · 1 discover · 2 generate/idea-engine · 3 score · 4 validate) + `new-ad-potential-scorecard.md` |
| `research/reference/` | **VERIFIED Teeinblue mechanics** (`teeinblue-assets-guide.md` — source of truth, don't re-guess) + `teeinblue.md` (fit/verdict) |
| `research/templates/` | design-brief, experiment-card, idea-database templates |
| `research/scripts/` | all code: `score_concepts.py`, `score_ads.jq`, `score_gpd.py`, `build_calendar.py` |
| `research/calendar/` | gifting-occasion calendar (`occasions-calendar.{md,csv,ics}`) |
| `research/sprints/` | live work, one folder per sprint (see `sprints/README.md`); each greenlit concept is a self-contained sub-folder (e.g. `2026-09-grandparents-day/GPD02-garden-birds/`) |

---

## `teeinblue-assets/` — personalizer asset library

Mirrors Teeinblue's Asset structure so uploads are drag-a-folder. See
[`teeinblue-assets/ASSET-SYSTEM.md`](teeinblue-assets/ASSET-SYSTEM.md) for the rules.

```
teeinblue-assets/
├── ASSET-SYSTEM.md              taxonomy + naming rules (top level = Teeinblue Asset Types)
├── asset-registry.csv           owner's index of every asset (code → type → category → file)
├── Clipart-Categories/          images PLACED on design (transparent PNG + SVG)
│   └── Characters/{Crayon-Kids (CRK-01..11), Crayon-Pets (CRP-01..04)}/{png,svg}
├── Additional-Options/          form choices w/ item thumbnails (no layer; drive conditional)
│   ├── Titles/Dad-Grandpa/png   9 word tiles (dad…custom-yours) + Relationship-Titles.md
│   └── Numbers/Digits-1-15/png  1..15 tiles + Counts.md
├── Color-Categories/            text-color sets (Backgrounds.md = note: bg is clipart, not here)
├── Font-Categories/             fonts (Impact = title)
├── Vector-Categories/           (SVG cliparts, when used)
└── Layer-Types/                 Photo-Faces.md (Upload-photo layer note; not an Asset)
```

**Rule of thumb:** placed image → Clipart Categories (transparent). Form choice shown as tiles →
Additional Options (upload thumbnail per item; render via conditional text/clipart layers).

---

## `product-clone/` — per-product build pipelines

### `NV984-pajama/` — "Best Dad/Grandpa Ever" all-over pajama (active build)
Cut-and-sew, 2 leg panels; **master print size 6335×7057 @300 DPI** (4XL max).

| Stage | Contents |
|---|---|
| `01-reference/` | scraped listing, mockups, size chart, print spec |
| `02-photoshop-build/` | `leg-master-1to10.psd` (base: bg + palms + stars + BEST/EVER + crowns + 10 slots), `assets/palm-silhouette.png` |
| `03-clipart-candidates/` | style research |
| `04-competitor-cliparts/` | competitor previews + `vectorized/` traces (reference only) |
| `05-ai-recreate-test/` | 16 AI-recreated bodies (on white) + `_BATCH-RECIPE.md` |
| `06-bodies-transparent/` | 16 bodies bg-removed → transparent, pets solidified (`_pre-fill-backup/`) |
| `07-vector-cliparts/` | vectorized transparent set (kid-01..11, pet-01..04) svg+png |

### `legend-husband-dad-grandpa/` — Legend shirt clone (reference SVG + font IDs)

---

## Related: `sop-docs` (SEPARATE repo)

Operational SOPs live in `../sop-docs` (Vietnamese; framework Task/Workflow/Process, IDs
`{TYPE}-{DEPT}-{NNN}`). Teeinblue-related:
- **WF-MKT-005** upload product workflow
- **TASK-MKT-007** prepare assets · **TASK-MKT-008** build campaign · **TASK-MKT-009** QC & launch
- **TASK-MKT-010** replicate clipart · **TASK-MKT-011** personalization patterns
- **TASK-MKT-012** organize/name assets · **TASK-MKT-013** upload + image-option→text
Routing: reusable, org-level operating procedures → `sop-docs`. Project-specific research/assets →
this repo.

---

## Where to start for a task
- **Resume work** → newest file in `_SESSION-LOGS/`
- **How Teeinblue works** → `research/reference/teeinblue-assets-guide.md`
- **Add/find an asset** → `teeinblue-assets/ASSET-SYSTEM.md` + `asset-registry.csv`
- **Build the pajama** → `product-clone/NV984-pajama/` + `_SESSION-LOGS/2026-07-20-pajama-clone-handoff.md`
- **New design idea** → `research/` (README + method/ + templates/)
