import logging
import pathlib
import re

from advent_of_code_2022.day_15.arguments import init_args
from advent_of_code_2022.day_15.coord import Boundaries, Coord
from advent_of_code_2022.day_15.sensor import Sensor
from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")

input_regex = re.compile(
    r"^Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)$"
)
SENSOR = "S"
BEACON = "B"
SCANNED = "#"
EMPTY = "."


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


def blend_coverage_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Blend the overlapping ranges together"""
    ranges = sorted(ranges, key=lambda x: x[0])
    blended_ranges = [ranges[0]]
    for start, end in ranges:
        logging.debug(f"Blended: {blended_ranges}")
        logging.debug(f"Current: {start, end}")

        last_start, last_end = blended_ranges[-1]
        if start <= last_end + 1 and end >= last_end:
            blended_ranges[-1] = (last_start, end)
        elif start <= last_end and end <= last_end:
            continue
        else:
            blended_ranges.append((start, end))

    return blended_ranges


def get_sensors_coverage_at_row(sensors: set[Sensor], row: int):
    """Get the coverage of the sensors at the given row"""
    coverage_ranges = [
        sensor.get_coverage_at_row(row)
        for sensor in sensors
        if sensor.get_coverage_at_row(row)
    ]
    logging.debug(f"Coverage ranges: {coverage_ranges}")
    # not sure why, but mypy doesn't see the None check in the list comprehension
    blended_ranges = blend_coverage_ranges(coverage_ranges)  # type: ignore[arg-type]
    logging.debug(f"Blended ranges: {blended_ranges}")
    return blended_ranges


@perf
def part1(data: dict[Coord, Coord], row: int = 10) -> int:
    """Solve part 1"""
    sensors = set()
    for sensor, beacon in data.items():
        scan_range = sensor.distance(beacon)
        sensors.add(Sensor(sensor, scan_range))

    covered_at_row = get_sensors_coverage_at_row(sensors, row)
    beacons_at_row = {beacon for beacon in data.values() if beacon.y == row}
    covered = sum(end - start + 1 for start, end in covered_at_row)
    return covered - len(beacons_at_row)


@perf
def part2(data: dict[Coord, Coord], search_area_size: int = 20) -> int:
    """Solve part 2"""


def solve(puzzle_input: str, row: int, search_area_size: int) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data, row)
    solution2 = part2(data, search_area_size)
    return solution1, solution2


if __name__ == "__main__":
    args = init_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    data_file = "example.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    row = 10 if not args.data else 2_000_000
    search_area_size = 20 if not args.data else 4_000_000
    solutions = solve(puzzle_input, row, search_area_size)
    print("\n".join(str(solution) for solution in solutions))
