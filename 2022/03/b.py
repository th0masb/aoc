#!/usr/bin/env python3
import sys
from pathlib import Path
from operator import and_
from itertools import batched
from functools import reduce

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]


def get_priority_map():
    lower = [chr(n) for n in range(ord("a"), ord("z") + 1)]
    upper = [chr(n) for n in range(ord("A"), ord("Z") + 1)]
    return { str(c): i + 1 for i, c in enumerate(lower + upper) }

def get_badge(bags: list[str]):
    return reduce(and_, map(set, bags)).pop()

priorities = get_priority_map()
print(sum(priorities[get_badge(b)] for b in batched(input, 3)))
