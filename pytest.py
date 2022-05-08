import Calculator
import unittest

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator.Calculator()

    def test_add_method(self):
        result = self.calculator.add(4, 2)
        self.assertEqual(6, result)

    def test_add_method_invalid_value(self):
        self.assertRaises(ValueError, self.calculator.add, "four", "five")

    def test_multiply_method(self):
        result = self.calculator.multiply(5, 3)
        self.assertEqual(15, result)

    def test_multiply_method_invalid_value(self):
        self.assertRaises(ValueError, self.calculator.multiply, "four", "five")

    def test_sub_method(self):
        result = self.calculator.sub(6, 4)
        self.assertEqual(2, result)

    def test_sub_method_invalid_value(self):
        self.assertRaises(ValueError, self.calculator.sub, "four", "five")

if __name__ == '__main__':
    unittest.main()
