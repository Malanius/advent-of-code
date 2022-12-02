from enum import Enum
import pathlib

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.splitlines()


def is_win(hand1: Hand, hand2: Hand) -> bool:
    """Determine if hand1 beats hand2"""
    if hand1 == Hand.ROCK:
        return hand2 == Hand.SCISSORS
    if hand1 == Hand.PAPER:
        return hand2 == Hand.ROCK
    if hand1 == Hand.SCISSORS:
        return hand2 == Hand.PAPER


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
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
