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

def winner_count(card):
    return len(card[1] & card[2])

cards = [parse(line) for line in input]
card_counts = { id: 1 for id, _, _ in cards }
for i, card in enumerate(cards):
    count = card_counts[card[0]]
    winners = winner_count(card)
    for j in range(i, i + winners):
        card_counts[cards[j+1][0]] += count

print(sum(card_counts.values()))


