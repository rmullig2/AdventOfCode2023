import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def string_to_list(string):
    string_list = list(string.split())
    return list(map(int, string_list))

def get_next_list(current_list):
    next_list = []
    for i in range(len(current_list)-1):
        next_list.append(current_list[i+1] - current_list[i])
    return next_list

def get_first_value(list_of_lists):
    list_of_lists[-1].insert(0, 0)
    current_list = list_of_lists.pop()
    previous_list = list_of_lists.pop()
    while True:
        previous_list.insert(0, previous_list[0] - current_list[0])
        current_list = previous_list
        if len(list_of_lists) == 0:
            return previous_list[0]
        else:
            previous_list = list_of_lists.pop()

def get_next_value(num_list):
    list_of_lists = [num_list]
    current_list = list_of_lists[-1]
    while not all([ value == 0 for value in current_list ]):
        list_of_lists.append(get_next_list(current_list))
        current_list = list_of_lists[-1]
    return get_first_value(list_of_lists)

def get_sum_of_lists(lines):
    total = 0
    for line in lines:
        num_list = string_to_list(line)
        total += get_next_value(num_list)
    return total

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: day9_part2.py input_filename")
        exit(1)
    lines = get_input(sys.argv[1])
    print(get_sum_of_lists(lines))
