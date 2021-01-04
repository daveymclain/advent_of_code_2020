sample = 5764801

door = 16616892
card = 14505727


def find_loop_size(to_find):
    value = 1
    for loop_size in range(1, 1000000000):
        value = value * 7
        value = value % 20201227
        if value == to_find:
            return loop_size
        if loop_size % 1000 == 0:
            print("loop number = {}\n".format(loop_size))

def find_key(loops, subect_number):
    value = 1
    for loop_size in range(loops):
        value = value * subect_number
        value = value % 20201227
        if loop_size % 1000 == 0:
            print("loop number = {}\n".format(loop_size))
    return value

print(find_key(find_loop_size(door), card))
