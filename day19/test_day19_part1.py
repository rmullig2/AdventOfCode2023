import unittest
from day19_part1 import *

workflows, ratings = get_input("input_test.txt")

class TestInput(unittest.TestCase):
    def test_workflows(self):
        self.assertEqual(workflows[2], 'lnx{m>1548:A,A}')
        self.assertEqual(len(workflows), 11)
    def test_ratings(self):
        self.assertEqual(ratings[1], '{x=1679,m=44,a=2067,s=496}')
        self.assertEqual(len(ratings), 5)

workflows_dict = create_workflows_dict(workflows)
test_rating = create_ratings_dict(ratings[1])
test_rating2 = create_ratings_dict(ratings[2])

class TestWorkflowsRatings(unittest.TestCase):
    def test_workflows_dict(self):
        self.assertEqual(workflows_dict['rfg'], 's<537:gd,x>2440:R,A')
        self.assertEqual(workflows_dict['crn'], 'x>2662:A,R')
    def test_ratings_dict(self):
        self.assertEqual(test_rating['x'], 1679)
        self.assertEqual(test_rating['m'], 44)
        self.assertEqual(test_rating['a'], 2067)
        self.assertEqual(test_rating['s'], 496)
    def test_rating_sum(self):
        self.assertEqual(rating_sum('{x=787,m=2655,a=1222,s=2876}'), 7540)
        self.assertEqual(rating_sum('{x=2036,m=264,a=79,s=2244}'), 4623)
        self.assertEqual(rating_sum('{x=2127,m=1623,a=2188,s=1013}'), 6951)

class TestResults(unittest.TestCase):
    def test_workflows_result(self):
        self.assertEqual(workflows_result(workflows_dict, test_rating, 'in'), 'px')
        self.assertEqual(workflows_result(workflows_dict, test_rating, 'px'), 'rfg')
        self.assertEqual(workflows_result(workflows_dict, test_rating, 'rfg'), 'gd')
        self.assertEqual(workflows_result(workflows_dict, test_rating, 'gd'), 'R')
    def test_rating_accepted(self):
        self.assertEqual(rating_accepted(workflows_dict, test_rating), False)
        self.assertEqual(rating_accepted(workflows_dict, test_rating2), True)
    def test_rating_sum(self):
        self.assertEqual(rating_sum(ratings[0]), 7540)
        self.assertEqual(rating_sum(ratings[2]), 4623)
        self.assertEqual(rating_sum(ratings[4]), 6951)
    def test_sum_accepted_parts(self):
        self.assertEqual(sum_accepted_parts(workflows, ratings), 19114)
