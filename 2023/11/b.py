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

def compute_empties(input: Galaxy):
    rows, cols = set(), set()
    for i in range(input.rows):
        if all(c == "." for c in get_row(input, i)):
            rows.add(i)
    for i in range(input.cols):
        if all(c == "." for c in get_col(input, i)):
            cols.add(i)
    return (rows, cols)
    
def distance(coord_pair, empties):
    empty_rows, empty_cols = empties
    a, b = tuple(coord_pair)
    a0, a1 = a[0], a[1]
    b0, b1 = b[0], b[1]
    rows_traversed = list(range(min(a0, b0) + 1, max(a0, b0)))
    cols_traversed = list(range(min(a1, b1) + 1, max(a1, b1)))
    empties = sum(1 for r in rows_traversed if r in empty_rows) \
        + sum(1 for c in cols_traversed if c in empty_cols)
    others = abs(a0 - b0) + abs(a1 - b1) - empties
    return others + empties * 1_000_000

empties = compute_empties(input)
coords = list(product(range(input.rows), range(input.cols)))
hashes = [(r, c) for r, c in coords if input.grid[r][c] == "#"]
pairs = frozenset(frozenset(p) for p in permutations(hashes, 2))
print(sum(distance(p, empties) for p in pairs))
