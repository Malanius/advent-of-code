import logging
import pathlib

from arguments import init_args
from game import DrawSet, Game, ParsedGame

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse_draw(draw: str) -> DrawSet:
    cube_counts = draw.split(", ")
    draw_set: DrawSet = {}
    for count in cube_counts:
        count, color = count.split(" ")
        draw_set[color] = int(count)
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

        parsed_games.append(game)

    return parsed_games


@perf
def part1(data: list[ParsedGame]):
    """Solve part 1"""
    playable_games: list[Game] = []
    for parsed_game in data:
        game = Game(
            id=parsed_game["id"],
            max_counts={"red": 12, "green": 13, "blue": 14},
        )

        for draw in parsed_game["draws"]:
            game.add_draw(draw)

        if game.is_playable:
            playable_games.append(game)

    return sum(game.id for game in playable_games)


@perf
def part2(data):
    """Solve part 2"""
    games: list[Game] = []
    for parsed_game in data:
        game = Game(
            id=parsed_game["id"],
            max_counts={"red": 12, "green": 13, "blue": 14},
        )

        for draw in parsed_game["draws"]:
            game.add_draw(draw)

        games.append(game)

    return sum(game.power for game in games)


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
