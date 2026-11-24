"""Offline tests: stage rules, order picking, KB matching, draft flags. No network, no keys.
Run: cd ops/customer-support && python3 -m unittest discover -s tests -t ."""
import json, unittest
from datetime import datetime
from pathlib import Path
from cs import draft as D, kb, stages
from cs.config import support_cfg
from cs.shopify import find_order_number

FIX = Path(__file__).parent / "fixtures"
ORDERS = json.loads((FIX / "orders.json").read_text())
NOW = datetime.fromisoformat(ORDERS["_now"])
CFG = support_cfg()


def unf(created, **kw):
    o = {"name": "#1", "createdAt": created, "cancelledAt": None, "displayFinancialStatus": "PAID",
         "displayFulfillmentStatus": "UNFULFILLED", "fulfillments": []}
    o.update(kw)
    return o


class Stages(unittest.TestCase):
    def code(self, o):
        return stages.classify(o, CFG, NOW).code

    def test_unshipped_age_bands(self):
        # now = 2026-11-24; thresholds 2 / 4 / 10
        self.assertEqual(self.code(unf("2026-11-24T01:00:00Z")), "JUST_PLACED")
        self.assertEqual(self.code(unf("2026-11-22T01:00:00Z")), "JUST_PLACED")
        self.assertEqual(self.code(unf("2026-11-21T01:00:00Z")), "IN_PRODUCTION")
        self.assertEqual(self.code(unf("2026-11-20T01:00:00Z")), "IN_PRODUCTION")
        self.assertEqual(self.code(unf("2026-11-19T01:00:00Z")), "SHIPPING_SOON")
        self.assertEqual(self.code(unf("2026-11-15T01:00:00Z")), "SHIPPING_SOON")
        self.assertEqual(self.code(unf("2026-11-14T01:00:00Z")), "OVERDUE")

    def test_terminal_states_win(self):
        self.assertEqual(self.code(unf("2026-11-01T00:00:00Z", cancelledAt="2026-11-02T00:00:00Z")), "CANCELLED")
        self.assertEqual(self.code(unf("2026-11-01T00:00:00Z", displayFinancialStatus="REFUNDED")), "REFUNDED")
        self.assertEqual(self.code(unf("2026-11-20T00:00:00Z", displayFinancialStatus="PENDING")), "PAYMENT_PENDING")
        self.assertEqual(self.code(unf("2026-11-20T00:00:00Z", displayFulfillmentStatus="ON_HOLD")), "ON_HOLD")

    def test_shipped_states(self):
        o = ORDERS["by_email"]["cara@example.com"][0]
        st = stages.classify(o, CFG, NOW)
        self.assertEqual((st.code, st.carrier, st.days), ("SHIPPED", "USPS", 5))
        f = dict(o["fulfillments"][0], displayStatus="DELIVERED")
        self.assertEqual(self.code(dict(o, fulfillments=[f])), "DELIVERED")
        f = dict(o["fulfillments"][0], displayStatus="FAILURE")
        self.assertEqual(self.code(dict(o, fulfillments=[f])), "DELIVERY_ISSUE")
        late = stages.classify(o, CFG, datetime.fromisoformat("2026-12-10T00:00:00+00:00"))
        self.assertEqual(late.code, "SHIPPED_DELAYED")

    def test_business_days(self):
        # Fri 2026-11-20 -> Tue 2026-11-24 = 2 business days, 4 calendar days
        start = datetime.fromisoformat("2026-11-20T10:00:00+00:00")
        self.assertEqual(stages.days_between(start, NOW, "business"), 2)
        self.assertEqual(stages.days_between(start, NOW, "calendar"), 4)

    def test_pick_order(self):
        a, b = unf("2026-11-20T00:00:00Z", name="#1001"), unf("2026-11-10T00:00:00Z", name="#1002")
        self.assertEqual(stages.pick_order([], None), (None, "NO_ORDER_FOUND"))
        self.assertEqual(stages.pick_order([a, b], None), (None, "MULTIPLE_ORDERS"))
        self.assertEqual(stages.pick_order([a, b], "1002")[0]["name"], "#1002")
        b_done = dict(b, displayFulfillmentStatus="FULFILLED")
        self.assertEqual(stages.pick_order([a, b_done], None)[0]["name"], "#1001")


class KbAndDraft(unittest.TestCase):
    def test_kb_entries_valid(self):
        es = kb.load()
        ids = [e["id"] for e in es]
        self.assertEqual(len(ids), len(set(ids)), "duplicate KB ids")
        for e in es:
            self.assertIn(e["status"], kb.STATUSES, e["id"])
            self.assertTrue(e["keywords"], e["id"])
            if e["status"] == "approved" and e["id"] != D.ORDER_STATUS_KB:
                self.assertTrue(e["answer"], f"{e['id']} approved without an answer")

    def test_kb_match(self):
        self.assertEqual(kb.match("Can I change the name? I made a typo")[0].entry["id"], "change-personalization")
        self.assertEqual(kb.match("my package arrived broken")[0].entry["id"], "damaged-item")
        self.assertEqual(kb.match("hello")[:1], [])

    def test_order_number(self):
        self.assertEqual(find_order_number("Order #1234 is late"), "1234")
        self.assertEqual(find_order_number("my order number: 10234"), "10234")
        self.assertIsNone(find_order_number("I ordered 2 items"))

    def test_draft_flags_and_text(self):
        d = D.build(1, "Amy Tran", "when will my order ship?", ORDERS["by_email"]["amy@example.com"], now=NOW)
        self.assertEqual(d.stage, "JUST_PLACED")
        self.assertIn("Hi Amy,", d.text)
        self.assertIn("placed 2 days ago", d.text)
        self.assertTrue(any("unconfirmed fact" in f for f in d.flags))
        d = D.build(2, "", "where is my order", ORDERS["by_email"]["eve@example.com"], now=NOW)
        self.assertEqual(d.stage, "OVERDUE")
        self.assertTrue(d.signals["escalate"])
        self.assertIn("Hi there,", d.text)
        d = D.build(3, "Dan", "where is my order", None, now=NOW)
        self.assertIn("Shopify not checked", d.flags)

    def test_every_stage_has_a_reply(self):
        from cs.config import stage_replies
        codes = {"NO_ORDER_FOUND", "MULTIPLE_ORDERS", "JUST_PLACED", "IN_PRODUCTION", "SHIPPING_SOON", "OVERDUE",
                 "ON_HOLD", "SHIPPED", "PARTIALLY_SHIPPED", "SHIPPED_DELAYED", "DELIVERY_ISSUE", "DELIVERED",
                 "CANCELLED", "REFUNDED", "PAYMENT_PENDING"}
        self.assertEqual(set(stage_replies()), codes)


if __name__ == "__main__":
    unittest.main()
