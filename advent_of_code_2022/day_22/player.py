from dataclasses import dataclass
from typing import Literal
from advent_of_code_2022.day_22.coord import Coord

from advent_of_code_2022.day_22.direction import Direction
from advent_of_code_2022.day_22.elements import Air, Element, Void


@dataclass
class Player(Element):
    coords: Coord
    facing: Direction = Direction.RIGHT

    def __str__(self) -> str:
        return "*"

    def can_move_to(self, element: Element) -> bool:
        if isinstance(element, Air) or isinstance(element, Void):
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
