# Session Handoff — 2026-07-10 · session-01

> **Inherits from:** _(none — first session)_
> **The latest handoff is the source of truth.** Each new session copies the still-true state
> forward into a new dated file (see [`README.md`](README.md)), so no context is lost.

## What this project is
MadeJustForYou = Shopify **print-on-demand personalized-gift** store (website handled by a
freelancer). The priority is a **systematic design-idea research & testing workflow** to replace
ad-hoc competitor spying. This session built that workflow **and** ran it end-to-end on the first
occasion.

## What got built this session

### 1. The research playbook (`research/`)
A documented, repeatable pipeline: **Discover → Generate → Score → Brief → Validate → Learn.**
- `README.md` — hub, cadence, automation map, 7 principles
- `01-dimension-libraries.md` — product/recipient/occasion/personalization/angle vocabularies
- `02-signal-sources.md` — 7 demand signals + exact tools/queries (now proven)
- `03-scoring-rubric.md` — weighted 6-criteria scoring
- `04-validation-testing.md` — test tiers + **design-vs-product = two sequential experiments**
- `05-idea-crafting.md` — the **idea engine** (mechanic + angle + hook + aesthetic); demand data
  filters & supplies vocabulary, it does NOT generate the design
- `templates/` — idea-database.csv, design-brief.md, experiment-card.md
- `occasions-calendar.{md,csv,ics}` + `build_calendar.py` — US occasions with start-sell (−2mo) &
  last-order (−14d) dates

### 2. Grandparents Day 2026 sprint (`research/sprints/`) — ran live, real data
- **Search** (Ahrefs US), **marketplace velocity** (Etsy in-cart via Apify), **social**
  (Pinterest saves + TikTok plays via Apify) — all live-pulled, scored into `idea-database.csv`.
- **16 ideas scored, 4 greenlit:** GPD01 grandma names mug (4.24) · GPD02 birth-flower sweatshirt
  (4.15) · GPD15 recipe keepsake (4.06) · GPD07 "First Dad Now Grandpa" mug (4.03).
- `2026-09-grandparents-day.md` (sprint report), `2026-09-grandparents-day-concepts.md` (12 crafted
  concepts w/ reference links), `competitor-intel-2026-07.md` (macorner/wanderprints targeted pull).
- **Mockups** (`mockups/`) + **4K concept design files** (`print-files/`) for the leads, incl. a
  3-way metaphor set (Garden / Birds / Night Sky).
- **Tier-1 test plan + captions** (`tier1-test-plan-gpd02.md`) + filled experiment card.

### 3. Tooling research (`research/tools/teeinblue.md`)
Teeinblue chosen as the Shopify personalizer. Confirmed **Conditional Logic + Clipart** is the
engine for "one-motif-per-grandchild"; **PSD import**; auto print-file → 30+ PODs. $49/mo + usage.

## Key decisions & insights (the "why")
- **Demand data = filter + vocabulary, not idea generator.** Craft designs via the idea engine.
- **Test design first (one cheap product), then product** — don't confound the two variables.
- **Text must be a customer-customizable dynamic layer**, never baked in. Variable child count →
  designer-built **consistent component library** assembled by Teeinblue conditional logic. **AI is
  reference-only** (can't guarantee count-accurate, consistent motifs; RGB no-alpha; raster text).
- **Recency matters:** Ahrefs volume (monthly) + Etsy in-cart are current; Pinterest/TikTok counts
  are lifetime (flagged). **Meta Ad Library `is_active:true` = present-tense spend** (best signal).
- **White space found:** competitors don't actively advertise a grandma names-mug or recipe
  keepsake → GPD01 + GPD15 are their blind spot.
- **Reference-linking is a standard step** (principle #7): every idea/concept links its sources.

## State
- Git: clean, all pushed to `github.com/neokahu/madejustforyou` (branch `main`).
- Note: `print-files/` adds ~88 MB of 4K PNGs to the repo (offered git-LFS/gitignore if unwanted).

## Open items / next steps (in priority order)
1. **Run the Tier-1 metaphor test** (Garden vs Birds vs Night Sky, same sweatshirt) — validate before
   paying a designer. Plan + captions + experiment card are ready.
2. **Designer brief for the winning metaphor** — 12 birth-flower component spec + Teeinblue
   conditional-logic/layer setup (not yet written — offered).
3. **Confirm Teeinblue per-order fee tiers** in-app and fold into margin/CPA gates.
4. **Fall cluster sprint** (Boss's Day / Sweetest Day / Halloween — sell-by windows open mid-Aug).
5. **Set up the weekly cadence** so this runs as an ongoing engine, not a one-off.

## Reusable Apify datasets (for refreshing reference links)
Etsy `Tr77mPjhVXXMyjLep` · Pinterest `eAn1JJqoqnxQ93lE9` · TikTok search `obrCNbh1kei0EvuFn` ·
TikTok profiles `RA4bBRCO2vYZhmzod` · Meta ads `LkEZN8wCuJbwQYECm`.
