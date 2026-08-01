# Extracts scoring-relevant fields from a WinningHunter search_facebook_ads response.
# Usage: jq -r --argjson today <epoch> -f score_ads.jq <file>
# Emits TSV: PAGE  DAYS  ACTV  GRW1m%  PRICE  CUR  RANK  DUP  FMT  DOMAIN
def days($t): if .started then (($t - (.started|split("T")[0]|strptime("%Y-%m-%d")|mktime))/86400|floor) else "?" end;
def cur: (.shopify_currency | if type=="object" then (.active // "") elif type=="array" then (.[0].active // "") else "" end);
.data[]
| [ (.pageName // "?" | .[0:22]),
    days($today),
    (.total_active_ads_on_page // "?"),
    ((.total_active_ads_on_page_growth_1m // 0)|tostring),
    ((.shopify_productprice // "?")|tostring),
    cur,
    (.ad_rank // "?"),
    (.countActive // .activeSeen // "?"),
    (.display_format // "?"),
    (.shopify_shopifydomain // "?")
  ] | @tsv
