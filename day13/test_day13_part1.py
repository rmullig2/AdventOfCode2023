import unittest
from day13_part1 import *

lines = get_input("input_test.txt")
patterns = get_patterns(lines)

class TestPatterns(unittest.TestCase):
    def test_patterns(self):
        self.assertEqual(len(patterns), 2)

test_pattern0 = patterns[0]
test_pattern1 = patterns[1]

class TestHorizontal(unittest.TestCase):
    def test_get_horizontal(self):
        self.assertEqual(get_horizontal(test_pattern0), None)
        self.assertEqual(get_horizontal(test_pattern1), 4)

class TestVertical(unittest.TestCase):
    def test_get_vertical(self):
        self.assertEqual(get_vertical(test_pattern0), 5)
        self.assertEqual(get_vertical(test_pattern1), None)

