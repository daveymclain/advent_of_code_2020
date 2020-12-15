import DATA
import time

sample = 0, 3, 6
sample_1 = 1, 3, 2


def game(raw_data, finish_number):
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
    while turn != finish_number:
        turn += 1
        if last_num_new:
            ans = 0
            last_num = ans
            if ans not in turn_results_dict.keys():
                turn_results_dict[ans] = [turn]
                last_num_new = True
            else:
                last_num_new = False
                turn_results_dict[ans].append(turn)
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


start = time.time()
print("part one ans = {}".format(game(DATA.Day_15, 2020)))
print("part two ans = {}".format(game(sample_1, 30000000)))
end = time.time()
print("Time taken = {}".format(end - start))
