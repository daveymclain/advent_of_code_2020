import DATA
import time
import re
import math
from memoization import cached

sample = """389125467"""
data = "215694783"


@cached
def wrap_around_select(pos, cups):
    if pos > cups - 1:
        return pos % cups
    return pos


def parse_data(raw_data):
    return [int(i) for i in raw_data]


def game(cups, amount):
    current_cup_pos = 0
    biggest_cup = len(cups)
    for game_round in range(1, amount + 1):
        # print(f"round {game_round}")
        # start = time.time()
        current_cup = cups[current_cup_pos]
        pick_up_cups = []
        for i in range(1, 4):
            pick_up_cups.append(cups[wrap_around_select(current_cup_pos + i, len(cups))])
        if current_cup_pos < len(cups) - 3:
            for i in range(3):
                cups.pop(current_cup_pos + 1)
        else:
            for cup in pick_up_cups:
                cups.remove(cup)
        destination_cup = current_cup - 1
        if destination_cup <= 0:

            destination_cup = biggest_cup
        while destination_cup in pick_up_cups:
            destination_cup -= 1
            if destination_cup <= 0:
                destination_cup = biggest_cup
        destination_cup_pos = cups.index(destination_cup)
        for cup in pick_up_cups[::-1]:
            cups.move(destination_cup_pos + 1, cup)
        while current_cup != cups[current_cup_pos]:
            left_cup = cups.pop(0)
            cups.append(left_cup)
        current_cup_pos = wrap_around_select(current_cup_pos + 1, len(cups))
        # print(time.time() - start)
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
print(part_2(game(generate_cups(parse_data(sample), 1000000), 1000)))
end = time.time()
print(end - start)
