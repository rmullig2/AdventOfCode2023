import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def process_input(lines):
    space = []
    for line in lines:
        space.append(list(line))
    return space

def add_rows_and_columns(space):
    new_rows, new_cols, new_space = [], [], []
    for row in range(len(space)):
        blank = True
        for col in range(len(space[0])):
            if space[row][col] != '.':
                blank = False
        if blank:
            new_rows.append(row)
    for col in range(len(space[0])):
        blank = True
        for row in range(len(space)):
            if space[row][col] != '.':
                blank = False
        if blank:
            new_cols.append(col)
    counter = 1
    for row in range(len(space)):
        new_space.append(space[row])
        if row in new_rows:
            new_space.append(['.'] * len(space[0]))
    counter = 1
    for col in range(len(space[0])):
        if col in new_cols:
            for row in range(len(new_space)):
                new_space[row].insert(col+counter, '.')
            counter += 1
    return new_space

def get_galaxy_list(space):
    galaxy_list = []
    for row in range(len(space)):
        for col in range(len(space[0])):
            if space[row][col] == '#':
                galaxy_list.append([row,col])
    return galaxy_list

def compute_distances(galaxy_list):
    distances = 0
    while galaxy_list:
        current_galaxy = galaxy_list.pop()
        for galaxy in galaxy_list:
            distances += abs(current_galaxy[0] - galaxy[0]) + abs(current_galaxy[1] - galaxy[1])
    return distances

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: day11_part1.py input_filename')
        exit(1)
    lines = get_input(sys.argv[1])
    space = process_input(lines)
    space = add_rows_and_columns(space)
    galaxy_list = get_galaxy_list(space)
    print(compute_distances(galaxy_list))
