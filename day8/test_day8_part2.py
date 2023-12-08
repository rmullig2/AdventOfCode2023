import unittest
from day8_part2 import *

input_list = get_input("input_test_part2.txt")
instructions = get_instructions(input_list)
nodes = get_nodes(input_list)

start_nodes = get_start_nodes(list(nodes.keys()))
finished_1 = check_finish(['GGZ', 'HHW'])
finished_2 = check_finish(['GGZ', 'HHZ'])
steps = get_steps(instructions, nodes)

class FindStartAndEndNodes(unittest.TestCase):
    def test_start_nodes(self):
        self.assertEqual(start_nodes, ['GGA', 'HHA'])
    def test_finish(self):
        self.assertEqual(finished_1, False)
        self.assertEqual(finished_2, True)

class ComputeSteps(unittest.TestCase):
    def test_get_steps(self):
        self.assertEqual(steps, 6)
