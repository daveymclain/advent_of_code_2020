import DATA
import time
import re
import math
from memoization import cached
from collections import deque

sample = """389125467"""
data = "215694783"



@cached
def wrap_around_select(pos, cups):
    if pos > cups - 1:
        return pos % cups
    return pos


def parse_data(raw_data):
    return deque([int(i) for i in raw_data])


def game(cups, amount):
    current_cup_pos = 0
    biggest_cup = len(cups)
    for game_round in range(1, amount + 1):
        start = time.time()
        current_cup = cups[current_cup_pos]
        pick_up_cups = []
        # removing pick up cups
        for i in range(1, 4):
            pick_up_cups.append(cups[wrap_around_select(current_cup_pos + i, biggest_cup)])
        offset = 0
        time_making_pickup_list = time.time()

        for cup in pick_up_cups:
            cups_length = len(cups)
            if current_cup_pos + 1 < cups_length:
                del cups[current_cup_pos + 1]
            else:
                del cups[wrap_around_select(current_cup_pos + 1 - offset, cups_length)]
                offset += 1
        time_removing_cups = time.time()

        destination_cup = current_cup - 1
        if destination_cup <= 0:
            destination_cup = biggest_cup
        while destination_cup in pick_up_cups:
            destination_cup -= 1
            if destination_cup <= 0:
                destination_cup = biggest_cup
        time_destinations = time.time()

        destination_cup_pos = cups.index(destination_cup)
        time_destinations_index = time.time()

        for cup in pick_up_cups[::-1]:
            cups.insert(destination_cup_pos + 1, cup)
        time_insert_cups = time.time()

        while current_cup != cups[current_cup_pos]:
            left_cup = cups.popleft()
            cups.append(left_cup)
        time_adjust = time.time()

        current_cup_pos = wrap_around_select(current_cup_pos + 1, biggest_cup)
        round_time = time.time() - start
        if round_time > .01:
            print(f"round {game_round}")
            print(f"total time {round_time}")
            pick_up = time_making_pickup_list - start
            print(f"making pick up list {pick_up}")
            removing_cups = time_removing_cups - time_making_pickup_list
            print(f"removing cups = {removing_cups}")
            workout_destination_cup = time_destinations - time_removing_cups
            print(f"time to work out destination {workout_destination_cup}")
            find_index = time_destinations_index - time_destinations
            print(f"time to find index {find_index}")
            insert_cups = time_insert_cups - time_destinations_index
            print(f"time to insert {insert_cups}")
            adjust = time_adjust - time_insert_cups
            print(f"time to adjust {adjust}")

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
    highest_cup = len(cups)
    for i in range(amount - highest_cup):
        highest_cup += 1
        cups.append(highest_cup)
    print("Length of cups {}".format(len(cups)))
    return cups


def part_2(cups):
    pos = cups.index(1)
    return cups[pos + 1] * cups[pos + 2]
start = time.time()
print(after_one(game(generate_cups(parse_data(data), 0), 100)))
end = time.time()
print(end - start)