import unittest
from day2_part1 import *

input_list = get_input("input_test.txt")

class DayTwoTestsPartOne(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_possible_true(self):
        self.assertTrue(determine_possible(7,8,9))
    def test_possible_false(self):
        self.assertFalse(determine_possible(15,8,9))
    def test_process_game_possible(self):
        self.assertEqual(process_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), 1)
    def test_process_game_impossible(self):
        self.assertEqual(process_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"), 0)
    def test_process_game_possible(self):
        self.assertEqual(process_game("Game 99: 2 green, 9 red, 1 blue; 3 green, 1 blue, 14 red; 5 green, 6 blue; 1 blue, 2 green, 3 red; 4 blue, 10 red, 1 green"), 0)
    def test_process_game_possible(self):
        self.assertEqual(process_game("Game 97: 2 green, 2 red; 2 blue, 1 green; 7 blue, 3 red"), 97)
    def test_get_total(self):
        self.assertEqual(get_total(input_list), 8)
