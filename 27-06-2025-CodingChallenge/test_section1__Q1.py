# test_section1q1.py
import unittest
from io import StringIO
import sys

# Import the functions from your section1q1 script
import section1__Q1

class TestMovieBooking(unittest.TestCase):
    def test_calculate_amount(self):
        # Test known prices
        self.assertEqual(section1__Q1.calculate_amount("Avengers", 3), 250 * 3)
        self.assertEqual(section1__Q1.calculate_amount("Parasite", 2), 150 * 2)
        # Unknown movie should cost 0
        self.assertEqual(section1__Q1.calculate_amount("Unknown", 5), 0)

    def test_booking_flow_valid(self):
        # Simulate user input: pick movie 1 (Avengers), then 2 tickets
        inputs = ["1", "2"]
        # Capture stdout
        backup_stdout = sys.stdout
        sys.stdout = StringIO()
        # Monkey-patch input()
        backup_input = __builtins__.input
        __builtins__.input = lambda prompt="": inputs.pop(0)

        try:
            section1__Q1.book_tickets()
            output = sys.stdout.getvalue()
        finally:
            # Restore
            sys.stdout = backup_stdout
            __builtins__.input = backup_input

        # Check that the output mentions the correct booking and total
        self.assertIn("booked 2 ticket", output)
        self.assertIn("Total amount: Rs.500", output)

    def test_booking_flow_invalid_movie(self):
        # Non-numeric movie choice should abort early
        inputs = ["x"]
        backup_stdout = sys.stdout
        sys.stdout = StringIO()
        backup_input = __builtins__.input
        __builtins__.input = lambda prompt="": inputs.pop(0)

        try:
            section1__Q1.book_tickets()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = backup_stdout
            __builtins__.input = backup_input

        self.assertIn("Invalid input", output)

    def test_booking_flow_invalid_qty(self):
        # Valid movie choice, then invalid ticket count
        inputs = ["2", "-3"]
        backup_stdout = sys.stdout
        sys.stdout = StringIO()
        backup_input = __builtins__.input
        __builtins__.input = lambda prompt="": inputs.pop(0)

        try:
            section1__Q1.book_tickets()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = backup_stdout
            __builtins__.input = backup_input

        self.assertIn("Invalid input", output)

if __name__ == "__main__":
    unittest.main()
