#!/usr/bin/env python3

import sys
from pathlib import Path

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

input = input[0]
marker_size = 14
for i in range(marker_size - 1, len(input)):
    if len(set(input[i-marker_size+1:i+1])) == marker_size:
        print(i + 1)
        break
