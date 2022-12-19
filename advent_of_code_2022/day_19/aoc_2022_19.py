import logging
import pathlib
import re
from dataclasses import dataclass
from typing import Generator

from advent_of_code_2022.day_19.arguments import init_args
from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")

BLUEPRINT_PATTERN = re.compile(
    r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
)


@dataclass
class Blueprint:
    id: int
    ore_bot_cost_ores: int
    clay_bot_cost_ores: int
    obsidian_bot_cost_ores: int
    obsidian_bot_cost_clay: int
    geode_bot_cost_ores: int
    geode_bot_cost_obsidian: int

Blueprints = Generator[Blueprint, None, None]


def parse(puzzle_input: str) -> Blueprints:
    """Parse input"""
    for line in puzzle_input.splitlines():
        match = BLUEPRINT_PATTERN.match(line)
        if not match:
            raise ValueError(f"Failed to parse line: {line}")
        yield Blueprint(
            id=int(match.group(1)),
            ore_bot_cost_ores=int(match.group(2)),
            clay_bot_cost_ores=int(match.group(3)),
            obsidian_bot_cost_ores=int(match.group(4)),
            obsidian_bot_cost_clay=int(match.group(5)),
            geode_bot_cost_ores=int(match.group(6)),
            geode_bot_cost_obsidian=int(match.group(7)),
        )


@perf
def part1(data: Blueprints):
    """Solve part 1"""


@perf
def part2(data: Blueprints):
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
