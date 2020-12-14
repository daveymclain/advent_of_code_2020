import operator
import time
import DATA

sample = """939
7,13,x,x,59,x,31,19"""
sample_1 = """202
1789,37,47,1889"""


def work_out_wait_time(start_wait, bus_id):
    wait_time = bus_id - (start_wait % bus_id)
    return wait_time

def work_out_wait_time_offset(start_wait, bus_id):
    left_over = abs((start_wait % bus_id) - bus_id)
    if left_over >= bus_id:
        left_over = left_over % bus_id

    return left_over


def raw_data_to_list(raw_data):
    return_list = []
    data = raw_data.splitlines()
    start_wait = int(data.pop(0))
    data = data[0].split(",")
    for bus_id in data:
        if bus_id == "x":
            return_list.append(bus_id)
        else:
            return_list.append(int(bus_id))
    return start_wait, return_list


def offset_calc(bus_id_list):
    dict_ret = {}
    offset = 0
    for bus_id in bus_id_list:
        if bus_id == "x":
            offset += 1
            continue
        else:
            dict_ret[bus_id] = offset
            offset += 1
    return dict_ret


def test_ans(rev_list, bus_id_offset, test):
    test += bus_id_offset[rev_list[0]]
    for num, id in enumerate(rev_list):
        if num == len(rev_list) - 1:
            break
        dif = bus_id_offset[rev_list[0]] - bus_id_offset[rev_list[num + 1]]
        if (test - dif) % rev_list[num + 1] == 0:
            run_2 = True
        else:
            run_2 = False
            break
    return run_2


def main(raw_data):
    start_wait, bus_id_list = raw_data_to_list(raw_data)
    result_dict = {}
    bus_id_offset = offset_calc(bus_id_list)
    for bus_id in bus_id_list:
        if bus_id == "x":
            continue
        result_dict[bus_id] = work_out_wait_time(start_wait, bus_id)
    bus_id_lowest_wait = min(result_dict.items(), key=operator.itemgetter(1))[0]
    lowest_wait = result_dict[bus_id_lowest_wait]
    rev_list = bus_id_list[::-1]
    rev_list = [ x for x in rev_list if isinstance(x, int)]

    print(bus_id_offset)
    run_2 = True
    test = 0
    number_increase = rev_list.pop(0)
    start_number = number_increase
    print(rev_list)
    while run_2:
        # print(test)
        test += number_increase

        for num, id in enumerate(rev_list):
            dif = bus_id_offset[start_number] - bus_id_offset[id]
            if num == len(rev_list) -1:
                if (test - dif) % id == 0:
                    print("number {} solved".format(id))
                    run_2 = False
                    break
                else:
                    run_2 = True
                    break
            if (test - dif) % rev_list[num] == 0:
                print(test)
                number_increase = number_increase * rev_list.pop(0)
                print("number increase = {}".format(number_increase))
                print("number {} solved".format(id))
                print("list {}. len {}".format(rev_list, len(rev_list)))
            else:
                break

    test -= bus_id_offset[start_number]
    return lowest_wait * bus_id_lowest_wait, test



if __name__ == '__main__':

    start = time.time()
    ans1, ans2 = main(DATA.Day_13)
    print(ans2)
    if ans2 == 1202161486:
        print("pass")
    else:
        print("fail")

    end = time.time()
    print(end - start)
