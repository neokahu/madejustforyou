"""Freshdesk API v2 client (stdlib only).

Secrets: FRESHDESK_DOMAIN (e.g. madejustforyou, or madejustforyou.freshdesk.com) and FRESHDESK_API_KEY.
Reads are free to run. reply(), note() and set_status() write to the ticket; the CLI only calls them after an explicit --yes.
"""
from __future__ import annotations
import base64, html, json, os, re, urllib.error, urllib.parse, urllib.request
from .config import require, secret

STATUS = {2: "Open", 3: "Pending", 4: "Resolved", 5: "Closed"}


class Freshdesk:
    def __init__(self):
        if not secret("FRESHDESK_API_KEY") and secret("FRESKDESK_API_KEYS"):  # name as saved in the keys file
            os.environ["FRESHDESK_API_KEY"] = secret("FRESKDESK_API_KEYS")
        s = require("FRESHDESK_DOMAIN", "FRESHDESK_API_KEY")
        dom = s["FRESHDESK_DOMAIN"].removeprefix("https://").rstrip("/")
        self.base = f"https://{dom if '.' in dom else dom + '.freshdesk.com'}/api/v2"
        self.auth = "Basic " + base64.b64encode(f"{s['FRESHDESK_API_KEY']}:X".encode()).decode()

    def _req(self, method: str, path: str, params: dict | None = None, body: dict | None = None):
        url = self.base + path + ("?" + urllib.parse.urlencode(params) if params else "")
        req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body else None,
                                     headers={"Authorization": self.auth, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            raise SystemExit(f"Freshdesk {method} {path}: HTTP {e.code} {e.read()[:300]!r}")

    def open_tickets(self, statuses=(2, 3)) -> list[dict]:
        out, page = [], 1
        while True:
            batch = self._req("GET", "/tickets", {"include": "requester", "order_by": "created_at",
                                                  "order_type": "asc", "per_page": 100, "page": page})
            out += [t for t in batch if t.get("status") in statuses]
            if len(batch) < 100:
                return out
            page += 1

    def ticket(self, tid: int) -> dict:
        return self._req("GET", f"/tickets/{tid}", {"include": "requester,conversations"})

    def conversations(self, tid: int) -> list[dict]:
        return self._req("GET", f"/tickets/{tid}/conversations", {"per_page": 100})

    def reply(self, tid: int, text: str) -> dict:
        return self._req("POST", f"/tickets/{tid}/reply", body={"body": to_html(text)})

    def set_status(self, tid: int, status: int) -> dict:
        return self._req("PUT", f"/tickets/{tid}", body={"status": status})

    def note(self, tid: int, text: str) -> dict:
        return self._req("POST", f"/tickets/{tid}/notes", body={"body": to_html(text), "private": True})


def to_html(text: str) -> str:
    return "<br>".join(html.escape(line) for line in text.split("\n"))


def plain(t: dict) -> str:
    """Best plain-text body of a ticket or conversation entry."""
    if t.get("description_text") or t.get("body_text"):
        return (t.get("description_text") or t.get("body_text")).strip()
    return re.sub(r"<[^>]+>", " ", t.get("description") or t.get("body") or "").strip()
