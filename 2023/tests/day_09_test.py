import unittest
from solutions import day_09

class TestSolutions(unittest.TestCase):

    def setUp(self):
        self.test_input = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

    def test_09_01(self):

        correct_answer = 114
        result = day_09.MirageMaintenance.get_extrapolated_values_sum(self.test_input)
        self.assertEqual(correct_answer, result)

    def test_09_02(self):

        correct_answer = 2
        result = day_09.MirageMaintenance.get_extrapolated_values_sum(self.test_input, backwards=True)
        self.assertEqual(correct_answer, result)

if __name__ == '__main__':
    unittest.main()
