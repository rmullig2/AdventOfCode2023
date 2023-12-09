import unittest
from day9_part1 import *

input_list = get_input("input_test.txt")
num_list = string_to_list(input_list[0])
next_value = get_next_value(num_list)
total_sum = get_sum_of_lists(input_list)

class ReadAndProcessInput(unittest.TestCase):
    def test_get_input(self):
        self.assertEqual(type(input_list), list)
    def test_convert_string_to_list(self):
        self.assertEqual(type(num_list[-1]), int)

class ComputeNextNumber(unittest.TestCase):
    def test_get_next_value(self):
        self.assertEqual(next_value, 18)

class ComputeTotal(unittest.TestCase):
    def test_get_sum_of_lists(self):
        self.assertEqual(total_sum, 114)
