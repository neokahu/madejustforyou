# Sprints — living research work

One folder per sprint. Each sprint holds its own research docs; each **greenlit concept** is a
self-contained sub-folder (brief + specs + experiment card + `_assets/`). Finished reusable
component libraries **graduate** to the repo-root `library/personalizer/` (so a library isn't trapped
in one sprint).

## Convention
```
<YYYY-MM>-<sprint-name>/
├── README.md              # the sprint doc (scope, findings, greenlit ideas)
├── <supporting docs>.md   # competitor spy, concepts, links, test plan…
├── <CONCEPT-id>-<slug>/   # one folder per greenlit concept
│   ├── STATUS.md          # build checklist for this concept
│   ├── brief.md           # the design brief
│   ├── <specs>.md         # layout / asset-library briefs
│   ├── experiment-*.md    # the test card
│   └── _assets/           # gitignored, Drive-synced (raw gen, mockups, print-files)
└── _assets/               # sprint-wide shared assets (multi-concept mockups etc.)
```
> **Binaries live in Google Drive** (`.gitignore` ignores `*.png/*.jpg/*.svg/…`). Docs are tracked;
> `_assets/` folders hold the Drive-synced images + tracked `.md` recipes/notes.

## Sprints
| Sprint | Focus | Key output |
|---|---|---|
| [`2026-07-competitor-ad-scoring/`](2026-07-competitor-ad-scoring/README.md) | Score 133 competitor ad concepts (PFG, Macorner, Wander Prints) | tiered Replicate/Test shortlist + `concept-scores-full.tsv` |
| [`2026-09-grandparents-day/`](2026-09-grandparents-day/README.md) | Grandparents Day concepts + the lead **GPD02 Garden/Birds** build | [`GPD02-garden-birds/`](2026-09-grandparents-day/GPD02-garden-birds/STATUS.md) concept (brief, libraries, layout, lamp spec) |
