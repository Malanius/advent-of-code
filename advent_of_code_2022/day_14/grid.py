import logging
from dataclasses import dataclass, field
from itertools import pairwise

from advent_of_code_2022.day_14.elements import Air, Element, Rock, SandGenerator


@dataclass
class Grid:
    grid: list[list[Element]] = field(default_factory=list)
    generator_coords: tuple[int, int] = field(default_factory=lambda: (500, 0))

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
        self.offset_x = int(min_x)

    def _create_grid(self) -> None:
        self.grid = [
            [Air() for _ in range(self.size_x + 1)] for _ in range(self.size_y + 1)
        ]

    def _create_vertical_rock(
        self, start: tuple[int, int], end: tuple[int, int]
    ) -> None:
        logging.debug(f"Drawing vertical line, start: {start}, end: {end}")
        for y in range(start[1], end[1] + 1):
            self.grid[y][start[0] - self.offset_x] = Rock()

    def _create_horizontal_rock(
        self, start: tuple[int, int], end: tuple[int, int]
    ) -> None:
        logging.debug(f"Drawing horizontal line, start: {start}, end: {end}")
        draw_left = start[0] < end[0]
        if draw_left:
            start, end = end, start
        for x in range(start[0], end[0] - 1, -1):
            self.grid[start[1]][x - self.offset_x] = Rock()

    def _create_rock(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        is_vertitcal = start[0] == end[0]
        if is_vertitcal:
            self._create_vertical_rock(start, end)
        else:
            self._create_horizontal_rock(start, end)

    def _create_rocks(self) -> None:
        for rock_line in self.rock_lines:
            for start, end in pairwise(rock_line):
                self._create_rock(start, end)

    def _create_sand_generator(self) -> None:
        self.grid[0][500 - self.offset_x] = SandGenerator()

    @classmethod
    def bootstrap(cls, puzzle_input: str) -> "Grid":
        simulation = Grid()
        simulation._parse_data(puzzle_input)
        simulation._create_grid()
        simulation._create_rocks()
        simulation._create_sand_generator()
        return simulation
