from dataclasses import dataclass
from typing import Literal

from advent_of_code_2022.day_22.direction import Direction


class Element:
    pass


class Void(Element):
    def __str__(self) -> str:
        return " "
        return "\u2588"  # Full block for debugging


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
