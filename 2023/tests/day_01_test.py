import unittest
from solutions import *

class TestSolutions(unittest.TestCase):

    def test_01_01(self):

        test_input = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
        correct_answer = 142
        result = day_01.Trebuchet.get_calibration_from_document(test_input)

        self.assertEqual(correct_answer, result)

    def test_01_02(self):

        test_input = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

        correct_answer = 281
        result = day_01.Trebuchet.get_calibration_from_document_with_spelled_numbers(test_input)

        self.assertEqual(correct_answer, result)


if __name__ == '__main__':
    unittest.main()
