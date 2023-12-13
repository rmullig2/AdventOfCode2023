import sys
import np

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_patterns(lines):
    pattern, patterns = [], []
    for line in lines:
        if line:
            pattern.append(line)
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)
    return patterns

def perfect_reflection(pattern, first, second):
    while first > 0 and second < len(pattern)-1:
        first -= 1
        second += 1
        if pattern[first] != pattern[second]:
            return False
    return True

def get_horizontal(pattern):
    for row in range(len(pattern)-1):
        if pattern[row] == pattern[row+1] and perfect_reflection(pattern, row, row+1):
            return row+1
    return 0

def get_vertical(pattern):
    list_of_lists = []
    for line in pattern:
        list_of_lists.append(list(line))
    transposed_list_of_lists = np.transpose(list_of_lists)
    new_pattern = []
    for transposed_list in transposed_list_of_lists:
        new_pattern.append(''.join(transposed_list))
    return get_horizontal(new_pattern)

def get_total(patterns):
    total = 0
    for pattern in patterns:
        score = get_horizontal(pattern)
        if score:
            total += (score * 100)
        else:
            total += get_vertical(pattern)
    print(total)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage day13_part1.py input_filename")
        exit(1)
    lines = get_input(sys.argv[1])
    patterns = get_patterns(lines)
    get_total(patterns)
