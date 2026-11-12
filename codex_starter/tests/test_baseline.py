import copy
import unittest
from triage import prioritize

def ticket(**changes):
    t = dict(id="X", category="question", impact="single", blocked=False,
             age_hours=2, manual_priority=None, notes="Example")
    t.update(changes)
    return t

class BaselineTests(unittest.TestCase):
    def test_output_contract(self):
        result = prioritize(ticket())
        self.assertEqual(set(result), {"id", "priority", "rule", "reason", "review_required"})
        self.assertTrue(result["review_required"])
        self.assertIsInstance(result["reason"], str)
        self.assertTrue(result["reason"].strip())

    def test_input_is_unchanged(self):
        original = ticket()
        before = copy.deepcopy(original)
        prioritize(original)
        self.assertEqual(original, before)
