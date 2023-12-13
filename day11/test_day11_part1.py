import unittest
from day11_part1 import *

input_list = get_input("input_test.txt")
space = process_input(input_list)

class ReadAndProcessInput(unittest.TestCase):
    def test_get_input(self):
        self.assertEqual(type(input_list), list)
    def test_process_input(self):
        self.assertEqual(space[0][7], '.')

new_space = add_rows_and_columns(space)

class AddRowsAndColumns(unittest.TestCase):
    def test_new_rows(self):
        self.assertEqual(len(new_space), len(space)+2)
    def test_new_cols(self):
        self.assertEqual(len(new_space[0]), 13)

galaxies = get_galaxy_list(new_space)
expected_galaxies = [[0,4], [1,9], [2,0], [5,8], [6,1], [7, 12], [10,9], [11,0], [11,5]]

class GetGalaxies(unittest.TestCase):
    def test_galaxies(self):
        self.assertEqual(galaxies, expected_galaxies)

new_galaxies = []
for galaxy in galaxies:
    new_galaxies.append(galaxy)
distances = compute_distances(new_galaxies)

class ComputeDistances(unittest.TestCase):
    def test_compute_distances(self):
        self.assertEqual(distances, 374)
