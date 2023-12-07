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
            high_card.append(hand)
        elif len(unique_ranks) == 4:
            one_pair.append(hand)
        elif len(unique_ranks) == 3:
            if len(re.findall(unique_ranks[0], hand)) == 2:
                two_pair.append(hand)
            elif len(re.findall(unique_ranks[0], hand)) == 3:
                three_of_kind.append(hand)
            else:
                if len(re.findall(unique_ranks[1], hand)) == 2:
                    two_pair.append(hand)
                else:
                    three_of_kind.append(hand)
        elif len(unique_ranks) == 2:
            if len(re.findall(unique_ranks[0], hand)) in [2, 3]:
                full_house.append(hand)
            else:
                four_of_kind.append(hand)
        elif len(unique_ranks) == 1:
             five_of_kind.append(hand)
    return five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card

def type_sort(hand_type):
    alphabet = '23456789TJQKA'
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
        print("Usage: day7_part1.py input_filename")
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
