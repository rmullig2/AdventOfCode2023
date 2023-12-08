import sys
import re

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_instructions(input_list):
    return input_list[0]

def get_nodes(input_list):
    nodes = {}
    for line in input_list[2:]:
        items = re.findall('[A-Z]+', line)
        nodes[items[0]] = (items[1], items[2])
    return nodes

def get_steps(instructions, nodes):
    steps = 0
    location = 'AAA'
    while True:
        instruction = instructions[steps % len(instructions)]
        if instruction == 'L':
            location = nodes[location][0]
        else:
            location = nodes[location][1]
        steps += 1
        if location == 'ZZZ':
            return steps

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: day8_part1.py input_filename")
        exit(1)
    input_list = get_input(sys.argv[1])
    instructions = get_instructions(input_list)
    nodes = get_nodes(input_list)
    print(get_steps(instructions, nodes))
