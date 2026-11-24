"""Shopify Admin GraphQL, read-only, via app `mj4u-orders` (scopes read_orders, read_customers).

Secrets: SHOPIFY_STORE_DOMAIN, SHOPIFY_ORDERS_CLIENT_ID, SHOPIFY_ORDERS_CLIENT_SECRET.
Token from the client-credentials grant (24h, never stored). The app must be installed on the store first.
Fields that need Protected Customer Data approval (email, customer name, address) are deliberately not
requested: the customer's name comes from Freshdesk, and the email is only used as a search filter.
Without read_all_orders, Shopify only returns orders from the last 60 days.
"""
from __future__ import annotations
import json, re, urllib.error, urllib.parse, urllib.request
from .config import require, support_cfg

ORDER_FIELDS = """name createdAt processedAt cancelledAt displayFinancialStatus displayFulfillmentStatus
  lineItems(first:10){nodes{title quantity}}
  fulfillments{status displayStatus createdAt inTransitAt deliveredAt estimatedDeliveryAt
    trackingInfo{company number url}}"""

Q = "query($q:String!){orders(first:10, query:$q, sortKey:CREATED_AT, reverse:true){nodes{%s}}}" % ORDER_FIELDS


class Shopify:
    def __init__(self):
        s = require("SHOPIFY_STORE_DOMAIN", "SHOPIFY_ORDERS_CLIENT_ID", "SHOPIFY_ORDERS_CLIENT_SECRET")
        self.shop = s["SHOPIFY_STORE_DOMAIN"]
        self.api = support_cfg()["shopify_api_version"]
        body = urllib.parse.urlencode({"grant_type": "client_credentials", "client_id": s["SHOPIFY_ORDERS_CLIENT_ID"],
                                       "client_secret": s["SHOPIFY_ORDERS_CLIENT_SECRET"]}).encode()
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request(
                f"https://{self.shop}/admin/oauth/access_token", data=body), timeout=30))
        except urllib.error.HTTPError as e:
            raise SystemExit(f"Shopify token request failed (HTTP {e.code}). Is the mj4u-orders app installed on the store?")
        self.token = r["access_token"]

    def gql(self, query: str, variables: dict) -> dict:
        req = urllib.request.Request(f"https://{self.shop}/admin/api/{self.api}/graphql.json",
                                     data=json.dumps({"query": query, "variables": variables}).encode(),
                                     headers={"X-Shopify-Access-Token": self.token, "Content-Type": "application/json"})
        r = json.load(urllib.request.urlopen(req, timeout=30))
        if r.get("errors"):
            raise SystemExit(f"Shopify GraphQL error: {r['errors']}")
        return r["data"]

    def orders_by_email(self, email: str) -> list[dict]:
        return self.gql(Q, {"q": f'email:"{email}"'})["orders"]["nodes"]

    def order_by_name(self, number: str) -> list[dict]:
        """number = digits only (from find_order_number); store names look like #MJ4U1014."""
        prefix = support_cfg().get("order_name_prefix", "")
        return self.gql(Q, {"q": f"name:#{prefix}{number}"})["orders"]["nodes"]


# "#MJ4U1014", "MJ4U-1014", "MJ4U 1014", "#1014", "order 1014", "order number: 1014", "ID - 1014"
ORDER_NO = re.compile(r"(?:MJ4U[\s-]?#?|#|order\s*(?:no\.?|number|num)?\s*:?\s*#?|\bid\s*[-:#]?)\s*(\d{4,7})\b", re.I)


def find_order_number(text: str) -> str | None:
    """Digits of the first order number in the text, without the store prefix."""
    m = ORDER_NO.search(text or "")
    return m.group(1) if m else None
