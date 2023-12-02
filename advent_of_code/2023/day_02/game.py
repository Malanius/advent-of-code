import math
from dataclasses import dataclass, field
from typing import TypedDict


class DrawSet(TypedDict, total=False):
    red: int
    green: int
    blue: int


class ParsedGame(TypedDict):
    id: int
    draws: list[DrawSet]


@dataclass
class Game:
    id: int
    max_counts: DrawSet
    draws: list[DrawSet] = field(default_factory=list)
    is_playable: bool = True
    required_counts: DrawSet = field(
        default_factory=lambda: {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
    )

    def add_draw(self, draw: DrawSet):
        self.draws.append(draw)
        # If the game is already not playable, don't bother checking
        if self.is_playable:
            self.is_playable = self._is_draw_valid(draw)

        self._update_required_counts(draw)

    @property
    def power(self) -> int:
        required_values = list(self.required_counts.values())
        return math.prod(required_values)

    def _is_draw_valid(self, draw: DrawSet) -> bool:
        for color, count in draw.items():
            if count > self.max_counts[color]:
                return False
        return True

    def _update_required_counts(self, draw: DrawSet):
        for color, count in draw.items():
            self.required_counts[color] = max(self.required_counts[color], count)
