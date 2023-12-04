import unittest
from day3_part2 import *

input_list = get_input("input_test.txt")
formatted_input = make_border(input_list)

class DayThreeTestsPartTwo(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_border(self):
        self.assertEqual(len(input_list)+2, len(formatted_input))
    def test_calculate_sum(self):
       self.assertEqual(calculate_sum(formatted_input), 467835)

