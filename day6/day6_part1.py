import sys
def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def get_times_and_distances(input_list):
    times = list(map(int, input_list[0].split(":")[1].split()))
    distances = list(map(int, input_list[1].split(":")[1].split()))
    return times, distances

def get_number_of_winners(total_time, distance):
    winners = 0
    for charge_time in range(total_time):
        race_time = total_time - charge_time
        race_distance = charge_time * race_time
        if race_distance > distance:
            winners += 1
    return winners

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: day6_part1.py input_filename")
        exit(1)
    input_list = get_input(sys.argv[1])
    times, distances = get_times_and_distances(input_list)
    winners = 1
    for i in range(len(times)):
        winners *= get_number_of_winners(times[i], distances[i])
    print(winners)
