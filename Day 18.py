import DATA
import time
from itertools import product
import re

samples = {26: """2 * 3 + (4 * 5)""",
           437: """5 + (8 * 3 + 9 + 3 * 4 * 3)""",
           12240: """5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))""",
           13632: """((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""}


def bracket_find(brackets):
    backets_copy = brackets
    brack = re.finditer(r"\((.*)\)", str(brackets))
    contents = False
    skip = True
    for b in brack:
        sp = b.span()
        contents = b.group(1)
        print(contents)
        continue
    if not contents:
        next_ = backets_copy
        brack = re.finditer(r"(\d.*)\)", str(next_))

        for b in brack:
            skip = False
            sp = b.span()
            contents = b.group(1)
            print(contents)
        if skip:
            next_ = backets_copy
            brack = re.finditer(r"\((\d.*)", str(next_))
            for b in brack:
                sp = b.span()
                contents = b.group(1)
                print(contents)

    if "(" in str(contents) or ")" in str(contents):
        first_half = backets_copy[:sp[0]]
        second_half = backets_copy[sp[1]:]
        contents = bracket_find(contents)
        ret = first_half + str(contents) + second_half
        return ret
    else:
        first_half = backets_copy[:sp[0]]
        second_half = backets_copy[sp[1]:]
        contents = new_math(contents)
        if "(" in str(first_half) or ")" in str(first_half):
            first_half = bracket_find(first_half)
            ret = first_half + str(contents) + second_half
            return ret
        if "(" in str(second_half) or ")" in str(second_half):
            first_half = bracket_find(second_half)
            ret = first_half + str(contents) + second_half
            return ret
        ret = new_math(first_half + str(contents) + second_half)
        return ret


def new_math(equation):
    total = 0
    equation = equation.split()
    temp_equation = []
    print(equation)
    for pos, value in enumerate(equation):
        temp_equation.append(value)
        if len(temp_equation) == 3:
            temp = ""
            for i in temp_equation:
                temp += str(i)
            total = eval(temp)
            temp_equation = [total]
    return total


# for test in samples:
#     if bracket_find(samples[test]) == test:
#         print("pass")

bracket_find(samples[13632])

