from collections import deque
import logging
import pathlib
from dataclasses import dataclass
from enum import Enum
from typing import Optional, TypedDict

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent

logging.basicConfig(level=logging.INFO, format="%(message)s")


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
    def is_valid(cls, coord: "Coord", grid_size: tuple[int, int]) -> bool:
        return 0 <= coord.x < grid_size[0] and 0 <= coord.y < grid_size[1]

    def can_move_to(self, other: "Coord") -> bool:
        # can move on same height
        # can climb down by any
        if self.height >= other.height:
            logging.debug(f"Can move from {self.height} to {other.height}")
            return True

        # can climb up by one
        if other.height - self.height == 1:
            logging.debug(f"Can climb from {self.height} to {other.height}")
            return True

        return False

    def get_path(self) -> list["Coord"]:
        path = []
        current = self
        while current:
            logging.debug(f"Adding {current} to path")
            path.append(current)
            current = current.parent
        return path

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Coord({self.x}, {self.y}, {self.height})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.height})"


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


def find_path(
    grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> list[Coord]:
    grid_size_x = len(grid)
    grid_size_y = len(grid[0])
    start_coord = Coord(*start, height=ord(grid[start[0]][start[1]]) - ord("a"))
    end_coord = Coord(*end, height=ord(grid[end[0]][end[1]]) - ord("a"))
    queue = deque([start_coord])
    visited = set()

    while queue:
        current = queue.popleft()
        logging.debug(f"Processing: {current}")

        if current in visited:
            logging.debug(f"Already visited: {current}")
            continue
        visited.add(current)

        if current == end_coord:
            logging.debug(f"Found end: {current}")
            return current.get_path()

        for direction in Direction:
            new_coord = current + direction.value
            logging.debug(f"New coord: {new_coord}")

            if not Coord.is_valid(new_coord, (grid_size_x, grid_size_y)):
                logging.debug(f"Invalid coord: {new_coord}")
                continue

            new_coord.height = ord(grid[new_coord.x][new_coord.y]) - ord("a")

            if not current.can_move_to(new_coord):
                logging.debug(f"Can't move to: {new_coord}")
                continue

            logging.debug(f"Can move to: {new_coord}")
            new_coord.parent = current
            queue.append(new_coord)

    logging.debug("No path found")
    return []


@perf
def part1(data: ParsedInput) -> int:
    """Solve part 1"""
    path = find_path(data["grid"], data["start"], data["end"])
    return len(path) - 1  # don't count start


@perf
def part2(data: ParsedInput) -> int:
    """Solve part 2"""
    grid = data["grid"]
    possible_starts =[]
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == "a":
                possible_starts.append((x, y))

    paths = []
    for start in possible_starts:
        path = find_path(grid, start, data["end"])
        if path:
            paths.append(path)

    return min(len(path) - 1 for path in paths)


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
