import unittest
from solutions import *

class TestSolutions(unittest.TestCase):

    def setUp(self) -> None:
        self.test_input = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    def test_03_01(self):
        
        correct_answer = 4361
        
        result = day_03.GearRatios.get_part_numbers_sum(self.test_input)

        self.assertEqual(correct_answer, result)

    def test_03_02(self):

        correct_answer = 467835

        result = day_03.GearRatios.get_gear_ratio_sum(self.test_input)

        self.assertEqual(correct_answer, result)

if __name__ == '__main__':
    unittest.main()
