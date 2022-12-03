import pathlib
import string
from typing import Generator, Iterable

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent

PRIORITIES = dict(zip(string.ascii_lowercase, range(1, 27))) | dict(
    zip(string.ascii_uppercase, range(27, 57))
)


def parse(puzzle_input: str) -> Generator[tuple[str, str], None, None]:
    """Parse input"""
    for line in puzzle_input.splitlines():
        half = len(line) // 2
        yield (line[:half], line[half:])


@perf
def part1(inventory: Iterable[tuple[str, str]]) -> int:
    """Find items that are in both inventories and return sum of their priorities"""
    priority_sum = 0
    for inventory_left, inventory_right in inventory:
        # Using sets as first part doesn't seem to care if item is duplicated in one compartment
        set_left = set(inventory_left)
        set_right = set(inventory_right)
        priority_sum += sum(PRIORITIES[item] for item in set_left if item in set_right)
    return priority_sum


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
