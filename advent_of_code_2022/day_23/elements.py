from dataclasses import dataclass
from typing import Optional

from advent_of_code_2022.day_23.coords import Coord, Direction


class Element:
    pass


@dataclass
class Elf(Element):
    coord: Coord
    proposed_coord: Optional[Coord] = None

    def __str__(self) -> str:
        return "#"


class Tile(Element):
    claims: int = 0

    def __str__(self) -> str:
        return "." if self.claims == 0 else str(self.claims)
