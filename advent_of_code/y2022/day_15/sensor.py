from dataclasses import dataclass
from typing import Optional

from advent_of_code.y2022.day_15.coord import Boundaries, Coord


@dataclass
class Sensor:
    coord: Coord
    scan_range: int

    @property
    def scan_bounds(self) -> Boundaries:
        min_x = self.coord.x - self.scan_range
        max_x = self.coord.x + self.scan_range
        min_y = self.coord.y - self.scan_range
        max_y = self.coord.y + self.scan_range

        return Boundaries(max_x, max_y, min_x, min_y)

    def get_coverage_at_row(self, y: int) -> Optional[tuple[int, int]]:
        # Y is out of range
        if y < self.coord.y - self.scan_range or y > self.coord.y + self.scan_range:
            return None

        return (
            self.coord.x - (self.scan_range - abs(self.coord.y - y)),
            self.coord.x + (self.scan_range - abs(self.coord.y - y)),
        )

    def __hash__(self) -> int:
        return hash(self.coord)
