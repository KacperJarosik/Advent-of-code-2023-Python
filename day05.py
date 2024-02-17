# PART 1
def part1():
    with open("input.txt", "r") as file:
        text = file.readlines()

        result = []
        converts = []
        convert = []
        change_num = -1

        seeds = text[0].split(":")
        seeds = seeds[1]
        seeds = seeds[1:-1].split(" ")
        temp = []
        for object_id in seeds:
            temp.append(int(object_id))
        seeds = temp

        for line in text[1:]:
            if "map" in line:
                if len(convert) != 0:
                    converts.append(convert)
                convert = []
                change_num += 1
            if not any(char.isdigit() for char in line):
                continue
            values = line.split(" ")
            start_input_value = int(values[1])
            end_input_value = start_input_value + int(values[2])
            addition = int(values[0]) - start_input_value
            convert.append([start_input_value, end_input_value, addition])
        if len(convert) != 0:
            converts.append(convert)

        for object_id in seeds:
            for conv in converts:
                for scope in conv:
                    if scope[0] <= object_id < scope[1]:
                        object_id += scope[2]
                        break
            result.append(object_id)
        result = min(result)
    return result


# PART 2
def part2():
    with open("input.txt", "r") as file:
        text = file.readlines()

        result = []
        converts = []
        convert = []

        seeds_line = text[0].split(":")[1].split()
        seeds = [(int(seeds_line[i]), int(seeds_line[i+1]) + int(seeds_line[i])) for i in range(0, len(seeds_line), 2)]

        for line in text[1:]:
            if "map" in line:
                if convert:
                    converts.append(convert)
                convert = []
            if any(char.isdigit() for char in line):
                values = list(map(int, line.split()))
                start_input_value, end_input_value, addition = values[1], values[1] + values[2], values[0] - values[1]
                convert.append([start_input_value, end_input_value, addition])

        if convert:
            converts.append(convert)

        print("Loading: ", end="")
        for seed_values in seeds:
            print("#", end="")
            for object_id in range(seed_values[0], seed_values[1]):
                for conv in converts:
                    for scope in conv:
                        if scope[0] <= object_id < scope[1]:
                            object_id += scope[2]
                            break
                result.append(object_id)
        print()
        return min(result)



if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
