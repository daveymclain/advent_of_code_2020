import DATA


def main(data, length):
    data = data.splitlines()
    data = list(map(int, data))
    for place in range(len(data)):
        place += length
        add_up = False
        # TODO: Change to enumerate
        for i in range(place - length, place):
            for ii in range(place - length, place):
                if data[i] == data[ii]:
                    continue
                if data[i] + data[ii] == data[place]:
                    add_up = True
                    break
        if not add_up:
            return data[place]


def solve(num, data):
    data = data.splitlines()
    data = list(map(int, data))
    for start in range(len(data)):
        total = 0
        current_list = [data[start]]
        for next_num in range(start, len(data)):
            current_list.append(data[next_num])
            total += data[next_num]
            if total == num:
                return sorted(current_list)[0] + sorted(current_list)[-1]


if __name__ == "__main__":
    part_1_ans = main(DATA.Day_9, 25)
    print("part 1 = {}".format(part_1_ans))
    part_2_ans = solve(main(DATA.Day_9, 25), DATA.Day_9)
    print("part 2 = {}".format(part_2_ans))
