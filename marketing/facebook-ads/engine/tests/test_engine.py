"""Tests for the FB-ads decision engine: break-even economics and the kill/keep/scale verdicts.

Run: python3 -m unittest discover -s marketing/facebook-ads/engine/tests   (or: bash scripts/verify.sh)
Read-only: uses sample_data.json and config/, never calls Meta, never writes reports.
"""
from __future__ import annotations

import json
import math
import sys
import unittest
from pathlib import Path

ENGINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ENGINE))

import economics  # noqa: E402
import rules  # noqa: E402


class TestEconomics(unittest.TestCase):
    def test_break_even_by_hand(self):
        # revenue 50, cogs 20, fee 10% -> fee 5, contribution 25, break-even ROAS 50/25 = 2.0
        e = economics.Economics("T-1", "test", revenue_per_order=50, cogs_all_in=20, fee_pct=0.10)
        self.assertAlmostEqual(e.fee, 5.0)
        self.assertAlmostEqual(e.contribution, 25.0)
        self.assertAlmostEqual(e.break_even_cpa, 25.0)
        self.assertAlmostEqual(e.break_even_roas, 2.0)

    def test_roas_uses_pixel_value_when_it_differs(self):
        # pixel reports 45 (no shipping) while true revenue is 50: ROAS is judged on what Meta sees
        e = economics.Economics("T-2", "test", 50, 20, 0.10, reported_value_per_order=45)
        self.assertAlmostEqual(e.break_even_roas, 45 / 25)
        self.assertAlmostEqual(e.break_even_cpa, 25.0)  # CPA still on true revenue

    def test_no_margin_means_no_roas_can_break_even(self):
        e = economics.Economics("T-3", "test", 30, 30, 0.0)
        self.assertTrue(math.isinf(e.break_even_roas))

    def test_products_config_loads_with_positive_margin(self):
        products = economics.load_products(ENGINE / "config" / "products.json")
        self.assertIn("MJ4U-111", products)
        for p in products.values():
            self.assertGreater(p.contribution, 0, f"{p.product_id} has no margin: check products.json")


class TestProductCode(unittest.TestCase):
    def test_maps_campaign_to_product(self):
        self.assertEqual(rules.product_code("MJ4U-111 | Garden Film | Linear entry"), "MJ4U-111")
        self.assertIsNone(rules.product_code("Generic retargeting"))
        self.assertIsNone(rules.product_code(None))


class TestVerdictsOnSample(unittest.TestCase):
    """Characterization test: locks today's verdicts on the synthetic sample.
    If a rule or threshold change moves a verdict, this fails on purpose: confirm the new
    verdict is intended, then update EXPECTED in the same commit as the rule change."""

    EXPECTED = {
        "Linear-entry v1": "SCALE",
        "Linear-entry v2 (young)": "KEEP",
        "Emotional-VO": "KEEP",
        "Flash-forward hook": "KILL",
        "Static testimonial": "KILL",
        "UGC unboxing": "WATCH",
        "Grandkids-POV test (dud)": "KILL",
        "Generic retargeting": "UNMAPPED",
    }

    def test_sample_verdicts(self):
        data = json.loads((ENGINE / "sample_data.json").read_text())
        products = economics.load_products(ENGINE / "config" / "products.json")
        thr = rules.load_thresholds(ENGINE / "config" / "thresholds.json")
        got = {}
        for row in data["insights"]:
            m = rules.normalize_row(row)
            code = rules.product_code(m.campaign_name)
            got[m.ad_name] = rules.decide(m, products.get(code) if code else None, thr).verdict
        self.assertEqual(got, self.EXPECTED)


if __name__ == "__main__":
    unittest.main()
