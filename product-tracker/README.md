# Product Tracker

Tracks each product through the full pipeline: **design → sent to freelancer → live on store → ads → ad status.**
One row per product. File: `product-tracker.csv`. Update `last_updated` whenever a row changes.

## Where it lives (two copies, one writer)
- **`product-tracker.csv`** (this repo) — canonical + git history.
- **Google Sheet** (your dashboard) — ID `1BBO5WRBeBVQLkJI8l6zVBe2Ud1qzl7QOL7g5VS8ZoTE`, in the `nam.vu@firebits.com` Drive, link-shared as editor: https://docs.google.com/spreadsheets/d/1BBO5WRBeBVQLkJI8l6zVBe2Ud1qzl7QOL7g5VS8ZoTE/edit

Only Claude writes to both (from your verbal updates); you view the Sheet. On every change, update the CSV **and** re-push the Sheet so they stay identical. Don't hand-edit the CSV.

Seeded 2026-08-05 with the 12 validated **Tier-1 clone targets** (from `research/sprints/2026-07-competitor-ad-scoring/clone-shortlist-links.csv`) at `stage=backlog`. Add your existing live products and the Wander-Prints Tier-1 candidates as you go.

## Columns
| Column | Meaning |
|---|---|
| `product_id` | Stable ID, `MJP-001`… — never reuse |
| `product_name` | What the product is |
| `recipient` | Grandparents / Parents / Couples / Family / Siblings / Friends / Pets / Kids-Grandkids / Self-Hobby / Memorial / Graduate / Occupation |
| `clone_source` | Competitor concept it's based on, or `original` |
| `stage` | **Master status** — see vocab below (the one column to glance at) |
| `design_status` | `not-started` / `in-progress` / `ready` (Teeinblue assets + mockup done) |
| `sent_to_freelancer` | Date sent to freelancer to upload (`YYYY-MM-DD`), else blank |
| `live_date` | Date it went live on the store, else blank |
| `store_url` | Live product URL once uploaded |
| `ad_status` | `none` / `draft` / `in-review` / `active` / `paused` / `killed` |
| `ad_launch_date` | Date ads first went live |
| `ad_result` | Spend / ROAS / verdict (manual until a Meta Ads MCP is connected) |
| `last_updated` | `YYYY-MM-DD` of last change to the row |
| `notes` | Anything else |

## `stage` vocabulary (the pipeline, in order)
1. `backlog` — chosen to build, not started
2. `design` — assets/mockup in production
3. `sent-to-freelancer` — handed off for upload, not live yet
4. `live` — live on store, no ads yet
5. `ads-live` — live + ads running
6. `scaling` — ads working, increasing spend
7. `paused` — ads paused (seasonal / testing)
8. `killed` — dropped (dead product or dead ads)

## Quick filters
- **What's live:** `stage` in {live, ads-live, scaling, paused} (or `live_date` not blank)
- **Sent to freelancer, awaiting upload:** `stage = sent-to-freelancer`
- **Running ads:** `ad_status = active`
- **Ad status at a glance:** the `ad_status` column

> Ad data (`ad_status`, `ad_result`) is **manual** for now — WinningHunter only sees competitors' public ads, not your own account. Connect a Meta Marketing API MCP to auto-fill these later.
