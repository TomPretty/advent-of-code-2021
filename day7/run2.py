import statistics


def run():
    positions = read_input()
    fuel = find_min_total(positions)

    print(f"ans: {fuel}")


def read_input():
    with open("input.txt") as f:
        raw = f.read().strip()
    return [int(num) for num in raw.split(",")]


def find_min_total(positions):
    min_pos, max_pos = min(positions), max(positions)

    min_total = 10e12
    for i in range(min_pos, max_pos + 1):
        total = total_distance(positions, i)

        if total < min_total:
            min_total = total

    return min_total


def total_distance(positions, point):
    return sum(distance(p, point) for p in positions)


def distance(p1, p2):
    d = abs(p1 - p2)

    if d % 2 == 0:
        return (1 + d) * (d // 2)
    else:
        return (1 + d) * (d // 2) + (d + 1) // 2


if __name__ == "__main__":
    run()
