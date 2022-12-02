from enum import Enum
import pathlib

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent

WIN_SCORE = 6
DRAW_SCORE = 3


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


HAND_MAP = {
    "A": Hand.ROCK,
    "B": Hand.PAPER,
    "C": Hand.SCISSORS,
    "X": Hand.ROCK,
    "Y": Hand.PAPER,
    "Z": Hand.SCISSORS,
}


def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.splitlines()


def convert_hand(hand: str) -> Hand:
    """Convert a hand string to a Hand enum"""
    return HAND_MAP[hand]


def is_win(hand1: Hand, hand2: Hand) -> bool:
    """Determine if hand1 beats hand2"""
    if hand1 == Hand.ROCK:
        return hand2 == Hand.SCISSORS
    if hand1 == Hand.PAPER:
        return hand2 == Hand.ROCK
    if hand1 == Hand.SCISSORS:
        return hand2 == Hand.PAPER


def is_draw(hand1: Hand, hand2: Hand) -> bool:
    """Determine if hand1 and hand2 are a draw"""
    return hand1 == hand2


@perf
def part1(data: list[str]) -> int:
    """Calculate total score for provided strategy"""
    score = 0
    for line in data:
        elf_hand, my_hand = line.split()
        elf_hand = convert_hand(elf_hand)
        my_hand = convert_hand(my_hand)
        if is_win(my_hand, elf_hand):
            score += WIN_SCORE
        elif is_draw(my_hand, elf_hand):
            score += DRAW_SCORE
        score += my_hand.value
    return score


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
