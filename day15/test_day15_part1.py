import unittest
from day15_part1 import *

lines = get_input("input_test.txt")

class TestInput(unittest.TestCase):
    def test_input(self):
        self.assertEqual(len(lines), 1)

class TestHash(unittest.TestCase):
    def test_hash(self):
        self.assertEqual(get_total(lines), 1320)
