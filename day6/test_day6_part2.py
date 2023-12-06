import unittest
from day6_part2 import *

input_list = get_input("input_test.txt")
time, distance = get_time_and_distance(input_list)

class InputAndList(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_times(self):
        self.assertEqual(time, 71530)
    def test_distances(self):
        self.assertEqual(distance, 940200)

class RaceWinners(unittest.TestCase):
    def test_race(self):
        self.assertEqual(get_number_of_winners(time, distance), 71503)
