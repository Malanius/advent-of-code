from dataclasses import dataclass


@dataclass(frozen=True)
class Coord:
    y: int
    x: int

    def __call__(self) -> tuple[int, int]:
        return self.x, self.y

    def __add__(self, other):
        return Coord(self.y + other.y, self.x + other.x)

    def __sub__(self, other):
        return Coord(self.y - other.y, self.x - other.x)

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __repr__(self):
        return f"Coord({self.y}, {self.x})"

    def __str__(self) -> str:
        return f"({self.y}, {self.x})"
