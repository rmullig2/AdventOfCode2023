import unittest
from day4_part1 import *

input_list = get_input("input_test.txt")
card1 = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
winners = ['83', '86', '17', '48']

class DayThreeTestsPartOne(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_process_card(self):
        winning_cards, my_cards = process_card(card1)
        self.assertEqual(winning_cards, ['41', '48', '83', '86', '17'])
        self.assertEqual(my_cards, ['83', '86', '6', '31', '17', '9', '48', '53'])
        self.assertEqual(find_winners(winning_cards, my_cards), winners)
    def test_card_total(self):
        self.assertEqual(card_total(winners), 8)
