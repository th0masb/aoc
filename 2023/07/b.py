#!/usr/bin/env python3

import sys
from pathlib import Path
from collections import Counter

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

with open(Path(sys.argv[0]).parent / "test.txt") as f:
    test_input = [line.strip() for line in f.readlines()]

hand_scores = {
    (1, 1, 1, 1, 1): 1,
    (1, 1, 1, 2): 2,
    (1, 2, 2): 3,
    (1, 1, 3): 4,
    (2, 3): 5,
    (1, 4): 6,
    (5,): 7
}

def compute_hand_score(hand):
    card_score = sum(compute_card_score(c) * (100**(5 - i)) for i, c in enumerate(hand))
    multiplicities = Counter(hand)
    wildcards = multiplicities.get('J', 0)
    del multiplicities['J']
    if len(multiplicities) == 0:
        multiplicities['A'] = wildcards
    else:
        largest_group = max(multiplicities.keys(), key=multiplicities.get)
        multiplicities[largest_group] += wildcards
    hand_score = hand_scores[tuple(sorted(multiplicities.values()))]
    return (10**10) * (10**hand_score) + card_score

def compute_card_score(card):
    letter_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
    return int(letter_map.get(card, card))

input.sort(key=lambda s: compute_hand_score(s.split(" ")[0]))
print(sum((i + 1) * int(s.split(" ")[1]) for i, s in enumerate(input)))
