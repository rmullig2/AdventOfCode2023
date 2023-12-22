import sys
import re

def get_input(filename):
    workflows = []
    f = open(filename, 'r')
    string = f.readline().rstrip()
    while string:
        workflows.append(string)
        string = f.readline().rstrip()
    string = f.readline().rstrip()
    f.close()
    return workflows

def create_workflows_dict(workflows):
    workflows_dict = {}
    for workflow in workflows:
        key, values = workflow.split('{')
        values = values[:-1]
        workflows_dict[key] = values
    return workflows_dict

def change_ratings(current_step, next_step, categories):
    available_steps = current_step.split(',')
    for step in available_steps:
        if bool(re.search(':', step)):
            condition, result = step.split(':')
            if result == next_step:
                category, comparison, value = condition[0], condition[1], int(condition[2:])
                if comparison == '<':
                    if value <= categories[category][1]:
                        categories[category][1] = value - 1
                elif comparison == '>':
                    if value >= categories[category][0]:
                        categories[category][0] = value + 1
    return

def get_path_result(accepted_path, workflows_dict):
    categories = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    steps = accepted_path.split('->')
    for i in range(len(steps)-1):
        change_ratings(workflows_dict[steps[i]], steps[i+1], categories)
    results = []
    results.append(categories['x'])
    results.append(categories['m'])
    results.append(categories['a'])
    results.append(categories['s'])
    return results

def get_accepted_paths(workflows_dict, current_path, accepted_paths):
    path_string = workflows_dict[current_path.split('->')[-1]]
    for path in path_string.split(','):
        if bool(re.search(':', path)):
            result = path.split(':')[1]
        else:
            result = path
        new_path = current_path + '->' + result
        if result == 'A':
            accepted_paths.append(new_path)
        elif result == 'R':
            pass
        else:
            get_accepted_paths(workflows_dict, new_path, accepted_paths)
    return

def get_path_combinations(path):
    x = path[0][1] - path[0][0] + 1
    m = path[1][1] - path[1][0] + 1
    a = path[2][1] - path[2][0] + 1
    s = path[3][1] - path[3][0] + 1
    #print(f'x: {x}, x: {m}, a: {a}, s: {s}')
    return x * m * a * s

def compute_collisions(path1, path2):
    collisions = 1
    for i in range(len(path1)):
        collisions *= len(range(max(path1[i][0], path2[i][0]), min(path1[i][1], path2[i][1])+1))
    return collisions

def sum_combinations(workflows):
    accepted_paths = []
    workflows_dict = create_workflows_dict(workflows)
    get_accepted_paths(workflows_dict, 'in', accepted_paths)
    path_results = []
    for accepted_path in accepted_paths:
        path_results.append(get_path_result(accepted_path, workflows_dict))
    combinations = 0
    for path_result in path_results:
        combinations += get_path_combinations(path_result)
    collisions = 0
    for i in range(len(path_results)-1):
        for j in range(i+1, len(path_results)):
            collisions += compute_collisions(path_results[i], path_results[j])
    print(f'number of combinations: {combinations}, number of collisions: {collisions}')
    return combinations - collisions

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: day19_part2.py input_filename')
        exit(1)
    workflows = get_input(sys.argv[1])
    print(sum_accepted_parts(workflows, ratings))
