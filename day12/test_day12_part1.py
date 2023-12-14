import unittest
from day12_part1 import *

input_list = get_input("input_test.txt")
spring_rows, broken_number = get_spring_rows_and_broken_number(input_list)

class ReadAndProcessInput(unittest.TestCase):
    def test_get_input(self):
        self.assertEqual(type(input_list), list)
    def test_initial_grid(self):
        self.assertEqual(spring_rows[2][4], '?')
        self.assertEqual(spring_rows[3][5], '#')

arrangements1 = equal_areas_and_groups(spring_rows[1], broken_number[1])

class CalculateArrangements(unittest.TestCase):
    def test_both_equal(self):
        self.assertEqual(len(get_areas(spring_rows[1])), 3)
        self.assertEqual(arrangements1, 4)
