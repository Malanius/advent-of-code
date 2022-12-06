from collections import Counter, deque
from itertools import islice
import pathlib
from typing import Iterable

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def sliding_window(data: Iterable, n: int) -> Iterable:
    it = iter(data)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


@perf
def part1(data):
    """Solve part 1"""
    size = 4
    for window in sliding_window(data, size):
        letter_counts = Counter(window)
        if len(letter_counts) == size:
            index = data.find("".join(window)) + size
            print(window, index)
            return index


@perf
def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
