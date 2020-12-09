from DATA import Day_5
import math

input_data = Day_5.splitlines()
total_row = 128


def find_split(number):
    sm = number[0]
    bg = number[1]
    dif = bg - sm
    if dif == 1:
        return sm, bg
    half = dif / 2 + sm
    lower = [sm, math.floor(half)]
    upper = [math.floor(half) + 1, bg]
    return lower, upper


def sort_input(input_data):
    raw_seat_list = []
    seat_final = []
    for seat in input_data:
        row_code = seat[:7]
        col_code = seat[-3:]
        raw_seat_list.append([row_code, col_code])

    for seat_raw in raw_seat_list:
        start_row = [0, 127]
        start_col = [0, 7]
        # print("new ticket {}".format(seat_raw))
        for row in seat_raw[0]:

            if row == "F":
                start_row = find_split(start_row)[0]
            else:
                start_row = find_split(start_row)[1]
            # print("row letter = {} row current range = {}".format(row, start_row))

        for col in seat_raw[1]:
            if col == "L":
                start_col = find_split(start_col)[0]
            else:
                start_col = find_split(start_col)[1]
            # print("col letter = {} col current range = {}".format(col, start_col))
        seat_final.append([start_row, start_col])
    return seat_final


seat_id = []
for i in sort_input(input_data):
    seat_id.append(i[0] * 8 + i[1])
seat_id_sorted = sorted(seat_id)

seat_check = 1
for i in range(max(seat_id)):
    if i == 0:
        continue
    if seat_id_sorted[i - 1] + 1 == seat_id_sorted[i] == seat_id_sorted[i + 1] - 1:
        pass

    else:
        print("missing")
        print(seat_id_sorted[i])

print(max(seat_id))
