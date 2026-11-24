#!/usr/bin/env python3
"""Shopify catalog <-> MJ4U product IDs (app `mj4u-catalog`, scopes read/write_products).

  python3 scripts/shopify_catalog.py pull     # read-only: every store product -> products/_registry/shopify-products.json
  python3 scripts/shopify_catalog.py tag      # dry run: show which MJ4U-NNN tag each product would get (from the registry map)
  python3 scripts/shopify_catalog.py tag --apply   # write the tags to the live store (approved list only)

Credentials in ~/.global-keys.env: SHOPIFY_STORE_DOMAIN, SHOPIFY_CLIENT_ID, SHOPIFY_CLIENT_SECRET.
Tokens come from the client-credentials grant and last 24h; never stored. Stdlib only.
"""
from __future__ import annotations
import json, os, sys, urllib.parse, urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
REG = REPO / "products/_registry"
OUT = REG / "shopify-products.json"
MAP = REG / "product-ids.json"
API = "2026-10"


def env():
    vals = {}
    for line in Path.home().joinpath(".global-keys.env").read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            vals[k.strip().removeprefix("export ")] = v.strip().strip('"').strip("'")
    return {k: os.environ.get(k) or vals.get(k) for k in ("SHOPIFY_STORE_DOMAIN", "SHOPIFY_CLIENT_ID", "SHOPIFY_CLIENT_SECRET")}


class Admin:
    def __init__(self):
        e = env()
        self.shop = e["SHOPIFY_STORE_DOMAIN"]
        body = urllib.parse.urlencode({"grant_type": "client_credentials", "client_id": e["SHOPIFY_CLIENT_ID"],
                                       "client_secret": e["SHOPIFY_CLIENT_SECRET"]}).encode()
        self.token = json.load(urllib.request.urlopen(
            urllib.request.Request(f"https://{self.shop}/admin/oauth/access_token", data=body)))["access_token"]

    def gql(self, query, variables=None):
        req = urllib.request.Request(f"https://{self.shop}/admin/api/{API}/graphql.json",
                                     data=json.dumps({"query": query, "variables": variables or {}}).encode(),
                                     headers={"X-Shopify-Access-Token": self.token, "Content-Type": "application/json"})
        r = json.load(urllib.request.urlopen(req))
        if r.get("errors"):
            raise SystemExit(f"GraphQL error: {r['errors']}")
        return r["data"]


Q = """query($after:String){products(first:100, after:$after, sortKey:CREATED_AT){
  pageInfo{hasNextPage endCursor}
  nodes{id legacyResourceId title handle status tags productType createdAt onlineStoreUrl}}}"""


def pull():
    a, out, after = Admin(), [], None
    while True:
        d = a.gql(Q, {"after": after})["products"]
        out += d["nodes"]
        if not d["pageInfo"]["hasNextPage"]:
            break
        after = d["pageInfo"]["endCursor"]
    rows = [{"shopify_product_id": n["legacyResourceId"], "title": n["title"], "handle": n["handle"], "status": n["status"],
             "product_type": n["productType"], "created_at": n["createdAt"], "url": n["onlineStoreUrl"], "tags": n["tags"]} for n in out]
    OUT.write_text(json.dumps({"store": a.shop, "count": len(rows), "products": rows}, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(rows)} products -> {OUT.relative_to(REPO)}")


TAG_M = "mutation($id:ID!,$tags:[String!]!){tagsAdd(id:$id,tags:$tags){userErrors{field message}}}"


def tag(apply: bool):
    ids = json.loads(MAP.read_text())["products"]
    todo = [p for p in ids if p.get("shopify_product_id")]
    a = Admin() if apply else None
    for p in todo:
        print(("TAG " if apply else "would tag ") + f"{p['shopify_product_id']} <- {p['product_id']}  ({p['name']})")
        if apply:
            errs = a.gql(TAG_M, {"id": f"gid://shopify/Product/{p['shopify_product_id']}", "tags": [p["product_id"]]})["tagsAdd"]["userErrors"]
            if errs:
                raise SystemExit(f"{p['product_id']}: {errs}")
    print(f"{len(todo)} products {'tagged' if apply else '(dry run; add --apply to write)'}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "pull":
        pull()
    elif cmd == "tag":
        tag("--apply" in sys.argv)
    else:
        print(__doc__)
