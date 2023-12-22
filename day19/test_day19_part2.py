import unittest
from day19_part2 import *

workflows = get_input("input_test.txt")

class TestInput(unittest.TestCase):
    def test_workflows(self):
        self.assertEqual(workflows[2], 'lnx{m>1548:A,A}')
        self.assertEqual(len(workflows), 11)

workflows_dict = create_workflows_dict(workflows)
accepted_paths = []
get_accepted_paths(workflows_dict, 'in', accepted_paths)
#print(set(accepted_paths))
path0_result = get_path_result(accepted_paths[0], workflows_dict)
path1_result = get_path_result(accepted_paths[1], workflows_dict)

class TestWorkflowsRatings(unittest.TestCase):
    def test_workflows_dict(self):
        self.assertEqual(workflows_dict['rfg'], 's<537:gd,x>2440:R,A')
        self.assertEqual(workflows_dict['crn'], 'x>2662:A,R')
    def test_get_accepted_paths(self):
        self.assertEqual(len(set(accepted_paths)), 8)
    def test_change_ratings(self):
        categories_test1 = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
        change_ratings('s<1351:px,qqz', 'px', categories_test1)
        self.assertEqual(categories_test1, {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 1350]})
        categories_test2 = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
        change_ratings('s>2770:qs,m<1801:hdj,R', 'hdj', categories_test2)
        self.assertEqual(categories_test2, {'x': [1, 4000], 'm': [1, 1800], 'a': [1, 4000], 's': [1, 4000]})
        categories_test3 = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
        change_ratings('m>838:A,pv', 'pv', categories_test3)
        self.assertEqual(categories_test3, {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]})

class TestResults(unittest.TestCase):
    def test_get_path_result(self):
        self.assertEqual(path0_result[0], [1,1415])
        self.assertEqual(path0_result[1], [1,4000])
        self.assertEqual(path0_result[2], [1,2005])
        self.assertEqual(path0_result[3], [1,1350])
        self.assertEqual(path1_result[0], [2663,4000])
        self.assertEqual(path1_result[1], [1,4000])
        self.assertEqual(path1_result[2], [1,2005])
        self.assertEqual(path1_result[3], [1,1350])
    def test_get_path_combinations(self):
        self.assertEqual(get_path_combinations(path0_result), 15320205000000)
        self.assertEqual(get_path_combinations(path1_result), 14486526000000)
    def test_compute_collisions(self):
        path10 = [[1, 4000], [1, 4000], [1, 4000], [1, 2000]]
        path11 = [[1, 4000], [1, 4000], [1, 4000], [2000, 4000]]
        self.assertEqual(compute_collisions(path10, path11), 64000000000)
        path12 = [[1, 2000], [1, 4000], [1, 4000], [1, 2000]]
        path13 = [[2000, 4000], [1, 4000], [1, 4000], [2000, 4000]]
        self.assertEqual(compute_collisions(path12, path13), 16000000)
    def test_sum_combinations(self):
        self.assertEqual(sum_combinations(workflows), 16740907986800)
