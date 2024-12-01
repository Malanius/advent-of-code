import logging
import pathlib
import pyparsing as pp

from arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.splitlines()


def get_digits(input: str) -> list[str]:
    return [num for num in input if num.isdigit()]


@perf
def part1(data: list[str]):
    """Solve part 1"""
    first_and_last_nums = []
    for line in data:
        numbers = get_digits(line)
        first_and_last_nums.append(int(numbers[0] + numbers[-1]))

    return sum(first_and_last_nums)


valid_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

digits = pp.oneOf(list(valid_digits.keys()) + list(valid_digits.values()))


def replace_words(input: str) -> str:
    for word, digit in valid_digits.items():
        input = input.replace(word, digit)
    return input


def convert_to_number(input: str) -> str:
    if input.isdigit():
        return input
    return valid_digits[input]


@perf
def part2(data: list[str]):
    """Solve part 2"""
    first_and_last_nums = []
    for line in data:
        scanned = list(digits.scan_string(line, overlap=True))
        first_match: str = scanned[0][0].as_list()[0]
        last_match: str = scanned[-1][0].as_list()[0]
        first_match = convert_to_number(first_match)
        last_match = convert_to_number(last_match)
        first_and_last_nums.append(int(first_match + last_match))

    return sum(first_and_last_nums)


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

    data_file = "example1.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
