#!/usr/bin/env python3
import sys
from pathlib import Path
import re
from math import prod

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

game_id = re.compile("Game (\d+):")
ball_count = re.compile("(\d+)\s+(red|green|blue)")

def parse_game(game: str):
    id = int(game_id.findall(game)[0])
    game = game.removeprefix(f"Game {id}:").strip()
    draws = [parse_draw(d) for d in game.split(";")]
    return id, draws

def parse_draw(draw: str):
    return { color[0]: int(count) for count, color in ball_count.findall(draw) }

def min_cube_set(game):
    return {
        c: max(d.get(c, 0) for d in game[1]) for c in ["r", "g", "b"]
    }

parsed_input = list(map(parse_game, input))
print(sum(prod(min_cube_set(game).values()) for game in parsed_input))
