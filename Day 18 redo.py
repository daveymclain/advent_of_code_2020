import DATA
import time
from itertools import product
import re

samples = {26: """2 * 3 + (4 * 5)""",
           437: """5 + (8 * 3 + 9 + 3 * 4 * 3)""",
           12240: """5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))""",
           13632: """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""}


def get_bracket(equation):
    raw = equation
    bracket = re.finditer(r"\([0-9+* ]+\)", equation)

    for b in bracket:
        sp = b.span()
        # print(b)
        contents = b.group(0)
        first_half = raw[:sp[0]]
        second_half = raw[sp[1]:]
        contents = contents.replace("(", "").replace(")", "")
        contents = new_math(contents)
        raw = first_half + str(contents) + second_half
        # print(raw)
        if ")" in raw or "(" in raw:
            raw = get_bracket(raw)

        return raw


def new_math(equation):
    total = 0
    equation = equation.split()
    temp_equation = []
    for pos, value in enumerate(equation):
        temp_equation.append(value)
        if len(temp_equation) == 3:
            temp = ""
            for i in temp_equation:
                temp += str(i)
            total = eval(temp)
            temp_equation = [total]
    return total


total = 0
for line in DATA.Day_18.splitlines():
    print(line)
    if ")" in line:
        total += new_math(get_bracket(line))
    else:
        total += new_math(line)

print(total)
