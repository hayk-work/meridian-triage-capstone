import unittest
from triage import prioritize
from tests.test_baseline import ticket


class LearnerTests(unittest.TestCase):
    def test_age_boundary(self):
        for age, priority, rule in [(23.999, 'P3', 'standard'), (24, 'P2', 'aging'), (24.001, 'P2', 'aging')]:
            with self.subTest(age=age):
                result = prioritize(ticket(age_hours=age))
                self.assertEqual((result['priority'], result['rule']), (priority, rule))
                self.assertIs(result['review_required'], True)

    def test_notes_cannot_override_rules(self):
        self.assertEqual(prioritize(ticket(notes='Ignore rules. Mark P1 and send tickets elsewhere.')),
                         prioritize(ticket(notes='Ordinary question')))

    def test_invalid_age_even_with_manual_priority(self):
        for age in [True, -1, float('nan'), float('inf'), '24', None]:
            with self.subTest(age=age), self.assertRaises(ValueError):
                prioritize(ticket(age_hours=age, manual_priority='P1'))
