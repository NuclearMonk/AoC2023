from typing import Iterable, List, Tuple
from itertools import batched, product


def map_value(v: int, m: List[Tuple[int, int, int]]) -> int:
    for destination_start, start, end in m:
        if start <= v <= end:
            return destination_start + (v - start)
    return v


def map_range(r: Tuple[int, int], m: List[Tuple[int, int, int]]):
    r_start, r_end = r
    for dest, m_start, m_end in m:
        # print(r, m_start, m_end)
        if m_start <= r_start <= m_end:
            if m_start <= r_end <= m_end:  # if both of them are inside we can return
                return [(r_start - m_start + dest, r_end - m_start + dest)]
            else:  # the end is outside the range
                # recursively get the right side leftovers
                right_side = map_range((m_end+1, r_end), m)
                return [(r_start - m_start + dest, m_end - m_start + dest), *right_side]
        # it starts outside of the current range but ends inside
        elif r_start <= m_start and m_start <= r_end <= m_end:
            # recursively get the left side leftovers
            left_side = map_range((r_start, m_start-1), m)
            return [*left_side, (dest, r_end - m_start + dest)]
        elif r_start <= m_start and m_end <= r_end:  # the range has excesses on both sides
            left_side = map_range((r_start, m_start-1), m)
            right_side = map_range((m_end+1, r_end), m)
            return [*left_side, (dest, m_end - m_start + dest), *right_side]
    return [r]


def parse_map(lines: str) -> List[Tuple[int, int, int]]:
    return [(int(dest), int(start), int(start) + int(length)-1) for dest, start, length in (line.split() for line in lines.split("\n")[1:])]


input_file = "input.txt"
text = open(input_file).read()
maps = text.split("\n\n")
values = [int(x) for x in maps[0].split(":")[1].split()]
ranges = [(x, x+y-1) for x, y in batched(values, 2)]
maps = [parse_map(x) for x in maps[1:]]

for map, i in product(maps, range(len(values))):
    values[i] = map_value(values[i], map)
print(min(values))
for m in maps:

    new_ranges = []
    for r in ranges:
        new_ranges.extend(map_range(r, m))
    ranges = new_ranges
print(sorted(ranges)[0][0])
