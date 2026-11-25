#!/bin/bash
# usage: atlas_poll.sh outdir name=id [name=id...] — waits for each Atlas prediction, downloads the first output,
# and logs it (price + file specs) to marketing/facebook-ads/media-cost-ledger.csv via media_ledger.py.
# Optional env: LEDGER_PURPOSE=refs|turntable|stills|clips|tests
set -a; source ~/.global-keys.env 2>/dev/null; set +a
OUT=$1; shift; mkdir -p "$OUT"
for pair in "$@"; do n=${pair%%=*}; id=${pair#*=}
  for i in $(seq 1 90); do
    r=$(curl -s -H "Authorization: Bearer $ATLASCLOUD_API_KEY" "https://api.atlascloud.ai/api/v1/model/prediction/$id")
    st=$(echo "$r" | python3 -c "import sys,json;print(json.load(sys.stdin)['data']['status'])")
    case $st in completed|succeeded) u=$(echo "$r" | python3 -c "import sys,json;print(json.load(sys.stdin)['data']['outputs'][0])"); ext=${u##*.}; ext=${ext%%\?*}; curl -s -o "$OUT/$n.$ext" "$u"; echo "$n done $OUT/$n.$ext"; python3 "$(dirname "$0")/media_ledger.py" log "$id" "$OUT/$n.$ext" ${LEDGER_PURPOSE:+--purpose "$LEDGER_PURPOSE"} || true; break;;
      failed|timeout|canceled) echo "$n $st: $(echo $r | head -c 300)"; break;; esac
    sleep 5; done; done
