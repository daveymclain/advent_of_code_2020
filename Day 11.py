import copy
import DATA
import time

sample = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

seat_check_list = [[-1, -1], [-1, 0], [-1, 1]], \
                  [[0, -1], [0, 1]], \
                  [[1, -1], [1, 0], [1, 1]]

vectors = [1, 0], [- 1, 0], [0, 1], [0, -1], \
          [- 1, 1], [1, 1], [1, -1], [-1, -1]

dict_test = {}


def split(word):
    return [char for char in word]


def gen_coord(input_list):
    re_list = []
    for row in range(len(input_list)):
        for col in range(len(input_list[row])):
            re_list.append([row, col])
    return re_list


def gen_test_list(row_pos, col_pos, d):
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
            if d[r][c] in "#L":
                ret_list.append([r, c])
                break
    return ret_list


def gen_test_dict(d):
    global dict_test
    for row in range(len(d)):
        for col in range(len(d[row])):
            dict_test[row, col] = gen_test_list(row, col, d)


def data_to_list(raw_data):
    d = raw_data.splitlines()
    re_list = []
    for i in d:
        i = split(i)
        re_list.append(i)
    return re_list


def seat_sim(date_list):
    run_count = 0
    run = True
    while run:
        test_seats = copy.deepcopy(date_list)
        run = False
        for row, all_row in enumerate(test_seats):

            for col, seat in enumerate(test_seats[row]):
                # Check surrounding seats
                empty_adj = True
                occ_count = 0
                test_list = dict_test[row, col]
                for check in test_list:
                    if seat == "#":
                        if test_seats[check[0]][check[1]] == "#":
                            occ_count += 1
                    if seat == "L" and empty_adj:
                        if test_seats[check[0]][check[1]] in "L.":
                            empty_adj = True
                        else:
                            empty_adj = False
                if occ_count >= 5 and seat == "#":
                    date_list[row][col] = "L"
                    run_count += 1
                    run = True
                if empty_adj and seat == "L":
                    date_list[row][col] = "#"
                    run_count += 1
                    run = True
    part_1 = 0
    for i in date_list:
        part_1 += i.count("#")
    return part_1


if __name__ == '__main__':
    start = time.time()
    data = DATA.Day_11
    coord = gen_coord(data_to_list(data))
    gen_test_dict(data_to_list(data))
    part_one_ans = (seat_sim(data_to_list(data)))
    print("Part two answer = {}".format(part_one_ans))
    end = time.time()
    print("run time = {}".format(end - start))
