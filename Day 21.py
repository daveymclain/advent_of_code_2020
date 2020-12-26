import DATA
import time
import re
import math

sample = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""


class Item:
    def __init__(self, line):
        self.raw_line = line
        self.allergens = []
        self.ingredients = []
        self.ingredients_edited =[]
        self.parse_line()

    def parse_line(self):
        line = self.raw_line.split("(")
        line[1] = re.sub("contains ", "", line[1])
        line[1] = line[1][:-1]
        if re.search(",", line[1]):
            line[1] = re.split(", ", line[1])
            for allergen in line[1]:
                self.allergens.append(allergen)
        else:
            self.allergens.append(line[1])
        line[0] = line[0].split(" ")[:-1]
        for ingredient in line[0]:
            self.ingredients.append(ingredient)
        self.ingredients_edited = self.ingredients


not_allergens = []
items = []

for line in DATA.Day_21.splitlines():
    items.append(Item(line))

for item in items:
    for ingredient in item.ingredients_edited:
        not_allergens.append(ingredient)

# get
for i in range(1):
    for pos_allergen,  item in enumerate(items):
        if len(item.allergens) == 1:
            single_allergen = item.allergens[0]
            single_allergen_ingredients = item.ingredients_edited.copy()
            for ingredient in single_allergen_ingredients:
                item_with_allergen_count = 0
                item_with_allergen_and_ingredient_count = 0
                for pos_tests, item_test in enumerate(items):
                    # if pos_allergen != pos_tests:
                        if single_allergen in item_test.allergens:
                            item_with_allergen_count += 1
                            if ingredient in item_test.ingredients:
                                item_with_allergen_and_ingredient_count += 1
                if item_with_allergen_and_ingredient_count < item_with_allergen_count:
                    for pos_del,  item_del in enumerate(items):
                        if single_allergen in item_del.allergens:
                            # if pos_allergen == pos_del:
                            #     pass
                            if ingredient in item_del.ingredients_edited:
                                count = item_del.ingredients.count(ingredient)
                                for i in range(count):
                                    item_del.ingredients_edited.remove(ingredient)


def check_ingredient(ingredient, allergen):
    if item in items:
        if allergen in item.allergens:
            if ingredient not in item.ingredients:
                return False
    return True



for i in items:
    if len(i.allergens) == 1:
        print(i.allergens[0])
        print(i.ingredients_edited)


# for i in range(1):
#     for pos, item in enumerate(items):
#         if len(item.allergens) == 1:
#             allergen = item.allergens[0]
#             print(allergen)
#             print(item.ingredients_edited)
#
#             if len(item.ingredients_edited) == 1:
#                 ingredient = item.ingredients_edited[0]
#                 for pos_tes, item_test in enumerate(items):
#                     if pos != pos_tes:
#                         temp = item_test.ingredients_edited.copy()
#                         if ingredient in temp:
#                             if allergen not in item_test.allergens:
#                                 for i in range(temp.count(ingredient)):
#                                     item_test.ingredients_edited.remove(ingredient)



allergens = {}
for pos, item in enumerate(items):
    if len(item.allergens) == 1:
        allergen = item.allergens[0]
        if len(item.ingredients_edited) == 1:
            ingredient = item.ingredients_edited[0]
            allergens[ingredient] = allergen
print(allergens)
for ingredient in allergens:
    count = not_allergens.count(ingredient)
    for i in range(count):
        not_allergens.remove(ingredient)

print(not_allergens)
print(len(not_allergens))






