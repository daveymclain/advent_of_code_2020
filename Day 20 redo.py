import DATA
import time
import re
import math

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
    return total  #


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


class Tile:
    def __init__(self, raw_tile):
        self.type = ""
        self.possible_connections = 0
        self.raw = raw_tile
        self.raw_lines = raw_tile.splitlines()
        self.name = re.search(r"\d+", self.raw_lines.pop(0)).group(0)
        self.sides = {"top": 0, "right": 0, "bottom": 0, "left": 0}
        self.invert = {}
        self.rotation = 0
        self.image = []
        self.convert_image_to_list()
        self.set_current_edges()
        self.connected = {}

    def set_current_edges(self):

        self.sides["top"] = bit_to_num(["1" if x == "#" else "0" for x in self.image[0]])
        self.invert[self.sides["top"]] = bit_to_num(["1" if x == "#" else "0" for x in self.image[0][::-1]])
        self.sides["bottom"] = bit_to_num(["1" if x == "#" else "0" for x in self.image[-1]])
        self.invert[self.sides["bottom"]] = bit_to_num(["1" if x == "#" else "0" for x in self.image[-1][::-1]])
        right, left = [], []
        for pos, line in enumerate(self.image):
            left.append(line[0])
            right.append(line[-1])
        self.sides["left"] = bit_to_num(["1" if x == "#" else "0" for x in left[::-1]])
        self.invert[self.sides["left"]] = bit_to_num(["1" if x == "#" else "0" for x in left])
        self.sides["right"] = bit_to_num(["1" if x == "#" else "0" for x in right])
        self.invert[self.sides["right"]] = bit_to_num(["1" if x == "#" else "0" for x in right[::-1]])

    def rotate(self):

        self.rotate_image()

        sides_temp = self.sides.copy()
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
        new_image = []
        for i in range(len(self.image)):
            new_image.append([])
        for row, col_full in enumerate(self.image):
            for col, pixel in enumerate(col_full):
                new_image[col].insert(0, pixel)
        self.image = new_image

    def orientate_left(self, side):
        while self.sides["left"] != side and self.sides["left"] != invert_num(side):
            self.rotate()

    def orientate_up(self, side):
        while self.sides["top"] != side and self.sides["top"] != invert_num(side):
            self.rotate()

    def connection(self, dir):
        side = self.sides[dir]
        if side in self.connected or invert_num(side) in self.connected:
            return True
        else:
            return False

    def print(self):
        try:
            top = self.connected[self.sides["top"]]
        except KeyError:
            try:
                top = self.connected[invert_num(self.sides["top"])]
            except KeyError:
                top = "None"
        try:
            right = self.connected[self.sides["right"]]
        except KeyError:
            try:
                right = self.connected[invert_num(self.sides["right"])]
            except:
                right = "None"
        try:
            bottom = self.connected[self.sides["bottom"]]
        except KeyError:
            try:
                bottom = self.connected[invert_num(self.sides["bottom"])]
            except:
                bottom = "None"
        try:
            left = self.connected[self.sides["left"]]
        except KeyError:
            try:
                left = self.connected[invert_num(self.sides["left"])]
            except:
                left = "None"

        print("\t{top}\n{left} {name} \t{right}\n\t{bottom}".format(top=top, left=left, right=right, bottom=bottom,
                                                                    name=self.name))

    def image_flip(self, axis):
        temp_top = self.sides.copy()

        if axis == "y":
            print("flipped top")
            self.sides["top"] = temp_top["bottom"]
            self.sides["bottom"] = temp_top["top"]
            self.image = self.image[::-1]

        if axis == "x":
            print("flipped right")
            self.sides["left"] = temp_top["right"]
            self.sides["right"] = temp_top["left"]
            temp_image = []
            for row in self.image:
                temp_image.append(row[::-1])
            self.image = temp_image


def parse_data(raw_data):
    data = raw_data.split("\n\n")
    return data


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
        axis = "x"
    else:
        axis = "y"
    if connected:
        if test in tile.connected or invert_num(test) in tile.connected:
            print("connected")
        else:
            tile.image_flip(axis)
            if test in tile.connected or invert_num(test) in tile.connected:
                print(f"passed {axis} invert")
            else:
                print(f"failed {axis} invert")
    else:
        if test in tile.connected or invert_num(test) in tile.connected:
            tile.image_flip(axis)
            if test in tile.connected or invert_num(test) in tile.connected:
                print(f"failed {axis} invert")
            else:
                print(f"passed {axis} invert")
    return tile


def gen_pic(tiles):
    starting_corner = first_tile(tiles)
    grid = []
    print("starting corner")
    print(starting_corner)
    col = [starting_corner, next_tile(starting_corner, tiles, "right")]
    top = False
    while len(grid) < math.sqrt(len(tiles)):
        while len(col) < math.sqrt(len(tiles)):
            col.append(next_tile(col[-1], tiles, "right"))
        temp_col = []
        for tile in col:
            temp_col.append(test_orientation(tile, "top", connected=top))
        top = True
        grid.append(temp_col)
        if len(grid) == math.sqrt(len(tiles)):
            break
        starting_edge = next_tile(temp_col[0], tiles, "bottom")
        starting_edge.print()
        starting_edge.orientate_up(temp_col[0].sides["bottom"])
        starting_edge = test_orientation(starting_edge, "left", False)
        starting_edge.print()
        col = [starting_edge]
    for rows in grid:
        for row, tile in enumerate(rows):
            if row == 0:
                print("test top row")
                test_orientation(tile, "bottom", True)
                print("finish")
            tile.set_current_edges()
    check_middle_flips(grid)
    trim_edges(grid)
    merge_tiles_border_string(grid)
    final_image = merge_tiles(grid)

    count = 1
    monster_count = 1
    while not search_monster(final_image):
        # print("rotated")
        if count == 4:
            final_image = flip_image(final_image)
        final_image = rotate_image(final_image)
        count += 1
    while search_monster(final_image):
        monster_count += 1
    while search_monster(final_image):
        monster_count += 1

    for row, i in enumerate(final_image):
        temp_row = f"{row}" + "".join(i)
        print(temp_row)

    print(count)
    waves = convert_image_to_string(final_image).count("#")
    print("waves {}".format(waves))

    return grid

