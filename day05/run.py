import re
from collections import Counter
from dataclasses import dataclass
from typing import List


def run():
    descs = read_input("input.txt")
    counts = count_locations(descs)

    locs = locations_with_at_least_n_vents(counts, 2)

    print(f"ans: {len(locs)}")


INPUT_LINE_REGEX = "(\d+),(\d+) -> (\d+),(\d+)"


@dataclass
class VentDesc:
    x1: int
    y1: int
    x2: int
    y2: int

    @staticmethod
    def from_input_line(line: str):
        x1, y1, x2, y2 = re.match(INPUT_LINE_REGEX, line).groups()

        return VentDesc(
            x1=int(x1),
            y1=int(y1),
            x2=int(x2),
            y2=int(y2),
        )

    def locations(self):
        dx = delta(self.x1, self.x2)
        dy = delta(self.y1, self.y2)

        x, y = self.x1, self.y1
        points = [(x, y)]
        while not (x == self.x2 and y == self.y2):
            x, y = x + dx, y + dy
            points.append((x, y))

        return points


def delta(x1, x2):
    if x2 > x1:
        return 1
    elif x1 > x2:
        return -1
    else:
        return 0


def read_input(path: str):
    with open(path) as f:
        lines = f.read().splitlines()
    return [VentDesc.from_input_line(l) for l in lines]


def count_locations(descs: List[VentDesc]):
    counter = Counter()
    for desc in descs:
        counter.update(desc.locations())
    return counter


def locations_with_at_least_n_vents(counts, n):
    return [loc for loc, count in counts.items() if count >= n]


if __name__ == "__main__":
    run()
