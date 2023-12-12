import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_grid(lines):
    grid = []
    grid.append(['O'] * (len(lines[0])+2))
    for line in lines:
        grid.append(['O'] + list(line) + ['O'])
    grid.append(['O'] * (len(lines[0])+2))
    return grid

def get_move_grid(grid):
    next_move = {}
    next_move['|'] = ('north', 'south')
    next_move['-'] = ('east', 'west')
    next_move['L'] = ('north', 'east')
    next_move['J'] = ('north', 'west')
    next_move['7'] = ('south', 'west')
    next_move['F'] = ('south', 'east')
    next_move['.'] = ()
    next_move['S'] = ()
    next_move['O'] = ()
    move_grid = []
    for row in range(len(grid)):
        new_row = []
        for col in range(len(grid[0])):
            new_row.append(next_move[grid[row][col]])
        move_grid.append(new_row)
    return move_grid

def get_s_location(grid):
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'S':
                return [row, col]
    return None

def get_S_moves(s_location, move_grid):
    S_moves = []
    row, col = s_location[0], s_location[1]
    if 'south' in move_grid[row-1][col]:
        S_moves.append([row-1, col])
    if 'north' in move_grid[row+1][col]:
        S_moves.append([row+1, col])
    if 'west' in move_grid[row][col+1]:
        S_moves.append([row, col+1])
    if 'east' in move_grid[row][col-1]:
        S_moves.append([row, col-1])
    return S_moves

def get_next_moves(location, move_grid):
    next_moves = []
    row, col = location[0], location[1]
    moves = move_grid[row][col]
    for move in moves:
        if move == 'north':
            next_moves.append([row-1, col])
        if move == 'south':
            next_moves.append([row+1, col])
        if move == 'east':
            next_moves.append([row, col+1])
        if move == 'west':
            next_moves.append([row, col-1])
    return next_moves

def get_loop(grid, move_grid):
    loop = []
    s_location = get_s_location(grid)
    loop.append(s_location)
    next_location = get_S_moves(s_location, move_grid)[0]
    while True:
        new_location = False
        loop.append(next_location)
        next_moves = get_next_moves(next_location, move_grid)
        for move in next_moves:
            if move not in loop:
                next_location = move
                new_location = True
        if not new_location:
            return loop

def bottom_pipe(location, grid, loop):
    row, col = location[0], location[1]
    if location in loop and grid[row][col] in ['-', 'L', 'J']:
        return True
    return False

def top_pipe(location, grid, loop):
    row, col = location[0], location[1]
    if location in loop and grid[row][col] in ['-', '7', 'F']:
        return True
    return False

def left_pipe(location, grid, loop):
    row, col = location[0], location[1]
    if location in loop and grid[row][col] in ['|', '7', 'J']:
        return True
    return False

def right_pipe(location, grid, loop):
    row, col = location[0], location[1]
    if location in loop and grid[row][col] in ['|', 'L', 'F']:
        return True
    return False

def mark_pipe_nodes(grid, move_grid, loop):
    pipe_nodes = []
    rows, cols = len(grid), len(grid[0])
    for row in range(1, rows-1):
        col = 1
        pipe = False
        while grid[row][col] == 'O' and col < cols-1:
            col += 1
        while bottom_pipe([row,col], grid, loop) and top_pipe([row+1,col], grid, loop):
            pipe = True
            col += 1
        if pipe:
            pipe_nodes.append([row,col])
            pipe_nodes.append([row+1,col])
        col = cols-1
        pipe = False
        while grid[row][col] == 'O' and col > 1:
            col -= 1
        while bottom_pipe([row,col], grid, loop) and top_pipe([row+1,col], grid, loop):
            pipe = True
            col -= 1
        if pipe:
            pipe_nodes.append([row,col])
            pipe_nodes.append([row+1,col])
    for col in range(1, cols-1):
        row = 1
        pipe = False
        while grid[row][col] == 'O' and row < rows-1:
            row += 1
        while left_pipe([row,col], grid, loop) and right_pipe([row,col+1], grid, loop):
            pipe = True
            row += 1
        if pipe:
            pipe_nodes.append([row,col])
            pipe_nodes.append([row,col+1])
        row = rows-1
        pipe = False
        while grid[row][col] == 'O' and row > 1:
            row -= 1
        while left_pipe([row,col], grid, loop) and right_pipe([row,col+1], grid, loop):
            pipe = True
            row -= 1
        if pipe:
            pipe_nodes.append([row,col])
            pipe_nodes.append([row,col+1])
    for node in pipe_nodes:
        grid[node[0]][node[1]] = 'O'
    return None

def adjacent_outside(location, grid, loop):
    if location in loop:
        return False
    row, col = location[0], location[1]
    if grid[row-1][col] == 'O' or grid[row+1][col] == 'O' or grid[row][col-1] == 'O' or grid[row][col+1] == 'O':
        return True
    return False

def mark_outside_nodes(grid, loop):
    change = True
    rows, cols = len(grid), len(grid[0])
    while change:
        change = False
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if adjacent_outside([row,col], grid, loop) and grid[row][col] != 'O':
                    grid[row][col] = 'O'
                    change = True
    return None

def get_inside_nodes(grid, loop):
    inside_nodes = []
    rows, cols = len(grid), len(grid[0])
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if grid[row][col] != 'O' and [row,col] not in loop:
                print(f'inside node: {row}, {col}')
                inside_nodes.append([row,col])
    return inside_nodes

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: day10_part2.py input_filename')
        exit(1)
    lines = get_input(sys.argv[1])
    grid = get_grid(lines)
    move_grid = get_move_grid(grid)
    loop = get_loop(grid, move_grid)
    mark_pipe_nodes(grid, move_grid, loop)
    mark_outside_nodes(grid, loop)
    inside_nodes = get_inside_nodes(grid, loop)
    #print(grid)
    print(len(inside_nodes))
