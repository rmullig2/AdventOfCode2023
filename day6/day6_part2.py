import sys
def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_time_and_distance(input_list):
    time = int(''.join(input_list[0].split(":")[1].split()))
    distance = int(''.join(input_list[1].split(":")[1].split()))
    return time, distance


def get_number_of_winners(total_time, distance):
    charge_time = total_time // 2
    race_time = total_time - charge_time
    winners = 0
    while True:
        if charge_time * race_time <= distance:
            break
        else:
            winners += 1
            charge_time -= 1
            race_time += 1
    charge_time = total_time // 2 + 1
    race_time = total_time - charge_time
    while True:
        if charge_time * race_time <= distance:
            break
        else:
            winners += 1
            charge_time += 1
            race_time -= 1
    return winners

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: day6_part1.py input_filename")
        exit(1)
    input_list = get_input(sys.argv[1])
    time, distance = get_time_and_distance(input_list)
    winners = get_number_of_winners(time, distance)
    print(winners)
