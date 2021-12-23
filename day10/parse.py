from dataclasses import dataclass


@dataclass
class InvalidLine:
    invalid_token: str


@dataclass
class IncompleteLine:
    completion: str


def parse(lines):
    invalids = []
    incompletes = []

    for line in lines:
        parsed = parse_line(line)

        if isinstance(parsed, InvalidLine):
            invalids.append(parsed)
        else:
            incompletes.append(parsed)

    return invalids, incompletes


def is_closer(char):
    return char in [")", "]", "}", ">"]


def is_opener(char):
    return char in ["(", "[", "{", "<"]


def closer_for(char):
    return {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }[char]


def get_completion(stack):
    return "".join(closer_for(c) for c in reversed(stack))


def parse_line(line):
    stack = []
    for c in line:
        if is_closer(c):
            top = stack.pop()
            if is_opener(top):
                expected = closer_for(top)

                if not expected == c:
                    return InvalidLine(invalid_token=c)
            else:
                return InvalidLine(invalid_token=c)
        else:
            stack.append(c)

    return IncompleteLine(completion=get_completion((stack)))
