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
    directions = {"nw": [0, 1], "ne": [1, 1], "e": [1, 0], "w": [-1, 0], "sw": [0, -1], "se": [1, -1]}
    directions_odd = {"nw": [-1, 1], "ne": [0, 1], "e": [1, 0], "w": [-1, 0], "sw": [-1, -1], "se": [0, -1]}
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
    count = list(flipped.values()).count(True)
    print(len(flipped))
    print(count)


flip_tiles(DATA.Day_24)
