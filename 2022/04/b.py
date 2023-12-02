#!/usr/bin/env python3

import sys
from pathlib import Path
import re

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

range_pattern = re.compile(r"(\d+)-(\d+)")

def parse_ranges(ranges: str):
    matches = range_pattern.findall(ranges)
    return [set(range(int(l), int(u) + 1)) for l, u in matches]

def is_overlapping(pair):
    left, right = pair
    return len(left & right) > 0

parsed_input = [parse_ranges(line) for line in input]
print(sum(1 for _ in filter(is_overlapping, parsed_input)))