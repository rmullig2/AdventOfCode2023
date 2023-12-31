import sys
from math import inf

def get_input(filename):
    with open(filename) as f:
        strings = f.read().splitlines()
    return strings

def build_dig_plan(strings):
    dig_plan = []
    for string in strings:
        fields = string.split(' ')
        direction_num = fields[2][-2:-1]
        if direction_num == '0':
            direction = 'R'
        elif direction_num == '1':
            direction = 'D'
        elif direction_num == '2':
            direction = 'L'
        elif direction_num == '3':
            direction = 'U'
        distance_hex = fields[2][2:-2]
        distance = int(distance_hex, 16)
        dig_plan.append((direction, distance))
    return dig_plan

def grid_dimensions(dig_plan):
    min_row = max_row = min_col = max_col = row = col = 0
    for step in dig_plan:
        direction = step[0]
        distance = step[1]
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

def get_lines(dig_plan):
    lines = []
    current_location = (0, 0)
    for step in dig_plan:
        direction = step[0]
        distance = step[1]
        row, col = current_location[0], current_location[1]
        print(f'direction: {direction}, row: {row}, col: {col}, distance: {distance}')
        if direction == 'U':
            end_location = ((row - distance), col)
        elif direction == 'D':
            end_location = ((row + distance), col)
        elif direction == 'L':
            end_location = (row, (col - distance))
        elif direction == 'R':
            end_location = (row, (col + distance))
        lines.append((current_location, end_location))
        current_location = end_location
    return lines

def in_grid(location, grid):
    row, col = location[0], location[1]
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

def free_neighbor(location, grid):
    row, col = location[0], location[1]
    north_neighbor = [row-1, col]
    south_neighbor = [row+1, col]
    west_neighbor =  [row, col-1]
    east_neighbor =  [row, col+1]
    if in_grid(north_neighbor, grid) and grid[row-1][col] == 'F':
        return True
    if in_grid(south_neighbor, grid) and grid[row+1][col] == 'F':
        return True
    if in_grid(west_neighbor, grid) and grid[row][col-1] == 'F':
        return True
    if in_grid(east_neighbor, grid) and grid[row][col+1] == 'F':
        return True
    return False

def change_enclosed(grid):
    for i in range(len(grid[0])):
        if grid[0][i] == '.':
            grid[0][i] = 'F'
        if grid[len(grid)-1][i] == '.':
            grid[len(grid)-1][i] = 'F'
    for i in range(len(grid)):
        if grid[i][0] == '.':
            grid[i][0] = 'F'
        if grid[i][len(grid[0])-1] == '.':
            grid[i][len(grid[0])-1] = 'F'
    changed = True
    while changed:
        changed = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '.' and free_neighbor([i,j], grid):
                    grid[i][j] = 'F'
                    changed = True

def count_enclosed(grid):
    rows, cols = len(grid), len(grid[0])
    enclosed = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] in ['#', '.']:
                enclosed += 1
    return enclosed

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage day18_part2.py input_filename')
        exit(1)
    strings = get_input(sys.argv[1])
    dig_plan = build_dig_plan(strings)
    lines = get_lines(dig_plan)
    exit(1)
    #grid = draw_grid(rows, cols, start, dig_plan)
    #change_enclosed(grid)
    #print(count_enclosed(grid))
