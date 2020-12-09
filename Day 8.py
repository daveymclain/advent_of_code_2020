import DATA
import copy

sample = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def create_list(data):
    list = []
    data = data.splitlines()

    for line in data:
        line = line.split(" ")
        # added a boolean so we can monitor if it has already ran
        line = [line[0], int(line[1]), False]
        list.append(line)
        list = list.copy()
    return list


def main(list):
    accumulator = 0
    pos = 0
    run = True
    count = 0
    while run:
        if count == 100000:
            return True
        count += 1
        if list[pos][2]:
            return True
        if len(list) - 1 == pos:
            run = False
        if list[pos][0] == "acc":
            accumulator += list[pos][1]
            list[pos][2] = True
            pos += 1
            continue
        if list[pos][0] == "jmp":
            list[pos][2] = True
            pos += list[pos][1]
            continue
        if list[pos][0] == "nop":
            list[pos][2] = True
            pos += 1
            continue
        count += 1
    return accumulator


def change(list):
    master = copy.deepcopy(list)
    run = True
    pos = 0
    while run:
        print("position = {}".format(pos))
        test_list = copy.deepcopy(master)
        if test_list[pos][0] == "jmp":
            test_list[pos][0] = "nop"
            test_ans = main(test_list)
            if test_ans == True or test_ans == 0:
                pos += 1
                continue
            else:
                return test_ans
        if test_list[pos][0] == "nop":
            test_list[pos][0] = "jmp"
            test_ans = main(test_list)
            if test_ans == True or test_ans == 0:
                pos += 1
                continue
            else:
                return test_ans
        pos += 1


# master = create_list(sample).copy()


# print(main(create_list(DATA.Day_8)))
print(change(create_list(DATA.Day_8).copy()))
