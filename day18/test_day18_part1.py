import unittest
from day18_part1 import *

strings = get_input("input_test.txt")
dig_plan = build_dig_plan(strings)

class TestInput(unittest.TestCase):
    def test_input(self):
        self.assertEqual(len(strings), 14)
        self.assertEqual(strings[2], 'L 2 (#5713f0)')
    def test_dig_plan(self):
        self.assertEqual(dig_plan[3][0], 'D')
        self.assertEqual(dig_plan[7][2], '(#caa173)')

rows, cols, start = grid_dimensions(dig_plan)
grid = draw_grid(rows, cols, start, dig_plan)

class TestGrid(unittest.TestCase):
    def test_dimensions(self):
        self.assertEqual(rows, 10)
        self.assertEqual(cols, 7)
        self.assertEqual(start, [0,0])
    def test_draw_grid(self):
        self.assertEqual(grid[2][3], '.')
        self.assertEqual(grid[5][6], '#')
        self.assertEqual(grid[7][1], '#')

class TestChanges(unittest.TestCase):
    def test_valid_neighbors(self):
        self.assertEqual(valid_neighbors([1,1], [1,1], grid), [[1,2]])
        self.assertEqual(valid_neighbors([5,3], [5,3], grid), [[4,3], [6,3]])
    def test_no_way_out(self):
        self.assertEqual(no_way_out([1,2], grid), True)
        self.assertEqual(no_way_out([6,5], grid), False)

new_grid = [row[:] for row in grid]
change_enclosed(new_grid)

class TestChangeEnclosed(unittest.TestCase):
    def test_change_enclosed(self):
        self.assertEqual(new_grid[1][2], '#')
        self.assertEqual(new_grid[3][1], '.')
        self.assertEqual(new_grid[6][6], '.')
    def test_count_enclosed(self):
        self.assertEqual(count_enclosed(new_grid), 62)
