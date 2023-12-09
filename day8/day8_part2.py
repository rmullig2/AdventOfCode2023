import sys
import re
from functools import reduce

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

def get_locations(nodes):
    locations = []
    for node in nodes:
        if node[2] == 'A':
            locations.append(node)
    return locations

def get_steps(instructions, nodes, location):
    steps = 0
    while True:
        instruction = instructions[steps % len(instructions)]
        if instruction == 'L':
            location = nodes[location][0]
        else:
            location = nodes[location][1]
        steps += 1
        if location[2] == 'Z':
            return steps

def get_factors(num):
    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append(i)
    return factors

def get_common_factor(factor_sets):
    common_factor = set(factor_sets[0])
    for i in range(1, len(factor_sets)):
        common_factor = common_factor & set(factor_sets[i])
    return int(list(common_factor)[0])

def get_total_steps(common_factor, factor_sets):
    for factor_set in factor_sets:
        factor_set.remove(common_factor)
    total_steps = common_factor
    for factor_set in factor_sets:
        total_steps *= factor_set.pop()
    return total_steps

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: day8_part1.py input_filename")
        exit(1)
    input_list = get_input(sys.argv[1])
    instructions = get_instructions(input_list)
    nodes = get_nodes(input_list)
    locations = get_locations(nodes)
    steps = []
    for location in locations:
        steps.append(get_steps(instructions, nodes, location))
    factor_sets = []
    for step in steps:
        factor_sets.append(get_factors(step))
    common_factor = get_common_factor(factor_sets)
    print(get_total_steps(common_factor, factor_sets))
