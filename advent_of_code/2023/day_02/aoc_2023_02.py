import logging
import pathlib

from arguments import init_args
from game import DrawSet, ParsedGame

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse_draw(draw: str) -> DrawSet:
    cube_counts = draw.split(", ")
    draw_set: DrawSet = {}
    for count in cube_counts:
        count = count.split(" ")
        draw_set[count[1]] = int(count[0])
    return draw_set


def parse(puzzle_input: str) -> list[ParsedGame]:
    """Parse input"""
    parsed_games: list[ParsedGame] = []
    for line in puzzle_input.splitlines():
        game_name, sets = line.split(": ")
        draws = sets.split("; ")
        game: ParsedGame = {
            "id": int(game_name.split(" ")[1]),
            "draws": [],
        }
        for draw in draws:
            game["draws"].append(parse_draw(draw))

        logging.debug(f"Game: {game}")
        parsed_games.append(game)
    return parsed_games


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
