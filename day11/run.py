from queue import Queue


def read_input():
    with open("input.txt") as f:
        lines = f.read().strip().splitlines()
    return lines


class Grid:
    def __init__(self, items):
        self.items = items

    @staticmethod
    def from_input(lines):
        items = [[int(c) for c in l] for l in lines]

        return Grid(items)

    def loc(self, i, j):
        return self.items[i][j]

    def set_loc(self, i, j, x):
        self.items[i][j] = x

    def neighbours(self, i, j):
        potential = [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1),
        ]
        ns = []
        for ni, nj in potential:
            if ni >= 0 and ni < self.height and nj >= 0 and nj < self.width:
                ns.append((ni, nj))
        return ns

    def print_items(self):
        for row in self.items:
            for col in row:
                print(col, end=" ")
            print("")
        print("")

    @property
    def height(self):
        return len(self.items)

    @property
    def width(self):
        return len(self.items[0])


def increment(grid):
    for i in range(grid.height):
        for j in range(grid.width):
            grid.set_loc(i, j, grid.loc(i, j) + 1)


def flash(grid):
    flashed = set()
    q = Queue()

    for i in range(grid.height):
        for j in range(grid.width):
            if grid.loc(i, j) > 9:
                q.put((i, j))
                flashed.add((i, j))

    while not q.empty():
        flasher = q.get()

        for n in grid.neighbours(*flasher):
            energy = grid.loc(*n)
            energy += 1
            grid.set_loc(*n, energy)

            if energy > 9 and not n in flashed:
                q.put(n)
                flashed.add(n)

    return len(flashed)


def reset(grid):
    for i in range(grid.height):
        for j in range(grid.width):
            if grid.loc(i, j) > 9:
                grid.set_loc(i, j, 0)


def step(grid):
    increment(grid)
    num_flashes = flash(grid)
    reset(grid)

    return num_flashes


def q1():
    lines = read_input()
    grid = Grid.from_input(lines)

    num_flashes = 0
    for _ in range(100):
        num_flashes += step(grid)

    print(f"ans: {num_flashes}")


def q2():
    lines = read_input()
    grid = Grid.from_input(lines)

    num_steps = 0
    while True:
        num_steps += 1
        num_flashes = step(grid)

        if num_flashes >= 100:
            break

    print(f"ans: {num_steps}")


if __name__ == "__main__":
    q1()
    q2()
