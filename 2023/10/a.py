#!/usr/bin/env python3

import sys
from pathlib import Path
from collections import namedtuple

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    real_input = [line.strip() for line in f.readlines()]

with open(Path(sys.argv[0]).parent / "test.txt") as f:
    test_input = [line.strip() for line in f.readlines()]

input = real_input
size = len(input)
assert all(len(x) == size for x in input)

Coord = namedtuple("Coord", "r c")

def find_start_coord():
    for i, line in enumerate(input):
        if "S" in line:
            return Coord(r=i, c=line.index("S"))
    raise AssertionError

def in_range(c: Coord):
    return 0 <= c.r < size and 0 <= c.c < size

shifts = {
    "n": (-1, 0),
    "e": (0, 1),
    "s": (1, 0),
    "w": (0, -1)
}

def move(start: Coord, dir: str):
    r, c = shifts[dir]
    return Coord(start.r + r, start.c + c)

pipes = {
    "|": {"n", "s"}, 
    "-": {"w", "e"}, 
    "L": {"n", "e"}, 
    "J": {"n", "w"},
    "7": {"s", "w"},
    "F": {"s", "e"},
}

def find_pipe_continuation(c: Coord):
    return frozenset(move(c, d) for d in pipes[input[c.r][c.c]])

dir_invert = {"n": "s", "e": "w", "s": "n", "w": "e"}

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

def compute_loop_steps(start, next_coord):
    steps = {start: 0}
    step_count = 1
    last_coord = start
    while next_coord != start:
        steps[next_coord] = step_count
        step_count += 1
        continuation = find_pipe_continuation(next_coord)
        continuation = continuation - {last_coord}
        last_coord = next_coord
        next_coord = next(iter(continuation))
    return steps

start = find_start_coord()
start_pipe = find_start_pipe(start)
input[start.r] = input[start.r].replace("S", start_pipe)
dirs = find_pipe_continuation(start)
steps = [compute_loop_steps(start, d) for d in dirs]
loop_coords = steps[0].keys()
max_distance = max(min(step[k] for step in steps) for k in loop_coords)
print(max_distance)