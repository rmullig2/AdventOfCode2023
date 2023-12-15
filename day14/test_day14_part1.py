import unittest
import np
from day14_part1 import *

input_array = get_input("input_test.txt")

class TestInput(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(input_array), 11)
    def test_type(self):
        self.assertEqual(type(input_array), np.ndarray)

class TestSubstringSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(substring_sort('OO..O..OO.O'), '.....OOOOOO')
        self.assertEqual(substring_sort('.OOO.O...O.'), '......OOOOO')
        self.assertEqual(substring_sort('.O..OOO.OOO'), '....OOOOOOO')
        self.assertEqual(substring_sort('OOO..OO...O'), '.....OOOOOO')

tilted = transpose_and_tilt(input_array)

class TestTransposeTile(unittest.TestCase):
    def test_transpose_tilt(self):
        self.assertEqual(tilted[0], '.##....OOOO')
        self.assertEqual(tilted[1], '........OOO')

total_load = get_total_load(tilted)

class TestTotalLoad(unittest.TestCase):
    def test_total_load(self):
        self.assertEqual(total_load, 136)
