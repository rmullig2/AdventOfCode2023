import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    contraption = []
    contraption.append('*' + ('*' * len(lines[0])) + '*')
    for line in lines:
        contraption.append('*' + line + '*')
    contraption.append('*' * len(lines[0]))
    return contraption

def in_bounds(tile, contraption):
    end_row = len(contraption)-1
    end_col = len(contraption[0])-1
    return tile[0] not in [0, end_row] and tile[1] not in [0, end_col]

def get_next_directions(tile, current_direction, contraption):
    row, col = tile[0], tile[1]
    tile_direction = contraption[row][col]
    if tile_direction == '/':
        if current_direction == 'right':
            new_direction = ['up']
        elif current_direction == 'left':
            new_direction = ['down']
        elif current_direction == 'up':
            new_direction = ['right']
        elif current_direction == 'down':
            new_direction = ['left']
    elif tile_direction == '\\':
        if current_direction == 'right':
            new_direction = ['down']
        elif current_direction == 'left':
            new_direction = ['up']
        elif current_direction == 'up':
            new_direction = ['left']
        elif current_direction == 'down':
            new_direction = ['right']
    elif tile_direction == '|':
        if current_direction in ['up','down']:
            new_direction = [current_direction]
        elif current_direction in ['left', 'right']:
            new_direction = ['up', 'down']
    elif tile_direction == '-':
        if current_direction in ['up','down']:
            new_direction = ['left', 'right']
        elif current_direction in ['left', 'right']:
            new_direction = [current_direction]
    else:
        new_direction = [current_direction]
    return new_direction

def get_next_tile(tile, direction):
    row, col = tile[0], tile[1]
    if direction == 'up':
        return (row-1, col)
    elif direction == 'down':
        return (row+1, col)
    elif direction == 'right':
        return (row, col+1)
    elif direction == 'left':
        return (row, col-1)

def stringify(tile, direction):
    return str(tile[0]) + '-' + str(tile[1]) + '-' + direction

def count_energized(energized):
    final_count = set()
    for tile in energized:
        final_count.add("-".join(tile.split('-')[0:2]))
    return len(final_count)

def follow_beam(contraption, tile, direction):
    # energized will contain strings corresponding to the next tile and direction entering the tile
    energized = set()
    tile_queue = []
    start_tile = tile
    start_directions = [direction]
    for start_direction in start_directions:
        tile_queue.append((start_tile, start_direction))
        energized.add(stringify(tile, start_direction))
    while tile_queue:
        tile, direction = tile_queue.pop(0)
        new_tile = get_next_tile(tile, direction)
        if in_bounds(new_tile, contraption) and stringify(new_tile, direction) not in energized:
            new_tile_directions = get_next_directions(new_tile, direction, contraption)
            for tile_direction in new_tile_directions:
                tile_queue.append((new_tile, tile_direction))
                energized.add(stringify(new_tile, direction))
    total_energized = count_energized(energized)
    return total_energized

def get_max_energized(contraption):
    start_row = 1
    end_row = len(contraption) - 1
    start_col = 1
    end_col = len(contraption) - 1
    num_energized = []
    for col in range(start_col, end_col):
        num_energized.append(follow_beam(contraption, (start_row, col), 'down'))
    for col in range(start_col, end_col):
        num_energized.append(follow_beam(contraption, (end_row-1, col), 'up'))
    for row in range(start_row, end_row):
        num_energized.append(follow_beam(contraption, (row, start_col), 'right'))
    for row in range(start_row, end_row):
        num_energized.append(follow_beam(contraption, (row, end_col-1), 'left'))
    return max(num_energized)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage day16_part2.py input_filename')
        exit(1)
    contraption = get_input(sys.argv[1])
    print(get_max_energized(contraption))
