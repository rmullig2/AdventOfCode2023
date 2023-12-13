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
    return new_rows, new_cols

def get_galaxy_list(space):
    galaxy_list = []
    for row in range(len(space)):
        for col in range(len(space[0])):
            if space[row][col] == '#':
                galaxy_list.append([row,col])
    return galaxy_list

def compute_distances(galaxy_list, new_rows, new_cols):
    distances = 0
    while galaxy_list:
        current_galaxy_row, current_galaxy_col = galaxy_list.pop()
        for galaxy in galaxy_list:
            galaxy_row, galaxy_col = galaxy[0], galaxy[1]
            row_start = min(current_galaxy_row, galaxy_row)
            row_end = max(current_galaxy_row, galaxy_row)
            while row_start < row_end:
                row_start += 1
                if row_start in new_rows:
                    distances += 1000000
                else:
                    distances += 1
            col_start = min(current_galaxy_col, galaxy_col)
            col_end = max(current_galaxy_col, galaxy_col)
            while col_start < col_end:
                col_start += 1
                if col_start in new_cols:
                    distances += 1000000
                else:
                    distances += 1
    return distances

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: day11_part1.py input_filename')
        exit(1)
    lines = get_input(sys.argv[1])
    space = process_input(lines)
    new_rows, new_cols = add_rows_and_columns(space)
    galaxy_list = get_galaxy_list(space)
    print(compute_distances(galaxy_list, new_rows, new_cols))
