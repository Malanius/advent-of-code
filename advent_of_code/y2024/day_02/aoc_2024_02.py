import logging
import pathlib
from itertools import pairwise

from advent_of_code.y2024.day_02.arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")

ParsedInput = list[list[int]]


def parse(puzzle_input: str) -> ParsedInput:
    """Parse input"""
    return [[int(x) for x in line.split()] for line in puzzle_input.splitlines()]


LOWER_SAFE_BOUND = 1
UPPER_SAFE_BOUND = 3


def is_safe_report(report: list[int]) -> bool:
    """Check if the report is safe"""
    direction = 1 if report[0] < report[1] else -1
    for pair in pairwise(report):
        if (
            abs(pair[0] - pair[1]) > UPPER_SAFE_BOUND
            or abs(pair[0] - pair[1]) < LOWER_SAFE_BOUND
        ):
            return False
        if direction == 1 and pair[0] > pair[1]:
            return False
        if direction == -1 and pair[0] < pair[1]:
            return False
    return True


@perf
def part1(data: ParsedInput) -> int:
    """Solve part 1"""
    safe_reports = [report for report in data if is_safe_report(report)]
    return len(safe_reports)


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
