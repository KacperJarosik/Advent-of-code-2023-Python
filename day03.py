# PART 1
def part1():
    with open("input.txt", "r") as file:
        text = file.readlines()
    result = 0
    lines_number = len(text)
    characters_number = len(text[-1])
    for index_line in range(lines_number):
        symbol_detected = False
        number = 0
        for index_character in range(characters_number):
            if '0' <= text[index_line][index_character] <= '9':
                number *= 10
                number += int(text[index_line][index_character])
                if not symbol_detected:
                    symbol_detected = find_symbol(index_character, index_line, lines_number, characters_number, text)
            if text[index_line][index_character] not in '0123456789' or index_character == characters_number - 1:
                if symbol_detected:
                    result += number
                number = 0
                symbol_detected = False
    return result


def find_symbol(x_position, y_position, x_limit, y_limit, text):
    for i in range(max(0, x_position - 1), min(x_limit, x_position + 2)):
        for j in range(max(0, y_position - 1), min(y_limit, y_position + 2)):
            if text[j][i] not in '0123456789.':
                return True
    return False


# PART 2
def part2():
    with open("input.txt", "r") as file:
        text = file.readlines()
    result = 0
    lines_number = len(text)
    characters_number = len(text[-1])
    for index_line in range(lines_number):
        for index_character in range(characters_number):
            if text[index_line][index_character] == '*':
                pair_multiplication = find_pair_numbers(index_character, index_line, lines_number, characters_number,
                                                        text)
                if pair_multiplication != -1:
                    result += pair_multiplication
    return result


def find_pair_numbers(x_position, y_position, x_limit, y_limit, text):
    digit_counter = 0
    result = 0

    for y in range(max(0, y_position - 1), min(y_limit, y_position + 2)):
        digit_in_line = 0
        for x in range(max(0, x_position - 1), min(x_limit, x_position + 2)):
            temp = text[y][int((max(0, x_position - 1) + min(y_limit, x_position + 2)) / 2)]
            if text[y][x] in '0123456789':
                if digit_in_line == 0:
                    if digit_counter == 0:
                        result += get_number(x, y, x_limit, text)
                    else:
                        result *= get_number(x, y, x_limit, text)
                    digit_counter += 1
                    digit_in_line += 1
                elif digit_in_line == 1 and temp not in '0123456789':
                    result *= get_number(x, y, x_limit, text)
                    digit_counter += 1
                    digit_in_line += 1

    if digit_counter == 2:
        return result
    return -1


def get_number(x_position, y_position, x_limit, text):
    while text[y_position][x_position - 1] in '0123456789' and x_position != 0:
        x_position -= 1
    number = 0
    while text[y_position][x_position] in '0123456789' and x_position != x_limit:
        number *= 10
        number += int(text[y_position][x_position])
        x_position += 1
    return number


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
