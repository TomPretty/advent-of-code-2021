from typing import List


def read_input(path: str) -> List[int]:
    with open(path) as f:
        lines = f.read().split("\n")
    return [int(l) for l in lines]


def number_of_increases(depths: List[int]) -> int:
    res = 0
    for d1, d2 in zip(depths, depths[1:]):
        if d2 > d1:
            res += 1
    return res


def sliding_window(depths: List[int], window_size: int) -> List[int]:
    return [
        sum(depths[i : i + window_size]) for i in range(len(depths) - window_size + 1)
    ]


depths = read_input("input.txt")
print(f"q1: {number_of_increases(depths)}")
print(f"q2: {number_of_increases(sliding_window(depths, 3))}")
