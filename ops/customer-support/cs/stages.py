"""Order -> stage. Pure function: no network, so it is unit-tested.

Input is one Shopify GraphQL order node as returned by shopify.ORDER_FIELDS.
"""
from __future__ import annotations
import re, urllib.parse
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

PROBLEM_DISPLAY = {"FAILURE", "ATTEMPTED_DELIVERY", "NOT_DELIVERED", "CANCELED"}


@dataclass
class Stage:
    code: str
    days: int = 0  # days since placed (unshipped) or since shipped (shipped stages)
    order_name: str = ""
    carrier: str = ""
    tracking_number: str = ""
    tracking_url: str = ""
    notes: list[str] = field(default_factory=list)


def parse_ts(s: str | None) -> datetime | None:
    return datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


def days_between(start: datetime, now: datetime, mode: str = "calendar") -> int:
    if mode != "business":
        return (now.date() - start.date()).days
    d, n = start.date(), 0
    while d < now.date():
        d += timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


def _latest_fulfillment(order: dict) -> dict | None:
    fs = [f for f in order.get("fulfillments") or [] if f.get("status") != "CANCELLED"]
    return max(fs, key=lambda f: f.get("createdAt") or "") if fs else None


def classify(order: dict, cfg: dict, now: datetime | None = None) -> Stage:
    now = now or datetime.now(timezone.utc)
    t = cfg["stage_thresholds_days"]
    mode = cfg.get("day_count", "calendar")
    st = Stage(code="", order_name=order.get("name", ""))

    if order.get("cancelledAt"):
        st.code = "CANCELLED"
        return st
    fin = order.get("displayFinancialStatus") or ""
    if fin in ("REFUNDED", "PARTIALLY_REFUNDED"):
        st.code = "REFUNDED"
        if fin == "PARTIALLY_REFUNDED":
            st.notes.append("partial refund: check what was refunded before replying")
        return st
    if fin in ("PENDING", "EXPIRED", "VOIDED"):
        st.code = "PAYMENT_PENDING"
        return st

    ful = order.get("displayFulfillmentStatus") or "UNFULFILLED"
    latest = _latest_fulfillment(order)
    if latest:
        ti = (latest.get("trackingInfo") or [{}])[0] or {}
        st.carrier = ti.get("company") or "the carrier"
        st.tracking_number = ti.get("number") or "(not available yet)"
        page = cfg.get("tracking_page_url")  # our own tracking page, never the carrier/17track link Shopify stores
        if ti.get("number") and page:
            st.tracking_url = page.format(tracking_number=urllib.parse.quote(ti["number"]))
        else:
            st.tracking_url = "(not available yet)"

    if ful in ("FULFILLED", "PARTIALLY_FULFILLED") and latest:
        shipped = parse_ts(latest.get("inTransitAt")) or parse_ts(latest.get("createdAt"))
        st.days = days_between(shipped, now, mode) if shipped else 0
        disp = latest.get("displayStatus") or ""
        if disp == "DELIVERED" or latest.get("deliveredAt"):
            st.code = "DELIVERED"
        elif disp in PROBLEM_DISPLAY:
            st.code = "DELIVERY_ISSUE"
            st.notes.append(f"carrier status {disp}")
        elif ful == "PARTIALLY_FULFILLED":
            st.code = "PARTIALLY_SHIPPED"
        elif st.days >= t["shipped_delayed_from"]:
            st.code = "SHIPPED_DELAYED"
        else:
            st.code = "SHIPPED"
        return st

    if ful == "ON_HOLD":
        st.code = "ON_HOLD"
        return st

    placed = parse_ts(order.get("processedAt") or order.get("createdAt"))
    st.days = days_between(placed, now, mode) if placed else 0
    if st.days <= t["just_placed_max"]:
        st.code = "JUST_PLACED"
    elif st.days <= t["in_production_max"]:
        st.code = "IN_PRODUCTION"
    elif st.days < t["overdue_from"]:
        st.code = "SHIPPING_SOON"
    else:
        st.code = "OVERDUE"
        st.notes.append(f"unshipped for {st.days} days: check with the POD supplier before replying")
    return st


def pick_order(orders: list[dict], wanted_name: str | None) -> tuple[dict | None, str | None]:
    """Choose the order a ticket is about. Returns (order, problem_stage_code)."""
    if wanted_name:
        want = re.sub(r"\D", "", wanted_name)
        for o in orders:
            if re.sub(r"\D", "", o.get("name", "").replace("MJ4U", "")) == want:
                return o, None
    open_orders = [o for o in orders if not o.get("cancelledAt") and o.get("displayFulfillmentStatus") != "FULFILLED"]
    if not orders:
        return None, "NO_ORDER_FOUND"
    if len(orders) == 1:
        return orders[0], None
    if len(open_orders) == 1:
        return open_orders[0], None
    return None, "MULTIPLE_ORDERS"
