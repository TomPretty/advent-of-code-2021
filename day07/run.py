import statistics


def run():
    positions = read_input()
    median = int(statistics.median(positions))
    fuel = total_distance(positions, median)

    print(f"ans: {fuel}")


def read_input():
    with open("input.txt") as f:
        raw = f.read().strip()
    return [int(num) for num in raw.split(",")]


def total_distance(positions, point):
    return sum(abs(pos - point) for pos in positions)


def total_distance2(positions, point):
    pass


def distance(p1, p2):
    d = abs(p1 - p2)

    if d % 2 == 0:
        return (1 + d) * (d // 2)
    else:
        return (1 + d) * (d // 2) + (d + 1) // 2
