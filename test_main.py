"""Basic unit tests for the expense tracker."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main


class ExpenseTrackerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_data_file = main.DATA_FILE
        main.DATA_FILE = Path(self.temp_dir.name) / "expenses.csv"

    def tearDown(self):
        main.DATA_FILE = self.original_data_file
        self.temp_dir.cleanup()

    def test_load_expenses_when_file_does_not_exist(self):
        self.assertEqual(main.load_expenses(), [])

    def test_save_and_load_expense(self):
        expense = {
            "date": "2026-11-11",
            "description": "Lunch",
            "category": "Food",
            "amount": "1500.00",
        }
        main.save_expense(expense)
        self.assertEqual(main.load_expenses(), [expense])

    def test_ask_amount_accepts_valid_amount(self):
        with patch("builtins.input", side_effect=["2,500.50"]):
            self.assertEqual(main.ask_amount(), "2500.50")

    def test_ask_amount_rejects_invalid_then_accepts_valid(self):
        with patch("builtins.input", side_effect=["abc", "-5", "200"]):
            self.assertEqual(main.ask_amount(), "200.00")


if __name__ == "__main__":
    unittest.main()
