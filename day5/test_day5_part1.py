import unittest
from day5_part1 import *

input_list = get_input("input_test.txt")
seeds_list, seed_to_soil_list, soil_to_fertilizer_list, fertilizer_to_water_list, water_to_light_list, \
light_to_temperature_list, temperature_to_humidity_list, humidity_to_location_list = get_lists(input_list)

class InputAndList(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_seeds(self):
        self.assertEqual(len(seeds_list), 4)
    def test_seed_to_soil(self):
        self.assertEqual(len(seed_to_soil_list), 2)
    def test_soil_to_fertilizer(self):
        self.assertEqual(len(soil_to_fertilizer_list), 3)
    def test_fertilizer_to_water(self):
        self.assertEqual(len(fertilizer_to_water_list), 4)
    def test_water_to_light(self):
        self.assertEqual(len(water_to_light_list), 2)
    def test_light_to_temperature(self):
        self.assertEqual(len(light_to_temperature_list), 3)
    def test_temperature_to_humidity(self):
        self.assertEqual(len(temperature_to_humidity_list), 2)
    def test_humidity_to_location(self):
        self.assertEqual(len(humidity_to_location_list), 2)

seed_to_soil = seeds_map(seeds_list, seed_to_soil_list)
soil_to_fertilizer = seeds_map(seed_to_soil, soil_to_fertilizer_list)
fertilizer_to_water = seeds_map(soil_to_fertilizer, fertilizer_to_water_list)
water_to_light = seeds_map(fertilizer_to_water, water_to_light_list)
light_to_temperature = seeds_map(water_to_light, light_to_temperature_list)
temperature_to_humidity = seeds_map(light_to_temperature ,temperature_to_humidity_list)
humidity_to_location = seeds_map(temperature_to_humidity, humidity_to_location_list)

class Transforms(unittest.TestCase):
    def test_seeds_transform(self):
        self.assertEqual(seed_to_soil, [81, 14, 57, 13])
    def test_soil_transform(self):
        self.assertEqual(soil_to_fertilizer, [81, 53, 57, 52])
    def test_fertilizer_transform(self):
        self.assertEqual(fertilizer_to_water, [81, 49, 53, 41])
    def test_water_transform(self):
        self.assertEqual(water_to_light, [74, 42, 46, 34])
    def test_light_transform(self):
        self.assertEqual(light_to_temperature, [78, 42, 82, 34])
    def test_temperature_transform(self):
        self.assertEqual(temperature_to_humidity, [78, 43, 82, 35])
    def test_humidity_transform(self):
        self.assertEqual(humidity_to_location, [82, 43, 86, 35])
