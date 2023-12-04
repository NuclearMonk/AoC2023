from math import prod
from typing import Dict, Iterable, List, Tuple
from itertools import chain, takewhile
from time import process_time
from pprint import pprint

input_file = "Hxtu.txt"


def create_schematic(text: List[List[str]]):
    schematic: Dict[Tuple(int, int), List[int]] = {}
    for line_nr, line in enumerate(text):
        for col, char in enumerate(line):
            part_numbers = []
            if char == "." or char.isdigit():
                continue
            if line_nr > 0:
                if x := get_number_at_position(text, line_nr-1, col):
                    part_numbers.append(x)
                else:
                    if x := get_number_at_position(text, line_nr-1, col-1):
                        part_numbers.append(x)
                    if x := get_number_at_position(text, line_nr-1, col+1):
                        part_numbers.append(x)
            if line_nr < len(text)-1:
                if x := get_number_at_position(text, line_nr+1, col):
                    part_numbers.append(x)
                else:
                    if x := get_number_at_position(text, line_nr+1, col-1):
                        part_numbers.append(x)
                    if x := get_number_at_position(text, line_nr+1, col+1):
                        part_numbers.append(x)
            if col < len(line) - 1 and (x := get_number_at_position(text, line_nr, col+1)):
                part_numbers.append(x)
            if col > 0 and (x := get_number_at_position(text, line_nr, col-1)):
                part_numbers.append(x)
            schematic[(line_nr, col, char)] = part_numbers
    return schematic


def get_number_at_position(text, line, col):
    left_side = "".join(
        takewhile(lambda char: char.isdigit(), text[line][col::-1]))
    right_side = "".join(
        takewhile(lambda char: char.isdigit(), text[line][col:]))
    if left_side and right_side:
        return int(left_side[::-1]+right_side[1:]), (line, col - len(left_side) + 1)
    return None


def get_without_duplicate_pos(values: Iterable[Tuple[int, Tuple[int, int]]]):
    positions = set()
    for x, pos in values:
        if pos not in positions:
            positions.add(pos)
            yield x


with open(input_file) as f:
    lines = f.read().splitlines()
total = process_time()
start = process_time()
schematic = create_schematic(lines)
print("Parsing:", process_time() - start)
start = process_time()
print(sum(get_without_duplicate_pos(chain(*schematic.values()))))
print("Part 1:", process_time() - start)
print("------------")
start = process_time()
print(sum(map(lambda kv_pair: prod(v for v, pos in kv_pair[1]), filter(
    lambda kv_pair: kv_pair[0][2] == "*" and len(kv_pair[1]) == 2, schematic.items()))))
print("Part 2", process_time() - start)
print("Total", process_time() - total)
