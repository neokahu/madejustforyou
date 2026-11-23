# Theme code → separate repo (pointer)

The Shopify **theme code** for MadeJustForYou is **NOT in this repo**. It lives in a dedicated repo:

- **Local:** `~/Desktop/projects/madejustforyou-theme/shopify-theme-1/`
- **GitHub:** `git@github.com:Minh-Quy-K/shopify-theme-1.git` (branch `main`)
- **Synced from Shopify** via the Shopify↔GitHub integration (commits like *"Update from Shopify for theme…"*). `main` mirrors the live theme.

## Repo split (who owns what)
| Repo | Holds | Write policy |
|---|---|---|
| **`madejustforyou/`** (this one — the **main folder**) | Research, marketing, design specs, competitor intelligence, Teeinblue asset system, occasion calendar, **all session logs & docs**, memory | All docs/notes/logs go **here** |
| **`madejustforyou-theme/shopify-theme-1/`** | Shopify theme Liquid/JS/CSS/JSON | **Code changes ONLY** — never write docs, logs, or pointers there (keeps it clean for Shopify sync) |

## Rules
- **Session logs, handoffs, research, specs → always here** (`_SESSION-LOGS/`, `research/`, etc.), even when the work was a theme code change.
- In the theme repo, touch **theme files only**. No READMEs, notes, or context files over there. The one exception: its root `CLAUDE.md`, a short pointer back to this repo so agents opened there find the context (added 2026-11-23).
- Work in the theme repo on `nam-dev`; merging or pushing to `main` publishes to the live store, so do it only when the user asks.
- When a task spans both, keep both folders open: **strategy/specs/assets here → Liquid/JS there.** Context lives here.

_History: the old `theme_export__…16JUL2026` snapshot (482 files) was removed 2026-07-30 — redundant now that the theme repo is the source of truth (it's a superset of the snapshot)._
