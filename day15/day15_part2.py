import sys

def get_input(filename):
    with open(filename) as f:
        string = f.read().rstrip()
    return string

def get_steps(string):
    return string.split(',')

def get_hash(label):
    hash_value = 0
    for ch in label:
        hash_value += ord(ch)
        hash_value *= 17
        hash_value %= 256
    return hash_value

def get_fields(step):
    label = ""
    i = 0
    while step[i].isalpha():
        label += step[i]
        i += 1
    operation = step[i]
    if operation == '=':
        focal_length = int(step[i+1])
    else:
        focal_length = None
    return label, operation, focal_length

def process_steps(steps):
    box_list, box_dict = [], []
    for i in range(256):
        box_list.append([])
        box_dict.append({})
    for step in steps:
        label, operation, focal_length = get_fields(step)
        hash_value = get_hash(label)
        if operation == '=':
            if not box_dict[hash_value].get(label):
                box_list[hash_value].append(label)
            box_dict[hash_value][label] = focal_length
        elif operation == '-':
            if box_dict[hash_value].get(label):
                box_dict[hash_value].pop(label)
                box_list[hash_value].remove(label)
    return box_list, box_dict

def compute_focus(box_list, box_dict):
    focus_power = 0
    for i in range(len(box_list)):
        for j in range(len(box_list[i])):
            label = box_list[i][j]
            focus_power += (i+1) * (j+1) * (box_dict[i][label])
    return focus_power

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage day15_part2 filename")
        exit(1)
    string = get_input(sys.argv[1])
    steps = get_steps(string)
    box_list, box_dict = process_steps(steps)
    print(compute_focus(box_list, box_dict))
