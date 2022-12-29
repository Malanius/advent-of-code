from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Coord:
    row: int
    col: int

    def __add__(self, other: "Coord") -> "Coord":
        if not isinstance(other, Coord):
            raise TypeError(f"Cannot add Coord to {type(other)}")

        return Coord(self.row + other.row, self.col + other.col)


class Direction(Enum):
    NORTH = Coord(-1, 0)
    NORTH_EAST = Coord(-1, 1)
    EAST = Coord(0, 1)
    SOUTH_EAST = Coord(1, 1)
    SOUTH = Coord(1, 0)
    SOUTH_WEST = Coord(1, -1)
    WEST = Coord(0, -1)
    NORTH_WEST = Coord(-1, -1)
