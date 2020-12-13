import DATA
import math

sample = """F10
N3
F7
L90
F11"""


direction_list = ["N", [0, 1]], ["E", [1, 0]], ["S", [0, -1]], ["W", [-1, 0]]
direction_dict = {"N": [0, 1], "E": [1, 0], "S": [0, -1], "W": [-1, 0]}



def input_list(raw_data):
    ret_dict = []
    split = raw_data.splitlines()
    for line in split:
        ret_dict.append([line[0], int(line[1:])])
    return ret_dict


def turn(deg, current_dir):
    increment = deg / 90 + current_dir
    if increment < 0:
        mod = increment % 4
        times = abs((increment - mod) / 4)
        return int(4 * times + increment)
    mod = increment % 4
    times = (increment - mod) / 4
    return int(increment - 4 * times)


def rotate(origin, point, angle):
    angle = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return round(qx), round(qy)


def main(raw_data):
    current_dir = 1
    coord = [0, 0]
    list_input = input_list(raw_data)
    for instruction in list_input:
        if instruction[0] == "F":
            x = direction_list[current_dir][1][0] * instruction[1]
            y = direction_list[current_dir][1][1] * instruction[1]
            coord[0] += x
            coord[1] += y
            continue
        if instruction[0] in "RL":
            if instruction[0] == "R":
                current_dir = turn(instruction[1], current_dir)
            else:
                current_dir = turn(-instruction[1], current_dir)
            continue
        if instruction[0] in "NESW":
            x = direction_dict[instruction[0]][0] * instruction[1]
            y = direction_dict[instruction[0]][1] * instruction[1]
            coord[0] += x
            coord[1] += y
            continue
    return abs(coord[0]) + abs(coord[1])


def main_pt_2(raw_data):
    current_dir = 1
    coord = [0, 0]
    waypoint = [10, 1]
    list_input = input_list(raw_data)
    for instruction in list_input:
        if instruction[0] == "F":
            x = waypoint[0] * instruction[1]
            y = waypoint[1] * instruction[1]
            coord[0] += x
            coord[1] += y
            continue
        if instruction[0] in "RL":
            if instruction[0] == "R":
                temp_dir = current_dir
                current_dir = turn(instruction[1], current_dir)
                dif = current_dir - temp_dir
                angle = abs((dif - 4) * 90)
                waypoint[0], waypoint[1] = rotate([0, 0], waypoint, angle)
                continue
            else:
                waypoint[0], waypoint[1] = rotate([0, 0], waypoint, instruction[1])
                current_dir = turn(-instruction[1], current_dir)
                continue
        if instruction[0] in "NESW":
            x = direction_dict[instruction[0]][0] * instruction[1]
            y = direction_dict[instruction[0]][1] * instruction[1]
            waypoint[0] += x
            waypoint[1] += y
            continue
    return abs(coord[0]) + abs(coord[1])


if __name__ == '__main__':
    print(main(DATA.Day_12))
    print(main_pt_2(DATA.Day_12))