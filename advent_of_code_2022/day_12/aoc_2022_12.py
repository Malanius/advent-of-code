import pathlib
from dataclasses import dataclass
from enum import Enum
from typing import Optional, TypedDict

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


class ParsedInput(TypedDict):
    grid: list[list[str]]
    start: tuple[int, int]
    end: tuple[int, int]


@dataclass
class Coord:
    x: int
    y: int
    height: int = 0
    parent: Optional["Coord"] = None

    @classmethod
    def is_valid(cls, coord: "Coord", grid_size: int) -> bool:
        return 0 <= coord.x < grid_size and 0 <= coord.y < grid_size

    def can_move(self, other: "Coord") -> bool:
        # can move on same height
        # can climb down by any
        if self.height >= other.height:
            return True

        # can climb up by one
        if other.height - self.height == 1:
            return True

        return False

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)


class Direction(Enum):
    UP = Coord(0, -1)
    DOWN = Coord(0, 1)
    LEFT = Coord(-1, 0)
    RIGHT = Coord(1, 0)


def parse(puzzle_input: str) -> ParsedInput:
    """Parse input"""
    lines = puzzle_input.splitlines()
    grid = []
    start, end = (0, 0), (0, 0)
    for n, line in enumerate(lines):
        grid.append([])
        for char in line:
            to_append = char
            if char == "S":
                start = (n, line.index(char))
                to_append = "a"
            if char == "E":
                end = (n, line.index(char))
                to_append = "z"
            grid[n].append(to_append)
    return {
        "grid": grid,
        "start": start,
        "end": end,
    }


def print_grid(grid):
    for row in grid:
        print("".join(row))


@perf
def part1(data):
    """Solve part 1"""
    print_grid(data["grid"])


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
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
