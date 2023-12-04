#!/usr/bin/env python3

import sys
from pathlib import Path
import re

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

def parse(card: str):
    id, contents = card.split(":")
    id = int(id.removeprefix("Card").strip())
    winners, ours = contents.split("|")
    winners = set(int(m) for m in re.findall(r"\d+", winners))
    ours = set(int(m) for m in re.findall(r"\d+", ours))
    return id, winners, ours

def points(card):
    _, winners, ours = card
    common = len(winners & ours)
    return 0 if common == 0 else 2**(common - 1)

print(sum(points(parse(line)) for line in input))