import logging
from typing import Optional

from advent_of_code.y2022.day_15.coord import Boundaries, Coord
from advent_of_code.y2022.day_15.scan_coverage import (
    get_scan_coverage_bounds,
    get_sensors_coverage_at_row,
)
from advent_of_code.y2022.day_15.sensor import Sensor

SENSOR = "S"
BEACON = "B"
SCANNED = "#"
EMPTY = "."


def print_grid(data: dict[Coord, Coord], boundaries: Optional[Boundaries] = None):
    """Print the grid"""
    grid = data_to_grid(data)
    sensors = {
        Sensor(sensor, sensor.distance(beacon)) for sensor, beacon in data.items()
    }
    if not boundaries:
        boundaries = get_scan_coverage_bounds(sensors)

    for row in range(boundaries.min_y, boundaries.max_y + 1):
        coverage = get_sensors_coverage_at_row(sensors, row)
        for start, end in coverage:
            for x in range(start, end + 1):
                if not grid.get(Coord(x, row)):
                    grid[Coord(x, row)] = SCANNED

    print(grid_repr(grid, boundaries))


def data_to_grid(data: dict[Coord, Coord]) -> dict[Coord, str]:
    """Convert the data to a grid"""
    grid = {}
    for sensor, beacon in data.items():
        grid[sensor] = SENSOR
        grid[beacon] = BEACON

    logging.debug(grid)
    return grid


def grid_repr(grid: dict[Coord, str], boundaries: Boundaries):
    """Print the grid"""

    min_x = boundaries.min_x
    max_x = boundaries.max_x
    min_y = boundaries.min_y
    max_y = boundaries.max_y

    repr = ""

    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            row += grid.get(Coord(x, y), EMPTY)
        repr += f"{y:>3d}: {row}\n"

    return repr
