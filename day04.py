# PART 1
def part1():
    with open("input.txt", "r") as file:
        text = file.readlines()
        result = 0
    for line in text:
        line = line.replace("  ", " ")
        line = line.split(":")
        line = line[1]
        line = line.split("|")
        wining_numbers = line[0][1:-1].split(" ")
        your_numbers = line[1][1:-1].split(" ")
        same_numbers = 0
        for number in wining_numbers:
            if number in your_numbers:
                same_numbers += 1
        if same_numbers:
            result += 2 ** (same_numbers - 1)
    return result


# PART 2
def part2():
    with open("input.txt", "r") as file:
        text = file.readlines()
        scratchcards = []
        for i in range(len(text)):
            scratchcards.append(1)
        result = 0
        game_number = 1
    for line in text:
        line = line.replace("  ", " ")
        line = line.split(":")
        line = line[1]
        line = line.split("|")
        wining_numbers = line[0][1:-1].split(" ")
        your_numbers = line[1][1:-1].split(" ")
        same_numbers = 0
        for number in wining_numbers:
            if number in your_numbers:
                same_numbers += 1
        for i in range(1, same_numbers + 1):
            scratchcards[game_number + i - 1] += 1 * scratchcards[game_number - 1]
        game_number += 1
    for scratchcard in scratchcards:
        result += scratchcard
    return result


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
