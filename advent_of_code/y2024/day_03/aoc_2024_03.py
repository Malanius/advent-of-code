import logging
import pathlib
import re

from advent_of_code.y2024.day_03.arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


MULTIPLY_PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.splitlines()


@perf
def part1(data: list[str]) -> int:
    """Solve part 1"""
    total = 0
    for line in data:
        operations = re.findall(MULTIPLY_PATTERN, line)
        for operation in operations:
            total += int(operation[0]) * int(operation[1])
    return total


@perf
def part2(data: list[str]) -> int:
    """Solve part 2"""
    INSTRUCTION_PATTERN = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))")
    total = 0
    mul_enabled = True
    for line in data:
        operations = re.findall(INSTRUCTION_PATTERN, line)
        for operation in operations:
            if operation[0] == "do()":
                mul_enabled = True
            elif operation[0] == "don't()":
                mul_enabled = False
            elif mul_enabled:
                total += int(operation[1]) * int(operation[2])
    return total


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

    data_file = "example_2.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
