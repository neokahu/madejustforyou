"""Read-only Meta Marketing API client (Insights + ad metadata).

Intentionally GET-only. This module cannot create, edit, pause, or delete
anything — writes belong to a later, guardrailed phase. Uses only the Python
standard library (urllib) so the engine runs with zero pip installs.
"""
from __future__ import annotations

import datetime as _dt
import json
import urllib.parse
import urllib.request

GRAPH = "https://graph.facebook.com"

# Ad-level insight fields we pull. Keep in sync with rules.normalize_row().
INSIGHT_FIELDS = [
    "campaign_id", "campaign_name", "adset_id", "adset_name", "ad_id", "ad_name",
    "impressions", "reach", "spend", "clicks", "ctr",
    "inline_link_clicks", "inline_link_click_ctr", "cpc", "cpm", "frequency",
    "actions", "action_values", "video_play_actions", "purchase_roas",
]


class MetaReadClient:
    def __init__(self, token: str, ad_account_id: str, version: str = "v26.0"):
        self.token = token
        self.acct = ad_account_id if ad_account_id.startswith("act_") else f"act_{ad_account_id}"
        self.version = version

    # -- low-level -----------------------------------------------------------
    def _open(self, url: str):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                data = json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")
            try:
                err = json.loads(body).get("error", body)
            except json.JSONDecodeError:
                err = body
            raise RuntimeError(f"Meta API {e.code}: {err}") from None
        if isinstance(data, dict) and data.get("error"):
            raise RuntimeError(f"Meta API error: {data['error']}")
        return data

    def _get(self, path: str, params: dict):
        params = {**params, "access_token": self.token}
        return self._open(f"{GRAPH}/{self.version}/{path}?{urllib.parse.urlencode(params)}")

    def _get_all(self, path: str, params: dict) -> list[dict]:
        rows: list[dict] = []
        data = self._get(path, params)
        rows.extend(data.get("data", []))
        while data.get("paging", {}).get("next"):
            data = self._open(data["paging"]["next"])
            rows.extend(data.get("data", []))
        return rows

    # -- reads ---------------------------------------------------------------
    def account(self) -> dict:
        return self._get(self.acct, {"fields": "name,account_status,currency,timezone_name,amount_spent,balance"})

    def ad_insights(self, days: int = 7) -> list[dict]:
        until = _dt.date.today()
        since = until - _dt.timedelta(days=days)
        time_range = json.dumps({"since": since.isoformat(), "until": until.isoformat()})
        return self._get_all(f"{self.acct}/insights", {
            "level": "ad",
            "time_range": time_range,
            "fields": ",".join(INSIGHT_FIELDS),
            "limit": 200,
        })

    def ad_insights_daily(self, days: int = 7) -> dict[str, list]:
        """ad_id -> list of per-day rows (time_increment=1) for sustained-profit + fatigue-trend checks."""
        until = _dt.date.today()
        since = until - _dt.timedelta(days=days)
        rows = self._get_all(f"{self.acct}/insights", {
            "level": "ad", "time_increment": 1,
            "time_range": json.dumps({"since": since.isoformat(), "until": until.isoformat()}),
            "fields": "ad_id,spend,cpm,inline_link_click_ctr,action_values,date_start",
            "limit": 500,
        })
        out: dict[str, list] = {}
        for r in rows:
            out.setdefault(str(r.get("ad_id", "")), []).append(r)
        return out

    def ads_meta(self) -> dict[str, dict]:
        """ad_id -> {created_time, effective_status} so we can compute age/status."""
        rows = self._get_all(f"{self.acct}/ads", {
            "fields": "id,name,created_time,effective_status,campaign_id,adset_id",
            "limit": 200,
        })
        return {r["id"]: r for r in rows}

    def adsets_meta(self) -> dict[str, dict]:
        """adset_id -> {name, daily_budget (cents), lifetime_budget, status, campaign_id}.

        daily_budget is null/absent for CBO (campaign-budget) ad sets — the executor
        detects that and refuses to scale them (scaling belongs at campaign level).
        """
        rows = self._get_all(f"{self.acct}/adsets", {
            "fields": "id,name,daily_budget,lifetime_budget,status,campaign_id",
            "limit": 200,
        })
        return {r["id"]: r for r in rows}


def age_days(created_time: str | None) -> int | None:
    """Days since an ISO8601 created_time like '2026-08-01T12:00:00-0700'."""
    if not created_time:
        return None
    try:
        d = _dt.datetime.fromisoformat(created_time.replace("Z", "+00:00")).date()
    except ValueError:
        return None
    return (_dt.date.today() - d).days
