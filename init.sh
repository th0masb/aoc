#!/usr/bin/env bash

set -e

problem_dir="$(dirname "$0")/$1/$2"

mkdir -p "$problem_dir"

touch "$problem_dir/input.txt"
cat > "$problem_dir/a.py" << EOL
import sys

with open(sys.argv[1]) as f:
    input = [line.strip() for line in f.readlines()]

EOL
