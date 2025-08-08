
import unittest
from pkg.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_expression_with_precedence(self):
        calculator = Calculator()
        result = calculator.evaluate("3 + 7 * 2")
        self.assertEqual(result, 17.0)

if __name__ == '__main__':
    unittest.main()
