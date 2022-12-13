from collections import namedtuple
import json
import pathlib
from typing import Generator

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent

Pair = namedtuple("Pair", ["left", "right"])


def parse(puzzle_input: str) -> Generator[Pair, None, None]:
    """Parse input"""
    pairs = puzzle_input.split("\n\n")
    for pair in pairs:
        parts = pair.splitlines()
        assert len(parts) == 2
        left = json.loads(parts[0])
        right = json.loads(parts[1])
        yield Pair(left, right)


@perf
def part1(data):
    """Solve part 1"""


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
