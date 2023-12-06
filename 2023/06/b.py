#!/usr/bin/env python3

import sys
from pathlib import Path
import re
from math import ceil, sqrt, floor

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

def parse_races():
    time = int("".join(re.findall(r"\d+", input[0])))
    record = int("".join(re.findall(r"\d+", input[1])))
    return time, record

# (t - w) * w > r <=> w^2 - tw + r < 0
def compute_record_waits(race_time, record):
    a, b, c = 1, -race_time, record
    discrim = b**2 - 4 * a * c
    if discrim <= 0:
        return []
    else:
        w1 = ceil((-b - sqrt(discrim)) / (2 * a))
        w2 = floor((-b + sqrt(discrim)) / (2 * a))
        return max(0, w2 + 1 - w1)

print(compute_record_waits(*parse_races()))
