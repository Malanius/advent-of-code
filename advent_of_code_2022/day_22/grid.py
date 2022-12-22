import logging
from dataclasses import dataclass, field
from itertools import pairwise, zip_longest
from typing import Optional

from advent_of_code_2022.day_22.elements import Air, Element, Rock, Void


@dataclass
class Grid:
    grid: list[list[Element]] = field(default_factory=list)
    start_coords: Optional[tuple[int, int]] = None

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
        lines = puzzle_input.splitlines()
        max_width = max(len(line) for line in lines)
        for y, line in enumerate(lines):
            self.grid.append([])
            for x, char in zip_longest(range(max_width), line):
                element: Element = Void()
                match char:
                    case "#":
                        element = Rock()
                    case ".":
                        if not self.start_coords:
                            self.start_coords = (x, y)
                        element = Air()
                self.grid[y].append(element)

    @classmethod
    def construct(cls, puzzle_input: str) -> "Grid":
        grid = Grid()
        grid._parse_data(puzzle_input)
        return grid
