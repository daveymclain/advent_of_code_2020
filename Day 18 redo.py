import DATA
import time
from itertools import product
import re

samples = {26: """2 * 3 + (4 * 5)""",
           437: """5 + (8 * 3 + 9 + 3 * 4 * 3)""",
           12240: """5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))""",
           13632: """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""}


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


def get_bracket(equation, math):
    raw = equation
    bracket = re.finditer(r"\([0-9+* ]+\)", equation)
    for b in bracket:
        sp = b.span()
        contents = b.group(0)
        first_half = raw[:sp[0]]
        second_half = raw[sp[1]:]
        contents = contents.replace("(", "").replace(")", "")
        contents = math(contents)
        raw = first_half + str(contents) + second_half
        if ")" in raw or "(" in raw:
            raw = get_bracket(raw, math)
        return raw


def three_num_equation(equation, pos):
    last_num = equation.pop(pos + 1)
    func = equation.pop(pos)
    first_num = equation.pop(pos - 1)
    result = str(eval(first_num + func + last_num))
    equation.insert(pos - 1, result)
    return equation


def new_new_math(equation):
    equation = equation.split()
    while len(equation) > 1:
        for pos, value in enumerate(equation):
            if "+" in equation:
                if value == "+":
                    equation = three_num_equation(equation, pos)
                    break
            else:
                if value == "*":
                    equation = three_num_equation(equation, pos)
                    break
    return int(equation[0])


def main(math):
    total = 0
    for line in DATA.Day_18.splitlines():
        if ")" in line:
            total += math(get_bracket(line, math))
        else:
            total += math(line)
    return total


start = time.time()
print("part one ans = {}".format(main(new_math)))
end = time.time()
print("{} seconds".format(round(end - start, 4)))
start_2 = time.time()
print("part two ans = {}".format(main(new_new_math)))
end = time.time()
print("{} seconds".format(round(end - start_2, 4)))
print("\ntotal time {} seconds".format(round(end - start, 4)))
