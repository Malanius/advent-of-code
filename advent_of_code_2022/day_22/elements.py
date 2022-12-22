from dataclasses import dataclass
from typing import Literal

from advent_of_code_2022.day_22.direction import Direction


class Element:
    pass


class Void(Element):
    def __str__(self) -> str:
        return " "
        return "\u2588" # Full block for debugging


class Rock(Element):
    def __str__(self) -> str:
        return "#"


@dataclass
class Air(Element):
    passed: bool = False
    passed_direction: Direction = Direction.UP

    def __str__(self) -> str:
        if not self.passed:
            return "."
        match self.passed_direction:
            case Direction.UP:
                return "^"
            case Direction.DOWN:
                return "v"
            case Direction.LEFT:
                return "<"
            case Direction.RIGHT:
                return ">"


@dataclass
class Player(Element):
    coords: tuple[int, int]
    facing: Direction = Direction.RIGHT

    def __str__(self) -> str:
        return "*"

    def can_move_to(self, element: Element) -> bool:
        if isinstance(element, Air):
            return True
        return False

    def move(self, direction: Direction):
        x, y = self.coords
        self.coords = (x + direction.value[0], y + direction.value[1])

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
