import sys
from collections import Counter

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f.readlines()]

def get_priority_map():
    lower = [chr(n) for n in range(ord("a"), ord("z") + 1)]
    upper = [chr(n) for n in range(ord("A"), ord("Z") + 1)]
    return { str(c): i + 1 for i, c in enumerate(lower + upper) }

def get_common_item(rucksack: str):
    mid = int(len(rucksack) / 2)
    return next(iter(set(rucksack[:mid]) & set(rucksack[mid:])))

priorities = get_priority_map()
print(sum(priorities[get_common_item(r)] for r in input))
