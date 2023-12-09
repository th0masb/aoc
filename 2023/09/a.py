#!/usr/bin/env python3

import sys
from pathlib import Path
import re

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    real_input = [line.strip() for line in f.readlines()]

with open(Path(sys.argv[0]).parent / "test.txt") as f:
    test_input = [line.strip() for line in f.readlines()]

input = real_input

def parse_sequence(line: str):
    sequences = [[int(d) for d in re.findall(r"-?\d+", line)]]
    last = sequences[-1]
    while any(l != 0 for l in last):
        next_level = []
        for i in range(len(last) - 1):
            next_level.append(last[i + 1] - last[i])
        sequences.append(next_level)
        last = next_level
    return sequences

def compute_next_value(sequences):
    v = 0
    n = len(sequences)
    for i in range(n - 1):
        v += sequences[-i - 2][-1]
    return v

print(sum(compute_next_value(parse_sequence(x)) for x in input))
