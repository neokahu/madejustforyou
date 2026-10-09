#!/usr/bin/env bash
# Back up every git-ignored media/heavy file to Google Drive via rclone.
# Mirrors repo-relative paths under gdrive:madejustforyou/repo/.
# Uses `rclone copy` — never deletes anything on Drive.
#
#   scripts/backup-media.sh            # upload new/changed files
#   scripts/backup-media.sh --dry-run  # show what would upload
set -euo pipefail

REMOTE="${MEDIA_REMOTE:-gdrive:madejustforyou/repo}"
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

LIST="$(mktemp)"
trap 'rm -f "$LIST"' EXIT

# Every ignored file, minus secrets, OS junk, deps and local config.
git ls-files --others --ignored --exclude-standard -z \
  | tr '\0' '\n' \
  | grep -vE '(^|/)(\.env[^/]*|\.DS_Store|node_modules/.*|.*\.log)$' \
  | grep -vE '^\.claude/' \
  > "$LIST" || true

COUNT="$(wc -l < "$LIST" | tr -d ' ')"
echo "backup-media: $COUNT ignored files → $REMOTE"
[ "$COUNT" -eq 0 ] && exit 0

rclone copy "$ROOT" "$REMOTE" \
  --files-from "$LIST" \
  --transfers 8 --checkers 16 \
  --drive-chunk-size 64M \
  --stats 30s --stats-one-line \
  "$@"
