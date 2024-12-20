import logging
import math
import pathlib

from advent_of_code.util.perf import perf
from advent_of_code.y2022.day_19.arguments import init_args
from advent_of_code.y2022.day_19.blueprint import BLUEPRINT_PATTERN, Blueprint
from advent_of_code.y2022.day_19.inventory import Inventory
from advent_of_code.y2022.day_19.optimized_factory import get_max_geodes_opt

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    # filename=PUZZLE_DIR / "log.txt",
    # filemode="w",
)


def parse(puzzle_input: str) -> list[Blueprint]:
    """Parse input"""
    blueprints = []
    for line in puzzle_input.splitlines():
        match = BLUEPRINT_PATTERN.match(line)
        if not match:
            raise ValueError(f"Failed to parse line: {line}")
        blueprints.append(
            Blueprint(
                id=int(match.group(1)),
                ore_bot_cost=Inventory(ore=int(match.group(2))),
                clay_bot_cost=Inventory(ore=int(match.group(3))),
                obsidian_bot_cost=Inventory(
                    ore=int(match.group(4)), clay=int(match.group(5))
                ),
                geode_bot_cost=Inventory(
                    ore=int(match.group(6)), obsidian=int(match.group(7))
                ),
            )
        )
    return blueprints


@perf
def part1(data: list[Blueprint]):
    """Solve part 1"""
    blueprint_output: dict[int, int] = {}
    for blueprint in data:
        blueprint_output[blueprint.id] = get_max_geodes_opt(
            time_left=24,
            blueprint=blueprint,
        )
    print(blueprint_output)
    return sum([id * quality for id, quality in blueprint_output.items()])


@perf
def part2(data: list[Blueprint]):
    """Solve part 2"""
    blueprint_output: dict[int, int] = {}
    # we have only 3 blueprints left
    for blueprint in data[:3]:
        blueprint_output[blueprint.id] = get_max_geodes_opt(
            time_left=32,
            blueprint=blueprint,
        )
    print(blueprint_output)
    return math.prod([geodes for geodes in blueprint_output.values()])


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
