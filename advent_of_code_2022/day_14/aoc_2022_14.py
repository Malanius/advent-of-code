from dataclasses import dataclass
from enum import Enum
import pathlib

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


class Direction(Enum):
    DOWN = (1, 0)
    DOWN_LEFT = (1, -1)
    DOWN_RIGHT = (1, 1)


class Element:
    pass


class SandGenerator(Element):
    def __str__(self) -> str:
        return "+"


class Rock(Element):
    def __str__(self) -> str:
        return "#"


@dataclass
class Air(Element):
    visited: bool = False

    def __str__(self) -> str:
        return "~" if self.visited else "."


@dataclass
class Sand(Element):
    is_resting: bool = False

    def __str__(self) -> str:
        return "o" if self.is_resting else "*"

    def can_move_to(self, element: Element) -> bool:
        if isinstance(element, Air):
            return True
        if isinstance(element, Sand):
            return element.is_resting
        return False
    """Parse input"""


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
