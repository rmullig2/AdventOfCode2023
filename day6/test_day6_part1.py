import unittest
from day6_part1 import *

input_list = get_input("input_test.txt")
times, distances = get_times_and_distances(input_list)

class InputAndList(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_times(self):
        self.assertEqual(times, [7, 15, 30])
    def test_distances(self):
        self.assertEqual(distances, [9, 40, 200])

class RaceWinners(unittest.TestCase):
    def test_first_race(self):
        self.assertEqual(get_number_of_winners(times[0], distances[0]), 4)
    def test_second_race(self):
        self.assertEqual(get_number_of_winners(times[1], distances[1]), 8)
    def test_third_race(self):
        self.assertEqual(get_number_of_winners(times[2], distances[2]), 9)
