

from itertools import accumulate, product
from typing import List, Tuple, NamedTuple
transition_lu = {
    "|": {(1, 0): (1, 0), (-1, 0): (-1, 0)},
    "-": {(0, 1): (0, 1), (0, -1): (0, -1)},
    "L": {(1, 0): (0, 1), (0, -1): (-1, 0)},
    "J": {(0, 1): (-1, 0), (1, 0): (0, -1)},
    "7": {(0, 1): (1, 0), (-1, 0): (0, -1)},
    "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},
}


def find_start(grid: List[List[str]]) -> Tuple[int, int]:
    for x, col in enumerate(grid):
        for y, v in enumerate(col):
            if v == "S":
                return x, y


input_file = "input.txt"

lines = open(input_file).readlines()
grid = [[x for x in y.strip()]for y in lines]
start = find_start(grid)


def traverse_pipes(grid, start):
    def find_start_direction():
        if 0 > start[0] and grid[start[0]-1][start[1]] in ["|", "F", "7"]:
            return (-1, 0)
        if start[0] <= len(grid) and grid[start[0]+1][start[1]] in ["|", "L", "J"]:
            return (1, 0)
        if 0 > start[1] and grid[start[0]][start[1]-1] in ["-", "F", "L"]:
            return (0, -1)
        if start[1] <= len(grid[start[0]]) and grid[start[0]][start[1]+1] in ["-", "J", "7"]:
            return (0, 1)

    direction = find_start_direction()
    yield *start, grid[start[0]][start[1]]
    x = start[0]+direction[0]
    y = start[1] + direction[1]
    while x != start[0] or y != start[1]:
        yield x, y, grid[x][y]
        direction = transition_lu[grid[x][y]][direction]
        x += direction[0]
        y += direction[1]


def calculate_enclosed_area(grid):
    total = 0
    for x, line in enumerate(grid):
        last = "."
        inside = False
        for y, v in enumerate(line):
            match last, v, inside:
                case ".", ".", _:
                    continue
                case _, ".", True:
                    print(x,y)
                    total += 1
                case ".", "|", False:
                    last = "|"
                    inside = True
                case ".", a, False:
                    last = a
                case _, "|", i:
                    last = "|"
                    inside = not i
                case "|", a, _:
                    last = a
                case "L", "J", _:
                    last = "J"
                case "F", "7", _:
                    last = "7"
                case "7", "F", _:
                    last = "F"
                case "J", "L", _:
                    last = "L"
                case "7", "L", i:
                    last = "L"
                case "J", "F", i:
                    last = "F"
                case "F", "J", i:
                    last = "J"
                    inside = not i
                case "L", "7", i:
                    inside = not i
                    last = "7"
            print(x,y,last,v, inside)
        
    return total


loop = list(traverse_pipes(grid, start))
print(len(loop)//2)
new_grid = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
for x, y, s in loop:
    new_grid[x][y] = s
print(calculate_enclosed_area(new_grid))
