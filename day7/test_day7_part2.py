import unittest
from day7_part2 import *

input_list = get_input("input_test.txt")

class ProcessInput(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)

bids = create_bids(input_list)
hands = create_hands(input_list)

class BidsAndHands(unittest.TestCase):
    def test_bids(self):
        self.assertEqual(bids['T55J5'], 684)
        self.assertEqual(bids['QQQJA'], 483)
    def test_hands(self):
        self.assertEqual(hands[2], 'KK677')
        self.assertEqual(hands[4], 'QQQJA')

hands_test = ['A72QT', '8883K', 'AAJAA', 'J39AT', '73K99', '88888', '7KK77', 'KKKJ9', '3T92A', 'A66J9', 'J7J43', 'A8A87', 'K33KJ', '77277']
five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card = strength_sort(hands_test)

class HandStrength(unittest.TestCase):
    def test_five_of_kind(self):
        self.assertEqual(five_of_kind, ['AAJAA', '88888'])
    def test_four_of_kind(self):
        self.assertEqual(four_of_kind, ['KKKJ9', '77277'])
    def test_full_house(self):
        self.assertEqual(full_house, ['7KK77', 'K33KJ'])
    def test_three_of_kind(self):
        self.assertEqual(three_of_kind, ['8883K', 'A66J9', 'J7J43'])
    def test_two_pair(self):
        self.assertEqual(two_pair, ['A8A87'])
    def test_one_pair(self):
        self.assertEqual(one_pair, ['J39AT', '73K99'])
    def test_high_card(self):
        self.assertEqual(high_card, ['A72QT', '3T92A'])

five_of_kind_test = ['77777', 'JJJJJ', '22222']
four_of_kind_test = ['27777', '2JJJJ', '29222']
full_house_test = ['37773', 'JJJAA', 'A22A2']
three_of_kind_test = ['7JJJ7', '77222', '7AAA7']
two_pair_test = ['72J27', '33KK9', '727A2']
one_pair_test = ['7A8J9', '7A827', '797JQ']
high_card_test = ['7AQT8', '72T98', '792AK']

class SortedType(unittest.TestCase):
    def test_five_of_kind_sort(self):
        self.assertEqual(type_sort(five_of_kind_test), ['JJJJJ', '22222', '77777'])
    def test_four_of_kind_sort(self):
        self.assertEqual(type_sort(four_of_kind_test), ['2JJJJ', '27777', '29222'])
    def test_full_house_sort(self):
        self.assertEqual(type_sort(full_house_test), ['JJJAA', '37773', 'A22A2'])
    def test_three_of_kind_sort(self):
        self.assertEqual(type_sort(three_of_kind_test), ['7JJJ7', '77222', '7AAA7'])
    def test_two_pair_sort(self):
        self.assertEqual(type_sort(two_pair_test), ['33KK9', '72J27', '727A2'])
    def test_one_pair_sort(self):
        self.assertEqual(type_sort(one_pair_test), ['797JQ', '7A8J9', '7A827'])
    def test_high_card_sort(self):
        self.assertEqual(type_sort(high_card_test), ['72T98', '792AK', '7AQT8'])

high_card_final = []
one_pair_final = ['32T3K']
two_pair_final = ['KTJJT', 'KK677']
three_of_kind_final = ['T55J5', 'QQQJA']
full_house_final = []
four_of_kind_final = []
five_of_kind_final = []
total_winnings = get_total_winnings(bids, high_card_final, one_pair_final, two_pair_final, three_of_kind_final, full_house_final, four_of_kind_final, five_of_kind_final)

class TotalWinnings(unittest.TestCase):
    def test_total_winnings(self):
        self.assertEqual(total_winnings, 6440)
