import unittest
import string_calc

class TestCalc(unittest.TestCase):
    def test_sum_of_numbers(self):
        self.assertEqual(string_calc.add(""),0)
        self.assertEqual(string_calc.add("1"),1)
        self.assertEqual(string_calc.add("1,2"),3)

if __name__ == '__main__':
    unittest.main()