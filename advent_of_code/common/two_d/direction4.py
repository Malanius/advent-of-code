from enum import Enum

from advent_of_code.common.two_d.coord import Coord


class Direction4(Enum):
    """Directions for 2D grid for 4 way movement.

    X axis is horizontal from left to right.
    Y axis is vertical from top to bottom.
    """

    UP = Coord(0, -1)
    DOWN = Coord(0, 1)
    RIGHT = Coord(1, 0)
    LEFT = Coord(-1, 0)
