import logging
import pathlib

from advent_of_code.common.two_d.coord import Coord
from advent_of_code.common.two_d.direction8 import Direction8
from advent_of_code.y2024.day_04.arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")

Crossword = dict[Coord, str]

def parse(puzzle_input: str) -> Crossword:
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


def check_word(grid: Crossword, start_coord: Coord, word: str):
    found_words = 0
    for direction in Direction8:
        logging.debug(f"Checking direction {direction}")
        for index, char in enumerate(word):
            logging.debug(f"Checking {char} at {start_coord}")
            checked_coord = start_coord + Coord(
                index * direction.value.x, index * direction.value.y
            )
            if grid.get(checked_coord) != char:
                logging.debug(f"Failed at {checked_coord}")
                break
        else:
            logging.debug(f"Found {word} at {start_coord}")
            found_words += 1
    return found_words


@perf
def part1(data: dict[Coord, str]) -> int:
    """Solve part 1"""
    word = "XMAS"
    count = 0
    for coord, char in data.items():
        if char == word[0]:
            count += check_word(data, coord, word)
    return count


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
