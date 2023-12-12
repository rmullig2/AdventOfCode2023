import unittest
from day10_part2 import *
from math import inf

input_list1 = get_input("input_test3.txt")
input_list2 = get_input("input_test4.txt")
input_list3 = get_input("input_test5.txt")
grid1 = get_grid(input_list1)
grid2 = get_grid(input_list2)
grid3 = get_grid(input_list3)
move_grid1 = get_move_grid(grid1)
move_grid2 = get_move_grid(grid2)
move_grid3 = get_move_grid(grid3)

s_location_grid1 = get_s_location(grid1)
s_location_grid2 = get_s_location(grid2)
s_location_grid3 = get_s_location(grid3)

loop1 = get_loop(grid1, move_grid1)
loop2 = get_loop(grid2, move_grid2)
loop3 = get_loop(grid3, move_grid3)

expected_loop1 = [[2,2], [2,3], [2,4], [2,5], [2,6], [2,7], [2,8], [2,9], [2,10],
                  [3,10], [4,10], [5,10], [6,10], [7,10], [8,10], [8,9], [8,8],
                  [8,7], [7,7], [6,7], [6,8], [6,9], [5,9], [4,9], [3,9], [3,8],
                  [3,7], [3,6], [3,5], [3,4], [3,3], [4,3], [5,3], [6,3], [6,4],
                  [6,5], [7,5], [8,5], [8,4], [8,3], [8,2], [7,2], [6,2], [5,2],
                  [4,2], [3,2]]

expected_loop2 = [[5,13], [5,14], [6,14], [7,14], [8,14], [9,14], [10,14], [10,15], [9,15],
                  [8,15], [8,16], [9,16], [10,16], [10,17], [9,17], [8,17], [7,17], [7,16],
                  [6,16], [6,15], [5,15], [5,16], [5,17], [6,17], [6,18], [7,18], [7,19],
                  [8,19], [8,20], [7,20], [6,20], [6,19], [5,19], [5,18], [4,18], [4,17],
                  [4,16], [3,16], [3,15], [2,15], [2,16], [1,16], [1,15], [1,14], [2,14],
                  [3,14], [4,14], [4,13], [3,13], [2,13], [1,13], [1,12], [2,12], [3,12],
                  [4,12], [5,12], [5,11], [4,11], [3,11], [2,11], [1,11], [1,10], [2,10],
                  [3,10], [4,10], [4,9], [3,9], [2,9], [1,9], [1,8], [2,8], [3,8], [4,8],
                  [4,7], [3,7], [2,7], [1,7], [1,6], [1,5], [1,4], [1,3], [1,2], [2,2],
                  [3,2], [4,2], [4,1], [5,1], [5,2], [5,3], [5,4], [4,4], [4,3], [3,3],
                  [2,3], [2,4], [2,5], [2,6], [3,6], [3,5], [4,5], [4,6], [5,6], [5,7],
                  [6,7], [6,6], [6,5], [7,5], [7,6], [8,6], [9,6], [9,5], [10,5], [10,6],
                  [10,7], [10,8], [10,9], [9,9], [9,8], [9,7], [8,7], [8,8], [7,8], [7,9],
                  [8,9], [8,10], [7,10], [6,10], [6,11], [7,11], [8,11], [9,11], [10,11],
                  [10,12], [9,12], [8,12], [8,13], [7,13], [7,12], [6,12], [6,13]]

class LoopLocations(unittest.TestCase):
    def test_loop_locations1(self):
        self.assertEqual(loop1.sort(), expected_loop1.sort())
        self.assertEqual(loop2.sort(), expected_loop2.sort())

mark_outside_nodes(grid3, loop3)
mark_pipe_nodes(grid3, move_grid3, loop3)

class PipeNodes(unittest.TestCase):
    def test_pipe_nodes3(self):
        self.assertEqual(grid3[5][5], 'O')
        self.assertEqual(grid3[5][6], 'O')

mark_outside_nodes(grid3, loop3)

class MarkOutsideNodes(unittest.TestCase):
    def test_outside_nodes(self):
        self.assertEqual(grid3[4][4], 'O')
        self.assertEqual(grid3[7][1], 'O')
        self.assertEqual(grid3[9][5], 'O')
        self.assertEqual(grid3[5][3], '|')

inside_nodes3 = get_inside_nodes(grid3, loop3)

class InsideNodes(unittest.TestCase):
    def test_inside_nodes(self):
        self.assertEqual(len(inside_nodes3), 4)
