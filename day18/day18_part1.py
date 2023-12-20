import sys
from math import inf

def get_input(filename):
    with open(filename) as f:
        strings = f.read().splitlines()
    return strings

def build_dig_plan(strings):
    dig_plan = []
    for string in strings:
        dig_plan.append(string.split(' '))
    return dig_plan

def grid_dimensions(dig_plan):
    min_row = max_row = min_col = max_col = row = col = 0
    for step in dig_plan:
        direction = step[0]
        distance = int(step[1])
        if direction == 'U':
            row -= distance
            if row < min_row: min_row = row
        elif direction == 'D':
            row += distance
            if row > max_row: max_row = row
        elif direction == 'L':
            col -= distance
            if col < min_col: min_col = col
        elif direction == 'R':
            col += distance
            if col > max_col: max_col = col
    rows = max_row - min_row + 1
    cols = max_col - min_col + 1
    start_row = rows - max_row - 1
    start_col = cols - max_col - 1
    return rows, cols, [start_row, start_col]

def draw_grid(rows, cols, start, dig_plan):
    grid = []
    for i in range(rows):
        grid.append(['.'] * cols)
    current_row, current_col = start[0], start[1]
    for step in dig_plan:
        direction = step[0]
        distance = int(step[1])
        if direction == 'U':
            for row in range(current_row, current_row - (distance+1), -1):
                grid[row][current_col] = '#'
            current_row = row
        elif direction == 'D':
            for row in range(current_row, current_row + (distance+1)):
                grid[row][current_col] = '#'
            current_row = row
        elif direction == 'L':
            for col in range(current_col, current_col - (distance+1), -1):
                grid[current_row][col] = '#'
            current_col = col
        elif direction == 'R':
            for col in range(current_col, current_col + (distance+1)):
                grid[current_row][col] = '#'
            current_col = col
    return grid

def valid_neighbors(location, visited, grid):
    possible_neighbors = []
    valid_neighbors = []
    row, col = location[0], location[1]
    possible_neighbors.append([row-1, col])
    possible_neighbors.append([row+1, col])
    possible_neighbors.append([row, col-1])
    possible_neighbors.append([row, col+1])
    for neighbor in possible_neighbors:
        if grid[neighbor[0]][neighbor[1]] == '.' and neighbor not in visited:
            valid_neighbors.append(neighbor)
    return valid_neighbors

def no_way_out_old(location, grid):
    check_list = [location]
    visited = []
    while check_list:
        current_location = check_list.pop(0)
        visited.append(current_location)
        row, col = current_location[0], current_location[1]
        if row in [0, len(grid)-1]:
            return False
        if col in [0, len(grid[0])-1]:
            return False
        for neighbor in valid_neighbors(current_location, visited, grid):
            check_list.append(neighbor)
    return True

def no_way_out(location, grid):
    row, col = location[0], location[1]
    first_row = first_col = inf
    last_row = last_col = -inf
    for i in range(len(grid[0])):
        if grid[row][i] == '#':
            first_col = i
            break
    for i in range(len(grid[0])-1, -1, -1):
        if grid[row][i] == '#':
            last_col = i
            break
    for i in range(len(grid)):
        if grid[i][col] == '#':
            first_row = i
            break
    for i in range(len(grid)-1, -1, -1):
        if grid[i][col] == '#':
            last_row = i
            break
    if col > first_col and col < last_col and row > first_row and row < last_row:
        return True
    return False

def change_enclosed(grid):
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '.' and no_way_out([row, col], grid):
                grid[row][col] = '#'
                print(f'Changed {row}-{col}')

def count_enclosed(grid):
    rows, cols = len(grid), len(grid[0])
    enclosed = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '#':
                enclosed += 1
    return enclosed

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage day18_part1.py input_filename')
        exit(1)
    strings = get_input(sys.argv[1])
    dig_plan = build_dig_plan(strings)
    rows, cols, start = grid_dimensions(dig_plan)
    grid = draw_grid(rows, cols, start, dig_plan)
    change_enclosed(grid)
    print(count_enclosed(grid))
