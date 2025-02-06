import unittest
from calculator import add, multiply

class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add(self):
        """Test addition of two numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        """Test multiplication of two numbers."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 10), 0)

if __name__ == "__main__":
    unittest.main()

