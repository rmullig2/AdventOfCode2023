import sys
import np
import re

def get_input(filename):
    with open(filename) as f:
        strings = f.read().splitlines()
    lines = [['.'] * len(strings[0])]
    for i in range(len(strings)-1, -1, -1):
        lines.append(list(strings[i]))
    return np.array(lines)

def substring_sort(string):
    l = list(string)
    l.sort()
    return "".join(l)

def transpose_and_tilt(input_array):
    transposed_array = np.transpose(input_array)
    transposed_strings, final_strings = [], []
    for arr in transposed_array:
        transposed_list = list(arr)
        transposed_strings.append(''.join(transposed_list))
    for string in transposed_strings:
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
        final_strings.append(current_string)
    return final_strings

def get_total_load(final_strings):
    total = 0
    for string in final_strings:
        for i in range(len(string)):
            if string[i] == 'O':
                total += i
    return total

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: day14_part1 input_filename')
        exit(1)
    input_array = get_input(sys.argv[1])
    final_strings = transpose_and_tilt(input_array)
    print(get_total_load(final_strings))
