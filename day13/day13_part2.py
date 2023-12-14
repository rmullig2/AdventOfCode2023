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

def get_differences(pattern, start, end):
    differences = 0
    for i in range(len(pattern[start])):
        if pattern[start][i] != pattern[end][i]:
            differences += 1
    return differences

def almost_perfect_reflection(pattern, row):
    differences = 0
    start, end = row, row+1
    while start >= 0 and end < len(pattern):
        differences += get_differences(pattern, start, end)
        start -= 1
        end += 1
    return differences == 1

def get_horizontal(pattern):
    for row in range(len(pattern)-1):
        if almost_perfect_reflection(pattern, row):
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
        print("Usage day13_part2.py input_filename")
        exit(1)
    lines = get_input(sys.argv[1])
    patterns = get_patterns(lines)
    get_total(patterns)
