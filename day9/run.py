from queue import Queue

with open("input.txt") as f:
    lines = f.read().strip().splitlines()


class Grid:
    def __init__(self, items):
        self.items = items

    @staticmethod
    def from_input(lines):
        items = [[int(c) for c in l] for l in lines]

        return Grid(items)

    def loc(self, i, j):
        return self.items[i][j]

    def neighbours(self, i, j):
        ns = []
        if i > 0:
            ns.append((i - 1, j))
        if i < self.height - 1:
            ns.append((i + 1, j))
        if j > 0:
            ns.append((i, j - 1))
        if j < self.width - 1:
            ns.append((i, j + 1))
        return ns

    @property
    def height(self):
        return len(self.items)

    @property
    def width(self):
        return len(self.items[0])


grid = Grid.from_input(lines)


def get_minima(grid):
    def is_minima(i, j):
        for n in grid.neighbours(i, j):
            if grid.loc(*n) < grid.loc(i, j):
                return False
        return True

    minima = []
    for i in range(grid.height):
        for j in range(grid.width):
            if is_minima(i, j):
                minima.append((i, j))

    return minima


def get_risk_level(minima, grid):
    return sum(grid.loc(*m) + 1 for m in minima)


def get_basin(start, grid):
    frontier = Queue()
    frontier.put(start)
    visited = {start}

    while not frontier.empty():
        current = frontier.get()
        for n in grid.neighbours(*current):
            if grid.loc(*n) < 9 and not n in visited:
                frontier.put(n)
                visited.add(n)

    return visited


minima = get_minima(grid)

risk_level = get_risk_level(minima, grid)

print(f"q1: {risk_level}")

basins = [get_basin(m, grid) for m in minima]
sizes = [len(b) for b in basins]

first, second, third = sorted(sizes, reverse=True)[:3]

print(f"q2: {first * second * third}")
