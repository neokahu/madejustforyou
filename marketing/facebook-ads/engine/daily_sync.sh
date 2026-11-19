#!/bin/bash
# Daily ads-DB sync (launchd: com.mj4u.ads-daily-sync, 15:00 Asia/Ho_Chi_Minh = 00:00 PST/01:00 PDT).
# Hook Lab (https://mj4u-hook-lab.vercel.app) reads Supabase live, so this job only refreshes the database.
# Re-pulls the last 7 days: Meta keeps revising recent days (in-day numbers settle down), upserts overwrite them.
set -euo pipefail
cd "$(dirname "$0")"
# On failure: macOS notification (the run is also recorded as failed in sync_runs, and Hook Lab shows a warning).
notify_fail() { /usr/bin/osascript -e 'display notification "Daily Meta pull failed: see marketing/facebook-ads/reports/daily-sync.log" with title "MJ4U Hook Lab" sound name "Basso"' || true; }
trap notify_fail ERR
mkdir -p ../reports
{
  echo "=== $(date '+%Y-%m-%d %H:%M %Z') ==="
  /opt/homebrew/bin/python3 db_sync.py all --days 7
} >> ../reports/daily-sync.log 2>&1
