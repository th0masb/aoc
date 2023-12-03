#!/usr/bin/env python3

import sys
from pathlib import Path
from itertools import chain
from functools import reduce
from operator import or_
from math import prod
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

def neighbourhood(index):
    def in_grid(index):
        return 0 <= index and index < len(grid)
    indices = [index + s for s in nbd_shifts if in_grid(index + s)]
    return set([(str(grid[i]), i) for i in indices])

adjacencies = {}
for m in re.finditer(r"\d+", grid):
    start, end = m.span()
    nbd = reduce(or_, map(neighbourhood, range(start, end)))
    for c, i in nbd:
        if c == "*":
            adjacencies.setdefault(i, []).append(int(grid[start:end]))

print(sum(prod(v) for v in adjacencies.values() if len(v) == 2))
