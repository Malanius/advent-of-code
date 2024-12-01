from dataclasses import dataclass


@dataclass
class Coord:
    x: int
    y: int

    def distance(self, other):
        """Calculates Manhattan distance between two coordinates"""
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Coord({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


@dataclass
class Boundaries:
    min_x: int
    max_x: int
    min_y: int
    max_y: int
