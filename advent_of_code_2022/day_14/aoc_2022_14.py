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


@dataclass
class Simulation:
    grid: list[list[Element]] = field(default_factory=list)

    def __str__(self) -> str:
        return "\n".join("".join(str(element) for element in row) for row in self.grid)

    def _parse_data(self, puzzle_input: str) -> None:
        self.rock_lines = []
        min_x, max_x, max_y = float("inf"), 0, 0
        for line in puzzle_input.splitlines():
            rock_line_points = line.split(" -> ")
            rock_line_coords = []
            for rock_line_point in rock_line_points:
                rock_line_point = rock_line_point.split(",")
                rock_line_coord = (int(rock_line_point[0]), int(rock_line_point[1]))
                if rock_line_coord[0] < min_x:
                    min_x = rock_line_coord[0]
                if rock_line_coord[0] > max_x:
                    max_x = rock_line_coord[0]
                if rock_line_coord[1] > max_y:
                    max_y = rock_line_coord[1]
                rock_line_coords.append(rock_line_coord)
            self.rock_lines.append(rock_line_coords)
        self.size_x = max_x - int(min_x)
        self.size_y = max_y

    def _create_grid(self) -> None:
        self.grid = [
            [Air() for _ in range(self.size_x + 1)] for _ in range(self.size_y + 1)
        ]


    def bootstrap(self, puzzle_input: str) -> None:
        self._parse_data(puzzle_input)
        self._create_grid()


def parse(puzzle_input: str) -> Simulation:
    """Parse input"""
    simulation = Simulation()
    simulation.bootstrap(puzzle_input)
    print(simulation)
    return simulation


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
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
