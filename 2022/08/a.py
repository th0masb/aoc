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

def compute_visible(trees, set_visible):
    prev_max = -1
    for i, tree in enumerate(trees):
        if prev_max < tree:
            set_visible(i)
            prev_max = tree

visible = [[False] * size for _ in range(size)]

def set_visible(i, j):
    visible[i][j] = True

for i in range(size):
    r = row(i)
    compute_visible(r, lambda j: set_visible(i, j))
    compute_visible(reversed(r), lambda j: set_visible(i, size - j - 1))
    c = column(i)
    compute_visible(c, lambda j: set_visible(j, i))
    compute_visible(reversed(c), lambda j: set_visible(size - j - 1, i))

print(sum(sum(1 for b in row if b) for row in visible))
