import DATA
import time
import re
import math
from memoization import cached

sample = """389125467"""


def wrap_around_select(pos, cups):
    if pos > len(cups) - 1:
        return 0 + (pos % (len(cups) ))
    return pos


def game(raw_data, amount):
    cups = [int(i) for i in raw_data]
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
        for i in range(3):
            pick_up_cups.append(cups.pop(wrap_around_select(current_cup_pos + 1, cups)))
        print(f"pick up cups {pick_up_cups}")
        destination_cup = current_cup - 1
        while destination_cup not in cups:
            destination_cup -= 1
            if destination_cup < 0:
                sorted_cups = cups.copy()
                sorted_cups.sort()
                destination_cup = sorted_cups[-1]
        print(f"destination = {destination_cup}")
        for pos, cup in enumerate(cups):
            if destination_cup == cup:
                destination_cup_pos = pos
        for i in range(3):
            cups.insert(wrap_around_select(destination_cup_pos + 1, cups), pick_up_cups.pop(-1))
        current_cup_pos = wrap_around_select(current_cup_pos + 1, cups)



game(sample, 10)

print(wrap_around_select(10, [int(i) for i in sample]))