"""Behavior checks for the published project copies, using unittest only."""

import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load(filename):
    spec = importlib.util.spec_from_file_location(filename[:-3], ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_program(filename, data):
    result = subprocess.run([sys.executable, str(ROOT / filename)], input=data,
                            capture_output=True, text=True, timeout=5)
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return result.stdout


guide = load("event_guide.py")
menu = load("dinner_menu_planner.py")
readings = load("readings_analyzer.py")


class EventGuideTests(unittest.TestCase):
    def test_student_and_nonstudent_prices(self):
        expected = {"music": (12, 25), "sports": (0, 15),
                    "festival": (0, 10), "fundraiser": (5, 20)}
        for event, (student, regular) in expected.items():
            with self.subTest(event=event):
                self.assertEqual(guide.get_ticket_price(event, True), student)
                self.assertEqual(guide.get_ticket_price(event, False), regular)

    def test_age_boundary(self):
        for event in ("music", "fundraiser"):
            self.assertFalse(guide.check_age_limit(event, 17))
            self.assertTrue(guide.check_age_limit(event, 18))
        self.assertTrue(guide.check_age_limit("sports", 12))

    def test_recommendation_combinations(self):
        for mood, money, expected in [("energetic", True, "fundraiser"),
                                      ("energetic", False, "sports"),
                                      ("relaxed", True, "music"),
                                      ("relaxed", False, "festival")]:
            self.assertEqual(guide.recommend_event(mood, money), expected)

    def test_invalid_event_recovers(self):
        output = run_program("event_guide.py", "yes\n18\n1\nunknown\n1\nmusic\n5\n")
        self.assertIn("Please choose one of the listed event types.", output)
        self.assertIn("Ticket price: $12.00", output)

    def test_invalid_menu_recovers(self):
        output = run_program("event_guide.py", "no\n17\n9\n2\nmusic\n5\n")
        self.assertIn("Sorry, that was not a valid option.", output)
        self.assertIn("You may not attend this event.", output)


class DinnerMenuTests(unittest.TestCase):
    def test_duplicate_dishes_count_once_per_guest(self):
        with patch("builtins.input", side_effect=["Guest A", " Pasta ", "pasta", "Soup",
                                                  "Guest B", "PASTA", "salad", "soup"]):
            with contextlib.redirect_stdout(io.StringIO()):
                counts = menu.get_preferences(2)
        self.assertEqual(counts, {"pasta": 2, "soup": 2, "salad": 1})

    def test_common_dishes_are_sorted(self):
        self.assertEqual(menu.find_common_dishes({"soup": 2, "pasta": 2, "salad": 1}, 2),
                         ["pasta", "soup"])

    def test_no_common_dishes(self):
        self.assertEqual(menu.find_common_dishes({"soup": 1, "pasta": 1}, 2), [])

    def test_complete_menu(self):
        output = run_program("dinner_menu_planner.py",
                             "2\nGuest A\npasta\nsoup\nsalad\nGuest B\npasta\nsoup\nrice\n")
        self.assertTrue(output.endswith("For dinner, we will have:\nPasta\nSoup\n"))


class ReadingsTests(unittest.TestCase):
    def test_above_threshold_is_strict(self):
        self.assertEqual(readings.count_above([2, 5, 8, 8], 5), 2)

    def test_remove_only_one_minimum(self):
        values = [5, 2, 2, 8]
        readings.remove_lowest(values)
        self.assertEqual(values, [5, 2, 8])

    def test_empty_readings(self):
        values = []
        readings.remove_lowest(values)
        self.assertEqual(values, [])
        self.assertIn("Readings above 5: 0", run_program("readings_analyzer.py", "0\n5\n"))

    def test_complete_analysis(self):
        output = run_program("readings_analyzer.py", "4\n5\n2\n8\n9\n5\n")
        self.assertIn("Readings above 5: 2", output)
        self.assertIn("After removing the lowest reading: 5 8 9", output)


class PartyCostTests(unittest.TestCase):
    def test_cheaper_to_host_with_multiple_dishes(self):
        output = run_program("party_cost_comparison.py",
                             "10\n3\nPasta\n2\n4\n6\nyes\nSalad\n1\n5\nno\n")
        self.assertIn("This dish will cost $10.00.", output)
        self.assertIn("This dish will cost $5.00.", output)
        self.assertIn("cheaper than attending", output)

    def test_more_expensive_to_host(self):
        output = run_program("party_cost_comparison.py", "10\n2\nPasta\n1\n30\nno\n")
        self.assertIn("cost more than attending", output)

    def test_equal_cost(self):
        output = run_program("party_cost_comparison.py", "10\n2\nPasta\n2\n5\n15\nno\n")
        self.assertIn("cost the same as attending", output)


if __name__ == "__main__":
    unittest.main()
