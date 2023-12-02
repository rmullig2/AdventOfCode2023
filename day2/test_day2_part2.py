import unittest
from day2_part2 import *

input_list = get_input("input_test.txt")

class DayTwoTestsPartTwo(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_process_game_game1(self):
        self.assertEqual(process_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), 48)
    def test_process_game_game4(self):
        self.assertEqual(process_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"), 630)
    def test_get_total(self):
        self.assertEqual(get_total(input_list), 2286)
