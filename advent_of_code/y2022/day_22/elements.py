from dataclasses import dataclass, field

from direction import Direction


class Element:
    pass


class Void(Element):
    def __str__(self) -> str:
        return "⬜"


class Rock(Element):
    def __str__(self) -> str:
        return "🪨"


class Star(Element):
    def __str__(self) -> str:
        return "🌟"


@dataclass
class Tile(Element):
    passed: bool = False
    passed_direction: Direction = Direction.UP
    edges: list[Direction] = field(default_factory=list)

    def __str__(self) -> str:
        if not self.passed:
            return "⬛"
        match self.passed_direction:
            # the arrows emojis are weird, they seem as two characters, but behaves as one?
            # can be compensated by adding a space after the emoji
            case Direction.UP:
                return "⬆️ "
            case Direction.DOWN:
                return "⬇️ "
            case Direction.LEFT:
                return "⬅️ "
            case Direction.RIGHT:
                return "➡️ "
