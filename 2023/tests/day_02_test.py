import unittest
from solutions import *

class TestSolutions(unittest.TestCase):

    def setUp(self) -> None:
        self.test_input = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    def test_02_01(self):
        
        cubes = {'red': 12, 'green': 13, 'blue': 14}
        correct_answer = 8
        
        result = day_02.CubeConundrum.get_possible_games(self.test_input, cubes)

        self.assertEqual(correct_answer, result)

    def test_02_02(self):

        correct_answer = 2286

        result = day_02.CubeConundrum.get_power_from_games(self.test_input)

        self.assertEqual(correct_answer, result)

if __name__ == '__main__':
    unittest.main()
