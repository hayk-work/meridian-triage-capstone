import unittest
from triage import prioritize
from tests.test_baseline import ticket

class AcceptanceTests(unittest.TestCase):
    def check(self, expected, rule, **fields):
        result = prioritize(ticket(**fields))
        self.assertEqual(result["priority"], expected)
        self.assertEqual(result["rule"], rule)
        self.assertTrue(result["review_required"])

    def test_company_outage(self):
        self.check("P1", "company_outage", category="incident", impact="company", blocked=True)

    def test_blocked_work(self):
        self.check("P2", "blocked", category="access", blocked=True)

    def test_aged_ticket(self):
        self.check("P2", "aging", age_hours=30)

    def test_manual_priority_precedes_outage(self):
        self.check("P3", "manual", category="incident", impact="company", blocked=True, manual_priority="P3")

    def test_blocked_precedes_aging(self):
        self.check("P2", "blocked", blocked=True, age_hours=48)

    def test_negative_age_rejected(self):
        with self.assertRaises(ValueError):
            prioritize(ticket(age_hours=-1))

    def test_invalid_category_rejected(self):
        with self.assertRaises(ValueError):
            prioritize(ticket(category="unknown"))
