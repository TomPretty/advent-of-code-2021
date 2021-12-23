import statistics


def invalid_token_score(token):
    return {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }[token]


def invalid_score(lines):
    return sum(invalid_token_score(l.invalid_token) for l in lines)


def incomplete_token_score(token):
    return {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }[token]


def incomplete_line_score(line):
    score = 0
    for token in line.completion:
        score *= 5
        score += incomplete_token_score(token)
    return score


def incomplete_scores(lines):
    scores = [incomplete_line_score(l) for l in lines]

    return int(statistics.median(scores))
