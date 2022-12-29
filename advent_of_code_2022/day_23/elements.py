from advent_of_code_2022.day_23.coords import Coord


class Element:
    pass


class Elf(Element):
    def __str__(self) -> str:
        return "#"


class Tile(Element):
    claims: int = 0

    def __str__(self) -> str:
        return "." if self.claims == 0 else str(self.claims)
