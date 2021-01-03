import re
import DATA

sample = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

directions = {"nw": [0, 1], "ne": [1, 1], "e": [1, 0], "w": [-1, 0], "sw": [0, -1], "se": [1, -1]}
directions_odd = {"nw": [-1, 1], "ne": [0, 1], "e": [1, 0], "w": [-1, 0], "sw": [-1, -1], "se": [0, -1]}


def parse_data(raw_data):
    data = raw_data.splitlines()
    tiles = []
    for raw_tile in data:
        tile = []
        line = re.finditer(r"(se|sw)|(ne|nw)|(e)|(w)", raw_tile)
        for i in line:
            tile.append(i.group())
        tiles.append(tile)
    return tiles


def flip_tiles(raw_data):
    tiles = parse_data(raw_data)
    flipped = {}
    for tile in tiles:
        tile_coord = [0, 0]
        for instruction in tile:
            if tile_coord[1] % 2 == 0:
                tile_coord = list(map(sum, zip(tile_coord, directions[instruction])))
            else:
                tile_coord = list(map(sum, zip(tile_coord, directions_odd[instruction])))
        tile_coord = tuple(tile_coord)
        if tile_coord in flipped:
            del flipped[tile_coord]
        else:
            flipped[tile_coord] = True
    print("part one {}".format(list(flipped.values()).count(True)))
    return flipped


def add_tile(border_tile, tiles_next_to_black):
    if border_tile in tiles_next_to_black:
        tiles_next_to_black[border_tile] += 1
    else:
        tiles_next_to_black[border_tile] = 1
    return tiles_next_to_black

def part_2(flipped, days):

    for day in range(days):
        tiles_next_to_black = {}
        for tile in flipped:
            if tile[1] % 2 == 0:
                for dir in directions.values():
                    border_tile = tuple(list(map(sum, zip(tile, dir))))
                    tiles_next_to_black = add_tile(border_tile, tiles_next_to_black)
            else:
                for dir in directions_odd.values():
                    border_tile = tuple(list(map(sum, zip(tile, dir))))
                    tiles_next_to_black = add_tile(border_tile, tiles_next_to_black)
        temp_flipped = flipped.copy()
        for black in temp_flipped:
            if black in tiles_next_to_black:
                if tiles_next_to_black[black] > 2:
                    del flipped[black]
                    del tiles_next_to_black[black]
            else:
                del flipped[black]
        for tile in tiles_next_to_black:
            if tiles_next_to_black[tile] == 2:
                flipped[tile] = True
    print("Part two {}".format(len(flipped)))




part_2(flip_tiles(DATA.Day_24), 100)
