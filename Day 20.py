import DATA
import time
from itertools import product
import re
import math
import types
from scipy.spatial import distance

search_patern = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

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


def gen_bit_template():
    ret_list = []
    last_num = 1
    for pos in range(10):
        if pos == 0:
            current_num = 1
        else:
            current_num = last_num * 2
            last_num = current_num
        ret_list.append(current_num)
    return ret_list


bit_template = gen_bit_template()


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


def num_to_bit(num):
    ret_bit = ""
    for bit_num in bit_template[::-1]:
        if num < bit_num:
            ret_bit += "0"
            continue
        else:
            ret_bit += "1"
            num -= bit_num
    return ret_bit


def invert_num(num):
    bit = num_to_bit(num)
    bit = bit[::-1]
    return bit_to_num(bit)


invert_1 = invert_num(1)
print(invert_num(invert_1))


class Tile:
    def __init__(self, raw_tile):
        self.type = ""
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
        self.image = []
        self.convert_image_to_list()

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
            self.rotate_image()
            # print("rotate")

            sides_temp = self.sides.copy()
            amount -= 90
            # top to right
            sides_temp["right"] = self.sides["top"]
            # right to bottom
            sides_temp["bottom"] = self.sides["right"]
            # bottom to left
            sides_temp["left"] = self.sides["bottom"]
            # left to top
            sides_temp["top"] = self.sides["left"]
            self.rotation += 1
            self.sides = sides_temp
        self.rotation = self.rotation % 4

    def convert_image_to_list(self):
        for line in self.raw_lines:
            self.image.append(list(line))

    def print_tile(self):

        for row, col_full in enumerate(self.image):
            print(col_full)

    def rotate_image(self):
        new_image = self.image
        print("old image")
        self.print_tile()
        print()
        new_image = []
        for i in range(len(self.image)):
            new_image.append([])

        for row, col_full in enumerate(self.image):
            for col, pixel in enumerate(col_full):
                new_image[col].insert(0, pixel)

        self.image = new_image
        print("rotated image")
        self.print_tile()
        print()

    def orientate_left(self, side):
        while self.sides["left"] != side and self.sides["left"] != invert_num(side):
            # print(self.sides["left"])
            self.rotate(90)

    def orientate_up(self, side):
        while self.sides["top"] != side and self.sides["top"] != invert_num(side):
            # print(self.sides["left"])
            self.rotate(90)

    def connection(self, dir):
        side = self.sides[dir]
        if side in self.connected or invert_num(side) in self.connected:
            return True
        else:
            return False

    def print(self):
        # print(self.name)
        # print("connected {}\nsides {}\ninverted values {}".format(self.connected, self.sides, self.invert))
        # print("connected amount {}".format(self.possible_connections))
        # print("\t{top}\n{left}\t{right}\n\t{bottom}".format(top=self.connection("top"),
        #                                                     left=self.connection("left"),
        #                                                     right=self.connection("right"),
        #                                                     bottom=self.connection("bottom")))

        pass

    def image_flip(self, axis):
        temp_top = self.sides.copy()

        if axis == "z":
            self.sides["top"] = temp_top["bottom"]
            self.sides["bottom"] = temp_top["top"]
            self.image = self.image[::-1]

        if axis == "y":
            self.sides["left"] = temp_top["right"]
            self.sides["right"] = temp_top["left"]
            temp_image = []
            for row in self.image:
                temp_image.append(row[::-1])
            self.image = temp_image


def parse_data(raw_data):
    data = raw_data.split("\n\n")
    return data


def main(raw_data):
    data = parse_data(raw_data)
    tiles = {}
    for tile in data:
        name = re.search(r"\d+", tile).group(0)
        tiles[name] = Tile(tile)
    corner_count = 0
    edge_count = 0
    middle_count = 0
    corners = []
    for tile in tiles.values():
        count = 0
        for search_tile in tiles.values():
            if tile == search_tile:
                continue
            for side in tile.sides.values():
                if side in search_tile.sides.values() or side in search_tile.invert.values():
                    count += 1
                    tile.connected[side] = search_tile.name
        tile.possible_connections = count
        if count == 2:
            corner_count += 1
            corners.append(int(tile.name))
            tile.type = "corner"
        if count == 3:
            edge_count += 1
            tile.type = "edge"
        if count == 4:
            middle_count += 1
            tile.type = "Middle"
    result = 1
    for corner_name in corners:
        result = result * corner_name

    print("corners = {}".format(corner_count))
    print("edge = {}".format(edge_count))
    print("middle = {}".format(middle_count))
    row_length = math.sqrt(len(tiles))
    print("row length {}".format(row_length))
    print("result = {}".format(result))
    final_tiles = gen_pic(tiles)


