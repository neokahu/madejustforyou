"""Customer-support CLI. Run from ops/customer-support:

  python3 -m cs.run demo                  # offline walk-through on fixtures (no keys needed)
  python3 -m cs.run inbox                 # Open Freshdesk tickets (statuses in config), each with its order stage
  python3 -m cs.run ticket 123            # one ticket: thread, orders, stage, KB hits, draft, flags
  python3 -m cs.run ticket 123 --json
  python3 -m cs.run send 123 --file reply.txt            # shows what would be sent; sends nothing
  python3 -m cs.run send 123 --file reply.txt --yes      # posts the public reply, then sets the ticket Resolved
  python3 -m cs.run send 123 --file reply.txt --yes --status pending   # reply asks the customer something
  python3 -m cs.run send 123 --file reply.txt --note --yes   # private note instead (customer never sees it)
  python3 -m cs.run kb [missing|list|show <id>]

Reads never change anything. Only `send ... --yes` writes, and it logs the outcome to log/ (gitignored)
as training data for the future confidence score.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
from . import draft as D, kb, stages
from .config import LOG_DIR, ROOT, support_cfg

FIX = ROOT / "tests" / "fixtures"


def _first_name(t: dict) -> str:
    return ((t.get("requester") or {}).get("name") or "").strip()


def _email(t: dict) -> str:
    return (t.get("requester") or {}).get("email") or ""


def _customer_text(t: dict, convs: list[dict]) -> str:
    from .freshdesk import plain
    parts = [t.get("subject") or "", plain(t)]
    parts += [plain(c) for c in convs if c.get("incoming")]
    return "\n".join(p for p in parts if p)


def _orders(shop, email: str, text: str) -> list[dict] | None:
    if shop is None:
        return None
    from .shopify import find_order_number
    num = find_order_number(text)
    found = shop.order_by_name(num) if num else []
    return found or (shop.orders_by_email(email) if email else [])


def _shop_or_none(no_shopify: bool):
    if no_shopify:
        return None
    from .shopify import Shopify
    return Shopify()


def show(d: D.Draft, as_json: bool, header: str = ""):
    if as_json:
        print(json.dumps(d.to_dict(), indent=2, ensure_ascii=False))
        return
    if header:
        print(header)
    print(f"intent: {d.intent}   stage: {d.stage}   kb: {', '.join(h['id'] + ':' + str(h['score']) for h in d.kb_hits) or '-'}")
    print("flags: " + ("; ".join(d.flags) if d.flags else "none"))
    print("-" * 60 + "\n" + d.text + "\n" + "-" * 60)


def cmd_demo(_):
    tickets = json.loads((FIX / "tickets.json").read_text())
    orders = json.loads((FIX / "orders.json").read_text())
    now = datetime.fromisoformat(orders["_now"])
    for t in tickets:
        found = orders["by_email"].get(t["requester"]["email"], [])
        d = D.build(t["id"], _first_name(t), t["subject"] + "\n" + t["description_text"], found, now=now)
        show(d, False, f"\n#{t['id']}  {t['subject']}  <{t['requester']['email']}>")


def cmd_inbox(a):
    from .freshdesk import Freshdesk, STATUS
    fd, shop = Freshdesk(), _shop_or_none(a.no_shopify)
    cfg = support_cfg()
    ts = fd.open_tickets(tuple(cfg["freshdesk_open_statuses"]))
    print(f"{len(ts)} open/pending ticket(s)")
    for t in ts:
        text = _customer_text(t, [])
        orders = _orders(shop, _email(t), text)
        stage = "-"
        if orders is not None:
            o, problem = stages.pick_order(orders, D.stages_order_hint(text))
            stage = problem or f"{stages.classify(o, cfg).code} {o['name']}"
        print(f"#{t['id']:<6} {STATUS.get(t['status'], t['status']):<8} {t['created_at'][:10]}  {stage:<24} {t.get('subject','')[:60]}")


def cmd_ticket(a):
    from .freshdesk import Freshdesk, plain
    fd, shop = Freshdesk(), _shop_or_none(a.no_shopify)
    t = fd.ticket(a.id)
    convs = fd.conversations(a.id)
    text = _customer_text(t, convs)
    orders = _orders(shop, _email(t), text)
    if not a.json:
        print(f"#{t['id']}  {t.get('subject')}\nfrom: {_first_name(t)} <{_email(t)}>\n")
        print("CUSTOMER: " + plain(t))
        for c in convs:
            print(("CUSTOMER: " if c.get("incoming") else ("NOTE: " if c.get("private") else "US: ")) + plain(c))
        if orders is not None:
            print(f"\norders found: {len(orders)}")
            for o in orders:
                st = stages.classify(o, support_cfg())
                items = ", ".join(f"{li['quantity']}x {li['title']}" for li in o["lineItems"]["nodes"])
                print(f"  {o['name']}  placed {o['createdAt'][:10]}  {o['displayFulfillmentStatus']}  -> {st.code}  [{items}]")
        print()
    show(D.build(a.id, _first_name(t), text, orders), a.json)


# Status after a public reply. Resolved: answered, nothing more needed. Pending: the reply asks the customer
# something (order number, photo). Either way it drops out of `inbox`; Freshdesk reopens it when the customer writes back.
SEND_STATUS = {"pending": 3, "resolved": 4}


def cmd_send(a):
    text = Path(a.file).read_text(encoding="utf-8").strip()
    kind = "PRIVATE NOTE" if a.note else "PUBLIC REPLY to the customer"
    print(f"{kind} on ticket #{a.id}:\n" + "-" * 60 + f"\n{text}\n" + "-" * 60)
    if not a.note and a.status != "keep":
        print(f"After sending, the ticket is set to {a.status.capitalize()}.")
    if not a.yes:
        print("Not sent. Add --yes to send.")
        return
    from .freshdesk import Freshdesk
    fd = Freshdesk()
    (fd.note if a.note else fd.reply)(a.id, text)
    status = None if a.note or a.status == "keep" else SEND_STATUS[a.status]
    if status:
        fd.set_status(a.id, status)
    LOG_DIR.mkdir(exist_ok=True)
    rec = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "ticket": a.id, "kind": "note" if a.note else "reply", "status": a.status,
           "draft_sha": a.draft_sha, "final_sha": hashlib.sha1(text.encode()).hexdigest()[:12], "final": text}
    with open(LOG_DIR / "sent.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("Sent." + (f" Ticket set to {a.status.capitalize()}." if status else ""))


def cmd_kb(a):
    es = kb.load()
    if a.action == "show":
        print(json.dumps(next(e for e in es if e["id"] == a.id), indent=2, ensure_ascii=False))
        return
    rows = [e for e in es if a.action == "list" or e["status"] == "needs_answer"]
    counts = {s: sum(e["status"] == s for e in es) for s in kb.STATUSES}
    print(f"{len(es)} entries  " + "  ".join(f"{k}={v}" for k, v in counts.items()))
    cat = None
    for e in rows:
        if e["category"] != cat:
            cat = e["category"]
            print(f"\n## {cat}")
        print(f"  [{e['status']:<12}] {e['id']:<26} {e['question']}")


def main(argv=None):
    p = argparse.ArgumentParser(prog="cs.run")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("demo")
    i = sub.add_parser("inbox"); i.add_argument("--no-shopify", action="store_true")
    t = sub.add_parser("ticket"); t.add_argument("id", type=int); t.add_argument("--json", action="store_true")
    t.add_argument("--no-shopify", action="store_true")
    s = sub.add_parser("send"); s.add_argument("id", type=int); s.add_argument("--file", required=True)
    s.add_argument("--note", action="store_true"); s.add_argument("--yes", action="store_true")
    s.add_argument("--status", choices=["resolved", "pending", "keep"], default="resolved",
                   help="ticket status after a public reply (default resolved; notes never change status)")
    s.add_argument("--draft-sha", default=None, help="sha of the original draft, to log whether it was edited")
    k = sub.add_parser("kb"); k.add_argument("action", nargs="?", default="missing", choices=["missing", "list", "show"])
    k.add_argument("id", nargs="?")
    a = p.parse_args(argv)
    {"demo": cmd_demo, "inbox": cmd_inbox, "ticket": cmd_ticket, "send": cmd_send, "kb": cmd_kb}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
