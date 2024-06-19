import numpy as np
import re


# PART 1
def part1():
    with open("input.txt", "r") as file:
        temp_results = np.array([0, 0, 0, 0])
        text = file.readlines()
        times = re.sub(r'\s+', ' ', text[0])
        times = np.array(times.strip().split(' ')[1:])
        distances = re.sub(r'\s+', ' ', text[1])
        distances = np.array(distances.strip().split(' ')[1:])
        for race_number in range(len(times)):
            for i in range(int(times[race_number])):
                if (int(times[race_number]) - i) * i > int(distances[race_number]):
                    temp_results[race_number] += 1
        result = temp_results[0]
        for i in range(1, len(temp_results)):
            result *= temp_results[i]
    return result


# PART 2
def part2():
    with open("input.txt", "r") as file:
        text = file.readlines()
        times = re.sub(r'\s+', ' ', text[0])
        times = np.array(times.strip().split(' ')[1:])
        distances = re.sub(r'\s+', ' ', text[1])
        distances = np.array(distances.strip().split(' ')[1:])
        time = ''
        for num in times:
            time += num
        time = int(time)
        distance = ''
        for num in distances:
            distance += num
        distance = int(distance)
        result = 0
        for i in range(time):
            if (time - i) * i > distance:
                result += 1
    return result


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
