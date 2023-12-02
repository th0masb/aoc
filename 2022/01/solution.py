import sys


def compute_highest_calories(lines):
    elves = []
    current = 0
    for line in lines:
        line = line.strip()
        if line == "":
            elves.append(current)
            current = 0
        else:
            current += int(line)
    elves.sort(reverse=True)
    return sum(elves[:3])


with open(sys.argv[1]) as f:
    print(compute_highest_calories(f.readlines()))
