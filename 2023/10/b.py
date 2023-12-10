#!/usr/bin/env python3

import sys
from pathlib import Path
from collections import namedtuple
from itertools import product

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    real_input = [line.strip() for line in f.readlines()]

with open(Path(sys.argv[0]).parent / "test.txt") as f:
    test_input = [line.strip() for line in f.readlines()]

input = real_input
rows = len(input)
cols = len(input[0])

Coord = namedtuple("Coord", "r c")

def find_start_coord():
    for i, line in enumerate(input):
        if "S" in line:
            return Coord(r=i, c=line.index("S"))
    raise AssertionError

def in_range(c: Coord):
    return 0 <= c.r < rows and 0 <= c.c < cols

def index(coord: Coord):
    return input[coord.r][coord.c]

shifts = {
    "n": (-1, 0),
    "e": (0, 1),
    "s": (1, 0),
    "w": (0, -1)
}

pipes = {
    "|": {"n", "s"}, 
    "-": {"w", "e"}, 
    "L": {"n", "e"}, 
    "J": {"n", "w"},
    "7": {"s", "w"},
    "F": {"s", "e"},
}

dir_invert = {
    "n": "s", 
    "e": "w", 
    "s": "n", 
    "w": "e",
}

left_right_turns = {
    ("n", "e"): (0, 1),
    ("n", "w"): (1, 0),
    ("e", "s"): (0, 1),
    ("e", "n"): (1, 0),
    ("s", "w"): (0, 1),
    ("s", "e"): (1, 0),
    ("w", "n"): (0, 1),
    ("w", "s"): (1, 0),
}

turn_results = {
    ("n", "L"): "w",
    ("n", "R"): "e",
    ("e", "L"): "n",
    ("e", "R"): "s",
    ("s", "L"): "e",
    ("s", "R"): "w",
    ("w", "L"): "s",
    ("w", "R"): "n",
}


def move(start: Coord, dir: str):
    r, c = shifts[dir]
    return Coord(start.r + r, start.c + c)


def find_start_pipe(start: Coord):
    def pipe_matches(dir):
        next = move(start, dir)
        if not in_range(next):
            return False
        return dir_invert[dir] in pipes.get(input[next.r][next.c], {})

    fitting = []
    for pipe, dirs in pipes.items():
        if all(pipe_matches(d) for d in dirs):
            fitting.append(pipe)
    assert len(fitting) == 1
    return fitting[0]

def compute_exit_dir(coord, entry_dir):
    dirs = pipes[index(coord)]
    return next(iter(dirs - {dir_invert[entry_dir]}))

def compute_oriented_loop(start, dir):
    lefts, rights = 0, 0
    exit_dir = dir
    curr_coord = start
    loop = []
    while len(loop) == 0 or curr_coord != loop[0]:
        loop.append(curr_coord)
        curr_coord = move(curr_coord, exit_dir)
        next_dir = compute_exit_dir(curr_coord, exit_dir)
        if next_dir != exit_dir:
            turn_left, turn_right = left_right_turns[(exit_dir, next_dir)]
            lefts += turn_left
            rights += turn_right
        exit_dir = next_dir
    assert lefts != rights
    orientation = "L" if lefts > rights else "R"
    oriented_loop = {}
    entry_dir = dir
    for coord in loop[1:] + loop[:1]:
        exit_dir = compute_exit_dir(coord, entry_dir)
        dirs = [entry_dir, exit_dir]
        oriented_loop[coord] = set(turn_results[(d, orientation)] for d in dirs)
        entry_dir = exit_dir
    return oriented_loop

def is_enclosed_tile(loop, coord):
    if coord in loop.keys():
        return False
    bounds = [find_loop_bound(loop, coord, d) for d in shifts.keys()]
    return all(b is not None for b in bounds) \
        and all(any(xrays(b, d, coord) for d in loop[b]) for b in bounds)

def find_loop_bound(loop, coord, dir):
    while in_range(coord):
        if coord in loop.keys():
            return coord
        else:
            coord = move(coord, dir)
    return None

def xrays(start, dir, target):
    assert start != target
    while in_range(start):
        if start == target:
            return True
        else:
            start = move(start, dir)
    return False

start = find_start_coord()
start_pipe = find_start_pipe(start)
input[start.r] = input[start.r].replace("S", start_pipe)
dir = min(pipes[index(start)])
loop = compute_oriented_loop(start, dir)
coords = (Coord(r, c) for r, c in product(range(rows), range(cols)))
enclosed = [c for c in coords if is_enclosed_tile(loop, c)]
print(len(enclosed))
