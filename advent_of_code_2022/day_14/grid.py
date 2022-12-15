import logging
from dataclasses import dataclass, field
from itertools import pairwise

from advent_of_code_2022.day_14.elements import Air, Element, Rock, Grain, SandGenerator


@dataclass
class Grid:
    transparent_air: bool = False
    bedrock: bool = False
    grid: list[list[Element]] = field(default_factory=list)
    generator_coords: tuple[int, int] = field(default_factory=lambda: (500, 0))

    def __str__(self) -> str:
        return "\n".join("".join(str(element) for element in row) for row in self.grid)

    def partial_str(self, actual_y: int, height: int = 35) -> str:
        half = height // 2
        start = actual_y - half
        end = actual_y + half
        if start < 0:
            start = 0
            end = height
        if end > len(self.grid):
            end = len(self.grid)
            start = end - height
        return "\n".join(
            "".join(str(element) for element in row) for row in self.grid[start:end]
        )

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
        self.size_y = max_y if not self.bedrock else max_y + 2
        self.offset_x = int(min_x)

    def _create_grid(self) -> None:
        self.grid = [
            [Air(transparent=self.transparent_air) for _ in range(self.size_x + 1)]
            for _ in range(self.size_y + 1)
        ]

    def _create_vertical_rock(
        self, start: tuple[int, int], end: tuple[int, int]
    ) -> None:
        logging.debug(f"Drawing vertical line, start: {start}, end: {end}")
        start_x, start_y = start
        _, end_y = end
        direction = 1 if start_y < end_y else -1
        for y in range(start_y, end_y + direction, direction):
            self.grid[y][start_x - self.offset_x] = Rock()

    def _create_horizontal_rock(
        self, start: tuple[int, int], end: tuple[int, int]
    ) -> None:
        logging.debug(f"Drawing horizontal line, start: {start}, end: {end}")
        start_x, start_y = start
        end_x, _ = end
        direction = 1 if start_x < end_x else -1
        for x in range(start_x, end_x + direction, direction):
            self.grid[start_y][x - self.offset_x] = Rock()

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

    def _create_bedrock(self) -> None:
        for x in range(self.size_x + 1):
            self.grid[self.size_y][x] = Rock()

    def _create_sand_generator(self) -> None:
        gen_x, gen_y = self.generator_coords
        self.grid[gen_y][gen_x - self.offset_x] = SandGenerator()

    @classmethod
    def construct(
        cls, puzzle_input: str, interactive: bool = False, bedrock: bool = False
    ) -> "Grid":
        grid = Grid(transparent_air=interactive, bedrock=bedrock)
        grid._parse_data(puzzle_input)
        grid._create_grid()
        grid._create_rocks()
        if bedrock:
            print("Creating bedrock")
            grid._create_bedrock()
        grid._create_sand_generator()
        return grid
