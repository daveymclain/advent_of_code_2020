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


def game(raw_data, amount):
    cups = [int(i) for i in raw_data]
    cups_len = len(cups)
    pick_up_cups = []
    print(cups)
    current_cup_pos = 0
    current_cup = 0

    for game_round in range(1, amount + 1):
        print(f"move -{game_round}-")
        temp_cups = cups.copy()
        replace_cup = temp_cups.pop(current_cup_pos)
        temp_cups.insert(current_cup_pos, "(" + str(replace_cup) + ")")
        print(f"cups: {temp_cups}")
        current_cup = cups[current_cup_pos]
        right = 0
        for i in range(3):
            temp_cups = cups.copy()
            pick_up_cups.append(temp_cups.pop(wrap_around_select(current_cup_pos + 1 + i, len(cups))))
        for cup in pick_up_cups:
            for pos, test_cup in enumerate(cups):
                if cup == test_cup:
                    cups.remove(cup)
                    if

        print(f"pick up cups {pick_up_cups}")
        destination_cup = current_cup - 1
        while destination_cup not in cups:
            destination_cup -= 1
            if destination_cup < 0:
                sorted_cups = cups.copy()
                sorted_cups.sort()
                destination_cup = sorted_cups[-1]
        print(f"destination = {destination_cup}")


        dif = cups_len - current_cup_pos - 1
        less_than = destination_cup < current_cup_pos

        for i in range(3):
            for pos, cup in enumerate(cups):
                if destination_cup == cup:
                    destination_cup_pos = pos
            cups.insert(wrap_around_select(destination_cup_pos + 1, cups_len), pick_up_cups.pop(-1))
            if less_than and dif > 0:
                cup_left = cups.pop(0)
                cups.append(cup_left)
                dif -= 1
        current_cup_pos = wrap_around_select(current_cup_pos + 1, cups_len)
    return cups


def after_one(cups):
    result = ""
    for pos, cup in enumerate(cups):
        if cup == 1:
            for i in range(len(cups) -1):
                pos += 1
                result += str(cups[wrap_around_select(pos, len(cups))])
    return result


print(after_one(game(sample, 10)))



