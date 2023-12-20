import unittest
from day18_part2 import *

strings = get_input("input_test.txt")
dig_plan = build_dig_plan(strings)

class TestInput(unittest.TestCase):
    def test_input(self):
        self.assertEqual(len(strings), 14)
        self.assertEqual(strings[2], 'L 2 (#5713f0)')
    def test_dig_plan(self):
        self.assertEqual(dig_plan[3][0], 'D')
        self.assertEqual(dig_plan[7][1], 829975)

rows, cols, start = grid_dimensions(dig_plan)
grid = draw_grid(rows, cols, start, dig_plan)

change_enclosed(grid)

class TestChangeEnclosed(unittest.TestCase):
    def test_count_enclosed(self):
        self.assertEqual(count_enclosed(new_grid), 952408144115)
