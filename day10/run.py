from parse import parse
from scores import incomplete_scores, invalid_score

with open("input.txt") as f:
    lines = f.read().strip().splitlines()

invalids, incompletes = parse(lines)

q1 = invalid_score(invalids)
q2 = incomplete_scores(incompletes)

print(f"q1: {q1}")
print(f"q2: {q2}")
