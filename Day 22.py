import DATA
import time
import re
import math
from memoization import cached

sample = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""


def parse_input(raw_data):
    data = raw_data.split("\n\n")
    players = {}
    for player_data in data:
        player = player_data.splitlines()
        player_name = player.pop(0)[:-1]
        players[player_name] = list(map(int, player))
    return players


def game_pt_1(raw_data):
    players = parse_input(raw_data)
    game_round = 0
    while len(players["Player 1"]) > 0 and len(players["Player 2"]) > 0:
        game_round += 1
        print(f"Round {game_round}")
        player_1_deck = players["Player 1"]
        print(f"Players 1's deck {player_1_deck}")
        player_2_deck = players["Player 2"]
        print(f"Players 1's deck {player_2_deck}")
        player_1_card = players["Player 1"].pop(0)
        print(f"Player 1 plays {player_1_card}")
        player_2_card = players["Player 2"].pop(0)
        print(f"Player 2 plays {player_2_card}")
        if player_1_card > player_2_card:
            print("player 1 wins")
            players["Player 1"].append(player_1_card)
            players["Player 1"].append(player_2_card)
        else:
            print("player 2 wins")
            players["Player 2"].append(player_2_card)
            players["Player 2"].append(player_1_card)
    if len(players["Player 1"]) > 1:
        return players["Player 1"]
    else:
        return players["Player 2"]


# @cached
def rec_game(players):
    game_round = 1
    player_1_deck_history = {tuple(players["Player 1"]): [game_round]}
    player_2_deck_history = {tuple(players["Player 2"]): [game_round]}
    while len(players["Player 1"]) > 0 and len(players["Player 2"]) > 0:
        player_1_card = players["Player 1"].pop(0)
        player_2_card = players["Player 2"].pop(0)
        if len(players["Player 1"]) >= player_1_card and len(players["Player 2"]) >= player_2_card\
                and len(players["Player 1"][:player_1_card]) > 0 and len(players["Player 2"][:player_2_card]) > 0:
            rec_game_decks = {"Player 1": players["Player 1"][:player_1_card].copy(),
                              "Player 2": players["Player 2"][:player_2_card].copy()}
            winner = rec_game(rec_game_decks)
            if len(winner["Player 1"]) > 0:
                players["Player 1"].append(player_1_card)
                players["Player 1"].append(player_2_card)
            else:
                players["Player 2"].append(player_2_card)
                players["Player 2"].append(player_1_card)
        else:
            if player_1_card > player_2_card:
                # print("player 1 wins")
                players["Player 1"].append(player_1_card)
                players["Player 1"].append(player_2_card)
            else:
                # print("player 2 wins")
                players["Player 2"].append(player_2_card)
                players["Player 2"].append(player_1_card)
     # test history
        if tuple(players["Player 1"]) in player_1_deck_history:
            if tuple(players["Player 2"]) in player_2_deck_history:
                if set(player_1_deck_history[tuple(players["Player 1"])]) & set(player_2_deck_history[tuple(players["Player 2"])]):
                    return {"Player 1": [1,1,1,1], "Player 2": []}
        if tuple(players["Player 1"]) in player_1_deck_history:
            player_1_deck_history[tuple(players["Player 1"])].append(game_round)
        else:
            player_1_deck_history[tuple(players["Player 1"])] = [game_round]
        if tuple(players["Player 2"]) in player_2_deck_history:
            player_2_deck_history[tuple(players["Player 2"])].append(game_round)
        else:
            player_2_deck_history[tuple(players["Player 2"])] = [game_round]
        game_round += 1
    return players


def part_1_score(winner):
    temp_score = []
    for mult, score in enumerate(winner[::-1], 1):
        temp_score.append(mult * score)
    ans = sum(temp_score)
    return ans

print("part one ans = {}".format(part_1_score(game_pt_1(DATA.Day_22))))

part_2_result = rec_game(parse_input(DATA.Day_22))
if len(part_2_result["Player 1"]) > 0:
    print("part two ans = {}".format(part_1_score(part_2_result["Player 1"])))
else:
    part_1_score(part_2_result["Player 2"])