import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    contraption = []
    contraption.append('*' * len(lines[0]))
    for line in lines:
        contraption.append('*' + line + '*')
    contraption.append('*' * len(lines[0]))
    return contraption

def in_bounds(tile, contraption):
    end_row = len(contraption)
    end_col = len(contraption[0])
    return tile[0] not in [0, end_row] and tile[1] not in [0, end_col]

def get_next_direction(tile, direction):
    if tile = '/':
        if direction == 'right':
            new_direction = ['up']:
        elif direction == 'left':
            new_direction = ['down']:
        elif direction == 'up':
            new_direction = ['right']:
        elif direction == 'down':
            new_direction = ['left']:
    elif tile = '\\':
        if direction == 'right':
            new_direction = ['down']:
        elif direction == 'left':
            new_direction = ['up']:
        elif direction == 'up':
            new_direction = ['left']:
        elif direction == 'down':
            new_direction = ['right']:
    elif tile = '|':
        if direction in ['up','down']:
            new_direction = [direction]
        elif direction in ['left', 'right']:
            new_direction = ['up', 'down']:
    elif tile = '-':
        if direction in ['up','down']:
            new_direction = ['left', 'right']:
        elif direction in ['left', 'right']:
            new_direction = [direction]
    else:
        direction = [direction]

    return direction
