import logging
import pathlib


# from .arguments import init_args
from advent_of_code.util.perf import perf
from advent_of_code.y2024.day_01.arguments import init_args

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")

ParsedInput = tuple[list[int], list[int]]


def parse(puzzle_input: str) -> ParsedInput:
    """Parse input"""
    lines = puzzle_input.splitlines()
    left_list = []
    right_list = []
    for line in lines:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list


@perf
def part1(data: ParsedInput) -> int:
    """Solve part 1"""
    left_list, right_list = data
    total_diff = 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        total_diff += abs(left - right)
    return total_diff


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
