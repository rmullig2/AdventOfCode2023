#!/home/rmulligan/AdventOfCode2023/venv/bin/python
import sys, re
from day1_part1 import get_input

def get_first_and_last(s):
    value = 0
    num_locations = {}
    num_strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(1, 10):
        matches = list(re.finditer(str(i), s))
        for match in matches:
            num_locations[match.span()[0]] = i
    for i in range(len(num_strings)):
        matches = list(re.finditer(num_strings[i], s))
        for match in matches:
            num_locations[match.span()[0]] = i
    first = num_locations[min(num_locations.keys())]
    last =  num_locations[max(num_locations.keys())]
    value = (first * 10) + last
    return value

def get_sum(input_list):
    sum = 0
    for s in input_list:
        sum += get_first_and_last(s)
    return sum

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: day1.py input_filename")
        exit(1)
    input_strings = get_input(sys.argv[1])
    print(get_sum(input_strings))
