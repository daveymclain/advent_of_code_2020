from string import ascii_lowercase
import DATA

main_data = DATA.Day_6
sample_data = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def gen_dict():
    dict = {}
    for i in ascii_lowercase:
        dict[i] = 0
    return dict


def clean_data(data):
    cleaned = data.splitlines()
    return cleaned


def count_ans(data):
    all_group_ans = []
    group_ans = gen_dict()
    for i in clean_data(data):
        # print(i)
        if i == "":
            all_group_ans.append(group_ans)
            group_ans = gen_dict()
            continue
        for ii in i:
            group_ans[ii] += 1
    all_group_ans.append(group_ans)
    return all_group_ans


def count_all_ans(answers):
    total = 0
    for group in answers:
        # print(group)
        for key in group.keys():
            if group[key] > 0:
                total += 1
    return total


def count_people_ans(data):
    all_group_ans = []
    group = []
    people_ans = gen_dict()

    for i in clean_data(data):
        # print(i)
        if i == "":
            all_group_ans.append(group)
            group = []
            continue
        for ii in i:
            people_ans[ii] += 1
        group.append(people_ans)
        people_ans = gen_dict()
    all_group_ans.append(group)
    return all_group_ans


def count_same_ans(list):
    total = 0
    for group in list:
        group_size = len(group)
        group_ans = gen_dict()
        print("")
        for person in group:
            for ans_key in person.keys():
                group_ans[ans_key] += person[ans_key]
        for key in group_ans.keys():
            if group_ans[key] == group_size:
                total += 1
    return total

print(count_same_ans(count_people_ans(main_data)))






# print("Sample answer:= {}".format(count_all_ans(count_ans(sample_data))))
#
# print("Main answer:= {}".format(count_all_ans(count_ans(main_data))))
