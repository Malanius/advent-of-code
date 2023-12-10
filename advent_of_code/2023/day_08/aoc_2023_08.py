import logging
import math
import pathlib
import re
from itertools import cycle
from pprint import pformat

from arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")

MAP_PATTENR = re.compile(r"^(\w+) = \((\w+), (\w+)\)$")


def parse(puzzle_input: str) -> dict[str, str]:
    """Parse input"""
    lines = puzzle_input.splitlines()
    instructions = lines.pop(0)
    lines.pop(0)

    map = {
        "instructions": instructions,
    }

    for line in lines:
        matches = MAP_PATTENR.match(line)
        if matches:
            map[matches.group(1)] = (matches.group(2), matches.group(3))  # type: ignore

    logging.debug(pformat(map))
    return map


def count_path_steps(
    map: dict[str, str], current_location: str, target_location_pattern: re.Pattern
) -> int:
    instructions = cycle(map["instructions"])

    steps = 0
    while not target_location_pattern.match(current_location):
        direction = next(instructions)
        if direction == "L":
            current_location = map[current_location][0]
        elif direction == "R":
            current_location = map[current_location][1]
        else:
            raise ValueError(f"Unknown direction: {direction}")
        steps += 1

    return steps


@perf
def part1(map: dict[str, str]) -> int:
    """Solve part 1"""
    current_location = "AAA"
    target_location = re.compile(r"ZZZ")
    return count_path_steps(map, current_location, target_location)


@perf
def part2(map: dict[str, str]) -> int:
    """Solve part 2"""
    current_locations = [node for node in map if node.endswith("A")]
    target_location = re.compile(r"^\w{2}Z")
    paths = []

    for current_location in current_locations:
        paths.append(count_path_steps(map, current_location, target_location))

    return math.lcm(*paths)


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
