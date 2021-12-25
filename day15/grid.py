class Grid:
    def __init__(self, items):
        self.items = items

    @staticmethod
    def from_input(lines, repeats=1):
        items = [[int(c) for c in l] for l in lines]

        repeated_items = []
        for y in range(len(items) * repeats):
            repeated_items.append([])
            indexy = y % len(items)
            for x in range(len(items[0]) * repeats):
                indexx = x % len(items[indexy])

                item = items[indexy][indexx]
                bonus = y // len(items) + x // len(items)

                item = (item + bonus - 1) % 9 + 1

                repeated_items[y].append(item)

        return Grid(repeated_items)

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
