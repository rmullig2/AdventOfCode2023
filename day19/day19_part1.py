import sys
import re

def get_input(filename):
    workflows, ratings = [], []
    f = open(filename, 'r')
    string = f.readline().rstrip()
    while string:
        workflows.append(string)
        string = f.readline().rstrip()
    string = f.readline().rstrip()
    while string:
        ratings.append(string)
        string = f.readline().rstrip()
    f.close()
    return workflows, ratings

def create_workflows_dict(workflows):
    workflows_dict = {}
    for workflow in workflows:
        key, values = workflow.split('{')
        values = values[:-1]
        workflows_dict[key] = values
    return workflows_dict

def create_ratings_dict(rating):
    ratings_dict = {}
    rating = rating[1:-1]
    categories = rating.split(',')
    for category in categories:
        category_fields = category.split('=')
        key = category_fields[0]
        value = int(category_fields[1])
        ratings_dict[key] = value
    return ratings_dict

def workflows_result(workflows_dict, rating_dict, key):
    rules = workflows_dict[key].split(',')
    for rule in rules:
        if len(rule) <= 1 or rule[1] not in ['<', '>']:
            return rule
        else:
            condition, result = rule.split(':')
            if condition[1] == '<':
                if rating_dict[condition[0]] < int(condition[2:]):
                    return result
            elif condition[1] == '>':
                if rating_dict[condition[0]] > int(condition[2:]):
                    return result

def rating_accepted(workflows_dict, rating_dict):
    result = workflows_result(workflows_dict, rating_dict, 'in')
    while result not in ['A', 'R']:
        result = workflows_result(workflows_dict, rating_dict, result)
    if result == 'A':
        return True
    elif result == 'R':
        return False

def rating_sum(rating):
    return sum(int(x) for x in re.findall('[0-9]+', rating))

def sum_accepted_parts(workflows, ratings):
    accepted_parts = 0
    workflows_dict = create_workflows_dict(workflows)
    for rating in ratings:
        rating_dict = create_ratings_dict(rating)
        if rating_accepted(workflows_dict, rating_dict):
            accepted_parts += rating_sum(rating)
    return accepted_parts

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: day19_part1.py input_filename')
        exit(1)
    workflows, ratings = get_input(sys.argv[1])
    print(sum_accepted_parts(workflows, ratings))
