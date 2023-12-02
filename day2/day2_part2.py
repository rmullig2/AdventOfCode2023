import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

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
            if color_name == 'red' and color_num > red:
                red = color_num
            elif color_name == 'green' and color_num > green:
                green = color_num
            elif color_name == 'blue' and color_num > blue:
                blue = color_num
    return red * green * blue

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
