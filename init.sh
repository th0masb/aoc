#!/usr/bin/env bash

set -e

problem_dir="$(dirname "$0")/$1/$2"

mkdir -p "$problem_dir"

touch "$problem_dir/input.txt"
cat > "$problem_dir/a.py" << EOL
#!/usr/bin/env python3

import sys
from pathlib import Path

with open(Path(sys.argv[0]).parent / "input.txt") as f:
    input = [line.strip() for line in f.readlines()]

with open(Path(sys.argv[0]).parent / "test.txt") as f:
    test_input = [line.strip() for line in f.readlines()]

EOL
chmod +x "$problem_dir/a.py"
