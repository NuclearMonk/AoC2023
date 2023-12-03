from math import prod
from typing import Iterable, Dict, List, Tuple
from time import process_time
filename = "bigboy.txt"
max_rgb = (12, 13, 14)


def string_to_game_info(lines: Iterable[str]):
    for line in lines:
        game_id_string, game_data_string = line.split(":")
        game_id = int(game_id_string.split()[1])
        games = game_data_string.split(";")
        yield game_id, map(game_data_to_counts, games)


def game_data_to_counts(game_string: str) -> Tuple[int, int, int]:
    r, g, b = 0, 0, 0
    color_data = game_string.split(",")
    for entry in color_data:
        try:
            count, color = entry.split()
        except:
            return 0,0,0
        match int(count), color:
            case x, "red":
                r += x
            case x, "green":
                g += x
            case x, "blue":
                b += x
    return r, g, b


def check_if_valid(game: Tuple[int, int, int]) -> bool:
    if game[0] > max_rgb[0]:
        return False
    if game[1] > max_rgb[1]:
        return False
    if game[2] > max_rgb[2]:
        return False
    return True


def get_min_needed_cubes(games: Iterable[Tuple[int, int, int]]) -> Tuple[int, int, int]:
    r_max, g_max, b_max = 0, 0, 0
    for r, g, b in games:
        r_max = max(r_max, r)
        g_max = max(g_max, g)
        b_max = max(b_max, b)
    return r_max, g_max, b_max


def solve1(lines: Iterable[str]) -> int:
    return sum(x[0] for x in filter(lambda y: all(map(check_if_valid, y[1])), string_to_game_info(lines)))


def solve2(lines: Iterable[str]) -> int:
    return sum(map(prod,(get_min_needed_cubes(games) for _,games in string_to_game_info(lines))))


with open(filename, "r") as f:
    lines = f.read().splitlines()
start = process_time()
print(solve1(lines))
print("Part 1:", process_time() - start)
print("------------")
start= process_time()
print(solve2(lines))
print("Part 2:",process_time() - start)
