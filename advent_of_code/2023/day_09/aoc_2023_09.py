import logging
import pathlib
from itertools import pairwise

from arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")

type Sequences = list[list[int]]


def parse(puzzle_input: str) -> Sequences:
    """Parse input"""
    sequences = []
    for line in puzzle_input.splitlines():
        sequences.append([int(number) for number in line.split()])
    return sequences


def find_next_sequence_number(sequence: list[int], reversed=False) -> int:
    """Find the next number in the sequence"""
    if all(number == 0 for number in sequence):
        return 0
    sequence_diffs = [pair[1] - pair[0] for pair in pairwise(sequence)]
    next = find_next_sequence_number(sequence_diffs, reversed)
    message = f"{sequence_diffs} -> {next}" if not reversed else f"{next} <- {sequence_diffs}"
    logging.debug(message)
    return sequence[-1] + next


@perf
def part1(data: Sequences):
    """Solve part 1"""
    logging.debug("=== Part 1 ===")
    predictions = []
    for sequence in data:
        next = find_next_sequence_number(sequence)
        logging.debug(f"{sequence} -> {next}")
        predictions.append(next)
        logging.debug("")
    logging.debug(predictions)

    return sum(predictions)


@perf
def part2(data: Sequences):
    """Solve part 2"""
    logging.debug("=== Part 2 ===")
    history = []
    for sequence in data:
        previous = find_next_sequence_number(list(reversed(sequence)), reversed=True)
        history.append(previous)
        logging.debug(f"{previous} <- {sequence}\n")
    logging.debug(history)

    return sum(history)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    logging.debug("=== Results ===")
    return solution1, solution2


if __name__ == "__main__":
    args = init_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    data_file = "example.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    solutions = solve(puzzle_input)
    logging.debug("\n".join(str(solution) for solution in solutions))
