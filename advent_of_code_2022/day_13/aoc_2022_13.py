from collections import namedtuple
from dataclasses import dataclass
from itertools import zip_longest
import json
import logging
import pathlib
from typing import Generator

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

Pair = namedtuple("Pair", ["left", "right"])


def parse(puzzle_input: str) -> Generator[Pair, None, None]:
    """Parse input"""
    pairs = puzzle_input.split("\n\n")
    for pair in pairs:
        parts = pair.splitlines()
        assert len(parts) == 2
        left = json.loads(parts[0])
        right = json.loads(parts[1])
        yield Pair(left, right)


def is_ordered_correctly(pair: Pair) -> bool:
    """Check if the pair is ordered correctly"""
    logging.debug(f"Checking pair: {pair}")
    left = pair.left
    right = pair.right

    if isinstance(left, int) and isinstance(right, int):
        result = left < right
        logging.debug(f"Pair is ordered correctly: {result}")
        return result

    if isinstance(left, list) and isinstance(right, int):
        pair = Pair(left, [right])
        return is_ordered_correctly(pair)

    if isinstance(left, int) and isinstance(right, list):
        pair = Pair([left], right)
        return is_ordered_correctly(pair)

    if isinstance(left, list) and isinstance(right, list):
        for left_part, right_part in zip_longest(left, right):
            if left_part is None:
                logging.debug(f"Left side ran out of items, right order.")
                return True
            if right_part is None:
                logging.debug(f"Right side ran out of items, not right order.")
                return False
            if is_ordered_correctly(Pair(left_part, right_part)):
                return True
        return False

    raise ValueError(f"Unexpected pair: {pair}")


@perf
def part1(data: Generator[Pair, None, None]) -> int:
    """Solve part 1"""
    correct_pairs = []
    for index, pair in enumerate(data, start=1):
        logging.debug(f"== Pair {index} ==")
        if is_ordered_correctly(pair):
            logging.debug(f"Pair {index} is ordered correctly.")
            correct_pairs.append(index)
        else:
            logging.debug(f"Pair {index} is not ordered correctly.")

    logging.debug(f"Correct pairs: {correct_pairs}")
    return sum(correct_pairs)


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
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
