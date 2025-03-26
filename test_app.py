"""
Unit tests for arithmetic functions in app.py.
"""

import unittest
from app import add, subtract, multiply, divide

class TestApp(unittest.TestCase):
    """Test case for arithmetic functions."""

    def test_add(self):
        """Test addition."""
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(multiply(5, 3), 15)

    def test_divide(self):
        """Test division."""
        self.assertEqual(divide(10, 2), 5)

if __name__ == "__main__":
    unittest.main()
