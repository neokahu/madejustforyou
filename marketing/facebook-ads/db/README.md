# MJ4U ads database

Supabase project **mj4u-ads** (ref `bjplojqovxetmbchzzms`, ap-southeast-1, **PostgreSQL 17.12**).
Purpose: link every Meta ad's results to how it was built (hook format/trigger/mechanism, concept, script, length) to find the winning formula.
Canonical build data = git CSVs (`products/_registry/*.csv`, `marketing/facebook-ads/_ledgers/*.csv`); the DB adds daily Meta metrics.
Sync: `engine/db_sync.py seed|media|pull|all` (`media` = Meta preview link, post, reel, thumbnail per ad; thumbnails are signed URLs that expire, so the daily job refreshes them; it also links newly launched ads to their Meta id via the ad_key in the ad name). Migrations: `migrations/` (001–005).
**Dashboard (Hook Lab):** https://mj4u-hook-lab.vercel.app (Vercel project `mj4u-hook-lab`, account neokahu). Source `hook-lab-web/`: `login.html` (/login, email code) → `index.html` (/, dashboard; redirects to /login when signed out), shared `styles.css` + `sb.js`, `vercel.json`; deploy with `cd hook-lab-web && vercel deploy --prod`.
It reads Supabase **live** with the publishable key. Login = Supabase email one-time code (`signInWithOtp` with `shouldCreateUser:false`, then `verifyOtp`).
**Access:** RLS on every table allows `select` only to signed-in users whose email is in `dashboard_viewers` (checked by `private.is_dashboard_viewer()`). Anonymous reads return nothing.
Auth config (set 2026-11-18 via the Management API, token `SUPABASE_ACCESS_TOKEN` in `~/.global-keys.env`): Magic-link template shows `{{ .Token }}`, 6-digit codes valid 1h, Site URL = the Vercel URL, custom SMTP = Gmail (namvu47@gmail.com) with a 50 emails/hour limit.
To add a viewer: insert the email into `dashboard_viewers` AND create the auth user (admin API, `email_confirm: true`) — strangers can't request codes.
Superseded: the claude.ai artifact snapshot (`dashboard/`, `engine/export_dashboard.py`) and the Cloudflare worker `mj4u-hook-lab.namvu47.workers.dev` (empty page).
**Daily job:** launchd `~/Library/LaunchAgents/com.mj4u.ads-daily-sync.plist` runs `engine/daily_sync.sh` at 15:00 Mac time (UTC+7) = 00:00 PST, after the ad account's day closes. It re-pulls the last 7 days (Meta revises recent days); the dashboard reads the result live. Log: `reports/daily-sync.log` (gitignored). It runs from this worktree path; move the plist if the repo moves.
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
