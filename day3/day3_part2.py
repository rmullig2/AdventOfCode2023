import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def make_border(input_list):
    formatted_input = []
    l = len(input_list[0]) + 2
    formatted_input.append('.' * l)
    for i in range(len(input_list)):
        formatted_input.append('.' + input_list[i] + '.')
    formatted_input.append('.' * l)
    return formatted_input

def check_top(row, col, numbers_indexes):
    for i in range(col-1, col+2):
        value = numbers_indexes.get((row-1,i))
        if value:
            return value
    return None

def check_bottom(row, col, numbers_indexes):
    for i in range(col-1, col+2):
        value = numbers_indexes.get((row+1,i))
        if value:
            return value
    return None

def check_left(row, col, numbers_indexes):
    return numbers_indexes.get((row, col-1))

def check_right(row, col, numbers_indexes):
    return numbers_indexes.get((row, col+1))

def add_to_indexes(row, col, num, numbers_indexes):
    start = col
    end = len(num) + col
    for i in range(start, end):
        numbers_indexes[(row, i)] = int(num)

def calculate_sum(formatted_input):
    numbers_indexes = {}
    sum_of_products = 0
    num = ''
    for i in range(1, len(formatted_input)-1):
        if num:
            previous_row = i - 1
            starting_col = len(formatted_input) - 1 - len(num)
            add_to_indexes(previous_row, starting_col, num, numbers_indexes)
            num = ''
        for j in range(1, len(formatted_input[i])-1):
            if formatted_input[i][j] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if num:
                    add_to_indexes(i, j - len(num), num, numbers_indexes)
                    num = ''
            else:
                num += formatted_input[i][j]
    for i in range(1, len(formatted_input)-1):
        for j in range(1, len(formatted_input[i])-1):
            if formatted_input[i][j] == "*":
                numbers_adjacent = []
                top_value = check_top(i, j, numbers_indexes)
                bottom_value = check_bottom(i, j, numbers_indexes)
                left_value = check_left(i, j, numbers_indexes)
                right_value = check_right(i, j, numbers_indexes)
                top_value and numbers_adjacent.append(top_value)
                bottom_value and numbers_adjacent.append(bottom_value)
                left_value and numbers_adjacent.append(left_value)
                right_value and numbers_adjacent.append(right_value)
                if len(numbers_adjacent) == 2:
                    sum_of_products += (numbers_adjacent[0] * numbers_adjacent[1])
    return sum_of_products

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: day3_part1.py input_filename")
        exit(1)
    lines = get_input(sys.argv[1])
    formatted_input = make_border(lines)
    print(calculate_sum(formatted_input))

