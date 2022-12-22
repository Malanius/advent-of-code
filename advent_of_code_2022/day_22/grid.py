import logging
from dataclasses import dataclass, field
from itertools import pairwise, zip_longest
from typing import Optional
from advent_of_code_2022.day_22.coord import Coord
from advent_of_code_2022.day_22.direction import Direction

from advent_of_code_2022.day_22.elements import Tile, Element, Rock, Void


@dataclass
class Grid:
    grid: list[list[Element]] = field(default_factory=list)
    start_coords: Optional[Coord] = None
    edge_points: set[Coord] = field(default_factory=set)

    def __str__(self) -> str:
        return "\n".join("".join(str(element) for element in row) for row in self.grid)

    def partial_str(self, actual_coord: Coord, height: int = 25, width=130) -> str:
        actual_y, actual_x = actual_coord()

        half_height = height // 2
        start_height = actual_y - half_height
        end_height = actual_y + half_height
        if start_height < 0:
            start_height = 0
            end_height = height
        if end_height > len(self.grid):
            end_height = len(self.grid)
            start_height = end_height - height

        half_width = width // 2
        start_width = actual_x - half_width
        end_width = actual_x + half_width
        if start_width < 0:
            start_width = 0
            end_width = width
        if end_width > len(self.grid[0]):
            end_width = len(self.grid[0])
            start_width = end_width - width

        return "\n".join(
            "".join(str(element) for element in row[start_width:end_width])
            for row in self.grid[start_height:end_height]
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
                            logging.debug(f"Found start at {y}, {x}.")
                            self.start_coords = Coord(y, x)
                        element = Tile()
                self.grid[y].append(element)

    def _mark_edge(self, tile: Tile, direction: Direction, coord: Coord) -> None:
        y, x = coord()
        logging.debug(f"Found {direction} edge at {y}, {x}.")
        tile.edges.append(direction)
        self.edge_points.add(coord)

    def _mark_edges(self) -> None:
        for y, row in enumerate(self.grid):
            for x, element in enumerate(row):
                if not isinstance(element, Tile):
                    logging.debug(f"Skipping {y}, {x} as it's not air")
                    continue

                for direction in Direction:
                    current_coord = Coord(y, x)
                    new_coord = current_coord + Coord(*direction.value)

                    out_of_bounds = False
                    # check vertical bounds
                    if new_coord.y < 0 or new_coord.y >= len(self.grid):
                        self._mark_edge(element, direction, Coord(y, x))
                        out_of_bounds = True

                    # check horizontal bounds
                    if new_coord.x < 0 or new_coord.x >= len(self.grid[0]):
                        self._mark_edge(element, direction, Coord(y, x))
                        out_of_bounds = True

                    if out_of_bounds:
                        continue

                    # check void bounds
                    if isinstance(self.grid[new_coord.y][new_coord.x], Void):
                        self._mark_edge(element, direction, Coord(y, x))

        logging.debug(f"Found {len(self.edge_points)} edge points.")

    def _row_bounds(self, coord: Coord) -> tuple[Coord, Coord]:
        y = coord.y
        row = self.grid[y]
        row_str = "".join(str(element) for element in row)
        # we can wrap to rocks as well
        row_str = row_str.replace(str(Rock()), str(Tile()))
        left = row_str.index(str(Tile()))
        right = row_str.rindex(str(Tile()))
        return Coord(y, left), Coord(y, right)

    def _col_bounds(self, coord: Coord) -> tuple[Coord, Coord]:
        x = coord.x
        col = [row[x] for row in self.grid]
        col_str = "".join(str(element) for element in col)
        # we can wrap to rocks as well
        col_str = col_str.replace(str(Rock()), str(Tile()))
        top = col_str.index(str(Tile()))
        bottom = col_str.rindex(str(Tile()))
        return Coord(top, x), Coord(bottom, x)

    def wraps_to(self, coord: Coord, incoming_direction: Direction) -> Coord:
        element = self.grid[coord.y][coord.x]
        if not isinstance(element, Tile):
            raise ValueError(f"Cannot wrap from {coord} as it's not air!")

        if not element.edges:
            raise ValueError(f"Cannot wrap from {coord} as it's not an edge!")

        if incoming_direction not in element.edges:
            return coord + Coord(*incoming_direction.value)

        match incoming_direction:
            case Direction.UP:
                _, bottom = self._col_bounds(coord)
                return Coord(bottom.y, coord.x)
            case Direction.DOWN:
                top, _ = self._col_bounds(coord)
                return Coord(top.y, coord.x)
            case Direction.LEFT:
                _, right = self._row_bounds(coord)
                return Coord(coord.y, right.x)
            case Direction.RIGHT:
                left, _ = self._row_bounds(coord)
                return Coord(coord.y, left.x)

    @classmethod
    def construct(cls, puzzle_input: str) -> "Grid":
        grid = Grid()
        grid._parse_data(puzzle_input)
        grid._mark_edges()
        return grid
