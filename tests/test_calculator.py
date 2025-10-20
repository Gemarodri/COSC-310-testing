import unittest
from src.calculator import add

class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add(self):
        """Test addition of two numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 5.6), 7.1)

if __name__ == "__main__":
    unittest.main()

