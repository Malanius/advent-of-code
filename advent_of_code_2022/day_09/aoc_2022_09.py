import pathlib
from dataclasses import dataclass, field
from enum import Enum
import logging

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent

logging.basicConfig(level=logging.INFO)


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

    def _is_touching(self, other: "Knot") -> bool:
        """Check if the other knot is next to this knot"""
        chebychev_distance = max(abs(self.x - other.x), abs(self.y - other.y))
        return chebychev_distance <= 1

    def _move_diagonally(self, other: "Knot"):
        """Move diagonally to the other knot"""
        if self.x < other.x:
            self.x += 1
        elif self.x > other.x:
            self.x -= 1
        if self.y < other.y:
            self.y += 1
        elif self.y > other.y:
            self.y -= 1
        self.visited.append((self.x, self.y))

    def catch_up(self, other: "Knot") -> None:
        """Catch up to the other knot"""
        if self._is_touching(other):
            logging.debug("Points are touching, not moving to keep up")
            return

        logging.debug("Points are not touching, moving to keep up")
        if self.x == other.x:
            # Move vertically
            if self.y < other.y:
                self.move(Direction.UP)
                return
            else:
                self.move(Direction.DOWN)
                return

        if self.y == other.y:
            # Move horizontally
            if self.x < other.x:
                self.move(Direction.RIGHT)
                return
            else:
                self.move(Direction.LEFT)
                return

        # Move diagonally
        self._move_diagonally(other)


def parse(puzzle_input: str) -> list[MoveCommand]:
    """Parse input"""
    lines = puzzle_input.splitlines()
    return [MoveCommand(Direction(line[0]), int(line[1:])) for line in lines]


def process_moves(moves: list[MoveCommand], head: Knot, tail: Knot) -> None:
    for move in moves:
        logging.debug(f"Move: {move.direction}, {move.distance}")
        for _ in range(move.distance):
            head.move(move.direction)
            tail.catch_up(head)
            logging.debug(f"Head: {head.x}, {head.y}")
            logging.debug(f"Tail: {tail.x}, {tail.y}")

    logging.debug(f"Head: {head.visited}")
    logging.debug(f"Tail: {tail.visited}")


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
