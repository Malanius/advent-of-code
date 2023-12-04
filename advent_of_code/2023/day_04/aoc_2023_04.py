import logging
import pathlib

from lottery_card import LotteryCard

from arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input: str) -> list[LotteryCard]:
    """Parse input"""
    cards = []
    for line in puzzle_input.splitlines():
        game, numbers = line.split(":")
        game = int(game.split()[1])
        winning_numbers, card_nubmers = numbers.split("|")
        winning_numbers = [int(number) for number in winning_numbers.split()]
        card_nubmers = [int(number) for number in card_nubmers.split()]
        card: LotteryCard = {
            "id": game,
            "winning_numbers": winning_numbers,
            "card_numbers": card_nubmers,
        }
        logging.debug(card)
        cards.append(card)
    
    return cards


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
    args = init_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    data_file = "example.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
