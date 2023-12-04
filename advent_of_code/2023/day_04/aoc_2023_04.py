import logging
import pathlib
from pprint import pformat

from arguments import init_args
from lottery_card import LotteryCard

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_matching_numbers(winning_numbers: list[int], card_numbers: list[int]) -> int:
    """Get number of matching numbers"""
    matching_numbers = 0
    for number in card_numbers:
        if number in winning_numbers:
            matching_numbers += 1

    return matching_numbers


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
            "matching_numbers": get_matching_numbers(winning_numbers, card_nubmers),
            "count": 1,
        }
        logging.debug(card)
        cards.append(card)

    return cards


def calculate_card_points(card: LotteryCard) -> int:
    """Calculate points for a single card"""
    matching_numbers = card["matching_numbers"]
    if matching_numbers == 0:
        return 0

    return 2 ** (matching_numbers - 1)


@perf
def part1(data: list[LotteryCard]):
    """Solve part 1"""
    logging.debug("=== Part 1 ===")
    total_points = 0
    for card in data:
        card_points = calculate_card_points(card)
        logging.debug(f"Card {card['id']} has {card_points} points")
        total_points += card_points

    return total_points


@perf
def part2(data: list[LotteryCard]):
    """Solve part 2"""
    logging.debug("=== Part 2 ===")
    cards = {card["id"]: card for card in data}
    for card in cards.values():
        matching_numbers = card["matching_numbers"]

        if matching_numbers == 0:
            logging.debug(f"Card {card['id']} has no matching numbers")
            continue

        logging.debug(f"Card {card['id']} has {matching_numbers} matching numbers")
        start_index = card["id"] + 1
        logging.debug(f"Awarding {matching_numbers} cards from index: {start_index}")
        for index in range(start_index, start_index + matching_numbers):
            try:
                cards[index]["count"] += card["count"]
            except KeyError:
                break  # Can't win cards that don't exist
            logging.debug(f"Card {index} now has {cards[index]['count']} cards")
        logging.debug("")

    logging.debug(pformat(cards))
    return sum(card["count"] for card in cards.values())


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
