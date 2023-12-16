import sys
import np
import re

string_cache = {}
map_cache = {}

def get_input(filename):
    with open(filename) as f:
        rock_map = f.read().splitlines()
    return rock_map

def flatten(rock_map):
    s = ""
    for string in rock_map:
        s += "".join(string)
    return s

def substring_sort(string):
    l = list(string)
    l.sort()
    return "".join(l)

def tilt_string(string):
    indexes = [index.start(0) for index in re.finditer('#', string)]
    start = 0
    current_string = ""
    while indexes:
        index = indexes.pop(0)
        sorted_substring = substring_sort(string[start:index])
        current_string += sorted_substring + '#'
        start = index + 1
    if start < len(string):
        current_string += substring_sort(string[start:])
    return current_string

def tilt_list(rock_map):
    tilted_strings = []
    for string in rock_map:
        current_string = string_cache.get(string)
        if not current_string:
            current_string = tilt_string(string)
            string_cache[string] = current_string
        tilted_strings.append(current_string)
    return tilted_strings

def tilt_north(rock_map):
    north = ["".join(reversed(x)) for x in list(zip(*rock_map))]
    rock_string = flatten(north)
    if map_cache.get(rock_string):
        north = list(map_cache.get(rock_string))
    else:
        north = tilt_list(north)
        map_cache[rock_string] = tuple(north)
    return ["".join(x) for x in reversed(list(zip(*north)))]

def tilt_west(rock_map):
    west = ["".join(reversed(x)) for x in rock_map]
    rock_string = flatten(west)
    if map_cache.get(rock_string):
        west = list(map_cache.get(rock_string))
    else:
        west = tilt_list(west)
        map_cache[rock_string] = tuple(west)
    return ["".join(reversed(x)) for x in west]

def tilt_south(rock_map):
    south = ["".join(x) for x in list(zip(*rock_map))]
    rock_string = flatten(south)
    if map_cache.get(rock_string):
        south = list(map_cache.get(rock_string))
    else:
        south = tilt_list(south)
        map_cache[rock_string] = tuple(south)
    return ["".join(x) for x in list(zip(*south))]

def tilt_east(rock_map):
    east = rock_map
    rock_string = flatten(east)
    if map_cache.get(rock_string):
        east = list(map_cache.get(rock_string))
    else:
        east = tilt_list(east)
        map_cache[rock_string] = tuple(east)
    return east

def cycle(rock_map):
    rock_map = tilt_north(rock_map)
    rock_map = tilt_west(rock_map)
    rock_map = tilt_south(rock_map)
    rock_map = tilt_east(rock_map)
    return rock_map

def get_total_load(rock_map):
    total = 0
    counter = 10
    for string in rock_map:
        for i in range(len(string)):
            if string[i] == 'O':
                total += counter
        counter -= 1
    return total

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: day14_part2 input_filename')
        exit(1)
    rock_map = get_input(sys.argv[1])
    results = []
    results.append(rock_map.copy())
    #for i in range(1000000000):
    for i in range(27):
        results.append(rock_map.copy())
        rock_map = cycle(rock_map)
        #if i % 1000000 == 0:
        #    print(f'Completed {i} cycles, {1000000000-i} cycles remaining.')
    result_totals = []
    for i in range(len(results)):
        result_totals.append([])
    for i in range(len(results)):
        for j in range(i+1, len(results)):
            if results[i] == results[j]:
                result_totals[i].append(j)
    for i in range(len(result_totals)):
        print(f'{i} matches {result_totals[i]}')
    print(get_total_load(rock_map))
