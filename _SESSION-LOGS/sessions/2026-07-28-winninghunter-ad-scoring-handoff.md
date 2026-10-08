# Session Handoff — 2026-07-28 · WinningHunter + ad-scoring framework + PSD-anchor gap

Inherits from `2026-07-26-teeinblue-asset-system-handoff.md`.

## Achieved
- **PSD → Drive-only rule locked.** PSD design sources are NOT in git (too heavy); `.gitignore` keeps all binaries out; git is docs-only. PSDs live on disk + firebits Drive.
- **Attempted character-body anchor fix** (so one face-slot fits all bodies). Automated erosion/torso detection **failed** — bodies are too inconsistent (scribble torsos, varying scale/neck). See "Open" below.
- **Connected WinningHunter MCP** (competitor ad/store/revenue spy) → `.claude.json` local config, key from `~/.global-keys.env`. Verified via direct curl: 33 tools, 1000 credits, auth OK. Pulled the 10 tracked brands.
- **Built a research-grounded ad/product replication framework** → `research/new-ad-potential-scorecard.md`. Two tracks (Evergreen + Trending), cited methodology (delegated deep-research agent, ~15 sources), thresholds marked [CALIBRATE].

## Learnt / decided (with evidence)
- **PSD/binaries → Drive only** (user: too heavy for git). Force-pushed to drop the 30MB blob from history.
- **Framework must be research-based, not my judgment or raw tool data** (user directive). Acted on: ran a deep-research agent; framework now cited. Key findings (see doc PART 1–4 for sources):
  - Ad run-time = real but imperfect profit proxy; needs a scaling co-signal (rising active-ads/variants). Judge longevity at TEMPLATE level (creative fatigue caps single-creative age ~1–8 wks).
  - Saturation: **margin + differentiation beat raw competitor count** (228-product dataset r≈0.08). Our personalization mechanic = the differentiation → can enter proven-but-crowded templates.
  - Evergreen vs Trending diagnosed from Google Trends curve shape (5yr durability + 90d momentum).
  - Competition unit = concept/template, not SKU (custom gifts rarely exact-copied).
- **WinningHunter is just the signal source**, not the methodology.
- **Two revenue engines, both used:** Evergreen (durable long-runners, foundation ~70%) + Trending (emerging, upside ~30%).

## Next session — TODO (ordered)
1. **RESTART the session** so native `mcp__winninghunter__*` tools load (added mid-session = not callable until restart).
2. **Calibrate the scorecard thresholds against DATA** — the #1 job: back-test scorecard vs the 10 tracked brands' actual history + your last ~20–30 launched concepts (win/breakeven/loss from sales data). Replace every [CALIBRATE] number with a data-derived value. (`analyze_tracked_brand`, `scan_ad` days-running, active-ads growth.)
3. **Fix character-body anchors** (blocker for the pajama face-slot) — automated failed; do manual alignment in Photoshop OR regenerate the 11 kid bodies from ONE controlled template (consistent neck position/width/scale). Recommended: regen. See prior handoff.
4. Then resume **Tile A Teeinblue build** (guide already written in chat / TASK-MKT-013): Clipart(chars) + Additional Options(Title tiles→conditional text, Number) + Share-option repeats + Upload-photo.

## Open decisions — waiting on user
- Character bodies: **manual align vs regenerate** (I recommend regenerate to a fixed template).
- Title render **Route A (conditional text layers) vs B (clipart word-images)**.

## Where things live
- Ad framework: `research/new-ad-potential-scorecard.md`
- Teeinblue mechanics: `research/tools/teeinblue-assets-guide.md` · Map: `PROJECT-INDEX.md`
- Assets (binary incl. PSD): firebits Drive `gdrive:madejustforyou/` (269 files) via rclone
- WinningHunter: MCP `winninghunter` (local), key in `~/.global-keys.env`

## Repos / sync at handoff
- **madejustforyou** `neokahu/madejustforyou` — HEAD **b15f187** (clean, pushed)
- **sop-docs** `neokahu/sop-docs` — HEAD **c0ba8dc** (clean, pushed)
- Firebits Drive — **269** files (verified)
