#!/usr/bin/env python3

import sys
from pathlib import Path

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

input = input[0]
for i in range(3, len(input)):
    if len(set(input[i-3:i+1])) == 4:
        print(i + 1)
        break
