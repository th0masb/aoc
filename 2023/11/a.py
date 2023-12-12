#!/usr/bin/env python3

import sys
from pathlib import Path
from itertools import product, permutations
from collections import namedtuple

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    real_input = [line.strip() for line in f.readlines()]

with open(Path(sys.argv[0]).parent / "test.txt") as f:
    test_input = [line.strip() for line in f.readlines()]

input = real_input

Galaxy = namedtuple("Galaxy", "grid rows cols")

input = Galaxy(
    grid=[list(line) for line in input],
    rows=len(input),
    cols=len(input[0])
)

def get_row(g: Galaxy, n):
    return g.grid[n]

def get_col(g: Galaxy, n):
    return [g.grid[i][n] for i in range(g.cols)]

def expand_space(input: Galaxy) -> Galaxy:
    next_grid = list(input.grid)
    for i in range(input.rows - 1, -1, -1):
        if all(c == "." for c in get_row(input, i)):
            next_grid.insert(i + 1, ["."] * input.cols)
    for i in range(input.cols - 1, -1, -1):
        if all(c == "." for c in get_col(input, i)):
            for row in next_grid:
                row.insert(i + 1, ".")
    return Galaxy(grid=next_grid, rows=len(next_grid), cols=len(next_grid[0]))
    
def distance(pair):
    a, b = tuple(pair)
    a0, a1 = a[0], a[1]
    b0, b1 = b[0], b[1]
    return abs(b0 - a0) + abs(b1 - a1)

input = expand_space(input)

coords = list(product(range(input.rows), range(input.cols)))
hashes = [(r, c) for r, c in coords if input.grid[r][c] == "#"]
pairs = frozenset(frozenset(p) for p in permutations(hashes, 2))
print(sum(distance(p) for p in pairs))

