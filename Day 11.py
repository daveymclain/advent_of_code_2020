import copy
import DATA
import time
# vectors around a seat that will need testing
vectors = [1, 0], [- 1, 0], [0, 1], [0, -1], \
          [- 1, 1], [1, 1], [1, -1], [-1, -1]


def split(string):
    """return a list of the individual characters in the string"""
    return [char for char in string]


def gen_test_list(row_pos, col_pos, d, part_1=False):
    """returns a list of other seats, around a seat, that need testing"""
    ret_list = []
    for angle in vectors:
        x, y = angle
        r = row_pos
        c = col_pos
        for width in range(len(d[0])):
            r += x
            c += y
            if r > len(d) - 1 or r < 0:
                break
            if c > len(d[0]) - 1 or c < 0:
                break
            if not part_1:
                if d[r][c] in "#L":
                    ret_list.append([r, c])
                    break
            else:
                ret_list.append([r, c])
                break
    return ret_list


def gen_test_dict(d, part_1=False):
    """returns a dictionary of seats and a corresponding list of seats around it that need testing"""
    dict_test = {}
    for row in range(len(d)):
        for col in range(len(d[row])):
            dict_test[row, col] = gen_test_list(row, col, d, part_1)
    return dict_test


def data_to_list(raw_data):
    """returns a list from the raw data string"""
    d = raw_data.splitlines()
    re_list = []
    for i in d:
        i = split(i)
        re_list.append(i)
    return re_list


def seat_sim(data_list, dict_test, seat_occ):
    """simulates people picking seats and returns the amount of seats taken when the simulation reaches equilibrium"""
    run = True
    while run:
        test_seats = copy.deepcopy(data_list)
        run = False
        for row, all_row in enumerate(test_seats):
            for col, seat in enumerate(test_seats[row]):
                # Check surrounding seats
                empty_adj = True
                occ_count = 0
                test_lists = dict_test[row, col]
                for check in test_lists:
                    if seat == "#":
                        if test_seats[check[0]][check[1]] == "#":
                            occ_count += 1
                    if seat == "L" and empty_adj:
                        if test_seats[check[0]][check[1]] in "L.":
                            empty_adj = True
                        else:
                            empty_adj = False
                if occ_count >= seat_occ and seat == "#":
                    data_list[row][col] = "L"
                    run = True
                if empty_adj and seat == "L":
                    data_list[row][col] = "#"
                    run = True
    seats = 0
    for i in data_list:
        seats += i.count("#")
    return seats


if __name__ == '__main__':
    start = time.time()
    data = data_to_list(DATA.Day_11)
    part_one_ans = (seat_sim(data, gen_test_dict(data, True), 4))
    print("Part one answer = {}".format(part_one_ans))
    data = data_to_list(DATA.Day_11)
    part_two_ans = (seat_sim(data, gen_test_dict(data), 5))
    print("Part two answer = {}".format(part_two_ans))
    end = time.time()
    print("run time = {}".format(end - start))
