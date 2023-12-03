#!/usr/bin/env python3

import sys
from pathlib import Path

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

size = len(input)

def row(i):
    return list(map(int, input[i]))

def column(i):
    return [int(input[j][i]) for j in range(size)]

def compute_dir_score(trees, accumulate_fn):
    for i, source in enumerate(trees):
        distance = 0
        for tree in trees[i+1:]:
            distance += 1
            if tree >= source:
                break
        accumulate_fn(i, distance)

scores = [[1] * size for _ in range(size)]

def prod_score(i, j, n):
    scores[i][j] *= n

for i in range(size):
    r = row(i)
    compute_dir_score(r, lambda j, n: prod_score(i, j, n))
    compute_dir_score(r[::-1], lambda j, n: prod_score(i, size - j - 1, n))
    c = column(i)
    compute_dir_score(c, lambda j, n: prod_score(j, i, n))
    compute_dir_score(c[::-1], lambda j, n: prod_score(size - j - 1, i, n))

print(max(max(row) for row in scores))