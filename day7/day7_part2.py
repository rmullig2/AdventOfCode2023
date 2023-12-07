import sys
import re

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def create_bids(input_file):
    bids = {}
    for line in input_file:
        hand, bid = line.split()
        bids[hand] = int(bid)
    return bids

def create_hands(input_file):
    hands = []
    for line in input_file:
        hands.append(line.split()[0])
    return hands

def strength_sort(hands):
    five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card = [], [], [], [], [], [], []
    for hand in hands:
        unique_ranks = list(set(hand))
        if len(unique_ranks) == 5:
            if 'J' in unique_ranks:
                one_pair.append(hand)
            else:
                high_card.append(hand)
        elif len(unique_ranks) == 4:
            if 'J' in unique_ranks:
                three_of_kind.append(hand)
            else:
                one_pair.append(hand)
        elif len(unique_ranks) == 3:					# two pair or three of a kind
            if len(re.findall(unique_ranks[0], hand)) == 2:		# two pair
                if 'J' not in unique_ranks:				# AA228
                    two_pair.append(hand)
                else:
                    if len(re.findall('J', hand)) == 2:			# JJ797
                        four_of_kind.append(hand)
                    else:
                        full_house.append(hand)				# 33J44
            elif len(re.findall(unique_ranks[0], hand)) == 3:		# three of a kind
                if 'J' not in unique_ranks:				# 7772A
                    three_of_kind.append(hand)
                else:							# J2229
                    four_of_kind.append(hand)
            elif len(re.findall(unique_ranks[0], hand)) == 1:		# can be either two pair or three of a kind
                if len(re.findall(unique_ranks[1], hand)) == 2:		# two pair
                    if 'J' in unique_ranks:
                        if len(re.findall('J', hand)) == 2:		# 3TTJJ
                            four_of_kind.append(hand)
                        else:						# J5522
                            full_house.append(hand)
                    else:
                        two_pair.append(hand)
                elif len(re.findall(unique_ranks[1], hand)) in [1, 3]:	# second character is one or three, therefore three of a kind
                    if 'J' in unique_ranks:				# J3933 or 7JJJ9
                        four_of_kind.append(hand)
                    else:						# 87AAA or 3KKK9
                        three_of_kind.append(hand)
        elif len(unique_ranks) == 2:
            if len(re.findall(unique_ranks[0], hand)) in [2, 3]:	# full house
                if 'J' in unique_ranks:
                    five_of_kind.append(hand)				# JJ333
                else:
                    full_house.append(hand)				# 55888
            else:							# four of a kind
                if 'J' in unique_ranks:
                    five_of_kind.append(hand)				# AJAAA
                else:
                    four_of_kind.append(hand)				# TT8TT
        elif len(unique_ranks) == 1:
             five_of_kind.append(hand)
    return five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card

def type_sort(hand_type):
    alphabet = 'J23456789TQKA'
    return sorted(hand_type, key=lambda word: [alphabet.index(c) for c in word])

def get_total_winnings(bids, high_card, one_pair, two_pair, three_of_kind, full_house, four_of_kind, five_of_kind):
    winnings = 0
    counter = 1
    for hand_type in [high_card, one_pair, two_pair, three_of_kind, full_house, four_of_kind, five_of_kind]:
        for hand in hand_type:
            winnings += counter * bids[hand]
            counter += 1
    return winnings

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: day7_part2.py input_filename")
        exit(1)
    input_list = get_input(sys.argv[1])
    bids = create_bids(input_list)
    hands = create_hands(input_list)
    five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card = strength_sort(hands)
    five_of_kind = type_sort(five_of_kind)
    four_of_kind = type_sort(four_of_kind)
    full_house = type_sort(full_house)
    three_of_kind = type_sort(three_of_kind)
    two_pair = type_sort(two_pair)
    one_pair = type_sort(one_pair)
    high_card = type_sort(high_card)
    print(get_total_winnings(bids, high_card, one_pair, two_pair, three_of_kind, full_house, four_of_kind, five_of_kind))
