"""The ONLY module that can mutate the ad account.

Kept separate from meta.py on purpose: the read client is provably incapable of
writing, and every mutation in the whole engine funnels through this one small
surface. The executor instantiates this only for a --live run; in dry-run it is
never constructed, so no write can physically happen.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request

GRAPH = "https://graph.facebook.com"


class MetaWriteClient:
    def __init__(self, token: str, version: str = "v26.0"):
        self.token = token
        self.version = version

    def _post(self, node: str, params: dict) -> dict:
        data = urllib.parse.urlencode({**params, "access_token": self.token}).encode()
        url = f"{GRAPH}/{self.version}/{node}"
        req = urllib.request.Request(url, data=data, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")
            try:
                err = json.loads(body).get("error", body)
            except json.JSONDecodeError:
                err = body
            raise RuntimeError(f"Meta API {e.code}: {err}") from None

    # -- the only two mutations this system performs -------------------------
    def pause_ad(self, ad_id: str) -> dict:
        return self._post(ad_id, {"status": "PAUSED"})

    def set_adset_daily_budget(self, adset_id: str, cents: int) -> dict:
        return self._post(adset_id, {"daily_budget": int(cents)})
