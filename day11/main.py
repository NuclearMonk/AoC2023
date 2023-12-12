from itertools import combinations
input_file = "input.txt"


def parse_file(file):
    vertical = set()
    horizontal = set()
    galaxies = []
    for x, line in enumerate(file.readlines()):
        for y, c in enumerate(line):
            if c == "#":
                galaxies.append((x, y))
                horizontal.add(x)
                vertical.add(y)

    return galaxies, vertical, horizontal

def galaxy_distance(a,b,vertical, horizontal, expansion_factor =2):
    ax,ay = a
    bx,by = b
    distance = abs(ax-bx) + abs(ay-by)
    for x in range(min(ax,bx), max(ax,bx)):
        if x not in horizontal:
            distance += expansion_factor -1
    for y in range(min(ay,by), max(ay,by)):
        if y not in vertical:
            distance += expansion_factor -1
    return distance

galaxies, vertical, horizontal = parse_file(open(input_file))
print(sum(galaxy_distance(a,b,vertical,horizontal) for a,b in combinations(galaxies, r=2)))
print(sum(galaxy_distance(a,b,vertical,horizontal, expansion_factor=1000000) for a,b in combinations(galaxies, r=2)))
# print(*combinations(galaxies, 2))
