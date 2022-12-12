import pathlib
from typing import TypedDict

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


class ParsedInput(TypedDict):
    grid: list[list[str]]
    start: tuple[int, int]
    end: tuple[int, int]


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
