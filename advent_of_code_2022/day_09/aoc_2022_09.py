import pathlib
from dataclasses import dataclass, field
from enum import Enum

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


class Direction(Enum):
    RIGHT = "R"
    LEFT = "L"
    UP = "U"
    DOWN = "D"


@dataclass
class MoveCommand:
    direction: Direction
    distance: int


@dataclass
class Knot:
    x: int = 0
    y: int = 0
    visited: list[tuple[int, int]] = field(default_factory=lambda: [(0, 0)])

    def move(self, direction: Direction):
        match direction:
            case Direction.RIGHT:
                self.x += 1
            case Direction.LEFT:
                self.x -= 1
            case Direction.UP:
                self.y += 1
            case Direction.DOWN:
                self.y -= 1
            case _:
                raise ValueError(f"Unknown direction: {direction}")
        self.visited.append((self.x, self.y))


def parse(puzzle_input: str) -> list[MoveCommand]:
    """Parse input"""
    lines = puzzle_input.splitlines()
    return [MoveCommand(Direction(line[0]), int(line[1:])) for line in lines]


def process_moves(moves: list[MoveCommand], head: Knot) -> None:
    for move in moves:
        for _ in range(move.distance):
            head.move(move.direction)


@perf
def part1(data):
    """Solve part 1"""
    head = Knot()


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
