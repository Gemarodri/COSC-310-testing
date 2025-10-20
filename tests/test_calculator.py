import unittest
from src.calculator import add,subtract

class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add(self):
        """Test addition of two numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 5.6), 7.1)

    def test_sub(self):
        """Test substraction of two numbers."""
        self.assertEqual(subtract(3, 7), -4)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(2.1, 2), 0.1)

if __name__ == "__main__":
    unittest.main()

