import logging
import math
import pathlib
from typing import TypedDict

from arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


class Race(TypedDict):
    time_limit: int
    record_distance: int


def parse(puzzle_input: str) -> list[Race]:
    """Parse input"""
    lines = puzzle_input.splitlines()
    time_line = [int(t) for t in lines[0].split()[1:]]
    distance_line = [int(d) for d in lines[1].split()[1:]]

    races = []
    for time, distance in zip(time_line, distance_line):
        races.append({"time_limit": time, "record_distance": distance})

    return races


def count_ways_to_win(race: Race) -> int:
    """Counts how many ways are there to win the race"""
    time_limit = race["time_limit"]
    time_range = range(1, time_limit)
    current_record = race["record_distance"]
    ways_to_win = 0

    for acceleration in time_range:
        remaining_time = time_limit - acceleration
        traveled_distance = acceleration * remaining_time
        if traveled_distance > current_record:
            ways_to_win += 1

    return ways_to_win


@perf
def part1(data: list[Race]) -> int:
    """Solve part 1"""
    ways_to_win = []
    for race_num, race in enumerate(data, start=1):
        ways = count_ways_to_win(race)
        logging.debug(f"Race {race_num}: {ways} ways to win")
        ways_to_win.append(ways)

    return math.prod(ways_to_win)


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
    args = init_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    data_file = "example.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
