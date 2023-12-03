import logging
import math
import pathlib
from collections import deque
from typing import DefaultDict

from arguments import init_args

from advent_of_code.common.two_d.coord import Coord
from advent_of_code.common.two_d.direction import Direction
from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")

type EngineSchematic = DefaultDict[Coord, str]

GEAR_SYMBOL = "*"


def parse(puzzle_input: str) -> EngineSchematic:
    """Parse input"""
    grid = DefaultDict[Coord, str](lambda: ".")
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            if not char == ".":
                grid[Coord(x, y)] = char

    logging.debug(grid)
    return grid


def find_symbols(grid: EngineSchematic) -> list[Coord]:
    """Find all coordinates of all symbols"""
    coords = []
    for coord, char in grid.items():
        if not char.isdigit():
            coords.append(coord)
    logging.debug("Found symbols coordinates:")
    logging.debug(coords)
    return coords


def find_neighbour_number(grid: EngineSchematic, coord: Coord) -> list[Coord]:
    """Find all neighbours of a given coordinate"""
    neighbours = []
    for direction in Direction:
        neighbour = coord + direction.value
        if grid[neighbour].isdigit():
            neighbours.append(neighbour)
    logging.debug(f"Found neighbours of {coord}:")
    logging.debug(neighbours)
    return neighbours


def scan_whole_number(grid: EngineSchematic, coord: Coord) -> dict[Coord, int]:
    """Find all all digits of the number on it's line"""
    number_dq: deque[int] = deque([int(grid[coord])])
    scan_start_coord = coord
    number_start_coord = coord

    logging.debug(f"Scanning left from number at {coord}")
    # scan for digits to the left, stop on non-digit
    left = Direction.LEFT.value
    while grid[coord + left].isdigit():
        logging.debug(f"Found digit at {coord + left}")
        number_dq.appendleft(int(grid[coord + left]))
        number_start_coord += left
        coord += left

    coord = scan_start_coord

    logging.debug(f"Scanning right from number at {coord}")
    # scan for digits to the right, stop on non-digit
    right = Direction.RIGHT.value
    while grid[coord + right].isdigit():
        logging.debug(f"Found digit at {coord + right}")
        number_dq.append(int(grid[coord + right]))
        coord += right

    number = int("".join(str(digit) for digit in number_dq))
    logging.debug(f"Found part number {number} at {number_start_coord}")
    return {number_start_coord: number}


@perf
def part1(data: EngineSchematic) -> int:
    """Solve part 1"""
    symbols = find_symbols(data)
    part_numbers: dict[Coord, int] = {}
    for symbol in symbols:
        near_numbers = find_neighbour_number(data, symbol)
        for near_number in near_numbers:
            found_part_nr = scan_whole_number(data, near_number)
            part_numbers.update(found_part_nr)

    logging.debug("Found part numbers:")
    logging.debug(part_numbers)

    return sum(part_numbers.values())


def find_possible_gears(grid: EngineSchematic) -> list[Coord]:
    """Find all coordinates of all symbols"""
    coords = []
    for coord, char in grid.items():
        if char == GEAR_SYMBOL:
            coords.append(coord)
    logging.debug("Found possible gears coordinates:")
    logging.debug(coords)
    return coords


@perf
def part2(data: EngineSchematic) -> int:
    """Solve part 2"""
    possible_gears = find_possible_gears(data)
    gears: dict[Coord, int] = {}

    for gear in possible_gears:
        near_numbers = find_neighbour_number(data, gear)
        near_part_numbers: dict[Coord, int] = {}
        for near_number in near_numbers:
            found_part_nr = scan_whole_number(data, near_number)
            near_part_numbers.update(found_part_nr)
        logging.debug(f"Found {len(near_part_numbers)} part numbers near gear {gear}")
        if len(near_part_numbers) == 2:
            gears[gear] = math.prod(near_part_numbers.values())

    logging.debug("Found gears:")
    logging.debug(gears)

    return sum(gears.values())


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    args = init_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    data_file = "example.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
