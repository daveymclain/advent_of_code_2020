import time

door = 16616892
card = 14505727


def find_loop_size(to_find):
    value = 1
    for loop_size in range(1, 1000000000):
        value = value * 7
        value = value % 20201227
        if value == to_find:
            return loop_size


def find_key(loops, subect_number):
    value = 1
    for loop_size in range(loops):
        value = value * subect_number
        value = value % 20201227
    return value


start = time.time()
print("part one {}".format(find_key(find_loop_size(door), card)))
print("time taken {}".format(time.time() - start))