from collections import defaultdict
from dataclasses import dataclass, field
from advent_of_code_2022.day_23.coords import Coord

from advent_of_code_2022.day_23.elements import Element, Elf, Tile


@dataclass
class Grid:
    # grid can infinetly span to all directions, constantly resizing lists is not efficient
    # defaultdict helps to track only the elements that are present - Elves possitions and claimed tiles
    # rest of the grid is filled with empty tiles
    elements: defaultdict[Coord, Element] = field(
        default_factory=lambda: defaultdict(lambda: Tile())
    )
    # keep track of all elves in the grid, so we can iterate over them
    elves: set[Coord] = field(default_factory=set)

    def __str__(self) -> str:
        grid = ""
        for row in range(self.min_row, self.max_row + 1):
            for col in range(self.min_col, self.max_col + 1):
                grid += str(self.elements[Coord(row, col)])
            grid += "\n"
        return grid

    def _parse_data(self, puzzle_input: str) -> None:
        for row, line in enumerate(puzzle_input.splitlines()):
            for col, char in enumerate(line):
                if char == "#":
                    self.elements[Coord(row, col)] = Elf()
                    self.elves.add(Coord(row, col))

    @property
    def min_row(self) -> int:
        return min(coord.row for coord in self.elements)

    @property
    def max_row(self) -> int:
        return max(coord.row for coord in self.elements)

    @property
    def min_col(self) -> int:
        return min(coord.col for coord in self.elements)

    @property
    def max_col(self) -> int:
        return max(coord.col for coord in self.elements)

    @property
    def elves_count(self) -> int:
        return len(self.elves)

    @classmethod
    def construct(cls, puzzle_input: str) -> "Grid":
        grid = Grid()
        grid._parse_data(puzzle_input)
        return grid
