import logging
from dataclasses import dataclass, field
from itertools import pairwise, zip_longest
from typing import Optional
from advent_of_code_2022.day_22.coord import Coord
from advent_of_code_2022.day_22.direction import Direction

from advent_of_code_2022.day_22.elements import Air, Element, Rock, Void


@dataclass
class Grid:
    grid: list[list[Element]] = field(default_factory=list)
    start_coords: Optional[Coord] = None
    edge_points: list[Coord] = field(default_factory=list)

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
                            self.start_coords = Coord(y, x)
                        element = Air()
                self.grid[y].append(element)

    def _mark_edges(self) -> None:
        for y, row in enumerate(self.grid):
            for x, element in enumerate(row):
                if not isinstance(element, Air):
                    logging.debug(f"Skipping {y}, {x} as it's not air")
                    continue

                for direction in Direction:
                    current_coord = Coord(y, x)
                    new_coord = current_coord + Coord(*direction.value)

                    # check vertical bounds
                    if new_coord.y < 0 or new_coord.y >= len(self.grid):
                        logging.debug(f"Found edge at {y}, {x}.")
                        element.is_edge = True
                        self.edge_points.append(Coord(y, x))
                        break

                    # check horizontal bounds
                    if new_coord.x < 0 or new_coord.x >= len(self.grid[new_coord.y]):
                        logging.debug(f"Found edge at {y}, {x}.")
                        element.is_edge = True
                        self.edge_points.append(Coord(y, x))
                        break

                    # check void bounds
                    if isinstance(self.grid[new_coord.y][new_coord.x], Void):
                        logging.debug(f"Found edge at {y}, {x}.")
                        element.is_edge = True
                        self.edge_points.append(Coord(y, x))
                        break
        logging.debug(f"Found {len(self.edge_points)} edge points.")

    def _row_bounds(self, coord: Coord) -> tuple[Coord, Coord]:
        y = coord.y
        row = self.grid[y]
        row_str = "".join(str(element) for element in row)
        # we can wrap to rocks as well
        row_str = row_str.replace(str(Rock()), str(Air()))
        left = row_str.index(str(Air()))
        right = row_str.rindex(str(Air()))
        return Coord(y, left), Coord(y, right)

    def _col_bounds(self, coord: Coord) -> tuple[Coord, Coord]:
        x = coord.x
        col = [row[x] for row in self.grid]
        col_str = "".join(str(element) for element in col)
        # we can wrap to rocks as well
        col_str = col_str.replace(str(Rock()), str(Air()))
        top = col_str.index(str(Air()))
        bottom = col_str.rindex(str(Air()))
        return Coord(top, x), Coord(bottom, x)

    def wraps_to(self, coord: Coord, incoming_direction: Direction) -> Coord:
        element = self.grid[coord.y][coord.x]
        if not isinstance(element, Air):
            raise ValueError(f"Cannot wrap from {coord} as it's not air!")

        if not element.is_edge:
            raise ValueError(f"Cannot wrap from {coord} as it's not an edge!")

        match incoming_direction:
            case Direction.UP:
                _, bottom = self._col_bounds(coord)
                if coord.y == bottom.y:
                    return coord
                return Coord(bottom.y, coord.x)
            case Direction.DOWN:
                top, _ = self._col_bounds(coord)
                if coord.y == top.y:
                    return coord
                return Coord(top.y, coord.x)
            case Direction.LEFT:
                _, right = self._row_bounds(coord)
                if coord.x == right.x:
                    return coord
                return Coord(coord.y, right.x)
            case Direction.RIGHT:
                left, _ = self._row_bounds(coord)
                if coord.x == left.x:
                    return coord
                return Coord(coord.y, left.x)

    @classmethod
    def construct(cls, puzzle_input: str) -> "Grid":
        grid = Grid()
        grid._parse_data(puzzle_input)
        grid._mark_edges()
        return grid
