import unittest
from day8_part1 import *

input_list_1 = get_input("input_test_1.txt")
input_list_2 = get_input("input_test_2.txt")
instructions_1 = get_instructions(input_list_1)
instructions_2 = get_instructions(input_list_2)
nodes_1 = get_nodes(input_list_1)
nodes_2 = get_nodes(input_list_2)

class ProcessInput(unittest.TestCase):
    def test_input(self):
        self.assertEqual(type(input_list_1), list)
        self.assertEqual(type(input_list_2), list)
    def test_get_instructions(self):
        self.assertEqual(instructions_1, 'RL')
        self.assertEqual(instructions_2, 'LLR')
    def test_get_nodes(self):
        self.assertEqual(nodes_1['DDD'], ('DDD', 'DDD'))
        self.assertEqual(nodes_2['BBB'], ('AAA', 'ZZZ'))

steps_1 = get_steps(instructions_1, nodes_1)
steps_2 = get_steps(instructions_2, nodes_2)

class ComputeSteps(unittest.TestCase):
    def test_get_steps(self):
        self.assertEqual(steps_1, 2)
        self.assertEqual(steps_2, 6)
