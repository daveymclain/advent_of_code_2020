import DATA
import time

sample = 0, 3, 6
sample_1 = 1, 3, 2


def game(raw_data, finish_number):
    input_data = raw_data
    turn = 0
    turn_results_dict = {}
    last_num = 0
    for num in input_data:
        turn += 1
        if num not in turn_results_dict.keys():
            turn_results_dict[num] = turn
        last_num = num
    while turn != finish_number:
        turn += 1
        if last_num not in turn_results_dict.keys():
            turn_results_dict[last_num] = turn - 1
            ans = 0
        else:
            ans = (turn - 1) - turn_results_dict[last_num]
            turn_results_dict[last_num] = turn - 1
        last_num = ans

    return last_num


start = time.time()
print("part one ans = {}".format(game(DATA.Day_15, 2020)))
print("part two ans = {}".format(game(DATA.Day_15, 30000000)))
end = time.time()
print("Time taken = {}".format(end - start))
