# 2026-11-18/19 — Video team, frameworks, ads database, Hook Lab

## Built (all committed on product-research)
- **Video team** (`research/reference/video-team/README.md`): 00A concept ideator · 00B concept critic · 00C concept selector · GATE 0 (user) ·
  01 hook ideator · 02 hook critic · 03 hook selector · 04 script editor · 05 visual director · 06 editor · 07 QA. Agents `.claude/agents/vt-*`,
  run `/video:new`. Tool-agnostic; tool prompt craft lives in `research/reference/video-team/adapters/`.
- **Frameworks**: `hook-framework.md` (format F1–F15 × trigger T1–T10, fake-reality rules) and `concept-framework.md` (core AN/BY/RC×OC,
  execution ST/PV/PF/PX/RV/EM, hook elements, testing ladder R0–R4). All codes in `marketing/facebook-ads/_ledgers/codebook.csv` (137).
- **Naming convention** (README §4a): ad key `MJ4U-003_R0_K01X1-H07_E0_v01` in the Meta ad name; files add `_916`/`_45` before the version.
- **Ads database**: Supabase `mj4u-ads` (`marketing/facebook-ads/db/README.md`). Daily 15:00 (=00:00 PST) launchd sync stores all 84 Meta
  insight fields raw + typed columns; `db_sync.py rebuild` re-derives from raw; `sync_runs` heartbeat. Only registered (framework) ads are stored.
- **Hook Lab**: https://mj4u-hook-lab.vercel.app (email OTP; viewers in `dashboard_viewers`). Groups results by any code, aliasing warning,
  real-vs-noise check, ad previews from Meta.
- **Fixed**: Meta action aliases were summed (ATC over-counted 3–5×) in db_sync and the engine's `rules.py`.
- **User rulings**: no AI-performer disclosure; relationship hooks ("Your granddaughter…") allowed; music = AI-generated (confirm paid plan);
  old MJ4U-111 ads and the hand-made suncatcher Phase 1 records removed (archived: `_ledgers/archive/2026-11-suncatcher-pre-pipeline/`).

## RESUME: rerun the suncatcher through the full pipeline (fresh session)
Run `/video:new MJ4U-003` starting at **0b Concepts (00A)**. Product = MJ4U-003 (pet memorial suncatcher).
- Inputs ready: product photos/lettering + 4K panel stills, approved AI music, brand kit (see archived README + `marketing/facebook-ads/suncatcher-phase1/`).
  Old renders/shots on Drive may be **reused as references**, but concepts/hooks/scripts must come from the roles.
- **Plan-page conflict to raise at GATE 0**: the plan page (test authority) still locks concepts 01/02/06 × hooks H1/H2. The new slate is
  approved by the user at Gate 0, then the plan page is updated. Do not restructure silently.
- Budget numbers: hook-rate read ≈ $11 (big diff) – $44 (small diff) per arm at CPM $13 (ad-science §5b).
