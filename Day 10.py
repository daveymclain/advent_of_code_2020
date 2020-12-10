import DATA
from memoization import cached


def create_list(data):
    data = data.splitlines()
    data = list(map(int, data))
    data = sorted(data)
    # Add device
    data.append(data[-1] + 3)
    # add start jolt
    data.insert(0, 0)
    return data


# part 1
def main(data):
    data = data.splitlines()
    data = list(map(int, data))
    start_jolts = 0
    data = sorted(data)
    # print(data)
    jolts_dif_1 = 0
    jolts_dif_3 = 0
    # Add device
    data.append(data[-1] + 3)
    # work out the first difference
    if data[0] - start_jolts == 1:
        jolts_dif_1 += 1
    if data[0] - start_jolts == 3:
        jolts_dif_3 += 1
    for pos, volt in enumerate(data):
        # print("pos = {}. volt = {}".format(pos, volt))
        if pos == len(data) - 1:
            return jolts_dif_1, jolts_dif_3
        if data[pos + 1] - volt == 1:
            jolts_dif_1 += 1
            continue
        if data[pos + 1] - volt == 3:
            jolts_dif_3 += 1
            continue


# part 2
count = 0


@cached
def solve(pos):
    global count
    inner_count = 0
    if adapter_list[pos] == adapter_list[-1]:
        return 1
    for i in range(1, 4):
        list_len = len(adapter_list)
        if pos + i > list_len - 1:
            continue
        dif = adapter_list[pos + i] - adapter_list[pos]
        if dif == 1:
            inner_count += solve(pos + i)
        if dif == 2:
            inner_count += solve(pos + i)
        if dif == 3:
            inner_count += solve(pos + i)
    count += inner_count
    return inner_count


if __name__ == '__main__':
    part_1_ans = main(DATA.Day_10)
    print("part 1 ans = {}".format(part_1_ans[0] * part_1_ans[1]))
    adapter_list = create_list(DATA.Day_10)
    print("part 2 ans = {}".format((solve(0))))
    print(solve.cache_info())
