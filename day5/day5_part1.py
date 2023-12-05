import sys
import re

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
        length = int(coords[2])
        transform_ints.append([destination, start, length])
    for seed in seeds:
        transformed = False
        for transform in transform_ints:
            destination, start, length = transform[0], transform[1], transform[2]
            if seed >= start and seed < start+length:
                offset = seed - start
                new_locations.append(destination+offset)
                transformed = True
        if not transformed:
            new_locations.append(seed)
    return new_locations

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: day5_part1.py input_filename")
        exit(1)
    almanac = get_input(sys.argv[1])
    seeds_list, seed_to_soil_list, soil_to_fertilizer_list, fertilizer_to_water_list, \
    water_to_light_list, light_to_temperature_list, temperature_to_humidity_list, \
    humidity_to_location_list = get_lists(almanac)

    seed_to_soil = seeds_map(seeds_list, seed_to_soil_list)
    soil_to_fertilizer = seeds_map(seed_to_soil, soil_to_fertilizer_list)
    fertilizer_to_water = seeds_map(soil_to_fertilizer, fertilizer_to_water_list)
    water_to_light = seeds_map(fertilizer_to_water, water_to_light_list)
    light_to_temperature = seeds_map(water_to_light, light_to_temperature_list)
    temperature_to_humidity = seeds_map(light_to_temperature ,temperature_to_humidity_list)
    humidity_to_location = seeds_map(temperature_to_humidity, humidity_to_location_list)

    print(min(humidity_to_location))

