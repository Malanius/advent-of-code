import logging
import pathlib

from arguments import init_args
from hand import Hand
from joker_hand import JokerHand

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse_part1(puzzle_input: str) -> list[Hand]:
    """Parse input"""
    hands = []
    for line in puzzle_input.splitlines():
        hand, bid = line.split()
        converted_hand = Hand(hand, int(bid))
        hands.append(converted_hand)

    logging.debug(hands)
    return hands


def parse_part2(puzzle_input: str) -> list[JokerHand]:
    """Parse input"""
    hands = []
    for line in puzzle_input.splitlines():
        hand, bid = line.split()
        converted_hand = JokerHand(hand, int(bid))
        hands.append(converted_hand)

    # logging.debug(hands)
    return hands


@perf
def part1(puzzle_input: str) -> int:
    """Solve part 1"""
    hands = parse_part1(puzzle_input)
    hands_by_strenght = sorted(
        hands, key=lambda hand: (hand.kind.value, hand.sortable_cards), reverse=True
    )
    hands_by_rank = list(reversed(hands_by_strenght))

    winings = 0
    for rank, hand in enumerate(hands_by_rank, start=1):
        logging.debug(f"{hand.cards} {hand.bid} {rank}")
        winings += rank * hand.bid

    return winings


@perf
def part2(puzzle_input: str) -> int:
    """Solve part 2"""
    hands = parse_part2(puzzle_input)
    hands_by_strenght = sorted(
        hands, key=lambda hand: (hand.kind.value, hand.sortable_cards), reverse=True
    )
    hands_by_rank = list(reversed(hands_by_strenght))

    winings = 0
    for rank, hand in enumerate(hands_by_rank, start=1):
        # logging.debug(f"{hand.sortable_cards} {hand.cards} {hand.bid} {rank}")
        winings += rank * hand.bid

    return winings


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    solution1 = part1(puzzle_input)
    solution2 = part2(puzzle_input)
    return solution1, solution2


if __name__ == "__main__":
    args = init_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    data_file = "example2.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
