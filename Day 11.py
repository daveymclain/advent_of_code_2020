import copy
import DATA

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


def gen_test_list(row_pos, col_pos, data):
    ret_list = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            row_dif = row - row_pos
            if col == col_pos + row_dif or col == col_pos + abs(row_dif):
                ret_list.append([row, col])
            if col == col_pos or row == row_pos:
                ret_list.append([row, col])
    return ret_list


def split(word):
    return [char for char in word]


def data_to_list(raw_data):
    data = raw_data.splitlines()
    list = []
    for i in data:
        i = split(i)
        list.append(i)

    return list


def seat_sim(data):
    run_count = 0

    run = True
    while run:
        test_seats = copy.deepcopy(data)
        run = False
        for row, all_row in enumerate(test_seats):
            top = bool(row == 0)
            bottom = bool(row == len(test_seats) - 1)
            for col, seat in enumerate(test_seats[row]):
                far_left = bool(col == 0)
                far_right = bool(col == len(test_seats[row]) - 1)

                # Check surrounding seats
                empty_adj = True
                occ_count = 0
                for r, all_r in enumerate(seat_check_list):
                    if top and r == 0:
                        continue
                    if bottom and r == len(seat_check_list) - 1:
                        continue
                    for c, check in enumerate(seat_check_list[r]):
                        if far_left and c == 0:
                            continue
                        if far_right and c == len(seat_check_list[r]) - 1:
                            continue
                        # Test if chair is empty
                        if seat == "L" and empty_adj:
                            if test_seats[row + check[0]][col + check[1]] in "L.":
                                empty_adj = True
                            else:
                                empty_adj = False
                        # test if chair is occupied
                        if seat == "#":
                            if test_seats[row + check[0]][col + check[1]] == "#":
                                occ_count += 1

                if occ_count >= 4 and seat == "#":
                    data[row][col] = "L"
                    run_count += 1
                    run = True
                if empty_adj and seat == "L":
                    data[row][col] = "#"
                    run_count += 1
                    run = True
    part_1 = 0
    for i in data:
        part_1 += i.count("#")
    return part_1


if __name__ == '__main__':
    part_one_ans = (seat_sim(data_to_list(sample)))
    print("Part one answer = {}".format(part_one_ans))
    print(gen_test_list(0,0, data_to_list(sample)))
