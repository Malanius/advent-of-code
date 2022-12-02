from enum import Enum, StrEnum
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


def is_win(hand1: Hand, hand2: Hand) -> bool:
    """Determine if hand1 beats hand2"""
    if hand1 == Hand.ROCK:
        return hand2 == Hand.SCISSORS
    if hand1 == Hand.PAPER:
        return hand2 == Hand.ROCK
    return hand2 == Hand.PAPER


def is_draw(hand1: Hand, hand2: Hand) -> bool:
    """Determine if hand1 and hand2 are a draw"""
    return hand1 == hand2


def play_win(elf_hand: Hand) -> Hand:
    """Play a winning hand"""
    if elf_hand == Hand.ROCK:
        return Hand.PAPER
    if elf_hand == Hand.PAPER:
        return Hand.SCISSORS

    return Hand.ROCK


def play_draw(elf_hand: Hand) -> Hand:
    """Play a draw hand"""
    return elf_hand


def play_loss(elf_hand: Hand) -> Hand:
    """Play a losing hand"""
    if elf_hand == Hand.ROCK:
        return Hand.SCISSORS
    if elf_hand == Hand.PAPER:
        return Hand.ROCK
    return Hand.PAPER


@perf
def part1(data: list[str]) -> int:
    """Calculate total score for provided strategy"""
    score = 0
    for line in data:
        elf_play, my_play = line.split()
        elf_hand = convert_hand(elf_play)
        my_hand = convert_hand(my_play)
        if is_win(my_hand, elf_hand):
            score += WIN_SCORE
        elif is_draw(my_hand, elf_hand):
            score += DRAW_SCORE
        score += my_hand.value
    return score


@perf
def part2(data: list[str]) -> int:
    """Solve part 2"""
    score = 0
    for line in data:
        elf_play, my_strategy = line.split()
        elf_hand = convert_hand(elf_play)
        if my_strategy == Outcome.WIN:
            my_hand = play_win(elf_hand)
            score += WIN_SCORE
        elif my_strategy == Outcome.DRAW:
            my_hand = play_draw(elf_hand)
            score += DRAW_SCORE
        else:
            my_hand = play_loss(elf_hand)
        score += my_hand.value
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
