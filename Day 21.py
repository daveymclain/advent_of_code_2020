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
        self.ingredients_edited = []
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


def check_ingredient(ingredient, allergen):
    for item in items:
        if allergen in item.allergens:
            if ingredient not in item.ingredients:
                return False
    return True


def remove_ingredient(ingredient, allergen):
    for item in items:
        if allergen in item.allergens:
            item.ingredients_edited = list(filter(lambda a: a != ingredient, item.ingredients_edited))


for i in range(1):
    for pos_allergen, item in enumerate(items):
        if len(item.allergens) == 1:
            single_allergen = item.allergens[0]
            single_allergen_ingredients = item.ingredients_edited.copy()
            for ingredient in single_allergen_ingredients:
                item_with_allergen_count = 0
                item_with_allergen_and_ingredient_count = 0
                if not check_ingredient(ingredient, single_allergen):
                    remove_ingredient(ingredient, single_allergen)

for i in range(1):
    for pos, item in enumerate(items):
        if len(item.allergens) == 1:
            allergen = item.allergens[0]
            if len(item.ingredients_edited) == 1:
                ingredient = item.ingredients_edited[0]
                for pos_tes, item_test in enumerate(items):
                    if pos != pos_tes:
                        temp = item_test.ingredients_edited.copy()
                        if ingredient in temp:
                            if allergen not in item_test.allergens:
                                for i in range(temp.count(ingredient)):
                                    item_test.ingredients_edited.remove(ingredient)

allergens = {}
for pos, item in enumerate(items):
    if len(item.allergens) == 1:
        allergen = item.allergens[0]
        for ingredient in item.ingredients_edited:
            if allergen not in allergens:
                allergens[allergen] = [ingredient]
            else:
                allergens[allergen].append(ingredient)
# print(allergens)
for ingredients in allergens.values():
    for ingredient in ingredients:
        count = not_allergens.count(ingredient)
        for i in range(count):
            not_allergens.remove(ingredient)
print(len(not_allergens))

for item in items:
    for ingredient_to_remove in not_allergens:
        item.ingredients = list(filter(lambda a: a != ingredient_to_remove, item.ingredients))

for i in range(4):
    for pos, item in enumerate(items):
        if len(item.allergens) == 1:
            single_allergen = item.allergens[0]
            single_allergen_ingredients = item.ingredients.copy()
            for ingredient in single_allergen_ingredients:
                if not check_ingredient(ingredient, single_allergen):
                    for item in items:
                        if len(item.allergens) == 1:
                            if single_allergen in item.allergens:
                                item.ingredients = list(filter(lambda a: a != ingredient, item.ingredients))

    for pos, item in enumerate(items):
        if len(item.allergens) == 1 and len(item.ingredients) == 1:
            single_allergen = item.allergens[0]
            single_ingredient = item.ingredients[0]
            for pos_del, item_del in enumerate(items):
                if pos != pos_del:
                    temp_ingredients = item.ingredients.copy()
                    if single_allergen in item_del.allergens:
                        item_del.allergens.remove(single_allergen)
                    if single_ingredient in item_del.ingredients:
                        item_del.ingredients.remove(single_ingredient)

final = {}
for item in items:
    if len(item.allergens) == 1:
        final[item.allergens[0]] = item.ingredients[0]

final_ans = ""
for allergen in sorted(final):
    final_ans += final[allergen] + ","
print(final_ans[:-1])
