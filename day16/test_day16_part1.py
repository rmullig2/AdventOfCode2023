import unittest
from day16_part1 import *

contraption = get_input("input_test.txt")

class TestInput(unittest.TestCase):
    def test_input(self):
        self.assertEqual(len(contraption), 12)
        self.assertEqual(contraption[1][2], '|')

class TestInBounds(unittest.TestCase):
    def test_in_bounds(self):
        print(f'rows: {len(contraption)}, cols: {len(contraption)}')
        self.assertEqual(in_bounds((0,5), contraption), False)
        self.assertEqual(in_bounds((7,11), contraption), False)
        self.assertEqual(in_bounds((4,9), contraption), True)
        self.assertEqual(in_bounds((2,6), contraption), True)

class TestDirection(unittest.TestCase):
    def test_next_direction(self):
        self.assertEqual(get_next_directions((1,2), 'right', contraption), ['up', 'down'])
        self.assertEqual(get_next_directions((2,3), 'up', contraption), ['left', 'right'])
        self.assertEqual(get_next_directions((4,9), 'left', contraption), ['up', 'down'])
        self.assertEqual(get_next_directions((5,5), 'down', contraption), ['down'])

class TestFollowBeam(unittest.TestCase):
    def test_follow_beam(self):
        self.assertEqual(follow_beam(contraption), 46)
