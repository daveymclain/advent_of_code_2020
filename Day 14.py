import DATA
from memoization import cached
import time

sample = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


def gen_bit_template():
    ret_list = []
    last_num = 1
    for pos in range(36):
        if pos == 0:
            current_num = 1
        else:
            current_num = last_num * 2
            last_num = current_num
        ret_list.append(current_num)
    return ret_list


bit_template = gen_bit_template()


def raw_data_dict(raw_data):
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


@cached
def bit_to_num(bit_mask):
    bit_mask = bit_mask[::-1]
    last_num = 1
    total = 0
    for pos, instr in enumerate(bit_mask):
        if pos == 0:
            current_num = 1
        else:
            current_num = last_num * 2
            last_num = current_num
        if instr == "1":
            total += current_num
    return total


@cached
def num_to_bit(num):
    ret_bit = ""
    for bit_num in bit_template[::-1]:
        if num < bit_num:
            ret_bit += "0"
            continue
        else:
            ret_bit += "1"
            num -= bit_num
    return ret_bit


def main(raw_data):
    data_dict = raw_data_dict(raw_data)
    mem_dict = {}
    for bit_mask in data_dict:
        for pos, instr in enumerate(data_dict[bit_mask]):
            mem, number = instr
            number_bit = num_to_bit(number)
            output_bit = ""
            print("mem = [{}] number = {}".format(mem, number))
            print("{}\n{}".format(number_bit, bit_mask))
            for i in range(36):
                if bit_mask[i] != "X":
                    output_bit += bit_mask[i]
                else:
                    output_bit += number_bit[i]
            output_num = bit_to_num(output_bit)
            mem_dict[mem] = output_num
    result = 0
    for value in mem_dict.values():
        result += value
    return result


def main_pt2(raw_data):
    data_dict = raw_data_dict(raw_data)
    mem_dict = {}
    # initiate memory
    for bit_mask in data_dict:
        for pos, instr in enumerate(data_dict[bit_mask]):
            mem, number = instr
            mem_dict[mem] = 0
    for bit_mask in data_dict:
        for pos, instr in enumerate(data_dict[bit_mask]):
            mem, number = instr
            number_bit = num_to_bit(mem)
            output_bit = ""
            for i in range(36):
                if bit_mask[i] == "0":
                    output_bit += number_bit[i]
                else:
                    output_bit += bit_mask[i]
            number_of_X = output_bit.count("X")
            float_list_raw = []
            for num in range(bit_template[number_of_X]):
                float_list_raw.append(num_to_bit(num)[-number_of_X:])
            result_floats = []
            for float_raws in float_list_raw:
                temp_float = output_bit
                for X in float_raws:
                    temp_float = temp_float.replace("X", X, 1)
                result_floats.append(temp_float)
                for float in result_floats:
                    memory = bit_to_num(float)
                    mem_dict[memory] = number
    result = 0
    for mem in mem_dict.values():
        result += mem
    return result


if __name__ == '__main__':
    start = time.time()
    print("part one answer = {}".format(main(DATA.Day_14)))
    print("part two answer = {}".format(main_pt2(DATA.Day_14)))
    end = time.time()
    print("time to complete = {}".format(end - start))
