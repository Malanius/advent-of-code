import logging
import pathlib
import re
from advent_of_code_2022.day_15.arguments import init_args

from advent_of_code_2022.day_15.coord import Boundaries, Coord
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
def get_scan_coverage_bounds(sensor_to_beacons: dict[Coord, Coord]) -> Boundaries:
    max_x = max(coord.x for coord in sensor_to_beacons.keys())
    max_y = max(coord.y for coord in sensor_to_beacons.keys())
    min_x = min(coord.x for coord in sensor_to_beacons.keys())
    min_y = min(coord.y for coord in sensor_to_beacons.keys())

    for sensor, beacon in sensor_to_beacons.items():
        distance_to_beacon = sensor.distance(beacon)

        sensor_max_x = sensor.x + distance_to_beacon
        if sensor_max_x > max_x:
            max_x = sensor_max_x

        sensor_max_y = sensor.y + distance_to_beacon
        if sensor_max_y > max_y:
            max_y = sensor_max_y

        sensor_min_x = sensor.x - distance_to_beacon
        if sensor_min_x < min_x:
            min_x = sensor_min_x

        sensor_min_y = sensor.y - distance_to_beacon
        if sensor_min_y < min_y:
            min_y = sensor_min_y

    return Boundaries(max_x, max_y, min_x, min_y)


@perf
def part1(data: dict[Coord, Coord], row: int = 10) -> int:
    """Solve part 1"""
    boundaries = get_scan_coverage_bounds(data)
    min_x = boundaries.min_x
    max_x = boundaries.max_x
    logging.debug(f"min_x: {min_x}, max_x: {max_x}")

    scanned_row = {}
    for x in range(min_x, max_x + 1):
        logging.debug(f"=== Scanning x: {x}, y: {row} ===")
        coord = Coord(x, row)
        for sensor, beacon in data.items():
            if sensor.y == row:
                scanned_row[sensor] = SENSOR

            if beacon.y == row:
                scanned_row[beacon] = BEACON

            distance_to_sensor = coord.distance(sensor)
            sensor_scan_distance = sensor.distance(beacon)
            logging.debug(
                f"coord: {coord}, sensor: {sensor}, beacon: {beacon}, "
                f"distance_to_sensor: {distance_to_sensor}, "
                f"sensor_scan_distance: {sensor_scan_distance}"
            )

            if distance_to_sensor <= sensor_scan_distance:
                logging.debug(f"Scanned: {coord}")
                scanned_row[coord] = SCANNED
                break  # No need to check other sensors
        logging.debug("")

    logging.debug("Scanned row:")
    print_bounds = Boundaries(max_x, row, min_x, row)
    logging.debug(grid_repr(scanned_row, print_bounds))

    return sum(1 for coord in scanned_row.values() if coord == SCANNED)


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
