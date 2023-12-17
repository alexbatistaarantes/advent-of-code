import unittest
from solutions import *

class TestSolutions(unittest.TestCase):

    def setUp(self) -> None:
        self.test_input = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    def test_05_01(self):
        
        correct_answer = 35
        
        result = day_05.IfYouGiveASeedAFertilizer.get_closest_location(self.test_input)

        self.assertEqual(correct_answer, result)

    # GAVE UP AND USED [THIS ONE](https://github.com/mgtezak/Advent_of_Code/blob/master/2023/Day_05.py) SO I COULD MOVE ON
    def test_05_02(self):

        correct_answer = 46

        result = day_05.IfYouGiveASeedAFertilizer.get_closest_location(self.test_input, seed_is_range=True)

        self.assertEqual(correct_answer, result)

if __name__ == '__main__':
    unittest.main()
