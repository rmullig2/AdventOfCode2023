import unittest
from day1_part1 import *

input_list = get_input("input_test.txt")

class DayOneTestsPartOne(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_line_one(self):
        self.assertEqual(input_list[0], "1abc2")
    def test_get_sum(self):
        sum = get_sum(input_list)
        self.assertEqual(sum, 142)

