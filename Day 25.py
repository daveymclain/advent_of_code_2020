import time

door = 16616892
card = 14505727


def find_loop_size(to_find):
    value = 1
    loop_size = 0
    while 1:
        loop_size += 1
        value = value * 7
        value = value % 20201227
        if value == to_find:
            return loop_size


def find_key(loops, subject_number):
    value = 1
    for loop_size in range(loops):
        value = value * subject_number
        value = value % 20201227
    return value


start = time.time()
print("part one {}".format(find_key(find_loop_size(door), card)))
print("time taken {}".format(time.time() - start))