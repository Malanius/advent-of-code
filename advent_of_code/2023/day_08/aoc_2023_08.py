import logging
import pathlib
import re

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
