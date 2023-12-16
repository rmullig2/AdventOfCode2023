import sys

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

d = {}
for i in range(32, 127):
     d[chr(i)] = i

def get_total(lines):
    values = []
    for line in lines:
        steps = line.split(',')
        for step in steps:
            current_value = 0
            for ch in step:
                current_value += d[ch]
                current_value *= 17
                current_value %= 256
            values.append(current_value)
    return sum(values)

if __name__ == '__main__':
    if len(sys.argv)< 2:
        print("Usage day15_part1.py input_filename")
        exit(1)
    lines = get_input(sys.argv[1])
    print(get_total(lines))
