import sys

with open(sys.argv[1]) as f:
    input = f.readlines()

indices = { "A": 0, "B": 1, "C": 2 }
outcome_scores = { "X": 0, "Y": 3, "Z": 6 }

def choose_shape(theirs, outcome):
    for i in range(0, 3):
        ours = (theirs + i) % 3
        if round_outcome(theirs, ours) == outcome:
            return ours
    raise Exception(f"{theirs} {outcome}")

def round_outcome(theirs, ours):
    if theirs == ours:
        return "Y"
    elif (theirs + 1) % 3 == ours:
        return "Z"
    else:
        return "X"

def our_round_score(round):
    theirs, outcome = round.strip().split(" ")
    theirs = indices[theirs]
    ours = choose_shape(theirs, outcome)
    return (ours + 1) + outcome_scores[outcome]

print(sum(our_round_score(round) for round in input))
