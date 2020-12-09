import DATA

DATA = DATA.DAY_3
DATA = DATA.splitlines().copy()
SLOPES = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


def slope(right, down):
    pos = [0, 0]
    count = 0
    while True:
        pos[0] += down
        pos[1] += right
        print(pos)
        if pos[0] >= len(DATA):
            return count
        if pos[1] > len(DATA[pos[0]]) - 1:
            pos[1] = pos[1] - len(DATA[pos[0]])
        if DATA[pos[0]][pos[1]] == "#":
            count += 1


result = 1
for test in SLOPES:
    result *= slope(test[0], test[1])

print(result)