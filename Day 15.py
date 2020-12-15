import DATA
import time

sample = 0, 3, 6


def game(raw_data):
    input_data = raw_data
    turn = 0
    turn_results_dict = {}
    last_num = 0
    last_num_new = False
    for num in input_data:
        turn += 1
        if num not in turn_results_dict.keys():
            turn_results_dict[num] = [turn]  # list of all the turns the number was used.
            last_num_new = True
        last_num = num
    while turn != 2020:
        turn += 1
        if last_num_new:
            turn_results_dict[0].append(turn)
            last_num_new = False
            last_num = 0
        else:
            ans = turn_results_dict[last_num][-1] - turn_results_dict[last_num][-2]
            last_num = ans
            if ans not in turn_results_dict.keys():
                turn_results_dict[ans] = [turn]
                last_num_new = True
            else:
                last_num_new = False
                turn_results_dict[ans].append(turn)
    return last_num


print(game(DATA.Day_15))
