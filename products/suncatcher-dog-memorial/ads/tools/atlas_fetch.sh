#!/usr/bin/env bash
# Wait for AtlasCloud predictions and download their first output.
#   atlas_fetch.sh <prediction_id> <out_path> [<prediction_id> <out_path> ...]
set -uo pipefail
source ~/.global-keys.env
while [ $# -ge 2 ]; do
  id=$1; out=$2; shift 2
  for i in $(seq 1 90); do
    j=$(curl -s -H "Authorization: Bearer $ATLASCLOUD_API_KEY" "https://api.atlascloud.ai/api/v1/model/prediction/$id")
    st=$(echo "$j" | python3 -c 'import sys,json; d=json.load(sys.stdin).get("data",{}); print(d.get("status",""))' 2>/dev/null)
    if [ "$st" = "completed" ] || [ "$st" = "succeeded" ]; then
      url=$(echo "$j" | python3 -c 'import sys,json; print(json.load(sys.stdin)["data"]["outputs"][0])')
      curl -sSo "$out" "$url" && echo "OK $id -> $out"; break
    elif [ "$st" = "failed" ] || [ "$st" = "timeout" ]; then echo "FAIL $id ($st): $(echo "$j" | head -c 300)"; break; fi
    sleep 10
  done
done
