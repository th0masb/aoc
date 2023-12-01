import sys

with open(sys.argv[1]) as f:
    input = f.readlines()

choice_scores = { "X": 1, "Y": 2, "Z": 3 }
indices = { "A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2 }
outcome_scores = { "L": 0, "D": 3, "W": 6 }

def round_winner(theirs, ours):
    theirs = indices[theirs]
    ours = indices[ours]
    if theirs == ours:
        return "D"
    elif (theirs + 1) % 3 == ours:
        return "W"
    else:
        return "L"

def our_round_score(round):
    theirs, ours = round.strip().split(" ")
    return choice_scores[ours] + outcome_scores[round_winner(theirs, ours)]

print(sum(our_round_score(r) for r in input))

