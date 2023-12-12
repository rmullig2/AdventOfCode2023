import sys
from math import inf

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_initial_grid(lines):
    initial_grid = []
    initial_grid.append(['.'] * (len(lines[0])+2))
    for line in lines:
        initial_grid.append(['.'] + list(line) + ['.'])
    initial_grid.append(['.'] * (len(lines[0])+2))
    return initial_grid

def get_move_grid(initial_grid):
    next_move = {}
    next_move['|'] = ('north', 'south')
    next_move['-'] = ('east', 'west')
    next_move['L'] = ('north', 'east')
    next_move['J'] = ('north', 'west')
    next_move['7'] = ('south', 'west')
    next_move['F'] = ('south', 'east')
    next_move['.'] = ()
    next_move['S'] = ()
    move_grid = []
    for row in range(len(initial_grid)):
        new_row = []
        for col in range(len(initial_grid[0])):
            new_row.append(next_move[initial_grid[row][col]])
        move_grid.append(new_row)
    return move_grid

def initialize_value_grid(initial_grid):
    values_grid = []
    rows = len(initial_grid)
    cols = len(initial_grid[0])
    for i in range(rows):
        values_grid.append([inf] * cols)
    return values_grid

def get_s_location(initial_grid):
    rows, cols = len(initial_grid), len(initial_grid[0])
    for row in range(rows):
        for col in range(cols):
            if initial_grid[row][col] == 'S':
                return (row, col)
    return None

def get_initial_moves(s_location, move_grid):
    initial_moves = []
    row, col = s_location[0], s_location[1]
    if 'south' in move_grid[row-1][col]:
        initial_moves.append([row-1, col])
    if 'north' in move_grid[row+1][col]:
        initial_moves.append([row+1, col])
    if 'west' in move_grid[row][col+1]:
        initial_moves.append([row, col+1])
    if 'east' in move_grid[row][col-1]:
        initial_moves.append([row, col-1])
    return initial_moves

def get_adjacent_moves(location, move_grid):
    adjacent_moves = []
    row, col = location[0], location[1]
    moves = move_grid[row][col]
    for move in moves:
        if move == 'north':
            adjacent_moves.append([row-1, col])
        if move == 'south':
            adjacent_moves.append([row+1, col])
        if move == 'east':
            adjacent_moves.append([row, col+1])
        if move == 'west':
            adjacent_moves.append([row, col-1])
    return adjacent_moves

def compute_steps(initial_grid, move_grid, values_grid):
    s_location = get_s_location(initial_grid)
    values_grid[s_location[0]][s_location[1]] = 0
    initial_moves = get_initial_moves(s_location, move_grid)
    moves_list = []
    for move in initial_moves:
        moves_list.append((move, 1))
    while moves_list:
        current_move = moves_list.pop()
        current_location = current_move[0]
        current_value = current_move[1]
        if current_value < values_grid[current_location[0]][current_location[1]]:
            values_grid[current_location[0]][current_location[1]] = current_value
            adjacent_moves = get_adjacent_moves(current_location, move_grid)
            for move in adjacent_moves:
                moves_list.append((move, current_value+1))
    return None

def get_farthest_point(values_grid):
    values = []
    for i in range(1, len(values_grid)-1):              # cut off top and bottom border
        for j in range(1, len(values_grid[0])-1):        # cut off left and right border
            if values_grid[i][j] != inf:
                values.append(values_grid[i][j])
    return max(values)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: day10_part1.py input_filename')
        exit(1)
    lines = get_input(sys.argv[1])
    initial_grid = get_initial_grid(lines)
    move_grid = get_move_grid(initial_grid)
    values_grid = initialize_value_grid(initial_grid)
    compute_steps = compute_steps(initial_grid, move_grid, values_grid)
    print(get_farthest_point(values_grid))
