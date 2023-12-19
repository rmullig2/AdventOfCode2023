import unittest
from day16_part2 import *

contraption = get_input("input_test.txt")

class TestMax(unittest.TestCase):
    def test_max_energized(self):
        self.assertEqual(get_max_energized(contraption), 51)
