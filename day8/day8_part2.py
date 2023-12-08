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

def get_start_nodes(nodes):
    end_nodes = []
    for node in nodes:
        if node[2] == 'A':
            end_nodes.append(node)
    return end_nodes

def check_finish(nodes):
    finished = True
    for node in nodes:
        if node[2] != 'Z':
            return False
    return True

def get_steps(instructions, nodes):
    steps = 0
    locations = get_start_nodes(list(nodes.keys()))
    while True:
        instruction = instructions[steps % len(instructions)]
        if instruction == 'L':
            for i in range(len(locations)):
                new_location = nodes[locations[i]][0]
                locations[i] = new_location
        else:
            for i in range(len(locations)):
                new_location = nodes[locations[i]][1]
                locations[i] = new_location
        steps += 1
        if check_finish(locations):
            return steps
        if not (steps % 1000000):
            print(f'steps: {steps}')
            print(f'locations: {locations}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: day8_part2.py input_filename")
        exit(1)
    input_list = get_input(sys.argv[1])
    instructions = get_instructions(input_list)
    nodes = get_nodes(input_list)
    print(get_steps(instructions, nodes))
