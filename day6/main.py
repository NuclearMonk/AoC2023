from math import ceil, floor, sqrt, prod


def get_solution_count(t, d):
    x = t*t - 4*d
    if x < 0:
        return 0
    if x == 0:
        return 1
    else:
        return ceil((t+sqrt(x))/2) - floor((t-sqrt(x))/2) - 1


input_file = "input.txt"
lines = open(input_file).readlines()
times, distances = ([int(x) for x in line.split(":")[1].split()]
                    for line in lines)
print(prod(get_solution_count(t, d) for t, d in zip(times, distances)))

time = int("".join(map(str, times)))
distance = int("".join(map(str, distances)))
print(get_solution_count(time, distance))
