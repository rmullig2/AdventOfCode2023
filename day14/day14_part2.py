import sys
import np
import re
import functools

def get_input(filename):
    with open(filename) as f:
        strings = f.read().splitlines()
    lines = []
    for i in range(len(strings)):
        lines.append(list(strings[i]))
    return np.array(lines)

def substring_sort(string):
    l = list(string)
    l.sort()
    return "".join(l)

def strings_to_array(string_list):
    l = []
    for row in string_list:
        l.append(list(row))
    return np.array(l)

@functools.cache
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

def tilt_array(input_array):
    string_list, tilted_strings = [], []
    for arr in input_array:
        row = list(arr)
        string_list.append(''.join(row))

    for string in string_list:
        #indexes = [index.start(0) for index in re.finditer('#', string)]
        #start = 0
        #current_string = ""
        #while indexes:
        #    index = indexes.pop(0)
        #    sorted_substring = substring_sort(string[start:index])
        #    current_string += sorted_substring + '#'
        #    start = index + 1
        #if start < len(string):
        #    current_string += substring_sort(string[start:])
        current_string = tilt_string(string)
        tilted_strings.append(current_string)

    return strings_to_array(tilted_strings)

def transpose_and_tilt(input_array):
    # Tilting Northa
    #print(f'input_array:\n{input_array}')
    input_array = np.flip(input_array, 0)
    input_array = np.transpose(input_array)
    input_array = tilt_array(input_array)
    input_array = np.transpose(input_array)
    input_array = np.flip(input_array, 0)
    #print(f'After North tilt:\n{input_array}')

    # Tilting West
    input_array = np.flip(input_array, 1)
    input_array = tilt_array(input_array)
    input_array = np.flip(input_array, 1)
    #print(f'After West tilt:\n{input_array}')

    # Tilting South
    input_array = np.transpose(input_array)
    input_array = tilt_array(input_array)
    input_array = np.transpose(input_array)
    #print(f'After South tilt:\n{input_array}')

    # Tilting East
    input_array = tilt_array(input_array)
    #print(f'After East tilt:\n{input_array}')

    return input_array

def get_total_load(final_array):
    total = 0
    print(final_array)
    for row in final_array:
        string = "".join(row)
        for i in range(len(string)):
            if string[i] == 'O':
                total += i
    return total

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: day14_part2 input_filename')
        exit(1)
    input_array = get_input(sys.argv[1])
    original_array = np.copy(input_array)

    for i in range(1000000000):
        input_array = transpose_and_tilt(input_array)
        if i % 10000000 == 0:
            print(f'Completed {i} cycles, {1000000000-i} cycles remaining.')
    print(get_total_load(input_array))
