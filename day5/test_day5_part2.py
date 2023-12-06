import unittest
from day5_part2 import *

input_list = get_input("input_test.txt")
seeds_list, seed_to_soil_list, soil_to_fertilizer_list, fertilizer_to_water_list, water_to_light_list, \
light_to_temperature_list, temperature_to_humidity_list, humidity_to_location_list = get_lists(input_list)
new_seeds = transform_seeds(seeds_list)

class SeedsTransform(unittest.TestCase):
    def test_seeds_transform(self):
        self.assertEqual(new_seeds[0], [79, 93])
        self.assertEqual(new_seeds[1], [55, 68])
    def test_seeds_map(self):
        self.assertEqual(seeds_map(([52, 58], [90, 95]), (['10 50 10'])), ([[12, 18], [90, 95]]))
        self.assertEqual(seeds_map(([52, 58], [40, 45]), (['10 50 10'])), ([[12, 18], [40, 45]]))
        #self.assertEqual(seeds_map(([62, 68], [45, 55]), (['10 50 20'])), ([[22, 28], [45, 49], [10, 15]]))
