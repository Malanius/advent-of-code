from dataclasses import dataclass, field

from advent_of_code_2022.day_22.direction import Direction


class Element:
    pass


class Void(Element):
    def __str__(self) -> str:
        return "⬜"


class Rock(Element):
    def __str__(self) -> str:
        return "🪨"


@dataclass
class Tile(Element):
    passed: bool = False
    passed_direction: Direction = Direction.UP
    edges: list[Direction] = field(default_factory=list)

    def __str__(self) -> str:
        if not self.passed:
            return "⬛"
        match self.passed_direction:
            case Direction.UP:
                return "⬆️ "
            case Direction.DOWN:
                return "⬇️ "
            case Direction.LEFT:
                return "⬅️ "
            case Direction.RIGHT:
                return "➡️ "
