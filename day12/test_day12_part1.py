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

arrangements0 = get_possible_arrangements(spring_rows[0], broken_number[0])
arrangements1 = get_possible_arrangements(spring_rows[1], broken_number[1])
arrangements2 = get_possible_arrangements(spring_rows[2], broken_number[2])
arrangements3 = get_possible_arrangements(spring_rows[3], broken_number[3])
arrangements4 = get_possible_arrangements(spring_rows[4], broken_number[4])
arrangements5 = get_possible_arrangements(spring_rows[5], broken_number[5])

valid_arrangements0 = get_valid_arrangements(arrangements0, broken_number[0])
valid_arrangements1 = get_valid_arrangements(arrangements1, broken_number[1])
valid_arrangements2 = get_valid_arrangements(arrangements2, broken_number[2])
valid_arrangements3 = get_valid_arrangements(arrangements3, broken_number[3])
valid_arrangements4 = get_valid_arrangements(arrangements4, broken_number[4])
valid_arrangements5 = get_valid_arrangements(arrangements5, broken_number[5])

total_valid = get_total_valid(spring_rows, broken_number)

class CalculateArrangements(unittest.TestCase):
    def test_possible_arrangements(self):
        self.assertEqual(len(arrangements0), 3)
        self.assertEqual(len(arrangements1), 10)
        self.assertEqual(len(arrangements2), 70)
        self.assertEqual(len(arrangements3), 1)
        self.assertEqual(len(arrangements4), 4)
        self.assertEqual(len(arrangements5), 84)
    def test_valid_arrangements(self):
        self.assertEqual(len(valid_arrangements0), 1)
        self.assertEqual(len(valid_arrangements1), 4)
        self.assertEqual(len(valid_arrangements2), 1)
        self.assertEqual(len(valid_arrangements3), 1)
        self.assertEqual(len(valid_arrangements4), 4)
        self.assertEqual(len(valid_arrangements5), 10)
    def test_total_arrangements(self):
        self.assertEqual(len(total_valid), 21)
