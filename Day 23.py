import DATA
import time
import re
import math
from memoization import cached

sample = """389125467"""
data = "215694783"


def wrap_around_select(pos, cups):
    if pos > cups - 1:
        return pos % (cups)
    return pos


def parse_data(raw_data):
    return [int(i) for i in raw_data]


def game(cups, amount):
    # print(cups)
    current_cup_pos = 0
    sorted_cups = cups.copy()
    sorted_cups.sort()
    biggest_cup = sorted_cups[-1]
    for game_round in range(1, amount + 1):
        # print(f"\tGame round {game_round}")
        current_cup = cups[current_cup_pos]
        pick_up_cups = []
        # temp_cups = cups.copy()
        # replace_cup = temp_cups.pop(current_cup_pos)
        # temp_cups.insert(current_cup_pos, "(" + str(replace_cup) + ")")
        # print(f"cups: {temp_cups}")
        # start = time.time()
        for i in range(1, 4):
            pick_up_cups.append(cups[wrap_around_select(current_cup_pos + i, len(cups))])
        # print("pick up cups time {}".format(time.time() - start))
        # print(f"pick up cups {pick_up_cups}")
        for cup in pick_up_cups:
            cups.remove(cup)
        # print(time.time() - start)
        destination_cup = current_cup - 1
        if destination_cup <= 0:
            sorted_cups = cups.copy()
            sorted_cups.sort()
            destination_cup = sorted_cups[-1]
        # start = time.time()
        while destination_cup in pick_up_cups:
            destination_cup -= 1
            if destination_cup <= 0:
                destination_cup = biggest_cup
        destination_cup_pos = cups.index(destination_cup)
        for cup in pick_up_cups[::-1]:
            cups.insert(destination_cup_pos + 1, cup)
        # print(time.time() - start)
        # test pos

        while current_cup != cups[current_cup_pos]:
            left_cup = cups.pop(0)
            cups.append(left_cup)
        current_cup_pos = wrap_around_select(current_cup_pos + 1, len(cups))
        # print(game_round)
        # print(part_2(cups))

    return cups


def after_one(cups):
    result = ""
    for pos, cup in enumerate(cups):
        if cup == 1:
            for i in range(len(cups) - 1):
                pos += 1
                result += str(cups[wrap_around_select(pos, len(cups))])
    return result


def generate_cups(cups, amount):
    cups_sorted = cups.copy()
    cups_sorted.sort()
    highest_cup = cups_sorted[-1]
    for i in range(amount - len(cups)):
        highest_cup += 1
        cups.append(highest_cup)
    print("Length of cups {}".format(len(cups)))
    return cups


def part_2(cups):
    pos = cups.index(1)
    return cups[pos + 1] * cups[pos + 2]


start = time.time()
print(part_2(game(generate_cups(parse_data(data), 1000000), 100000)))
end = time.time()
print(end - start)
