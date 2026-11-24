"""Build a reply draft for one ticket from (ticket text, orders) -> Draft.

Draft.signals is the seam for the future confidence score + Slack approval loop (see README):
every fact the scorer will need is collected here, so the scorer is a pure function of Draft.
"""
from __future__ import annotations
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime
from . import kb, stages
from .config import stage_replies, support_cfg

ORDER_STATUS_KB = "order-status"


@dataclass
class Draft:
    ticket_id: int | str
    first_name: str
    intent: str                     # kb entry id, or "order-status"
    stage: str | None               # stages.Stage.code when the order was looked up
    text: str
    kb_hits: list[dict] = field(default_factory=list)
    signals: dict = field(default_factory=dict)
    flags: list[str] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)


def fill(template: str, values: dict, cfg: dict, flags: list[str]) -> str:
    def fact(m):
        f = cfg["facts"].get(m.group(1))
        if not f:
            flags.append(f"unknown fact {m.group(1)}")
            return "[?]"
        if not f.get("confirmed"):
            flags.append(f"uses unconfirmed fact '{m.group(1)}' = {f['value']}")
        return f["value"]
    out = re.sub(r"\{fact:([a-z_]+)\}", fact, template)
    return out.format_map({k: ("" if v is None else v) for k, v in values.items()})


def build(ticket_id, first_name: str, text: str, orders: list[dict] | None,
          now: datetime | None = None, cfg: dict | None = None) -> Draft:
    """orders=None means Shopify was not checked (e.g. not connected); [] means checked and none found."""
    cfg = cfg or support_cfg()
    replies = stage_replies()
    flags: list[str] = []
    hits = kb.match(text)
    first = (first_name or "").split(" ")[0].strip() or "there"
    if first == "there":
        flags.append("no first name: greeting is 'Hi there'")

    top = hits[0].entry if hits else None
    is_status = (top is None) or top["id"] == ORDER_STATUS_KB or any(h.entry["id"] == ORDER_STATUS_KB for h in hits)
    intent = ORDER_STATUS_KB if is_status else top["id"]

    stage_code, body = None, ""
    if orders is not None:
        hint = stages_order_hint(text)
        order, problem = stages.pick_order(orders, hint)
        if problem == "NO_ORDER_FOUND" and hint:
            problem = "ORDER_NUMBER_NOT_FOUND"
        if problem:
            stage_code = problem
        else:
            st = stages.classify(order, cfg, now)
            stage_code = st.code
            flags += st.notes
        if is_status or stage_code in ("NO_ORDER_FOUND", "ORDER_NUMBER_NOT_FOUND", "MULTIPLE_ORDERS"):
            r = replies[stage_code]
            if r["escalate"]:
                flags.append(f"stage {stage_code} needs your decision")
            vals = {"first_name": first, "order_name": f"#{hint}" if hint else ""}
            if not problem:
                vals.update(order_name=st.order_name, days=st.days, days_ago=days_ago(st.days), carrier=st.carrier,
                            tracking_number=st.tracking_number, tracking_url=st.tracking_url)
            body = fill(r["reply"], vals, cfg, flags)
    else:
        flags.append("Shopify not checked")

    # the non-status question to answer: the top hit, or a second question next to "where is my order"
    kb_entry = next((h.entry for h in hits if h.entry["id"] != ORDER_STATUS_KB), None)
    if kb_entry:
        ans = kb_entry.get("answer") or ""
        if kb_entry.get("status") != "approved" or not ans:
            flags.append(f"KB '{kb_entry['id']}' has no approved answer yet")
        kb_text = fill(ans, {"first_name": first}, cfg, flags) if ans else f"[KB '{kb_entry['id']}': answer needed]"
        greeting = f"Hi {first},\n\nThank you for reaching out!\n\n"
        body = (body + "\n\n" + kb_text) if body else greeting + kb_text

    if len(hits) > 1 and hits[1].score >= hits[0].score and hits[1].entry["id"] != hits[0].entry["id"]:
        flags.append(f"two intents tie: {hits[0].entry['id']} / {hits[1].entry['id']}")
    if not body:
        body = f"Hi {first},\n\nThank you for reaching out!\n\n[write the answer]"
        flags.append("no draft: no KB match and no order stage")

    text_out = body.rstrip() + "\n\n" + cfg["signature"]
    signals = {
        "kb_top_score": hits[0].score if hits else 0.0,
        "kb_top_status": top.get("status") if top else None,
        "order_checked": orders is not None,
        "orders_found": len(orders) if orders is not None else None,
        "stage": stage_code,
        "escalate": bool(stage_code and replies.get(stage_code, {}).get("escalate")),
        "unconfirmed_facts": sum("unconfirmed fact" in f for f in flags),
    }
    return Draft(ticket_id, first, intent, stage_code, text_out,
                 [{"id": h.entry["id"], "score": h.score, "matched": h.matched} for h in hits], signals, flags)


def days_ago(n: int) -> str:
    return "today" if n <= 0 else "yesterday" if n == 1 else f"{n} days ago"


def stages_order_hint(text: str) -> str | None:
    from .shopify import find_order_number
    return find_order_number(text)
