#!/usr/bin/env python3

import sys
from pathlib import Path
import re
from itertools import batched

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

def is_empty(range):
    return range[1] < range[0]

def range_size(range):
    return max(0, 1 + range[1] - range[0])

# Closed ranges
def from_range_delete_range(range, to_delete):
    r0, r1 = range
    d0, d1 = to_delete
    deleted = (max(d0, r0), min(d1, r1))
    remaining = [(r0, deleted[0] - 1), (deleted[1] + 1, r1)]
    deleted = None if is_empty(deleted) else deleted
    return deleted, [r for r in remaining if not is_empty(r)]

def run_lookup(input, mapping):
    intype, inranges = input
    assert len(inranges) > 0
    types, values = mapping
    assert intype == types[0]
    input, output = list(inranges), []
    repeat = True
    while repeat:
        repeat = False
        for range, shift in values.items():
            if repeat:
                break
            for i in list(input):
                deleted, remaining = from_range_delete_range(i, range)
                if deleted is not None:
                    input.remove(i)
                    output.append((deleted[0] + shift, deleted[1] + shift))
                    input.extend(remaining)
                    repeat = True
                    break

    # Some ranges will not have been shifted
    output.extend(input)
    assert sum(map(range_size, output)) == sum(map(range_size, inranges))
    return types[1], output

def run_lookups(input, output_type, mappings):
    while input[0] != output_type:
        input = run_lookup(input, mappings[input[0]])
    return input


seeds = [(int(m), int(m) + int(s) - 1) for m, s in batched(re.findall(r"\d+", input[0]), 2)]
raw_maps = [[]]
for line in input[2:]:
    raw_maps.append([]) if line == "" else raw_maps[-1].append(line)

mappings = [parse_map(m) for m in raw_maps]
mappings = { m[0][0]: m for m in mappings }
mapped_seeds = run_lookups(("seed", seeds), "location", mappings)
print(min(r[0] for r in mapped_seeds[1]))
