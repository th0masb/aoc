#!/usr/bin/env python3

import sys
from pathlib import Path
import re
from itertools import cycle
from math import lcm

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    real_input = [line.strip() for line in f.readlines()]

with open(Path(sys.argv[0]).parent / "test.txt") as f:
    test_input = [line.strip() for line in f.readlines()]

input = real_input

mapping = {}
for line in input[2:]:
    src, left, right = re.findall(r"[A-Z0-9]{3}", line)
    mapping[src] = (left, right)

def compute_loop_size(start):
    current = start
    for i, dir in enumerate(cycle(input[0])):
        left, right = mapping[current]
        next_step = left if dir == 'L' else right
        if next_step[-1] == "Z":
            return int((i + 1) / len(input[0]))
        else:
            current = next_step

starts = [k for k in mapping.keys() if k[-1] == 'A']
print(lcm(*[compute_loop_size(s) for s in starts]) * len(input[0]))
