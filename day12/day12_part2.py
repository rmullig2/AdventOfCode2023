import sys
from itertools import combinations
import re

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def unfold(string, indicator):
    new_string = string
    for i in range(4):
        if indicator == "spring row":
            new_string += '?' + string
        elif indicator == "broken number":
            new_string += ',' + string
    return new_string

def get_spring_rows_and_broken_number(lines):
    spring_rows, broken_number = [], []
    for line in lines:
        first, second = line.split(' ')
        #spring_row = line.split(' ')[0]a
        spring_row = unfold(first, "spring row")
        #broken = list(map(int, line.split(' ')[1].split(',')))
        broken = list(map(int, unfold(second, "broken number").split(',')))
        spring_rows.append(spring_row)
        broken_number.append(broken)
    return spring_rows, broken_number

def get_possible_arrangements(spring_row, broken):
    found_broken =  len(re.findall('#', spring_row))
    total_broken = sum(broken)
    unknown_broken = total_broken - found_broken
    unknown_locations = []
    for location in re.finditer('\?', spring_row):
        unknown_locations.append(location.start())
    possible_locations = list(combinations(unknown_locations, unknown_broken))
    possible_strings = []
    for location in possible_locations:
        spring_row_list = list(spring_row)
        for index in location:
            spring_row_list[index] = '#'
        for index in range(len(spring_row_list)):
            if spring_row_list[index] == '?':
                spring_row_list[index] = '.'
        possible_strings.append(''.join(spring_row_list))
    return possible_strings

def get_valid_arrangements(possible_strings, broken):
    valid_strings = []
    for string in possible_strings:
        split_string = string.split('.')
        remove_empty = [s for s in split_string if s]
        new_broken = [len(s) for s in remove_empty]
        if new_broken == broken:
            valid_strings.append(string)
    return valid_strings

def get_total_valid(spring_rows, broken_number):
    valid = []
    for i in range(len(spring_rows)):
        possible_arrangements = get_possible_arrangements(spring_rows[i], broken_number[i])
        valid += get_valid_arrangements(possible_arrangements, broken_number[i])
    return valid

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage day12_part2.py input_filename')
        exit(1)
    lines = get_input(sys.argv[1])
    spring_rows, broken_number = get_spring_rows_and_broken_number(lines)
    total_valid = get_total_valid(spring_rows, broken_number)
    print(len(total_valid))
