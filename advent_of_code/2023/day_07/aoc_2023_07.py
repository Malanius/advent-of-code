import logging
import pathlib

from hand import Hand

from arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input: str) -> list[Hand]:
    """Parse input"""
    hands = []
    for line in puzzle_input.splitlines():
        hand, bid = line.split()
        converted_hand = Hand(hand, int(bid))
        hands.append(converted_hand)

    logging.debug(hands)
    return hands


@perf
def part1(data: list[Hand]) -> int:
    """Solve part 1"""
    hands_by_strenght = sorted(
        data, key=lambda hand: (hand.kind.value, hand.sortable_cards), reverse=True
    )
    hands_by_rank = list(reversed(hands_by_strenght))

    winings = 0
    for rank, hand in enumerate(hands_by_rank, start=1):
        logging.debug(f"{hand.cards} {hand.bid} {rank}")
        winings += rank * hand.bid

    return winings


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
