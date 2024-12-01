from dataclasses import dataclass, field
from typing import Literal

from coord import Coord
from direction import Direction
from elements import Tile, Element, Void


@dataclass
class Player(Element):
    coords: Coord
    facing: Direction = Direction.RIGHT
    standing_on: Element = field(init=False)
    crashed: bool = False

    def __str__(self) -> str:
        if self.crashed:
            return "💥"
        match self.facing:
            case Direction.UP:
                return "👆"
            case Direction.DOWN:
                return "👇"
            case Direction.LEFT:
                return "👈"
            case Direction.RIGHT:
                return "👉"

    def can_move_to(self, element: Element) -> bool:
        if isinstance(element, Tile) or isinstance(element, Void):
            return True
        return False

    def move_to(self, coord: Coord) -> None:
        self.coords = coord

    def turn(self, to: Literal["L", "R"]):
        match to, self.facing:
            case ("L", Direction.UP):
                self.facing = Direction.LEFT
            case ("L", Direction.LEFT):
                self.facing = Direction.DOWN
            case ("L", Direction.DOWN):
                self.facing = Direction.RIGHT
            case ("L", Direction.RIGHT):
                self.facing = Direction.UP
            case ("R", Direction.UP):
                self.facing = Direction.RIGHT
            case ("R", Direction.RIGHT):
                self.facing = Direction.DOWN
            case ("R", Direction.DOWN):
                self.facing = Direction.LEFT
            case ("R", Direction.LEFT):
                self.facing = Direction.UP
