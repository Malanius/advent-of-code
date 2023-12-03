from enum import Enum

from advent_of_code.common.two_d.coord import Coord


class Direction(Enum):
    """Directions for 2D grid.

    X axis is horizontal from left to right.
    Y axis is vertical from top to bottom.
    """

    UP = Coord(0, -1)
    UP_LEFT = Coord(-1, -1)
    UP_RIGHT = Coord(1, -1)
    DOWN = Coord(0, 1)
    DOWN_LEFT = Coord(-1, 1)
    DOWN_RIGHT = Coord(1, 1)
    RIGHT = Coord(1, 0)
    LEFT = Coord(-1, 0)
