import DATA
import time
from itertools import product
import re
import types


sample = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

sample_2 = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""

def parse_input(raw_data):
    data = raw_data.split("\n\n")
    rules = data[0].splitlines()
    rules = list(map(lambda x: re.sub(r"\"", "", x), rules))
    rules = list(map(lambda x: re.split(r":\s", x), rules))
    messages = data[1].splitlines()
    rule_dict = {}
    for rule in rules:
        rule_dict[rule[0]] = rule[1]
    return rule_dict, messages


rules, messages = parse_input(DATA.Day_19)

rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"

rule_zero = rules["0"].split(" ")
print(rules)
print(rule_zero)

size = 0

def match_string(rule_num):
    global size

    bl = "("
    br = ")"

    if re.search(r"[a-z]+", rules[rule_num]):
        return rules[rule_num]
    if re.fullmatch(r"\d+", rules[rule_num]):
        return bl + match_string(rules[rule_num]) + br
    if re.fullmatch(r"\d+\s\d+", rules[rule_num]):
        left, right = rules[rule_num].split(" ")
        return bl + match_string(left) + match_string(right) + br
    if re.search(r"\s\|\s", rules[rule_num]):
        or_rule = re.split(r"\s\|\s", rules[rule_num])
        left, right = or_rule
        left = left.split(" ")
        right = right.split(" ")
        left_final = ""
        for num in left:
            left_final += match_string(num)
        right_final = ""
        for num in right:
            if num == "8":
                size += 1
                if size == 100:
                    continue
            if num == "11":
                size += 1
                if size == 100:
                    continue
                print("yes")
            right_final += match_string(num)
        return bl + left_final + "|" + right_final + br
    return rules[rule_num]

for rule in rules:
    rules[rule] = match_string(rule)
    print(rules[rule])
    print(size)
    size = 0
match_sting = ""
for i in rule_zero:
    match_sting += rules[i]
print(match_sting)
total = 0
for i in messages:
    if re.fullmatch(match_sting, i):
        total += 1
print("total = {}".format(total))