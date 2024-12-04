import logging
import pathlib

from advent_of_code.common.two_d.coord import Coord
from advent_of_code.y2024.day_04.arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input: str) -> dict[Coord, str]:
    """Parse input"""
    lines = puzzle_input.splitlines()
    data = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            data[Coord(x, y)] = char
    logging.debug("Parsed data:")
    logging.debug(data)
    logging.debug("-" * len(lines[0]))
    return data


@perf
def part1(data):
    """Solve part 1"""


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
