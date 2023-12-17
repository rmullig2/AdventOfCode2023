import unittest
from day16_part1 import *

contraption = get_input("input_test.txt")

class TestInput(unittest.TestCase):
    def test_input(self):
        self.assertEqual(len(contraption), 12)
        self.assertEqual(contraption[1][2], '|')

class TestInBounds(unittest.TestCase):
    def test_in_bounds(self):
        self.assertEqual(in_bounds((0,5), contraption), False)
        self.assertEqual(in_bounds((7,10), contraption), False)
        self.assertEqual(in_bounds((4,9), contraption), True)
        self.assertEqual(in_bounds((2,6), contraption), True)

class TestDirection(unittest.TestCase):
    def test_next_direction(self):
        self.assertEqual(get_next_direction((1,2), 'right'), ['up'])
        self.assertEqual(get_next_direction((3,3), 'up'), ['left', 'right'])
        self.assertEqual(get_next_direction((4,10), 'left'), ['up', 'down'])
        self.assertEqual(get_next_direction((5,5), 'down'), ['down'])
