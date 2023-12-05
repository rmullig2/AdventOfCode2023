import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def process_card(card):
    winning_cards = card.split(':')[1].split('|')[0].split()
    my_cards = card.split(':')[1].split('|')[1].split()
    return winning_cards, my_cards

def find_winners(winning_cards, my_cards):
    winning_dict = {}
    for w in winning_cards:
        winning_dict[w] = 1
    winners = []
    for card in my_cards:
        if winning_dict.get(card):
            winners.append(card)
    return len(winners)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: day4_part1.py input_filename")
        exit(1)
    card_input = get_input(sys.argv[1])
    winning_cards = []
    my_cards = []
    total = [1] * len(card_input)
    for i in range(len(total)):
        winning_cards, my_cards = process_card(card_input[i])
        winners = find_winners(winning_cards, my_cards)
        for j in range(i+1, i+1+winners):
            total[j] += total[i]
    print(sum(total))
