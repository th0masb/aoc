#!/usr/bin/env python3

import sys
from pathlib import Path
import re

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

digit = re.compile(r"\d+")

def parse_initial_stacks():
    divider = next(i for i, line in enumerate(input) if line == "")
    num_stacks = sum(1 for _ in digit.findall(input[divider - 1]))
    stacks = [[] for _ in range(num_stacks)]
    for line in reversed(input[:divider - 1]):
        for i, c in enumerate(line[1:len(line):4]):
            if c != " ":
                stacks[i].append(c)
    return stacks

def move(count, source, dest):
    dest += source[-count:]
    del source[-count:]

stacks = parse_initial_stacks()
instruction_pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")

for line in input:
    for instruction in instruction_pattern.findall(line):
        count, source, dest = list(map(int, instruction))
        move(count, stacks[source - 1], stacks[dest - 1])

print("".join(stack[-1] for stack in stacks))

