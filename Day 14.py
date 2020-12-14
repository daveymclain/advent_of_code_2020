
sample = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXX00X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


def raw_data_list(raw_data):
    ret_dict = {}
    ret_list = []
    data = raw_data.splitlines()
    for line in data:
        if line[:4] == "mask":
            key = line[7:]
            ret_list = []
            continue
        line_list = line.split(" = ")
        line_list = [int(line_list[0].replace("mem", "").replace("[", "").replace("]", "")), int(line_list[1])]
        ret_list.append(line_list)
        ret_dict[key] = ret_list
    return ret_dict

print(raw_data_list(sample))