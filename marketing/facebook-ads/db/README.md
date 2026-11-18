# MJ4U ads database

Supabase project **mj4u-ads** (ref `bjplojqovxetmbchzzms`, ap-southeast-1, **PostgreSQL 17.12**).
Purpose: link every Meta ad's results to how it was built (hook format/trigger/mechanism, concept, script, length) to find the winning formula.
Canonical build data = git CSVs (`products/_registry/*.csv`, `marketing/facebook-ads/_ledgers/*.csv`); the DB adds daily Meta metrics.
Sync: `engine/db_sync.py seed|pull|all`. Migrations: `migrations/` (001–005).
**Dashboard (Hook Lab):** https://claude.ai/artifact/Xi39PdXEDMPLk1VmDQxnNt, page `dashboard/index.html` + snapshot `dashboard/data.json` (gitignored).
The artifact sandbox blocks calls to Supabase, so refresh = `engine/db_sync.py pull` → `engine/export_dashboard.py` → Claude republishes the page with `files: {data.json}` (same file path or the URL).
**Daily job:** launchd `~/Library/LaunchAgents/com.mj4u.ads-daily-sync.plist` runs `engine/daily_sync.sh` at 15:00 Mac time (UTC+7) = 00:00 PST, after the ad account's day closes. It re-pulls the last 7 days (Meta revises recent days) and re-exports data.json. Log: `reports/daily-sync.log` (gitignored). It runs from this worktree path; move the plist if the repo moves.
**Meta action aliases:** one event is reported under several names (add_to_cart / offsite_conversion.fb_pixel_add_to_cart / omni_add_to_cart…). Take the first present; never sum (fixed 2026-11-18).

<!-- DATABASE_ARCHITECTURE:START -->
## Database Architecture Summary (verified 2026-11-18)

### Tables
| Table | Grain | Key | Notes |
|---|---|---|---|
| products | product | `product_id` (MJ4U-NNN or slug) | from product-tracker.csv + engine economics |
| tests | test plan | `test_id` | status check |
| cells | concept × hook arm | `cell_id` | frozen hypothesis |
| hooks | hook card | `hook_id` | format / trigger / primitives / arm_axis tags |
| ads | one Meta ad (both ratios) | `ad_key` | holds `meta_ad_id` (unique); ad name must contain ad_key |
| creatives | one delivered file | `creative_id` | FK ad_key; ratio check 916/45 |
| ad_metrics_daily | Meta ad × day | (`meta_ad_id`, `date`) | FK ad_key (null = unmapped); non-negative check |
| view `ad_performance` | ad | — | ads + hook tags + summed metrics + hook/hold rate, CTR, cost/ATC, ROAS |

### Decisions vs the skills (database-architecture, database-design)
- **PG18 features not used** — the project runs PG17.12 (no `uuidv7()`, virtual generated columns, temporal constraints, skip scan). Revisit if Supabase offers PG18.
- **Natural text keys, not UUIDv7** — IDs are human-readable and travel in Meta ad names and CSVs; metrics key on Meta's own ad id + date. Tiny volume, no distributed inserts.
- **No soft-delete column** — rows are never deleted; lifecycle lives in `status` (killed / cut / parked).
- **ON DELETE RESTRICT on every FK** — test history is audit data.
- **No partitioning** — ~100 ads × 365 days ≈ tens of thousands of rows/year.
- Every FK column indexed; (ad_key, date) composite for per-ad time series. timestamptz only; created_at/updated_at + trigger on entity tables.
- RLS on all tables: select for anon/authenticated (dashboard), writes only via service role.

### Pending
- EXPLAIN ANALYZE on `ad_performance` and the dashboard queries once real data is backfilled.
<!-- DATABASE_ARCHITECTURE:END -->
