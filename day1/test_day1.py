import unittest
from day1 import *

input_list = get_input("input_test.txt")

class DayOneTests(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list), list)
    def test_line_one(self):
        self.assertEqual(input_list[0], "1abc2")
