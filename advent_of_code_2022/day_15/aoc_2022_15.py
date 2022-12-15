import logging
import pathlib
import re

from advent_of_code_2022.day_15.coord import Coord
from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")

input_regex = re.compile(
    r"^Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)$"
)
SENSOR = "S"
BEACON = "B"
SCANNED = "#"


def parse(puzzle_input: str) -> dict[Coord, Coord]:
    """Parse input"""
    data = {}
    for line in puzzle_input.splitlines():
        match = input_regex.match(line)
        if match:
            sensor = Coord(int(match.group(1)), int(match.group(2)))
            beacon = Coord(int(match.group(3)), int(match.group(4)))
            data[sensor] = beacon

    return data


def fill_scan_area(
    grid: dict[Coord, str], sensor: Coord, beacon: Coord
) -> dict[Coord, str]:
    """Fill the grid from sensor to beacon distance"""
    logging.debug(f"Filling for Sensor: {sensor}, Beacon: {beacon}")
    distance = sensor.distance(beacon)
    for y in range(sensor.y - distance, sensor.y + distance + 1):
        width = distance - abs(sensor.y - y)
        for x in range(sensor.x - width, sensor.x + width + 1):
            whats_there = grid.get(Coord(x, y), None)
            if not whats_there:
                logging.debug(f"Scanned: {Coord(x, y)}")
                grid[Coord(x, y)] = SCANNED
            else:
                logging.debug(f"Avoided: {Coord(x, y)}, {whats_there}")

    return grid


def print_grid(grid: dict[Coord, str]):
    """Print the grid"""
    min_x = min(coord.x for coord in grid.keys())
    max_x = max(coord.x for coord in grid.keys())
    min_y = min(coord.y for coord in grid.keys())
    max_y = max(coord.y for coord in grid.keys())

    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            row += grid.get(Coord(x, y), ".")
        print(f"{y:>3d}: {row}")
    print()


@perf
def part1(data: dict[Coord, Coord], row: int = 10) -> int:
    """Solve part 1"""
    sensors = {Coord(8, 7): SENSOR}
    beacons = {coord: BEACON for coord in data.values()}
    grid = {**sensors, **beacons}

    for sensor, beacon in data.items():
        grid = fill_scan_area(grid, sensor, beacon)

    print_grid(grid)
    scan_row = {coord: grid[coord] for coord in grid if coord.y == row}
    print("Scan row:")
    print_grid(scan_row)
    return sum(1 for coord in scan_row if scan_row[coord] == SCANNED)



@perf
def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
