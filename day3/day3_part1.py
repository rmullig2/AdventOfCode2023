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

def check_adjacent(row, col, formatted_input):
    if formatted_input[row-1][col-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return True
    if formatted_input[row-1][col] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return True
    if formatted_input[row-1][col+1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return True
    if formatted_input[row][col-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return True
    if formatted_input[row][col+1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return True
    if formatted_input[row+1][col-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return True
    if formatted_input[row+1][col] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return True
    if formatted_input[row+1][col+1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return True
    return False

def check_number(row, col, formatted_input, num):
    for i in range(col-len(num), col):
        if check_adjacent(row, i, formatted_input):
            return True
    return False

def calculate_sum(formatted_input):
    sum_of_nums = 0
    num = ''
    for i in range(1, len(formatted_input)-1):
        if num:
            if check_number(i-1, len(formatted_input[i])-1, formatted_input, num):
                sum_of_nums += int(num)
                num = ''
        for j in range(1, len(formatted_input[i])-1):
            if formatted_input[i][j] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if num:
                    if check_number(i, j, formatted_input, num):
                        sum_of_nums += int(num)
                    num = ''
            else:
                num += formatted_input[i][j]
    return sum_of_nums

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: day3_part1.py input_filename")
        exit(1)
    lines = get_input(sys.argv[1])
    formatted_input = make_border(lines)
    print(calculate_sum(formatted_input))

