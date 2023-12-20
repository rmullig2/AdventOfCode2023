import sys
from math import inf

def get_input(filename):
    with open(filename) as f:
        strings = f.read().splitlines()
    return strings

def build_city_map(strings):
    city_map = []
    for string in strings:
        row = []
        for ch in string:
            row.append(int(ch))
        city_map.append(row)
    return city_map

def next_city_block(current_block, direction):
    row, col = current_block[0], current_block[1]
    if direction == 'up':
        return [row-1, col]
    if direction == 'down':
        return [row+1, col]
    if direction == 'left':
        return [row, col-1]
    if direction == 'right':
        return [row, col+1]

def in_bounds(block, city_map):
    row, col = block[0], block[1]
    min_row, min_col = 0, 0
    max_row, max_col = len(city_map) - 1, len(city_map[0]) - 1
    if row < min_row or row > max_row or col < min_col or col > max_col:
        return False
    return True

def get_next_moves(city_block, visited, city_map):
    next_moves = []
    possible_moves = ['down', 'right', 'up', 'left']
    for move in possible_moves:
        next_block = next_city_block(city_block, move)
        if in_bounds(next_block, city_map) and next_block not in visited:
            next_moves.append(next_block)
    return next_moves

def stringify(city_block):
    return str(city_block[0]) + "-" + str(city_block[1])

def dfs(city_block, visited, city_map, min_loss_map):
    visited.append(city_block)
    city_block_string = stringify(city_block)
    if min_loss_map.get(city_block_string):
        return min_loss_map[city_block_string]
    heat_loss = city_map[city_block[0]][city_block[1]]
    #if city_block == [len(city_map)-1, len(city_map)-1]:
    #    return heat_loss
    loss_list = [inf]
    next_moves = get_possible_moves(city_block, visited, city_map)
    $if city_block == [10, 10]:
    $    print(f'city_block: {city_block}, direction: {direction}, next_moves: {next_moves}, visited: {visited}')
    for move in next_moves:
        loss_list.append(dfs(move, visited, city_map, min_loss_map))
    #print(f'city_block: {city_block}, loss_list: {loss_list}')
    min_loss_map[city_block_string] = min(loss_list) + heat_loss
    return min_loss_map[city_block_string]
