import unittest
from solutions import *

class TestSolutions(unittest.TestCase):

    def setUp(self) -> None:
        self.test_input = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

    def test_07_01(self):
        
        correct_answer = 6440
        
        result = day_07.CamelCards.get_total_winnings(self.test_input)

        self.assertEqual(correct_answer, result)

    def test_07_02(self):

        correct_answer = 5905

        result = day_07.CamelCards.get_total_winnings(self.test_input, with_jokers=True)

        self.assertEqual(correct_answer, result)

if __name__ == '__main__':
    unittest.main()
