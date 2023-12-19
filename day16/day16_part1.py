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
    #print(f'tile: {tile}')
    end_row = len(contraption)-1
    end_col = len(contraption[0])-1
    return tile[0] not in [0, end_row] and tile[1] not in [0, end_col]

def get_next_directions(tile, current_direction, contraption):
    row, col = tile[0], tile[1]
    tile_direction = contraption[row][col]
    #print(f'tile: {tile}, direction: {tile_direction}, current_direction: {current_direction}')
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
    #print(final_count)
    return len(final_count)

def follow_beam(contraption):
    # energized will contain strings corresponding to the next tile and direction entering the tile
    energized = set()
    tile_queue = []
    start_tile = (1,1)
    start_directions = get_next_directions(start_tile, "right", contraption)
    for start_direction in start_directions:
        tile_queue.append((start_tile, start_direction))
        energized.add(stringify([1,1], start_direction))
    while tile_queue:
        tile, direction = tile_queue.pop(0)
        new_tile = get_next_tile(tile, direction)
        #print(f'new_tile is {tile} with direction {direction}')
        if in_bounds(new_tile, contraption) and stringify(new_tile, direction) not in energized:
            new_tile_directions = get_next_directions(new_tile, direction, contraption)
            for tile_direction in new_tile_directions:
                #print(f'new_tile is {new_tile} with direction {tile_direction}')
                tile_queue.append((new_tile, tile_direction))
                energized.add(stringify(new_tile, direction))
    total_energized = count_energized(energized)
    return total_energized

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage day16_part1.py input_filename')
        exit(1)
    contraption = get_input(sys.argv[1])
    print(follow_beam(contraption))
