#!/usr/bin/env python3

import sys
from pathlib import Path
from itertools import cycle
import re

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    real_input = [line.strip() for line in f.readlines()]

with open(Path(sys.argv[0]).parent / "test.txt") as f:
    test_input = [line.strip() for line in f.readlines()]

input = real_input

mapping = {}
for line in input[2:]:
    src, left, right = re.findall(r"[A-Z]{3}", line)
    mapping[src] = (left, right)

current = "AAA"
for i, dir in enumerate(cycle(input[0])):
    left, right = mapping[current]
    next_step = left if dir == 'L' else right
    if next_step == "ZZZ":
        print(i + 1)
        break
    else:
        current = next_step
