import DATA
import time

sample = """.#.
..#
###"""


def parse_input_dict(raw_input, dimensions):
    data = raw_input.splitlines()
    coordinate = list(eval(("0," * (dimensions - 1)) + "0"))
    ret_dict = {}
    data = data[::-1]
    for line in data:
        coordinate[0] = 0
        for cube in line:
            ret_dict[tuple(coordinate)] = cube == "#"
            coordinate[0] += 1
        coordinate[1] += 1
    return ret_dict


def find_neighbors(coord):
    neighbor_list = []
    coord = list(coord)
    for z in range(-1, 2):
        for x in range(-1,2):
            for y in range(-1, 2):
                neighbor_list.append([coord[0] + x, coord[1] + y, coord[2] + z])
    neighbor_list.remove(coord)
    return neighbor_list


def find_neighbors_4d(coord):
    neighbor_list = []
    coord = list(coord)
    for w in range(-1, 2):
        for z in range(-1, 2):
            for x in range(-1,2):
                for y in range(-1, 2):
                    neighbor_list.append([coord[0] + x, coord[1] + y, coord[2] + z, coord[3] + w])
    neighbor_list.remove(coord)
    return neighbor_list


def print_boxes(boxes):
    print("----------------------------------------------------")
    output = []
    for z in range(-4, 4):
        slice = """"""
        for y in range(-3,6):
            for x in range(-3, 6):
                # print(x,y,z)
                if (x,y,z) in boxes:
                    if boxes[(x,y,z)]:
                        slice += "#"
                    else:
                        slice += "."
                else:
                    slice += "."
            slice += """\n"""
        slice_list = slice.splitlines()
        slice = slice_list[::-1]
        output.append(slice)
    for s in output:
        for o in s:
            print(o)
        print()


def sim(raw_data):
    boxes = parse_input_dict(raw_data, 3)
    for i in range(6):
        temp_dict = {}
        for box_coord in boxes:
            if boxes[box_coord]:
                for neigh in find_neighbors(box_coord):
                    if tuple(neigh) in temp_dict:
                        temp_dict[tuple(neigh)] += 1
                    else:
                        temp_dict[tuple(neigh)] = 1
        for temp_coord in temp_dict:
            if temp_coord in boxes:
                if boxes[temp_coord]:
                    if temp_dict[temp_coord] in range(2, 4):
                        boxes[temp_coord] = True
                    else:
                        boxes[temp_coord] = False
                else:
                    if temp_dict[temp_coord] == 3:
                        boxes[temp_coord] = True
            elif temp_dict[temp_coord] == 3:
                boxes[temp_coord] = True
        for box_coord in boxes:
            if box_coord not in temp_dict:
                boxes[box_coord] = False
    count = 0
    for coord in boxes:
        if boxes[coord]:
            count += 1
    print(count)


def sim_4d(raw_data):
    boxes = parse_input_dict(raw_data, 4)
    for i in range(6):
        temp_dict = {}
        for box_coord in boxes:
            if boxes[box_coord]:
                for neigh in find_neighbors_4d(box_coord):
                    if tuple(neigh) in temp_dict:
                        temp_dict[tuple(neigh)] += 1
                    else:
                        temp_dict[tuple(neigh)] = 1
        for temp_coord in temp_dict:
            if temp_coord in boxes:
                if boxes[temp_coord]:
                    if temp_dict[temp_coord] in range(2, 4):
                        boxes[temp_coord] = True
                    else:
                        boxes[temp_coord] = False
                else:
                    if temp_dict[temp_coord] == 3:
                        boxes[temp_coord] = True
            elif temp_dict[temp_coord] == 3:
                boxes[temp_coord] = True
        for box_coord in boxes:
            if box_coord not in temp_dict:
                boxes[box_coord] = False
    count = 0
    for coord in boxes:
        if boxes[coord]:
            count += 1
    print(count)

start = time.time()
sim(DATA.Day_17)
sim_4d(DATA.Day_17)


