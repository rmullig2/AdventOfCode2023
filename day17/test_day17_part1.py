import unittest
from day17_part1 import *

strings = get_input("input_test.txt")
city_map = build_city_map(strings)

class TestInput(unittest.TestCase):
    def test_input(self):
        self.assertEqual(len(strings), 13)
        self.assertEqual(strings[4][4], '6')
    def test_city_map(self):
        self.assertEqual(type(city_map[0]), list)
        self.assertEqual(city_map[7][2], 3)

class TestPossibleBlocks(unittest.TestCase):
    def test_next_city_block(self):
        self.assertEqual(next_city_block([2,2], 'up'), [1,2])
        self.assertEqual(next_city_block([2,2], 'down'), [3,2])
        self.assertEqual(next_city_block([2,2], 'left'), [2,1])
        self.assertEqual(next_city_block([2,2], 'right'), [2,3])
    def test_in_bounds(self):
        self.assertEqual(in_bounds((2,2), city_map), True)
        self.assertEqual(in_bounds((-1,2), city_map), False)
        self.assertEqual(in_bounds((2,-1), city_map), False)
        self.assertEqual(in_bounds((13,2), city_map), False)
        self.assertEqual(in_bounds((2,13), city_map), False)
    def test_get_possible(self):
        visited = [[0,0], [0,1], [1,0]]
        possible_moves = [([2,1], 'down', 1), ([1,2], "right", 1)]
        self.assertEqual(get_possible_moves([1,1], visited, "left", 1, city_map), possible_moves)
        visited = [[0,0], [0,1], [1,0], [12,7]]
        possible_moves = [([11, 8], 'up', 1)]
        self.assertEqual(get_possible_moves([12, 8], visited, "right", 3, city_map), possible_moves)

class TestDFS(unittest.TestCase):
    def test_dfs(self):
        self.assertEqual(dfs([11, 12], [], 'down', 1, city_map, {'12-12': 3}), 8)
        self.assertEqual(dfs([12, 11], [], 'down', 1, city_map, {'12-12': 3}), 6)
        self.assertEqual(dfs([11, 11], [], 'down', 1, city_map, {'12-12': 3}), 9)
        self.assertEqual(dfs([10, 12], [], 'down', 1, city_map, {'12-12': 3}), 11)
        self.assertEqual(dfs([10, 11], [], 'down', 1, city_map, {'12-12': 3}), 15)
        self.assertEqual(dfs([10, 10], [], 'down', 1, city_map, {'12-12': 3}), 20)
        #self.assertEqual(dfs([11, 11], [], 'down', 1, city_map, {'12-12': 3}), 9)
        #self.assertEqual(dfs([11, 11], [], 'down', 1, city_map, {'12-12': 3}), 9)
