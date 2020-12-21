import DATA
import time
from itertools import product
import re
import types

sample = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""


def bit_to_num(bit_mask):
    bit_mask = bit_mask[::-1]
    last_num = 1
    total = 0
    for pos, instr in enumerate(bit_mask):
        if pos == 0:
            current_num = 1
        else:
            current_num = last_num * 2
            last_num = current_num
        if instr == "1":
            total += current_num
    return total


class Tile:
    def __init__(self, raw_tile):
        self.possible_connections = 0
        self.ROTATION_RULE = {"invert", "invert", "same", "same"}
        self.raw = raw_tile
        self.raw_lines = raw_tile.splitlines()
        self.name = re.search(r"\d+", self.raw_lines.pop(0)).group(0)
        self.sides = {"top": 0, "right": 0, "bottom": 0, "left": 0}
        self.invert = {}
        self.rotation = 0
        self.set_current_edges()
        self.connected = {}  # name: side

    def set_current_edges(self):
        self.sides["top"] = bit_to_num(self.raw_lines[0].replace("#", "1").replace(".", "0"))
        self.invert[self.sides["top"]] = bit_to_num(self.raw_lines[0][::-1].replace("#", "1").replace(".",
                                                                                                      "0"))
        self.sides["bottom"] = bit_to_num(self.raw_lines[-1].replace("#", "1").replace(".", "0"))
        self.invert[self.sides["bottom"]] = bit_to_num(self.raw_lines[-1][::-1].replace("#", "1").replace(".",
                                                                                                          "0"))
        right, left = "", ""
        for pos, line in enumerate(self.raw_lines):
            left += line[0]
            right += line[-1]
        self.sides["left"] = bit_to_num(left[::-1].replace("#", "1").replace(".", "0"))
        self.invert[self.sides["left"]] = bit_to_num(left.replace("#", "1").replace(".", "0"))
        self.sides["right"] = bit_to_num(right[::-1].replace("#", "1").replace(".", "0"))
        self.invert[self.sides["right"]] = bit_to_num(right.replace("#", "1").replace(".", "0"))

    def rotate(self, amount):
        while amount > 0:
            sides_temp = self.sides.copy()
            amount -= 90
            # top to right
            sides_temp["right"] = self.invert[self.sides["top"]]
            # right to bottom
            sides_temp["bottom"] = self.sides["right"]
            # bottom to left
            sides_temp["left"] = self.invert[self.sides["bottom"]]
            # left to top
            sides_temp["top"] = self.sides["bottom"]
            self.rotation += 1
            self.sides = sides_temp
        self.rotation = self.rotation % 4


def parse_data(raw_data):
    data = raw_data.split("\n\n")
    return data


def main(raw_data):
    data = parse_data(raw_data)
    tiles = []
    for tile in data:
        tiles.append(Tile(tile))

    for tile in tiles:
        count = 0
        for search_tile in tiles:
            if tile == search_tile:
                continue
            for side in tile.sides.values():
                if side in search_tile.sides.values() or side in search_tile.invert.values():
                    count += 1
        tile.possible_connections = count
        print(count)


if __name__ == '__main__':
    main(sample)
