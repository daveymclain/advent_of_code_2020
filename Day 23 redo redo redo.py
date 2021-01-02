import DATA
import time
import re
import math
from memoization import cached
from collections import deque
import itertools

sample = """389125467"""
data = "215694783"


def wrap_around_select(pos, cups):
    if pos > cups - 1:
        return pos % cups
    return pos


def generate_cups(cups, amount):
    highest_cup = len(cups)
    for i in range(amount - highest_cup):
        highest_cup += 1
        cups.append(highest_cup)
    print("Length of cups {}".format(len(cups)))
    return cups


def convert_list_dict(input_list):
    ret_dict = {}
    for pos, cup in enumerate(input_list):
        if pos < len(input_list) - 1:
            ret_dict[cup] = input_list[pos + 1]
        else:
            ret_dict[cup] = input_list[0]
    return ret_dict


def game(raw_data, amount, list_length=0):
    cups_list = [int(a) for a in raw_data]
    generate_cups(cups_list, list_length)
    cups = convert_list_dict(cups_list)
    biggest_cup = len(cups_list)
    current_cup = cups_list[0]
    for game_round in range(1, amount + 1):
        cup_1 = cups[current_cup]
        cup_2 = cups[cup_1]
        cup_3 = cups[cup_2]
        next_current = cups[cup_3]
        pick_up_cups = [cup_1, cup_2, cup_3]
        destination_cup = current_cup - 1
        if destination_cup <= 0:
            destination_cup = biggest_cup
        while destination_cup in pick_up_cups:
            destination_cup -= 1
            if destination_cup <= 0:
                destination_cup = biggest_cup
        cups[cup_3] = cups[destination_cup]
        cups[destination_cup] = cup_1
        cups[current_cup] = next_current
        current_cup = next_current
    final_list = []
    for i in range(len(cups)):
        final_list.append(current_cup)
        current_cup = cups[current_cup]
    return final_list, cups


def part_1(cups):
    cup_1 = cups.index(1)
    result = "".join(str(x) for x in cups[cup_1 + 1:])
    result = result + "".join(str(x) for x in cups[:cup_1])
    return result


def part_2(cups):
    cup1 = cups[1]
    cup2 = cups[cup1]
    return cup1 * cup2


start = time.time()
print("part 1 {}".format(part_1(game(data, 100)[0])))
print("part 2 {}".format(part_2(game(data, 10000000, 1000000)[1])))
print("time = {}".format(time.time() - start))
