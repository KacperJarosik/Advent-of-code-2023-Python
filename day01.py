def part1():
    last_digit = 0
    result = 0
    file = open("input.txt", "r")
    for line in file:
        result += last_digit
        first_digit_detected = 0
        for character in line:
            if '0' <= character <= '9':
                if first_digit_detected == 0:
                    result += int(character) * 10
                    first_digit_detected = 1
                    last_digit = int(character)
                else:
                    last_digit = int(character)
    result += last_digit
    file.close()
    return result


def part2():
    last_digit = 0
    result = 0
    file = open("input.txt", "r")
    for line in file:
        result += find_first_digit(line) * 10
        result += find_last_digit(line)
    result += last_digit
    file.close()
    return result


def find_first_digit(line):
    first_digits_index = [999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999]  # 1 2 3 4 5 6 7 8 9

    memory_index = line.find("1")
    if memory_index < first_digits_index[0] and memory_index != -1:
        first_digits_index[0] = memory_index
    memory_index = line.find("one")
    if memory_index < first_digits_index[0] and memory_index != -1:
        first_digits_index[0] = memory_index

    memory_index = line.find("2")
    if memory_index < first_digits_index[1] and memory_index != -1:
        first_digits_index[1] = memory_index
    memory_index = line.find("two")
    if memory_index < first_digits_index[1] and memory_index != -1:
        first_digits_index[1] = memory_index

    memory_index = line.find("3")
    if memory_index < first_digits_index[2] and memory_index != -1:
        first_digits_index[2] = memory_index
    memory_index = line.find("three")
    if memory_index < first_digits_index[2] and memory_index != -1:
        first_digits_index[2] = memory_index

    memory_index = line.find("4")
    if memory_index < first_digits_index[3] and memory_index != -1:
        first_digits_index[3] = memory_index
    memory_index = line.find("four")
    if memory_index < first_digits_index[3] and memory_index != -1:
        first_digits_index[3] = memory_index

    memory_index = line.find("5")
    if memory_index < first_digits_index[4] and memory_index != -1:
        first_digits_index[4] = memory_index
    memory_index = line.find("five")
    if memory_index < first_digits_index[4] and memory_index != -1:
        first_digits_index[4] = memory_index

    memory_index = line.find("6")
    if memory_index < first_digits_index[5] and memory_index != -1:
        first_digits_index[5] = memory_index
    memory_index = line.find("six")
    if memory_index < first_digits_index[5] and memory_index != -1:
        first_digits_index[5] = memory_index

    memory_index = line.find("7")
    if memory_index < first_digits_index[6] and memory_index != -1:
        first_digits_index[6] = memory_index
    memory_index = line.find("seven")
    if memory_index < first_digits_index[6] and memory_index != -1:
        first_digits_index[6] = memory_index

    memory_index = line.find("8")
    if memory_index < first_digits_index[7] and memory_index != -1:
        first_digits_index[7] = memory_index
    memory_index = line.find("eight")
    if memory_index < first_digits_index[7] and memory_index != -1:
        first_digits_index[7] = memory_index

    memory_index = line.find("9")
    if memory_index < first_digits_index[8] and memory_index != -1:
        first_digits_index[8] = memory_index

    memory_index = line.find("nine")
    if memory_index < first_digits_index[8] and memory_index != -1:
        first_digits_index[8] = memory_index

    min_index_value = min(first_digits_index)
    digit = first_digits_index.index(min_index_value) + 1
    return digit


def find_last_digit(line):
    last_digits_index = [-1, -1, -1, -1, -1, -1, -1, -1, -1]  # 1 2 3 4 5 6 7 8 9

    last_digits_index[0] = line.rfind("1")
    memory_index = line.rfind("one")
    if memory_index > last_digits_index[0]:
        last_digits_index[0] = memory_index

    last_digits_index[1] = line.rfind("2")
    memory_index = line.rfind("two")
    if memory_index > last_digits_index[1]:
        last_digits_index[1] = memory_index

    last_digits_index[2] = line.rfind("3")
    memory_index = line.rfind("three")
    if memory_index > last_digits_index[2]:
        last_digits_index[2] = memory_index

    last_digits_index[3] = line.rfind("4")
    memory_index = line.rfind("four")
    if memory_index > last_digits_index[3]:
        last_digits_index[3] = memory_index

    last_digits_index[4] = line.rfind("5")
    memory_index = line.rfind("five")
    if memory_index > last_digits_index[4]:
        last_digits_index[4] = memory_index

    last_digits_index[5] = line.rfind("6")
    memory_index = line.rfind("six")
    if memory_index > last_digits_index[5]:
        last_digits_index[5] = memory_index

    last_digits_index[6] = line.rfind("7")
    memory_index = line.rfind("seven")
    if memory_index > last_digits_index[6]:
        last_digits_index[6] = memory_index

    last_digits_index[7] = line.rfind("8")
    memory_index = line.rfind("eight")
    if memory_index > last_digits_index[7]:
        last_digits_index[7] = memory_index

    last_digits_index[8] = line.rfind("9")
    memory_index = line.rfind("nine")
    if memory_index > last_digits_index[8]:
        last_digits_index[8] = memory_index

    max_index_value = max(last_digits_index)
    digit = last_digits_index.index(max_index_value) + 1
    return digit


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
