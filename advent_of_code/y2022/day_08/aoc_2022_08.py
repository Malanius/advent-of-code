import math
import pathlib
from dataclasses import dataclass, field
from enum import Enum

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


class VisibilityDirection(Enum):
    """Direction of visibility"""

    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"


@dataclass
class Tree:
    height: int
    visibility: dict[VisibilityDirection, bool] = field(
        default_factory=lambda: {
            VisibilityDirection.LEFT: False,
            VisibilityDirection.RIGHT: False,
            VisibilityDirection.TOP: False,
            VisibilityDirection.BOTTOM: False,
        }
    )
    seen_trees: dict[VisibilityDirection, int] = field(
        default_factory=lambda: {
            VisibilityDirection.LEFT: 0,
            VisibilityDirection.RIGHT: 0,
            VisibilityDirection.TOP: 0,
            VisibilityDirection.BOTTOM: 0,
        }
    )

    @property
    def is_visible(self) -> bool:
        """Is the tree visible?"""
        return any(self.visibility.values())

    @property
    def scenic_score(self) -> int:
        """Calculate scenic score"""
        return math.prod(self.seen_trees.values())


def parse(puzzle_input: str) -> list[list[Tree]]:
    """Parse input"""
    return [[Tree(int(x)) for x in line] for line in puzzle_input.splitlines()]


def flatten(list: list[list[Tree]]) -> list[Tree]:
    """Flatten a list of lists"""
    return [item for sublist in list for item in sublist]


def find_tallest(trees: list[Tree]) -> int:
    """Find index of the first tallest tree in a list"""
    return max(enumerate(trees), key=lambda x: x[1].height)[0]


def calculate_visibility(trees: list[Tree], direction: VisibilityDirection) -> None:
    """Calculate visibility of trees from the left"""
    # first tree is always visible
    trees[0].visibility[direction] = True

    # the first highest tree will be visible and block all behind, so no need to process all
    tallest_index = find_tallest(trees)
    trees[tallest_index].visibility[direction] = True

    # we can see only trees that are higher than the previous tallest one
    track_height = trees[0].height

    for i in range(1, tallest_index):
        if trees[i].height > track_height:
            track_height = trees[i].height
            trees[i].visibility[direction] = True


def calculate_visibility_from_left(trees: list[list[Tree]]) -> None:
    """Calculate visibility of trees from the left"""
    for row in trees:
        calculate_visibility(row, VisibilityDirection.LEFT)


def calculate_visibility_from_right(trees: list[list[Tree]]) -> None:
    """Calculate visibility of trees from the right"""
    for row in trees:
        calculate_visibility(row[::-1], VisibilityDirection.RIGHT)


def calculate_visibility_from_top(trees: list[list[Tree]]) -> None:
    """Calculate visibility of trees from the top"""
    for i in range(len(trees[0])):
        calculate_visibility([row[i] for row in trees], VisibilityDirection.TOP)


def calculate_visibility_from_bottom(trees: list[list[Tree]]) -> None:
    """Calculate visibility of trees from the bottom"""
    for i in range(len(trees[0])):
        calculate_visibility(
            [row[i] for row in trees[::-1]], VisibilityDirection.BOTTOM
        )


def calculate_visibility_from_all_directions(trees: list[list[Tree]]) -> None:
    """Calculate visibility of trees from all directions"""
    calculate_visibility_from_left(trees)
    calculate_visibility_from_right(trees)
    calculate_visibility_from_top(trees)
    calculate_visibility_from_bottom(trees)


@perf
def part1(data: list[list[Tree]]) -> int:
    """Solve part 1"""
    calculate_visibility_from_all_directions(data)
    flat_trees = flatten(data)
    return sum(1 for tree in flat_trees if tree.is_visible)


def calculate_visible_trees(trees: list[Tree], direction: VisibilityDirection) -> None:
    """Calculate visible trees from tree in a given direction"""
    for index, tree in enumerate(trees):
        # we are only interested in trees that are in front of the current one
        # and as we see them in reverse order, we need to reverse the list
        trees_left = reversed(trees[:index])
        seen = 0
        for tree_left in trees_left:
            seen += 1  # we always see at least one tree, if not at edge
            # if the tree is same height or higher, we can't see anything behind it
            if tree_left.height >= tree.height:
                break
        tree.seen_trees[direction] = seen


def calculate_visible_trees_left(trees: list[list[Tree]]) -> None:
    """Calculate visible trees from tree in a given direction"""
    for row in trees:
        calculate_visible_trees(row, VisibilityDirection.LEFT)


def count_visible_trees_right(trees: list[list[Tree]]) -> None:
    """Calculate visible trees from tree in a given direction"""
    for row in trees:
        calculate_visible_trees(row[::-1], VisibilityDirection.RIGHT)


def count_visible_trees_top(trees: list[list[Tree]]) -> None:
    """Calculate visible trees from tree in a given direction"""
    for i in range(len(trees[0])):
        calculate_visible_trees([row[i] for row in trees], VisibilityDirection.TOP)


def count_visible_trees_bottom(trees: list[list[Tree]]) -> None:
    """Calculate visible trees from tree in a given direction"""
    for i in range(len(trees[0])):
        calculate_visible_trees(
            [row[i] for row in trees[::-1]], VisibilityDirection.BOTTOM
        )


def count_visible_trees_from_all_directions(trees: list[list[Tree]]) -> None:
    """Calculate visible trees from tree in a given direction"""
    calculate_visible_trees_left(trees)
    count_visible_trees_right(trees)
    count_visible_trees_top(trees)
    count_visible_trees_bottom(trees)


@perf
def part2(data):
    """Solve part 2"""
    count_visible_trees_from_all_directions(data)
    flat_trees = flatten(data)
    return max(tree.scenic_score for tree in flat_trees)


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
