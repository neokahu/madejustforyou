#!/bin/bash
# Daily ads-DB sync (launchd: com.mj4u.ads-daily-sync, 15:00 Asia/Ho_Chi_Minh = 00:00 PST/01:00 PDT).
# Re-pulls the last 7 days: Meta keeps revising recent days (in-day numbers settle down), upserts overwrite them.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p ../reports
{
  echo "=== $(date '+%Y-%m-%d %H:%M %Z') ==="
  /opt/homebrew/bin/python3 db_sync.py all --days 7
  /opt/homebrew/bin/python3 export_dashboard.py
  # Deploy Hook Lab to Cloudflare, but only once Access (login) is confirmed on the workers.dev URL:
  # an unprotected deploy would make ad data public, so check the URL redirects to a Cloudflare Access login first.
  if curl -s -o /dev/null -w '%{redirect_url}' https://mj4u-hook-lab.namvu47.workers.dev/ | grep -q cloudflareaccess.com; then
    cp ../dashboard/index.html ../dashboard/data.json ../dashboard/public/
    (cd ../dashboard && PATH="$HOME/.nvm/versions/node/v22.19.0/bin:$PATH" npx -y wrangler@4 deploy) | tail -3
  else
    echo "SKIP deploy: mj4u-hook-lab.namvu47.workers.dev is not behind Cloudflare Access"
  fi
} >> ../reports/daily-sync.log 2>&1
