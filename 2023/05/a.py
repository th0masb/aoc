#!/usr/bin/env python3

import sys
from pathlib import Path
import re

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

types = set([
    "seed", "soil", "fertilizer", "water",
    "light", "temperature", "humidity", "location"
])

def parse_map(lines: list[str]):
    header, contents = lines[0], lines[1:]
    type_union = "|".join(types)
    from_type, dest_type = re.findall(f"({type_union})-to-({type_union})", header)[0]
    mapping = {}
    for line in contents:
        dr, sr, size = list(map(int, re.fullmatch(r"(\d+) (\d+) (\d+)", line).groups()))
        mapping[(sr, sr + size - 1)] = dr - sr
    return (from_type, dest_type), mapping

def run_lookup(input, mapping):
    intype, inval = input
    types, values = mapping
    assert intype == types[0]
    for k, v in values.items():
        lo, hi = k
        if lo <= inval <= hi:
            return types[1], inval + v
    return types[1], inval

def run_lookups(input, output_type, mappings):
    result = input[1]
    while input[0] != output_type:
        m = mappings[input[0]]
        input = run_lookup(input, m)
        result = input[1]
    return result


seeds = [int(m) for m in re.findall(r"\d+", input[0])]

raw_maps = [[]]
for line in input[2:]:
    if line == "":
        raw_maps.append([])
    else:
        raw_maps[-1].append(line)

mappings = [parse_map(m) for m in raw_maps]
mappings = { m[0][0]: m for m in mappings }

print(min(run_lookups(("seed", seed), "location", mappings) for seed in seeds))
