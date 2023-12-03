#!/usr/bin/env python3

import sys
from pathlib import Path

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

def parse_input():
    files, cd = {}, []
    for line in input:
        if line == "$ ls" :
            pass
        elif line.startswith("$ cd "):
            line = line.removeprefix("$ cd ").strip()
            match line:
                case "/":
                    cd.clear()
                case "..":
                    cd.pop()
                case _:
                    cd.append(line)
        else:
            dir = files
            for p in cd:
                dir = dir[p]
            if line.startswith("dir"):
                name = line.split(" ")[1]
                dir.setdefault(name, {})
            else:
                size, name = line.split(" ")
                dir[name] = int(size)
    return files

def dir_size(dir):
    if isinstance(dir, int):
        return dir
    else:
        return sum(dir_size(v) for v in dir.values())

def get_directories(filesystem):
    if isinstance(filesystem, int):
        return []
    dirs = [[]]
    for k, v in filesystem.items():
        for d in get_directories(v):
            dirs.append([k] + d)
    return dirs

filesystem, result = parse_input(), 0
for path in get_directories(filesystem):
    dir = filesystem
    for p in path:
        dir = dir[p]
    size = dir_size(dir)
    if size <= 100000:
        result += size

print(result)

