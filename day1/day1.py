#!/home/rmulligan/AdventOfCode2023/venv/bin/python
import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_sum(input_list):
    sum, first, last = 0, 0, 0
    for line in input_list:
        line_forward = line
        line_backward = line[-1::-1]
        for ch in line_forward:
            if ch.isdigit():
                first = int(ch)
                break
        for ch in line_backward:
            if ch.isdigit():
                last = int(ch)
                break
        sum += (first*10 + last)
    return sum

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: day1.py input_filename")
        exit(1)
    input_strings = get_input(sys.argv[1])
    print(get_sum(input_strings))
