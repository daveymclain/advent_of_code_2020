import DATA
import time
import re
import math
from memoization import cached
from collections import OrderedDict
import timeit

sample = """389125467"""
data = "215694783"


def wrap_around_select(pos, cups):
    if pos > cups - 1:
        return pos % cups
    return pos


class Labels:
    def __init__(self):
        self.label = {}
        self.position = OrderedDict()

    def add(self, label, position):
        self.label[label] = position
        self.position[position] = label

    def adjust(self, current_cup, current_cup_pos):
        while current_cup != self.position[current_cup_pos]:
            self.move(0, len(self.position) - 1)

    def move(self, pos_to_move, target):
        one_to_move = self.position[pos_to_move]
        # print(f"one to move {one_to_move}")
        if target < pos_to_move:
            # print(self.position.values())
            next_num = self.position[target + 1 + 1]
            for i in range(target + 1, pos_to_move + 1):
                last_num = self.position[i]
                self.position[i] = next_num
                self.label[next_num] = i
                next_num = last_num
            self.position[target+1] = one_to_move
            self.label[one_to_move] = target+1
        else:
            next_num = self.position[target]
            for i in range(pos_to_move, target + 1)[::-1]:
                last_num = self.position[i]
                self.position[i] = next_num
                self.label[next_num] = i
                next_num = last_num
            self.position[target] = one_to_move
            self.label[one_to_move] = target


def game(raw_input, amount, cups_total = 0):
    labels = Labels()
    pos = 0
    for label in raw_input:
        labels.add(int(label), pos)
        pos += 1

    current_cup_pos = 0
    biggest_cup = len(labels.label)

    for i in range(cups_total - biggest_cup):
        biggest_cup += 1
        labels.add(biggest_cup, pos)
        pos += 1
    print("Length of cups {}".format(len(labels.position)))


    for game_round in range(1, amount + 1):
        # print(f"Round {game_round}")
        cups = [a for a in labels.position.values()]
        # print(f"cups {cups}")
        # print(f"current pos {current_cup_pos}")
        pick_up_cups = []
        current_cup = labels.position[current_cup_pos]
        for i in range(1, 4):
            pick_up_cups.append(labels.position[wrap_around_select(current_cup_pos + i, biggest_cup)])
        destination_cup = current_cup - 1
        # print(f"pickup cups {pick_up_cups}")
        if destination_cup <= 0:
            destination_cup = biggest_cup
        while destination_cup in pick_up_cups:
            destination_cup -= 1
            if destination_cup <= 0:
                destination_cup = biggest_cup
        # print(f"destination cup {destination_cup}")

        for i in range(1, 4)[::-1]:
            move_target = wrap_around_select(labels.label[destination_cup], biggest_cup)
            labels.move(wrap_around_select(labels.label[current_cup] + i, biggest_cup),
                        move_target)
        labels.adjust(current_cup, current_cup_pos)
        current_cup_pos += 1

        if current_cup_pos > len(labels.label) - 1:
            current_cup_pos = 0

    return [a for a in labels.position.values()]


def after_one(cups):
    result = ""
    for pos, cup in enumerate(cups):
        if cup == 1:
            for i in range(len(cups) - 1):
                pos += 1
                result += str(cups[wrap_around_select(pos, len(cups))])
    return result

def part_2(cups):
    pos = cups.index(1)
    return cups[pos + 1] * cups[pos + 2]



start = time.time()
print(part_2(game(sample,100, 1000000)))
print(time.time() - start)
