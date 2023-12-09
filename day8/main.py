from itertools import cycle, takewhile
from math import lcm, prod
from re import findall
from typing import Dict, Tuple


def parse_input(lines):
    instructions = lines[0].strip()
    map: Dict[str, Tuple[str, str]] = {}
    for line in lines[2:]:
        key, left, right = findall(r"\w+", line)
        map[key] = (left, right)
    return instructions, map


def traverse_map(instructions: str, map: Dict[str, Tuple[str, str]], start="AAA"):
    current = start
    for index, direction in cycle(enumerate(instructions)):
        match direction:
            case "L":
                current = map[current][0]
            case "R":
                current = map[current][1]
        yield current, index


input_file = "input.txt"
lines = open(input_file).readlines()

instructions, map_info = parse_input(lines)

# print(len(list(takewhile(lambda location : location != "ZZZ",traverse_map(instructions, map_info))))+1)

start_points = list(filter(lambda x: x[-1] == "A", map_info))
generators = [traverse_map(instructions, map_info, start_point) for start_point in start_points]
# loop_lengths = []
# for generator in generators[:2]:
#     visited = set()
#     for i, x in enumerate(generator):
#         if x[0][-1] == "Z": first = i
#         if x in visited: 
#             print(first)
#             loop_lengths.append(len(visited))
#             loop_offset= len(visited) - x[1] - first
#             break
#         visited.add(x)
# print(loop_lengths)
# print(lcm(*loop_lengths))
loop_lengths = []
for generator in generators:
    visited = set()
    for i, x in enumerate(generator):
        if x[0][-1] == "Z": first = i
        if x in visited: 
            print(first)
            loop_lengths.append(len(visited))
            loop_offset= len(visited) - x[1] - first
            break
        visited.add(x)
print(loop_lengths)
z = lcm(*loop_lengths)
print(z)

loop_lengths = []
for generator in generators:
    visited = set()
    for i, x in enumerate(generator):
        if x[0][-1] == "Z": first = i
        if x in visited: 
            print(first)
            loop_lengths.append(len(visited))
            loop_offset= len(visited) - x[1] - first
            break
        visited.add(x)
print(loop_lengths)
z = lcm(*loop_lengths)
print(z)
