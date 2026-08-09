import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(5, '+', 3), 8)
        self.assertEqual(calculate(-1, '+', 1), 0)
        self.assertEqual(calculate(2.5, '+', 2.5), 5.0)

    def test_subtraction(self):
        self.assertEqual(calculate(5, '-', 3), 2)
        self.assertEqual(calculate(1, '-', 5), -4)
        self.assertEqual(calculate(5.5, '-', 2.5), 3.0)

    def test_multiplication(self):
        self.assertEqual(calculate(5, '*', 3), 15)
        self.assertEqual(calculate(-2, '*', 3), -6)
        self.assertEqual(calculate(2.5, '*', 2), 5.0)

    def test_division(self):
        self.assertEqual(calculate(6, '/', 3), 2)
        self.assertEqual(calculate(5, '/', 2), 2.5)
        self.assertEqual(calculate(-6, '/', 2), -3)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, '/', 0)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(5, '%', 3)

if __name__ == '__main__':
    unittest.main()
