from dataclasses import dataclass, field
import logging
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

    def add_draw(self, draw: DrawSet):
        self.draws.append(draw)
        # If the game is already not playable, don't bother checking
        if self.is_playable:
            self.is_playable = self._is_draw_valid(draw)

    def _is_draw_valid(self, draw: DrawSet) -> bool:
        for color, count in draw.items():
            if count > self.max_counts[color]:
                logging.debug(f"Draw is invalid, {color} count is too high")
                return False
        return True
