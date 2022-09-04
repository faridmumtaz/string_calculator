import unittest
import string_calc

class TestCalc(unittest.TestCase):
    def test_sum_of_numbers(self):
        self.assertEqual(string_calc.add(""),0)
        self.assertEqual(string_calc.add("1"),1)
        self.assertEqual(string_calc.add("1,2"),3)

    def test_unknown_amount_of_numbers(self):
        self.assertEqual(string_calc.add("8,17,244,690,812,990"),2761)

if __name__ == '__main__':
    unittest.main()