from grid import Grid
from priority import PriorityQueue


def parse_input():
    with open("input.txt") as f:
        lines = f.read().strip().splitlines()

    return Grid.from_input(lines, repeats=5)


def find_path(grid):
    frontier = PriorityQueue()
    came_from = {}
    cost_so_far = {}

    start = (0, 0)
    end = (grid.width - 1, grid.height - 1)

    frontier.add_task(start, priority=0)
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.pop_task()

        if current == end:
            break

        for n in grid.neighbours(*current):
            new_cost = cost_so_far[current] + grid.loc(*n)
            if not n in cost_so_far or new_cost < cost_so_far[n]:
                frontier.add_task(n, priority=new_cost)
                cost_so_far[n] = new_cost
                came_from[n] = current

    print(cost_so_far[end])


if __name__ == "__main__":
    grid = parse_input()
    find_path(grid)
