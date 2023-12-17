import unittest
from solutions import *

class TestSolutions(unittest.TestCase):

    def setUp(self) -> None:
        self.test_input = """\
Time:      7  15   30
Distance:  9  40  200"""

    def test_06_01(self):
        
        correct_answer = 288
        
        result = day_06.WaitForIt.get_product_of_number_of_ways_to_beat_record(self.test_input)

        self.assertEqual(correct_answer, result)

    def test_06_02(self):

        correct_answer = 71503

        result = day_06.WaitForIt.get_number_of_ways_to_beat_record_from_sheet(self.test_input)

        self.assertEqual(correct_answer, result)

if __name__ == '__main__':
    unittest.main()
