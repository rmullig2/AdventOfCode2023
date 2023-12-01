import unittest
from day1_part2 import *

input_list = get_input("input_test2.txt")

class DayOneTestsPartTwo(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_line_one(self):
        self.assertEqual(input_list[0], "two1nine")
    def test_get_sum(self):
        self.assertEqual(get_sum(input_list), 281)
