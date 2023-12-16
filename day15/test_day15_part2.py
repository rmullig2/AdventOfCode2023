import unittest
from day15_part2 import *

string = get_input("input_test.txt")
steps = get_steps(string)

class TestPatterns(unittest.TestCase):
    def test_input_string(self):
        self.assertEqual(len(string), 51)
        self.assertEqual(string[6], 'm')
    def test_steps(self):
        self.assertEqual(len(steps), 11)

class TestHash(unittest.TestCase):
    def test_get_fields(self):
        self.assertEqual(get_fields(steps[0]), ('rn', '=', 1))
        self.assertEqual(get_fields(steps[1]), ('cm', '-', None))
        self.assertEqual(get_fields(steps[2]), ('qp', '=', 3))
        self.assertEqual(get_fields(steps[3]), ('cm', '=', 2))
        self.assertEqual(get_fields(steps[4]), ('qp', '-', None))
        self.assertEqual(get_fields(steps[5]), ('pc', '=', 4))
        self.assertEqual(get_fields(steps[6]), ('ot', '=', 9))
        self.assertEqual(get_fields(steps[7]), ('ab', '=', 5))
        self.assertEqual(get_fields(steps[8]), ('pc', '-', None))
        self.assertEqual(get_fields(steps[9]), ('pc', '=', 6))
        self.assertEqual(get_fields(steps[10]), ('ot', '=', 7))
    def test_hash_function(self):
        label, operation, focal_length = get_fields(steps[0])
        self.assertEqual(get_hash(label), 0)
        label, operation, focal_length = get_fields(steps[1])
        self.assertEqual(get_hash(label), 0)
        label, operation, focal_length = get_fields(steps[2])
        self.assertEqual(get_hash(label), 1)
        label, operation, focal_length = get_fields(steps[3])
        self.assertEqual(get_hash(label), 0)
        label, operation, focal_length = get_fields(steps[4])
        self.assertEqual(get_hash(label), 1)
        label, operation, focal_length = get_fields(steps[5])
        self.assertEqual(get_hash(label), 3)
        label, operation, focal_length = get_fields(steps[6])
        self.assertEqual(get_hash(label), 3)
        label, operation, focal_length = get_fields(steps[7])
        self.assertEqual(get_hash(label), 3)
        label, operation, focal_length = get_fields(steps[8])
        self.assertEqual(get_hash(label), 3)
        label, operation, focal_length = get_fields(steps[9])
        self.assertEqual(get_hash(label), 3)
        label, operation, focal_length = get_fields(steps[10])
        self.assertEqual(get_hash(label), 3)

class TestSteps(unittest.TestCase):
    def test_process_steps(self):
        box_list, box_dict = process_steps(steps)
        self.assertEqual(len(box_list[0]), 2)
        self.assertEqual(len(box_list[3]), 3)
    def test_compute_focus(self):
        box_list, box_dict = process_steps(steps)
        self.assertEqual(compute_focus(box_list, box_dict), 145)
