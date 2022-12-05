import pathlib
import re

from attr import dataclass

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


@dataclass
class Move:
    count: int
    source: int
    target: int


COMMAND_PATTERN = re.compile(r"move (\d+) from (\d+) to (\d+)")


def parse_init(puzzle_input):
    """Parse initial state"""


def parse_moves(moves_input: str) -> list[Move]:
    """Parse input commands"""
    commands = []
    for line in moves_input.splitlines():
        match = COMMAND_PATTERN.match(line)
        if match:
            commands.append(Move(*map(int, match.groups())))
    return commands


@perf
def part1(init, moves):
    """Solve part 1"""


@perf
def part2(init, moves):
    """Solve part 2"""


def solve(init_input, moves_input):
    """Solve the puzzle for the given input"""
    init_data = parse_init(init_input)
    moves = parse_moves(moves_input)
    solution1 = part1(init_data, moves)
    solution2 = part2(init_data, moves)
    return solution1, solution2


if __name__ == "__main__":
    init_input = (PUZZLE_DIR / "data-init.csv").read_text().strip()
    moves_input = (PUZZLE_DIR / "data-moves.txt").read_text().strip()
    solutions = solve(init_input, moves_input)
    print("\n".join(str(solution) for solution in solutions))
