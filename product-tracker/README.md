# Product Tracker

Tracks each product through the full pipeline: **design → sent to freelancer → live on store → ads → ad status.**
One row per product. File: `product-tracker.csv`. Update `last_updated` whenever a row changes.

## Where it lives (two copies, one writer)
- **`product-tracker.csv`** (this repo) — canonical + git history.
- **Google Sheet** (your dashboard) — ID `1BBO5WRBeBVQLkJI8l6zVBe2Ud1qzl7QOL7g5VS8ZoTE`, in the `nam.vu@firebits.com` Drive, link-shared as editor: https://docs.google.com/spreadsheets/d/1BBO5WRBeBVQLkJI8l6zVBe2Ud1qzl7QOL7g5VS8ZoTE/edit

Only Claude writes to both (from your verbal updates); you view the Sheet. On every change, update the CSV **and** re-push the Sheet so they stay identical. Don't hand-edit the CSV.

**How Claude re-pushes the Sheet (keeps the same link):** copy the CSV to `/Users/neovh34/.workspace-mcp/attachments/product-tracker.csv`, then `update_drive_file(file_id=1BBO5WRBeBVQLkJI8l6zVBe2Ud1qzl7QOL7g5VS8ZoTE, file_path=…, source_format=csv)` — in-place, preserves the ID/link/sharing.

Seeded 2026-08-05 with **all 110 shortlist products** (Macorner 16, PFG 9, Wander Prints 85), ordered by tier then score, all at `stage=backlog`. Add existing live products as `original` rows.

## Columns
| Column | Meaning |
|---|---|
| `product_id` | Stable ID, `MJP-001`… — never reuse |
| `tier` | Build priority from the shortlist (1 = highest) |
| `product_name` | What the product is |
| `recipient` | Grandparents / Parents / Couples / Family / Siblings / Friends / Pets / Kids-Grandkids / Self-Hobby / Memorial / Graduate / Occupation |
| `clone_brand` | Competitor it's cloned from (Macorner / PFG / Wander Prints), or `original` |
| `ref_product_link` | The competitor's product URL (what you're cloning) |
| `ref_ads_link` | The competitor's live Meta Ad-Library link for this product |
| `stage` | **Master status** — see vocab below (the one column to glance at) |
| `design_status` | `not-started` / `in-progress` / `ready` (Teeinblue assets + mockup done) |
| `sent_to_freelancer` | Date sent to freelancer to upload (`YYYY-MM-DD`), else blank |
| `live_date` | Date it went live on the store, else blank |
| `store_url` | **Our** live product URL once uploaded |
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
