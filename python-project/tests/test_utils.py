"""
Unit tests for the utils module.
"""

import unittest
from mypackage.utils import format_greeting, is_even, reverse_string, get_timestamp


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""

    def test_format_greeting_without_title(self):
        """Test greeting without title."""
        result = format_greeting("Alice")
        self.assertEqual(result, "Hello, Alice!")

    def test_format_greeting_with_title(self):
        """Test greeting with title."""
        result = format_greeting("Bob", "Dr.")
        self.assertEqual(result, "Hello, Dr. Bob!")

    def test_is_even(self):
        """Test even number detection."""
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-3))

    def test_reverse_string(self):
        """Test string reversal."""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_get_timestamp(self):
        """Test timestamp generation."""
        timestamp = get_timestamp()
        self.assertIsInstance(timestamp, str)
        # Check it contains date components
        self.assertIn("-", timestamp)
        self.assertIn(":", timestamp)


if __name__ == "__main__":
    unittest.main()
