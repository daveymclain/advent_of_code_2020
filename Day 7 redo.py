sample = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
import DATA
from memoization import cached, CachingAlgorithmFlag
def total_bags(bag):
    total = 0
    for inner in dict_data[bag]:
        amount = dict_data[bag][inner]
        total += amount
        # total += total_bags(inner, total)
    dict_data["total"] = total
    return total
def data_to_dict(data):
    """Turn raw data string into a usable dictionary"""
    bag_dict = {}
    for line in data.splitlines():
        bag = line.split(" bags contain ")
        bag_contents = bag[1].split(", ")

        bag_contents_dict = {}
        for i in range(len(bag_contents)):
            bag_contents[i] = bag_contents[i].replace(" bags", "")
            bag_contents[i] = bag_contents[i].replace(" bag", "")
            bag_contents[i] = bag_contents[i].replace(".", "")
        # Split the numbers
        for i in range(len(bag_contents)):

            if bag_contents[i] == "no other":
                continue
            bag_contents_dict[bag_contents[i][2:]] =  int(bag_contents[i][0])
        bag_dict[bag[0]] = bag_contents_dict

    return bag_dict

# def rec_number_bags(bag, inner_bag):
#     for


def bags_in_bags_dict(bag, inner_bag):
    # for bag in dict_data:
    if 0 == len(dict_data[inner_bag].keys()):
        # print(dict_data[inner_bag])
        return
    for inner_inner_bag in dict_data[inner_bag]:
        if inner_inner_bag in dict_data[bag]:
            dict_data[bag][inner_inner_bag] += dict_data[bag][inner_inner_bag]
        else:
            dict_data[bag][inner_inner_bag] = dict_data[inner_bag][inner_inner_bag]
        # number = dict_data[bag][inner_inner_bag]
        # print(inner_inner_bag, number)
        bags_in_bags_dict(bag, inner_inner_bag)




dict_data = data_to_dict(DATA.Day_7)
test_dict = data_to_dict(DATA.Day_7)
#
#
# for bag in test_dict:
#     # print("--{}--".format(bag))
#     for inner_bag in test_dict[bag]:
#         bags_in_bags_dict(bag, inner_bag)

total = 0
# for bag in dict_data.keys():
#     if "shiny gold" in dict_data[bag]:
#         total += 1
# print("part 1 = {}".format(total))
#
# total = 0
# for bag in dict_data["shiny gold"]:
#     total += dict_data["shiny gold"][bag]
#
# print("bags in gold = {}".format(total))
# # print(test_dict["shiny gold"])

@cached
def total_bags(bag):
    total = 0
    for inner in test_dict[bag]:
        amount = test_dict[bag][inner]
        total += amount
        total += total_bags(inner) * amount
    dict_data["total"] = total
    return total




print(total_bags("shiny gold"))
print(total_bags.cache_info())
