import sys
import re

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f.readlines()]

game_id = re.compile("Game (\d+):")
ball_count = re.compile("(\d+)\s+(red|green|blue)")
max_counts = { "r": 12, "g": 13, "b": 14 }

def parse_game(game: str):
    id = int(game_id.findall(game)[0])
    game = game.removeprefix(f"Game {id}:").strip()
    draws = [parse_draw(d) for d in game.split(";")]
    return id, draws

def parse_draw(draw: str):
    return { color[0]: int(count) for count, color in ball_count.findall(draw) }

def is_valid(game):
    draws = game[1]
    return all(all(d.get(k, 0) <= v for k, v in max_counts.items()) for d in draws)


parsed_input = list(map(parse_game, input))
print(sum(g[0] for g in parsed_input if is_valid(g)))
