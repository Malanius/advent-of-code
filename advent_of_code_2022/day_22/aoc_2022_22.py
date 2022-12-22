import logging
import pathlib
from typing import Optional

from advent_of_code_2022.day_22.arguments import init_args
from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input):
    """Parse input"""


@perf
def part1(data, interactive: bool = False):
    """Solve part 1"""


@perf
def part2(data, interactive: bool = False):
    """Solve part 2"""


def solve(puzzle_input, interactive_part: Optional[int]) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data, interactive_part == 1)
    solution2 = part2(data, interactive_part == 2)
    return solution1, solution2


if __name__ == "__main__":
    args = init_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    data_file = "example.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    solutions = solve(puzzle_input, args.interactive)
    print("\n".join(str(solution) for solution in solutions))
