import pathlib
from enum import Enum, StrEnum

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


class Outcome(StrEnum):
    LOSS = "X"
    DRAW = "Y"
    WIN = "Z"


def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.splitlines()


def convert_hand(hand: str) -> Hand:
    """Convert a hand string to a Hand enum"""
    return HAND_MAP[hand]


def get_outcome(my_hand: Hand, elf_hand: Hand) -> Outcome:
    """Get the outcome of a game"""
    match (my_hand, elf_hand):
        case (Hand.ROCK, Hand.PAPER):
            return Outcome.LOSS
        case (Hand.ROCK, Hand.SCISSORS):
            return Outcome.WIN
        case (Hand.PAPER, Hand.ROCK):
            return Outcome.WIN
        case (Hand.PAPER, Hand.SCISSORS):
            return Outcome.LOSS
        case (Hand.SCISSORS, Hand.ROCK):
            return Outcome.LOSS
        case (Hand.SCISSORS, Hand.PAPER):
            return Outcome.WIN
        case _:
            return Outcome.DRAW


def play_hand(elf_hand: Hand, outcome: Outcome) -> Hand:
    """Play a hand based on the outcome"""
    match (elf_hand, outcome):
        case (Hand.ROCK, Outcome.WIN):
            return Hand.PAPER
        case (Hand.PAPER, Outcome.WIN):
            return Hand.SCISSORS
        case (Hand.SCISSORS, Outcome.WIN):
            return Hand.ROCK

        case (Hand.ROCK, Outcome.LOSS):
            return Hand.SCISSORS
        case (Hand.PAPER, Outcome.LOSS):
            return Hand.ROCK
        case (Hand.SCISSORS, Outcome.LOSS):
            return Hand.PAPER

        case _:
            return elf_hand


def count_score(my_hand: Hand, outcome: Outcome) -> int:
    """Count the score for a hand"""
    hand_score = my_hand.value
    match outcome:
        case Outcome.WIN:
            return hand_score + WIN_SCORE
        case Outcome.DRAW:
            return hand_score + DRAW_SCORE
        case Outcome.LOSS:
            return hand_score


@perf
def part1(data: list[str]) -> int:
    """Calculate total score for provided strategy"""
    score = 0
    for line in data:
        elf_play, my_play = line.split()
        elf_hand = convert_hand(elf_play)
        my_hand = convert_hand(my_play)
        outcome = get_outcome(my_hand, elf_hand)
        score += count_score(my_hand, outcome)
    return score


@perf
def part2(data: list[str]) -> int:
    """Solve part 2"""
    score = 0
    for line in data:
        elf_play, expected_outcome = line.split()
        elf_hand = convert_hand(elf_play)
        outcome = Outcome(expected_outcome)
        my_hand = play_hand(elf_hand, outcome)
        score += count_score(my_hand, outcome)
    return score


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
