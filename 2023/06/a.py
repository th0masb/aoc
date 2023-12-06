#!/usr/bin/env python3

import sys
from pathlib import Path
import re
from math import ceil, sqrt, floor, prod

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

def parse_races():
    times = map(int, re.findall(r"\d+", input[0]))
    records = map(int, re.findall(r"\d+", input[1]))
    return list(zip(times, records))

input = parse_races()

# t * w - w^2 > r <=> w^2 - tw + r < 0
def compute_record_waits(race_time, record):
    a, b, c = 1, -race_time, record
    discrim = b**2 - 4 * a * c
    if discrim <= 0:
        return []
    else:
        w1 = ceil((-b - sqrt(discrim)) / (2 * a))
        w2 = floor((-b + sqrt(discrim)) / (2 * a))
        return list(range(w1, w2 + 1))

print(prod(len(compute_record_waits(t, r)) for t, r in input))
