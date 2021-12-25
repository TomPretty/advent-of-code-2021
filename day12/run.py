from collections import defaultdict

layout = [
    "start-kc",
    "pd-NV",
    "start-zw",
    "UI-pd",
    "HK-end",
    "UI-kc",
    "pd-ih",
    "ih-end",
    "start-UI",
    "kc-zw",
    "end-ks",
    "MF-mq",
    "HK-zw",
    "LF-ks",
    "HK-kc",
    "ih-HK",
    "kc-pd",
    "ks-pd",
    "MF-pd",
    "UI-zw",
    "ih-NV",
    "ks-HK",
    "MF-kc",
    "zw-NV",
    "NV-ks",
]


class Grid:
    def __init__(self, paths):
        self.paths = paths

    @staticmethod
    def from_layout(layout):
        paths = defaultdict(lambda: [])
        for connection in layout:
            a, b = connection.split("-")
            paths[a].append(b)
            paths[b].append(a)
        return Grid(paths)

    def neighbours(self, node):
        return self.paths[node]


def is_big_cave(node):
    return node.upper() == node


def is_valid_small_cave_pt1(node, path):
    return node not in path


def is_valid_small_cave_pt2(node, path):
    if node not in path:
        return True

    if node in ["start", "end"]:
        return False

    small_nodes = [n for n in path if not is_big_cave(n)]

    return len(set(small_nodes)) == len(small_nodes)


grid = Grid.from_layout(layout)


def find_all_paths(grid, path, is_valid_small_cave):
    top = path[-1]

    if top == "end":
        return [path]

    all_paths = []
    for n in grid.neighbours(top):
        if is_big_cave(n) or is_valid_small_cave(n, path):
            all_paths += find_all_paths(
                grid, [x for x in path] + [n], is_valid_small_cave
            )
    return all_paths


p1 = find_all_paths(grid, ["start"], is_valid_small_cave_pt1)
p2 = find_all_paths(grid, ["start"], is_valid_small_cave_pt2)

print(f"q1: {len(p1)}")
print(f"q2: {len(p2)}")
