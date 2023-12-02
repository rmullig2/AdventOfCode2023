import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def determine_possible(red, green, blue):
    return red <= 12 and green <= 13 and blue <= 14

def process_game(game):
    red, green, blue = 0, 0, 0
    fields = game.split(":")
    game_number = int(fields[0].split(" ")[1])
    games = fields[1].split(";")
    for game in games:
        colors = game.split(",")
        for color in colors:
            color_num = int(color.split(" ")[1])
            color_name = color.split(" ")[2]
            if color_name == 'red':
                red = color_num
            elif color_name == 'green':
                green = color_num
            elif color_name == 'blue':
                blue = color_num
        if not determine_possible(red, green, blue):
            return 0
    return game_number

def get_total(input_lines):
    total = 0
    for game in input_lines:
        total += process_game(game)
    return total

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: day2_part1.py input_filename")
        exit(1)
    input_strings = get_input(sys.argv[1])
    print(get_total(input_strings))

