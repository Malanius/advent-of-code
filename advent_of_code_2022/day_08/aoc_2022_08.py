import pathlib
from dataclasses import dataclass, field
from enum import Enum

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


class VisibilityDirection(Enum):
    """Direction of visibility"""

    FROM_LEFT = "left"
    FROM_RIGHT = "right"
    FROM_TOP = "top"
    FROM_BOTTOM = "bottom"


@dataclass
class Tree:
    height: int
    visibility: dict[VisibilityDirection, bool] = field(
        default_factory=lambda: {
            VisibilityDirection.FROM_LEFT: False,
            VisibilityDirection.FROM_RIGHT: False,
            VisibilityDirection.FROM_TOP: False,
            VisibilityDirection.FROM_BOTTOM: False,
        }
    )

    @property
    def is_visible(self) -> bool:
        """Is the tree visible?"""
        return any(self.visibility.values())


def parse(puzzle_input: str) -> list[list[Tree]]:
    """Parse input"""
    return [[Tree(int(x)) for x in line] for line in puzzle_input.splitlines()]


def flatten(list: list[list[Tree]]) -> list[Tree]:
    """Flatten a list of lists"""
    return [item for sublist in list for item in sublist]

def find_tallest(trees: list[Tree]) -> int:
    """Find index of the first tallest tree in a list"""
    return max(enumerate(trees), key=lambda x: x[1].height)[0]

@perf
def part1(data: list[list[Tree]]) -> int:
    """Solve part 1"""
    # TODO: calculate visibility from each side
    flat_trees = flatten(data)
    return sum(1 for tree in flat_trees if tree.is_visible)


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
