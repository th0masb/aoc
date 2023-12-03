#!/usr/bin/env python3

import sys
from pathlib import Path
from itertools import chain
from functools import reduce
from operator import or_
import re

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

grid_rows = len(input)
grid_cols = len(input[0])
grid = "".join(input)
nbd_shifts = list(chain(
    range(-grid_cols - 1, -grid_cols + 2),
    [-1, 1],
    range(grid_cols - 1, grid_cols + 2)
))

def surrounding_chars(index) -> list[int]:
    def in_grid(index):
        return 0 <= index and index < len(grid)
    return set(str(grid[index + s]) for s in nbd_shifts if in_grid(index + s))

def is_part_nbd(nbd):
    numbers_and_period = set(map(str, range(0, 10))) | set(".")
    return len(nbd - numbers_and_period) > 0

digits = re.compile(r"\d+")

count = 0
for m in digits.finditer(grid):
    start, end = m.span()
    nbd = reduce(or_, map(surrounding_chars, range(start, end)))
    if is_part_nbd(nbd):
        count += int(grid[start:end])

print(count)
