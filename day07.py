import numpy as np
from collections import Counter


# PART 1
def part1():
    cards = np.array([])
    bets = np.array([])
    priorities = {}
    rank_mapping = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A'}

    with open("input.txt", "r") as file:
        text = file.readlines()
        for line in text:
            line = line.split()
            card_hand = list(line[0])

            # Replace card ranks based on the mapping
            for i in range(len(card_hand)):
                if card_hand[i] in rank_mapping:
                    card_hand[i] = rank_mapping[card_hand[i]]

            # Append the updated card hand to the cards list
            cards = np.append(cards, ''.join(card_hand))

            # Assuming the rest of the line contains bet values
            bets = np.append(bets, line[1])

    # Convert lists to numpy arrays
    cards = np.array(cards)
    bets = np.array(bets, dtype=float)

    # Calculate priorities
    for card in cards:
        counter = Counter(card).values()
        if 5 in counter:
            priorities[card] = 7
        elif 4 in counter:
            priorities[card] = 6
        elif 3 in counter and 2 in counter:
            priorities[card] = 5
        elif 3 in counter:
            priorities[card] = 4
        elif 2 in counter:
            temp = sum(1 for i in counter if i == 2)
            if temp >= 2:
                priorities[card] = 3
            else:
                priorities[card] = 2
        else:
            priorities[card] = 1

    sorted_priorities = dict(sorted(priorities.items(), key=lambda item: (item[1], item[0])))
    result = 0
    for i, item in enumerate(sorted_priorities):
        result += bets[np.where(cards == item)[0][0]] * (i + 1)  # Fixed bet extraction and multiplication
    #print(sorted_priorities)
    return int(result)


# PART 2
def part2():

    return None


if __name__ == "__main__":
    print("Result Part 1: ", part1())
    print("Result Part 2: ", part2())
