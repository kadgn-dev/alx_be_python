#!/usr/bin/env python3
"""
Unit tests for the SimpleCalculator class.
Covers addition, subtraction, multiplication, and division.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""

    def setUp(self):
        """Set up a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------------- ADDITION ----------------
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-5, 3), -2)

    def test_add_floats(self):
        """Test addition with floating-point numbers."""
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6, places=1)

    # ---------------- SUBTRACTION ----------------
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(3, 8), -5)

    def test_subtract_negative_numbers(self):
        """Test subtraction involving negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-2, 3), -5)

    def test_subtract_floats(self):
        """Test subtraction with floats."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=1)

    # ---------------- MULTIPLICATION ----------------
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(-2, -4), 8)

    def test_multiply_floats(self):
        """Test multiplication with floats."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 2.0), -3.0)

    # ---------------- DIVISION ----------------
    def test_divide_normal(self):
        """Test normal division."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_negative_and_floats(self):
        """Test division with negative and float numbers."""
        self.assertAlmostEqual(self.calc.divide(-9, 3), -3.0)
        self.assertAlmostEqual(self.calc.divide(5.5, 2.2), 2.5, places=1)


if __name__ == "__main__":
    unittest.main()
