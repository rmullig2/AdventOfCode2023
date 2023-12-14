import sys
from itertools import combinations
import re

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_spring_rows_and_broken_number(lines):
    spring_rows, broken_number = [], []
    for line in lines:
        spring_row = line.split(' ')[0]
        broken = list(map(int, line.split(' ')[1].split(',')))
        spring_rows.append(spring_row)
        broken_number.append(broken)
    return spring_rows, broken_number

def get_areas(spring_row):
    return [area for area in spring_row.split('.') if area]

def get_arrangements(area, broken_number):
    known_broken = len(re.findall('#', area))
    p = len(area) - known_broken
    r = broken_number - known_broken
    return combinations(p, r)

def equal_areas_and_groups(spring_row, broken_number):
    arrangements = 0
    areas = get_areas(spring_row)
    arrangements = 1
    for i in range(len(areas)):
        arrangements *= get_arrangements(areas[i], broken_number[i])
    return arrangements
