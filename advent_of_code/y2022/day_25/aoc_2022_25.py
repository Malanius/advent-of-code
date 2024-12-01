import logging
import pathlib

from arguments import init_args
from converter import dec_to_snafu, snafu_to_dec
from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.splitlines()


@perf
def part1(data: list[str]) -> str:
    """Solve part 1"""
    fuel_amounts = []
    for line in data:
        converted = snafu_to_dec(line)
        fuel_amounts.append(converted)

    total_fuel = sum(fuel_amounts)
    return dec_to_snafu(total_fuel)


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