# #################################################################################################################################

def convert_image_to_string(final_image):
    output_string = ""
    for col in final_image:
        for pixel in col:
            output_string += pixel

    # print(output_string)
    return output_string

def rotate_image(final_image):
    print("rotate")
    new_image = []
    for i in range(len(final_image)):
        new_image.append([])
    for row, col_full in enumerate(final_image):
        for col, pixel in enumerate(col_full):
            new_image[col].insert(0, pixel)
    return new_image

def flip_image(final_image):
    final_image = final_image[::-1]
    return final_image

def merge_tiles_border_string(row):
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
    temp_image = []
    for row in final_image:
        temp_row = []
        for item in row:
            temp_row += ["|"] + item + ["|"]
        temp_image.append(temp_row)
    final_image = temp_image
    count = 0
    for row in final_image:
        print("".join(row))
        count += 1
        if count == tile_width:
            print()
            count = 0
    return final_image


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
    temp_image = []
    for row in final_image:
        temp_row = []
        for item in row:
            temp_row += item
        temp_image.append(temp_row)
    final_image = temp_image
    for row in final_image:
        print(row)
    return final_image


def check_middle_flips(rows):
    print("################\nTesting middle")
    for row, cols in enumerate(rows):
        if row > 0:
            for col, tile in enumerate(cols):
                tile_above = rows[row - 1][col]
                tile.set_current_edges()
                tile_above.set_current_edges()
                if tile.sides["top"] == tile_above.sides["bottom"]:
                    print("passed")
                    continue

                else:
                    tile.image_flip("y")
                    print(tile_above.sides)
                    tile.set_current_edges()
                    tile_above.set_current_edges()
                    print(tile_above.sides)
                    print("flipped middle")
                    if tile.sides["top"] == tile_above.sides["bottom"]:
                        print("passed")
                    else:
                        print("Error############################################################################")


def trim_edges(row):
    for col in row:
        for tile in col:
            temp_image = []
            tile.image = tile.image[1:]
            tile.image = tile.image[:-1]
            for line in tile.image:
                temp_image.append(line[1:-1])
            tile.image = temp_image
    return row


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
            tile.type = "middle"
    part_one_result = 1
    for corner_name in corners:
        part_one_result = part_one_result * corner_name

    print("corners = {}".format(corner_count))
    print("edge = {}".format(edge_count))
    print("middle = {}".format(middle_count))
    row_length = math.sqrt(len(tiles))
    print("row length {}".format(row_length))
    print("result = {}".format(part_one_result))

    final_tiles = gen_pic(tiles)

def search_monster(image):
    line_0, line_1, line_2 = gen_search(search_patern)
    match = False
    for row, cols in enumerate(image):
        # if row == 0:
        #     continue
        # if row == len(image):
        #     return False
        str1 = ''.join(cols)
        offset = 0
        while len(str1) > 0:
            for dragon_body in re.finditer(line_1, str1):
                print("found a body")
                print(f"row {row} {dragon_body.span()}")
                end = dragon_body.span()[1] + offset
                legs = [dragon_body.span()[0] + offset, dragon_body.span()[1] + offset]
                if image[row - 1][end - 2] == "#":
                    print("found head")
                    str2 = "".join(image[row + 1])
                    str2 = str2[legs[0] + 1:legs[1]]
                    for dragon_legs in re.finditer(line_2, str2):
                        print("found some legs")
                        print(f"row {row + 1} {dragon_legs.span()}")
                        # if end == end_2:
                        print("found the legs")
                        image[row - 1].pop(end - 2)
                        image[row - 1].move(end - 2, "O")
                        for pos, group in enumerate(dragon_body.groups(), 1):
                            image[row].pop(dragon_body.span(pos)[0] + offset)
                            image[row].move(dragon_body.span(pos)[0] + offset, "O")
                        for pos, group in enumerate(dragon_legs.groups(), 1):
                            image[row + 1].pop(dragon_legs.span(pos)[0] + legs[0] + 1)
                            image[row + 1].move(dragon_legs.span(pos)[0] + legs[0] + 1, "O")
                        return True
                    else:
                        match = False
            str1 = str1[1:]
            offset += 1
    return match


def gen_search(search_thing_lines):
    search_thing_lines = search_thing_lines.splitlines()
    search_list = []
    search_string = ""
    first = True
    count = 0
    for line in search_thing_lines:
        for pixel in line:
            if pixel == "#":
                if first:
                    first = False
                    search_string += "(#).{"
                    count = 0
                else:
                    search_string += str(count) + "}(#).{"
                    count = 0
            else:
                count += 1
        search_string = search_string[:-2]
        search_list.append(search_string)
        search_string = ""
        count = 0
        first = True
    print(search_list)

    return search_list[0], search_list[1], search_list[2]

main(DATA.Day_20)
