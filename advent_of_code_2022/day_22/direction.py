from enum import Enum


class Direction(Enum):
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)

    @property
    def score(self) -> int:
        match self:
            case Direction.RIGHT:
                return 0
            case Direction.DOWN:
                return 1
            case Direction.LEFT:
                return 2
            case Direction.UP:
                return 3
