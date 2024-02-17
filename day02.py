def part1():
    red_dice_number_max = 12
    green_dice_number_max = 13
    blue_dice_number_max = 14
    file = open("input.txt", "r")
    result = 0
    for line in file:
        game = line.split(":")
        game_info = game[0].split(" ")
        game_number = game_info[1]
        error_dices_number = False
        game = game[1]
        rounds = game.split(";")
        for round in rounds:
            red_dice_number = 0
            green_dice_number = 0
            blue_dice_number = 0
            dices = round.split(",")
            for dice in dices:
                dice = dice.split(" ")
                dice = dice[1:]
                if "red" in dice[1]:
                    red_dice_number += int(dice[0])
                if "blue" in dice[1]:
                    blue_dice_number += int(dice[0])
                if "green" in dice[1]:
                    green_dice_number += int(dice[0])
            if red_dice_number > red_dice_number_max or green_dice_number > green_dice_number_max or blue_dice_number > blue_dice_number_max:
                error_dices_number = True
        if not error_dices_number:
            result += int(game_number)
    file.close()
    return result


def part2():
    file = open("input.txt", "r")
    result = 0
    for line in file:
        red_dices_necessary_amount = 0
        green_dices_necessary_amount = 0
        blue_dices_necessary_amount = 0
        game = line.split(":")
        game = game[1]
        rounds = game.split(";")
        for round in rounds:
            red_dice_number = 0
            green_dice_number = 0
            blue_dice_number = 0
            dices = round.split(",")
            for dice in dices:
                dice = dice.split(" ")
                dice = dice[1:]
                if "red" in dice[1]:
                    red_dice_number += int(dice[0])
                if "blue" in dice[1]:
                    blue_dice_number += int(dice[0])
                if "green" in dice[1]:
                    green_dice_number += int(dice[0])
            if red_dice_number > red_dices_necessary_amount:
                red_dices_necessary_amount = red_dice_number
            if green_dice_number > green_dices_necessary_amount:
                green_dices_necessary_amount = green_dice_number
            if blue_dice_number > blue_dices_necessary_amount:
                blue_dices_necessary_amount = blue_dice_number
        result += red_dices_necessary_amount * green_dices_necessary_amount * blue_dices_necessary_amount
    file.close()
    return result


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
