import unittest
import string_calc
from MyExceptions import NegativeValueException

class TestCalc(unittest.TestCase):
    def test_sum_of_numbers(self):
        self.assertEqual(string_calc.add(""),0)
        self.assertEqual(string_calc.add("1"),1)
        self.assertEqual(string_calc.add("1,2"),3)

    def test_unknown_amount_of_numbers(self):
        self.assertEqual(string_calc.add("8,17,244,690,812,990"),2761)

    def test_include_alphabets(self):
        self.assertEqual(string_calc.add("a"),1)
        self.assertEqual(string_calc.add("b"),2)
        self.assertEqual(string_calc.add("a,b"),3)
        self.assertEqual(string_calc.add("1,2,y,z"),54)

    def test_no_negative(self):
        self.assertRaises(NegativeValueException,string_calc.add,"-1")
        self.assertRaises(NegativeValueException,string_calc.add,"-2")
        self.assertRaises(NegativeValueException,string_calc.add,"1,2,-3,d")
        self.assertRaises(NegativeValueException,string_calc.add,"-1,-2")

    def test_multiple_negatives(self):
        self.assertRaises(NegativeValueException,string_calc.add,"-2,-1")
        self.assertRaises(NegativeValueException,string_calc.add,"a,4,-4,8,-8,-12")

    def test_ignore_1000_plus(self):
        self.assertEqual(string_calc.add("2022"),0)
        self.assertEqual(string_calc.add("1,2,1001"),3)

    def test_newline_delimiter(self):
        self.assertEqual(string_calc.add("1\n2,3"),6)
        self.assertEqual(string_calc.add("3\na,d\n4,1500"),12)

if __name__ == '__main__':
    unittest.main()