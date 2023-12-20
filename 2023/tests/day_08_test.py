import unittest
from solutions import day_08

class TestSolutions(unittest.TestCase):

    def test_08_01(self):

        self.test_input = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

        correct_answer = 2
        result = day_08.HauntedWasteland.get_steps_count(self.test_input)
        self.assertEqual(correct_answer, result)

        self.test_input = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

        correct_answer = 6
        result = day_08.HauntedWasteland.get_steps_count(self.test_input)
        self.assertEqual(correct_answer, result)

    def test_08_02(self):
        
        self.test_input = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

        correct_answer = 6
        result = day_08.HauntedWasteland.get_ghost_steps_count(self.test_input)
        self.assertEqual(correct_answer, result)

if __name__ == '__main__':
    unittest.main()