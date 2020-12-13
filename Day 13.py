import operator
import time
import DATA

sample = """939
7,13,x,x,59,x,31,19"""
sample_2 = """202
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


def main(raw_data):
    start_wait, bus_id_list = raw_data_to_list(raw_data)
    result_dict = {}
    bus_id_offset = offset_calc(bus_id_list)
    print(bus_id_offset)
    for bus_id in bus_id_list:
        if bus_id == "x":
            continue
        result_dict[bus_id] = work_out_wait_time(start_wait, bus_id)
    bus_id_lowest_wait = min(result_dict.items(), key=operator.itemgetter(1))[0]
    lowest_wait = result_dict[bus_id_lowest_wait]
    run = True
    rev_list = bus_id_list[::-1]
    rev_list = [ x for x in rev_list if isinstance(x, int)]
    print(rev_list)
    time = 0
    time_increment = bus_id_list.pop(0)
    run_2 = True
    test = 0
    # while run:
        # while run_2:
        #     # test = time
        #     test += bus_id_list[-1]
        #     if (test - bus_id_offset[bus_id_list[-1]]) % time_increment  == 0:
        #         time = test - bus_id_offset[bus_id_list[-1]] - time_increment
        #         break
    while run_2:
        test += rev_list[0]
        for num, id in enumerate(rev_list):
            if num == len(rev_list) - 1:
                break
            dif = bus_id_offset[rev_list[0]] - bus_id_offset[rev_list[num + 1]]
            if (test - dif) % rev_list[num + 1] == 0:
                run_2 = False
            else:
                run_2 = True
                break

    test -= bus_id_offset[rev_list[0]]
        # while run_2:
        #     test += rev_list[0]
        #     for num, id in enumerate(rev_list):
        #         if num == len(rev_list) - 2:
        #             break
        #         if (test - (bus_id_offset[id] - bus_id_offset[rev_list[num + 1]])) % rev_list[num + 1]:
        #             time = test - bus_id_offset[id] - time_increment
        #             run_2 = False
        #         else:
        #             run_2 = True
        #             break
        # run = False
        # time += time_increment
        # # print(time)
        # for num, bus_ids in enumerate(bus_id_list):
        #     previous_bus_offset = 0
        #     if bus_ids == "x":
        #         continue
        #     time_dif = work_out_wait_time_offset(time + previous_bus_offset, bus_ids)
        #
        #     prev = bus_id_offset[bus_ids] - previous_bus_offset
        #     if time_dif == bus_id_offset[bus_ids] - previous_bus_offset:
        #         run = False
        #     else:
        #         run = True
        #         break
        #     previous_bus_offset = bus_id_offset[bus_ids]


    return [lowest_wait * bus_id_lowest_wait],[test]

def main_2(raw_data):
    start_wait, bus_id_list = raw_data_to_list(raw_data)
    result_dict = {}
    bus_id_offset = offset_calc(bus_id_list)
    print(bus_id_offset)
    for bus_id in bus_id_list:
        if bus_id == "x":
            continue
        result_dict[bus_id] = work_out_wait_time(start_wait, bus_id)
    bus_id_lowest_wait = min(result_dict.items(), key=operator.itemgetter(1))[0]
    lowest_wait = result_dict[bus_id_lowest_wait]
    run = True
    rev_list = bus_id_list[::-1]
    rev_list = [ x for x in rev_list if isinstance(x, int)]
    print(rev_list)
    time = 0
    time_increment = bus_id_list.pop(0)
    run_2 = True
    test = 0
    while run:
        # while run_2:
        #     # test = time
        #     test += bus_id_list[-1]
        #     if (test - bus_id_offset[bus_id_list[-1]]) % time_increment  == 0:
        #         time = test - bus_id_offset[bus_id_list[-1]] - time_increment
        #         break


        # while run_2:
        #     test += rev_list[0]
        #     for num, id in enumerate(rev_list):
        #         if num == len(rev_list) - 2:
        #             break
        #         if (test - (bus_id_offset[id] - bus_id_offset[rev_list[num + 1]])) % rev_list[num + 1]:
        #             time = test - bus_id_offset[id] - time_increment
        #             run_2 = False
        #         else:
        #             run_2 = True
        #             break

        time += time_increment
        # print(time)
        for num, bus_ids in enumerate(bus_id_list):
            previous_bus_offset = 0
            if bus_ids == "x":
                continue
            time_dif = work_out_wait_time_offset(time + previous_bus_offset, bus_ids)

            prev = bus_id_offset[bus_ids] - previous_bus_offset
            if time_dif == bus_id_offset[bus_ids] - previous_bus_offset:
                run = False
            else:
                run = True
                break
            previous_bus_offset = bus_id_offset[bus_ids]


    return [lowest_wait * bus_id_lowest_wait],[time]
start = time.time()
print(main(sample_2))
end = time.time()
print(end - start)
