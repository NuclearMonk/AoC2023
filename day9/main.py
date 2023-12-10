from typing import List
from itertools import pairwise

input_file = "test.txt"

lines = open(input_file).readlines()


def create_tree(history: List[int]) -> List[List[int]]:
    next_row: List[int] = history
    tree: List[List[int]] = []
    while any(next_row):
        tree.append(next_row)
        next_row = [y-x for x,y in pairwise(next_row)]
    return tree

def predict(tree):
    return sum(row[-1] for row in tree[::-1])

def regress(tree):
    acc :int = 0
    for row in tree[::-1]:
        acc = row[0] - acc
    return acc

histories: List[List[int]] = [[int(x) for x in line.split()] for line in lines]
trees = [create_tree(history) for history in histories]
print(sum(predict(tree) for tree in trees))
print(sum(regress(tree) for tree in trees))
    