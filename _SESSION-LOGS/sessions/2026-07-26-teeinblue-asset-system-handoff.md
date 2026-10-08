# Session Handoff — 2026-07-26 · Teeinblue asset system, SOPs, asset↔git split

Inherits from `2026-07-20-pajama-clone-handoff.md` (NV984 pajama build state).

## Achieved
- **Pajama base PSD finished** (`product-clone/NV984-pajama/02-photoshop-build/leg-master-1to10.psd`, 6335×7057 @300): proper **crown** (band + 3 points + dot finials, not the earlier "mountain"), **real palm silhouettes** (AI-gen placed, Multiply), **irregular 50-star field**, `BEST / TITLE_var(max15) / EVER` titles. Built via Photoshop MCP `execute_script`.
- **Clipart prepped:** 16 character bodies → transparent (`06-bodies-transparent/`, pets flood-filled solid); vectorized set organized (`07-vector-cliparts/`, kid-01..11 + pet-01..04, svg+png).
- **Generated option art:** numbers **1–15** and **9 title words** (Dad…Custom Yours) as square 1:1 navy tiles.
- **Built the asset-library system** `teeinblue-assets/` — mirrors Teeinblue's real Asset types; `ASSET-SYSTEM.md` (rules) + `asset-registry.csv` (owner index) + per-category defs.
- **Researched Teeinblue official docs** → `research/tools/teeinblue-assets-guide.md` (verified mechanics; replaces guesswork).
- **SOPs (sop-docs repo):** added **TASK-MKT-012** (asset organize/name) + **TASK-MKT-013** (upload + image-option→text); rewrote **010** into a general reverse-engineer→recreate method; fixed factual errors in **011**; made asset-naming a real **step** in **007** (Bước 6 + gate); cross-linked **008**.
- **Created `PROJECT-INDEX.md`** (root map of the whole project).
- **Asset↔git split live:** assets → **firebits Google Drive** (`gdrive:madejustforyou`, via rclone); docs/code → GitHub. Untracked 130 old binaries (kept on disk + Drive); `.gitignore` now excludes image types.
- **Created universal `session-handoff` skill** (`~/.claude/skills/session-handoff/`).

## Learnt / decided (with evidence)
- **Teeinblue asset mechanics — VERIFIED** (source: support.teeinblue.com articles; full detail in `research/tools/teeinblue-assets-guide.md`):
  - Clipart Categories = images **placed** on a layer; **multi-level** parent/sub; **upload transparent → app auto-makes white thumbnail**; reposition is per-category (pre-size in PS).
  - Additional Options = form control, **adds no layer**, **1 level only**, **upload a thumbnail per item**, 5 display modes (confirmed via portal screenshot).
  - **Color Categories = text color, NOT background** (bg = Clipart bg-image or base layer).
  - **Image-picker→text render:** Text layer **cannot** populate from an Additional Option (only Maps/Star/Song/Moon/Custom `{{value}}`). → presets render via **conditional Text layers per item + a Custom text input** (Route A), or clipart word-images (Route B).
  - Repeated all-over patterns link via **"Share option with another layer."**
- **Photoshop MCP `execute_script` gotcha:** no `#target` line, must use explicit `return` (IIFE wrapper) or it fails silently. Evidence: DIAG test docs this session.
- **Pajama print size = 6335×7057 @300 DPI**, cut-and-sew leg panels. Evidence: Teeinblue product-base import table (user screenshot).
- **Memory is unreliable here → persist to DOCS** (user feedback). Acted on: moved Teeinblue facts to the research guide; deleted the redundant memory file.
- **Assets live in firebits Drive via rclone**, not gmail, not the local mount (user instruction).

## Next session — TODO
1. **Build the Teeinblue campaign** (TASK-MKT-008 + 013): import product base → upload Characters (Clipart, transparent) → Title & Number as **Additional Options** (thumbnails) → **conditional Text layers** for title render + Custom input → Upload-photo (face cutout) → **Share option** across the 7 title repeats. Acceptance: form shows image tiles, presets+custom render correct text, number drives figure count.
2. **Tile B (11–15)** layout variant for the pajama.
3. Fill in **background hex values** for Blue/Grey/Green/Red in `teeinblue-assets/Color-Categories/Backgrounds.md` + registry (currently `tbd`).
4. Optional polish: **distressed/grunge font+texture** on pajama titles.
5. **Send the homepage mobile-carousel spec** to the dev (spec already written — see this session's chat; 4s autoplay, 1-card/slide, pause-on-swipe, dots, reduced-motion).

## Open decisions — waiting on user
- **Title render: Route A** (conditional text layers, live text) **vs Route B** (clipart word-images)? Affects campaign build.
- **Renumber TASK-MKT-013 → TASK-MKT-008.001**? (It's a detailed step inside 008, per the sub-task convention.)
- Align **"Duplicate & Link" → "Share option with another layer"** term in TASK-MKT-008 Bước 4?
- **Doc status → "active":** requested but interrupted; most SOP docs are already `Hiệu lực`. Re-confirm scope.

## Where things live
- Root map: `PROJECT-INDEX.md`
- Teeinblue how-it-works: `research/tools/teeinblue-assets-guide.md`
- Asset library + index: `teeinblue-assets/ASSET-SYSTEM.md` + `asset-registry.csv`
- Pajama build: `product-clone/NV984-pajama/` (02 psd, 06 transparent bodies, 07 vectors) — **binaries now in Drive**
- SOPs: `sop-docs/Tasks/MKT/TASK-MKT-007..013`, `Workflows/MKT/WF-MKT-005`
- Assets (binary): **firebits Drive `gdrive:madejustforyou/`** (269 files)

## Repos / sync state at handoff
- **madejustforyou** GitHub `neokahu/madejustforyou` — HEAD **ba80c27** (clean, pushed)
- **sop-docs** GitHub `neokahu/sop-docs` — HEAD **c0ba8dc** (clean, pushed)
- Firebits Drive `gdrive:madejustforyou` — **269** files (matches local, verified)
