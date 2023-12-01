from typing import Iterable, Dict, List
filename = "input.txt"


def solve1(lines: Iterable[str]) -> int:
    answer: int = 0
    for line in lines:
        line = line.strip()
        line = strip_non_ints(line)
        value: int = int(line[0]+line[-1])
        answer += value
    return answer


def solve2(lines: Iterable[str]) -> int:
    answer: int = 0
    for line in lines:
        line = line.strip()
        line = convert_digit_string_to_char(line)
        line = strip_non_ints(line)
        value: int = int(line[0]+line[-1])
        answer += value
    return answer


def strip_non_ints(string: str) -> str:
    answer = ""
    for i in range(len(string)):
        if ord("0") <= ord(string[i]) <= ord("9"):
            answer += string[i]
    return answer


def convert_digit_string_to_char(string: str) -> str:
    lookup_table: Dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"}
    result : List[str]= []
    for c in range(len(string)):
        for k, v in lookup_table.items():
            if string.startswith(k, c):
                result.append(v)
                break
        else:
            result.append( string[c])
    return "".join(result)


with open(filename, "r") as lines:
    print(solve2(lines))
