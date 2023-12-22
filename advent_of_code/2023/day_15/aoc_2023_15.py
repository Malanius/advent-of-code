import logging
import pathlib

from arguments import init_args
from lens_box import LensBox

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.split(",")


def hash(string: str) -> int:
    """Hash a string"""
    hash_value = 0
    for char in string:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    return hash_value


@perf
def part1(data: list[str]) -> int:
    """Solve part 1"""
    logging.debug("=== Part 1 ===")
    hashes = [hash(instruction) for instruction in data]
    logging.debug(hashes)
    return sum(hashes)


@perf
def part2(data: list[str]) -> int:
    """Solve part 2"""
    logging.debug("=== Part 2 ===")
    boxes: dict[int, LensBox] = {}
    for instruction in data:
        if "=" in instruction:
            lens_type, focal_lenght = instruction.split("=")
            box_id = hash(lens_type)
            if box_id not in boxes:
                boxes[box_id] = LensBox(box_id)
            boxes[box_id].add_lens(lens_type, int(focal_lenght))

        elif "-" in instruction:
            lens_type, _ = instruction.split("-")
            box_id = hash(lens_type)
            if box_id not in boxes:
                boxes[box_id] = LensBox(box_id)
            boxes[box_id].remove_lens(lens_type)

        else:
            raise ValueError(f"Invalid instruction: {instruction}")

        logging.debug(f'After "{instruction}":')
        for box in boxes.values():
            if not box.is_empty:
                logging.debug(box)
        logging.debug("")

    return sum(box.focusing_power for box in boxes.values())


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
