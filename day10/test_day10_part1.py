import unittest
from day10_part1 import *
from math import inf

input_list1 = get_input("input_test1.txt")
input_list2 = get_input("input_test2.txt")
initial_grid1 = get_initial_grid(input_list1)
initial_grid2 = get_initial_grid(input_list2)
move_grid1 = get_move_grid(initial_grid1)
move_grid2 = get_move_grid(initial_grid2)

class ReadAndProcessInput(unittest.TestCase):
    def test_get_input(self):
        self.assertEqual(type(input_list1), list)
        self.assertEqual(type(input_list2), list)
    def test_initial_grid(self):
        self.assertEqual(initial_grid1[2][4], '7')
        self.assertEqual(initial_grid2[3][5], '7')
    def test_move_grid(self):
        self.assertEqual(move_grid1[3][2], ('north', 'south'))
        self.assertEqual(move_grid2[3][5], ('south', 'west'))

start_value_grid1 = initialize_value_grid(initial_grid1)
start_value_grid2 = initialize_value_grid(initial_grid2)
s_location_grid1 = get_s_location(initial_grid1)
s_location_grid2 = get_s_location(initial_grid2)
initial_moves1 = get_initial_moves(s_location_grid1, move_grid1)
initial_moves2 = get_initial_moves(s_location_grid2, move_grid2)

class IntializeAndSetValues(unittest.TestCase):
    def test_initial_value_grid(self):
        self.assertEqual(start_value_grid1[2][4], inf)
        self.assertEqual(start_value_grid2[3][5], inf)
    def test_get_s_location(self):
        self.assertEqual(s_location_grid1, (2,2))
        self.assertEqual(s_location_grid2, (3,1))
    def test_get_initial_moves(self):
        self.assertEqual(initial_moves1, [[3,2], [2,3]])
        self.assertEqual(initial_moves2, [[4,1], [3,2]])

adjacent_moves1_1 = get_adjacent_moves([2,4], move_grid1)
adjacent_moves1_2 = get_adjacent_moves([4,2], move_grid1)
adjacent_moves2_1 = get_adjacent_moves([3,4], move_grid2)
adjacent_moves2_2 = get_adjacent_moves([4,3], move_grid2)

class AdjacentMoves(unittest.TestCase):
    def test_get_adjacent_moves(self):
        self.assertEqual(adjacent_moves1_1, [[3,4], [2,3]])
        self.assertEqual(adjacent_moves1_2, [[3,2], [4,3]])
        self.assertEqual(adjacent_moves2_1, [[2,4], [3,5]])
        self.assertEqual(adjacent_moves2_2, [[4,4], [4,2]])

test_value_grid1 = initialize_value_grid(initial_grid1)
test_value_grid2 = initialize_value_grid(initial_grid2)
compute_steps(initial_grid1, move_grid1, test_value_grid1)
compute_steps(initial_grid2, move_grid2, test_value_grid2)

class ComputeSteps(unittest.TestCase):
    def test_compute_steps(self):
        results1 = [[inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf],
                    [inf, inf, 0, 1, 2, inf, inf],  [inf, inf, 1, inf, 3, inf, inf], [inf, inf, 2, 3, 4, inf, inf],
                    [inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf]]
        results2 = [[inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, 4, 5, inf, inf],
                    [inf, inf, 2, 3, 6, inf, inf], [inf, 0, 1, inf, 7, 8, inf], [inf, 1, 4, 5, 6, 7, inf],
                    [inf, 2, 3, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf]]
        self.assertEqual(results1, test_value_grid1)
        self.assertEqual(results2, test_value_grid2)

farthest_point1 = get_farthest_point(test_value_grid1)
farthest_point2 = get_farthest_point(test_value_grid2)

class ComputeFathestPoint(unittest.TestCase):
    def test_farthest_point(self):
        self.assertEqual(farthest_point1, 4)
        self.assertEqual(farthest_point2, 8)