def first_tile(tiles):
    for tile in tiles.values():
        if tile.type == "corner":
            print("Starting corner")
            tile.print()
            return tile


def next_tile(last_tile, tiles, dir):
    try:
        next_tile = tiles[last_tile.connected[last_tile.sides[dir]]]
    except KeyError:
        next_tile = tiles[last_tile.connected[invert_num(last_tile.sides[dir])]]
    next_tile.orientate_left(last_tile.sides[dir])
    return next_tile


def test_orientation(tile, dir, connected=True):
    test = tile.sides[dir]
    if dir == "left":
        axis = "y"
    else:
        axis = "z"
    if connected:
        if test in tile.connected or invert_num(test) in tile.connected:
            pass
        else:
            tile.image_flip(axis)
    else:
        if test in tile.connected or invert_num(test) in tile.connected:
            tile.image_flip(axis)
        else:
            pass
    return tile


def gen_pic(tiles):
    starting_corner = first_tile(tiles)
    row = []
    col = [starting_corner, next_tile(starting_corner, tiles, "right")]
    top = False
    while len(row) < math.sqrt(len(tiles)):
        while len(col) < math.sqrt(len(tiles)):
            col.append(next_tile(col[-1], tiles, "right"))
        temp_col = []
        for tile in col:
            temp_col.append(test_orientation(tile, "top", connected=top))
        top = True
        row.append(temp_col)
        if len(row) == math.sqrt(len(tiles)):
            break
        starting_edge = next_tile(temp_col[0], tiles, "bottom")
        starting_edge.print()
        starting_edge.orientate_up(temp_col[0].sides["bottom"])

        starting_edge = test_orientation(starting_edge, "left", False)
        starting_edge.print()
        col = [starting_edge]
    check_middle_flips(row)
    trim_edges(row)
    merge_tiles(row)
    gen_search(search_patern, merge_tiles(row))
    return row


def trim_edges(row):
    for col in row:
        for tile in col:
            temp_image = []
            tile.image = tile.image[1:]
            tile.image = tile.image[:-1]
            for line in tile.image:
                temp_image.append(line[1:-1])
            tile.image = temp_image
            for line in temp_image:
                print(line)
    return row






def check_middle_flips(rows):
    for row, col in enumerate(rows):
        if row > 0:
            for col_num, tile in enumerate(col):
                if col_num > 0:
                    tile_above = rows[row - 1][col_num]

                    if tile.sides["top"] == tile_above.sides["bottom"] or invert_num(tile.sides["top"]) == \
                            tile_above.sides["bottom"]:
                        continue
                    else:
                        tile.image_flip("z")


def merge_tiles(row):
    final_image = []
    tile_width = len(row[0][0].image[0])
    for i in range(tile_width * len(row)):
        final_image.append([])
    offset = 0
    for cols in row:
        for tile in cols:
            for row, image_row in enumerate(tile.image):
                final_image[row + offset].append(image_row)
        offset += tile_width
    for row in final_image:
        print(row)
    final_image = final_image
    final_image = final_image
    temp_image = []

    for row in final_image:
        temp_row = []
        for item in row:
            temp_row += item
        temp_row = temp_row
        temp_row = temp_row
        temp_image.append(temp_row)
    final_image = temp_image
    for row in final_image:
        print(row)
    return final_image


# def merge_tiles(final_tiles):


def gen_search(search_thing_lines, image):
    image_width = len(image[0])
    search_thing_lines = search_thing_lines.splitlines()
    search_thing_width = len(search_thing_lines[0])
    offset = image_width - search_thing_width
    search_string = ""
    first = True
    count = 0
    for line in search_thing_lines:
        count += offset
        for pixel in line:
            if pixel == "#":
                if first:
                    first = False
                    search_string += "#.{"
                    count = 0
                else:
                    search_string += str(count) + "}#{"
                    count = 0
            else:
                count += 1
    search_string = search_string[:-1]
    print(search_string)
    return search_string


if __name__ == '__main__':
    main(sample)
