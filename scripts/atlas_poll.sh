#!/bin/bash
# usage: poll.sh outdir name=id [name=id...]  — waits for each Atlas prediction, downloads first output
set -a; source ~/.global-keys.env 2>/dev/null; set +a
OUT=$1; shift; mkdir -p "$OUT"
for pair in "$@"; do n=${pair%%=*}; id=${pair#*=}
  for i in $(seq 1 90); do
    r=$(curl -s -H "Authorization: Bearer $ATLASCLOUD_API_KEY" "https://api.atlascloud.ai/api/v1/model/prediction/$id")
    st=$(echo "$r" | python3 -c "import sys,json;print(json.load(sys.stdin)['data']['status'])")
    case $st in completed|succeeded) u=$(echo "$r" | python3 -c "import sys,json;print(json.load(sys.stdin)['data']['outputs'][0])"); ext=${u##*.}; ext=${ext%%\?*}; curl -s -o "$OUT/$n.$ext" "$u"; echo "$n done $OUT/$n.$ext"; break;;
      failed|timeout|canceled) echo "$n $st: $(echo $r | head -c 300)"; break;; esac
    sleep 5; done; done
