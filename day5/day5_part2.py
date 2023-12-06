import sys
import re
from math import inf

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_lists(input_list):
    seeds_list = []
    seed_to_soil_list = []
    soil_to_fertilizer_list = []
    fertilizer_to_water_list = []
    water_to_light_list = []
    light_to_temperature_list = []
    temperature_to_humidity_list = []
    humidity_to_location_list = []

    start_list = None

    for line in input_list:
        if re.findall(r'^seeds', line):
            temp_list = line.split(':')[1].split()
            seeds_list = list(map(int, temp_list))
        elif re.findall(r'^seed-to-soil', line):
            start_list = seed_to_soil_list
        elif re.findall(r'^soil-to-fertilizer', line):
            start_list = soil_to_fertilizer_list
        elif re.findall(r'^fertilizer-to-water', line):
            start_list = fertilizer_to_water_list
        elif re.findall(r'^water-to-light', line):
            start_list = water_to_light_list
        elif re.findall(r'^light-to-temperature', line):
            start_list = light_to_temperature_list
        elif re.findall(r'^temperature-to-humidity', line):
            start_list = temperature_to_humidity_list
        elif re.findall(r'^humidity-to-location', line):
            start_list = humidity_to_location_list
        elif re.findall(r'^[0-9]+', line):
            start_list.append(line)
        elif re.findall(r'^\s*$', line):
            start_list = None

    return seeds_list, seed_to_soil_list, soil_to_fertilizer_list, fertilizer_to_water_list, \
    water_to_light_list, light_to_temperature_list, temperature_to_humidity_list, humidity_to_location_list

def seeds_map(seeds, transform_list):
    new_locations = []
    transform_ints = []
    for entry in transform_list:
        coords = entry.split()
        destination = int(coords[0])
        start = int(coords[1])
        end = int(start + int(coords[2]))
        transform_ints.append([start, end, destination])
    for seed in seeds:
        for transform in transform_ints:
            seed_start, seed_end, transform_start, transform_end, destination = seed[0], seed[1], transform[0], transform[1], transform[2]
            # Seed range is completely outside of transform range
            if seed_end <= transform_start or seed_start >= transform_end:
                continue
            # Seed range is completely inside of transform range
            elif seed_start >= transform_start and seed_end <= transform_end:
                new_location = [seed_start-transform_start+destination, seed_end-transform_start+destination]
                new_locations.append(new_location)
                seed = [-inf, -inf]
            # Seed range begins before transform range but does not extend past the end of the transform range
            elif seed_start < transform_start and seed_end <= transform_end:
                # get length of first and second sets
                first = transform_start - seed_start
                second = seed_end - transform_start
                seed = [seed_start, seed_start+first-1]
                new_locations.append([destination, destination+second])
            # Seed range begins inside transform range and extends past the end of the transform range
            elif seed_start >= transform_start and seed_end > transform_end:
                # get length of first and second sets
                #print(f'transform_start: {transform_start}, transform_end: {transform_end}')
                #print(f'seed_tart: {seed_start}, seed_end: {seed_end}')
                first = seed_start - transform_start
                second = seed_end - transform_end
                #print(f'first: {first}, second: {second}')
                new_locations.append([destination+first, destination+(transform_end - transform_start - 1)])
                seed = [transform_end, transform_end+second]
        if seed != [-inf, -inf]:
            new_locations.append([seed[0], seed[1]])
    return new_locations

def transform_seeds(seeds_list):
    seeds_new = []
    seeds_copy = seeds_list.copy()
    while seeds_copy:
        start = seeds_copy.pop(0)
        length = seeds_copy.pop(0)
        seeds_new.append([start, start+length])
    return seeds_new

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: day5_part1.py input_filename")
        exit(1)
    almanac = get_input(sys.argv[1])
    seeds_list, seed_to_soil_list, soil_to_fertilizer_list, fertilizer_to_water_list, \
    water_to_light_list, light_to_temperature_list, temperature_to_humidity_list, \
    humidity_to_location_list = get_lists(almanac)

    seeds_list = transform_seeds(seeds_list)
    seed_to_soil = seeds_map(seeds_list, seed_to_soil_list)
    soil_to_fertilizer = seeds_map(seed_to_soil, soil_to_fertilizer_list)
    fertilizer_to_water = seeds_map(soil_to_fertilizer, fertilizer_to_water_list)
    water_to_light = seeds_map(fertilizer_to_water, water_to_light_list)
    light_to_temperature = seeds_map(water_to_light, light_to_temperature_list)
    temperature_to_humidity = seeds_map(light_to_temperature ,temperature_to_humidity_list)
    humidity_to_location = seeds_map(temperature_to_humidity, humidity_to_location_list)

    print(min(humidity_to_location)[0])

