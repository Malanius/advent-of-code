from copy import deepcopy
import pathlib
import re
from collections import deque
from dataclasses import dataclass

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


INIT_PATTERN = re.compile(r"(\d+):(.*)")
COMMAND_PATTERN = re.compile(r"move (\d+) from (\d+) to (\d+)")


@dataclass
class Move:
    count: int
    source: int
    target: int


@dataclass
class CrateState:
    stacks: dict[int, deque[str]]

    def process_move_by_single_crate(self, move: Move):
        source = self.stacks[move.source]
        target = self.stacks[move.target]
        target.extend(source.pop() for _ in range(move.count))

    def process_move_by_multiple_crates(self, move: Move):
        source = self.stacks[move.source]
        target = self.stacks[move.target]
        taken = reversed([source.pop() for _ in range(move.count)])
        target.extend(taken)

    def get_top_crates(self) -> str:
        return "".join(stack[-1] for stack in self.stacks.values())


def parse_init(init_input):
    """Parse initial state"""
    init_data = {}
    for line in init_input.splitlines():
        match = INIT_PATTERN.match(line)
        if match:
            init_data[int(match.group(1))] = deque(match.group(2).strip().split(","))
    return init_data


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
    state = CrateState(init)
    for move in moves:
        state.process_move_by_single_crate(move)
    return state.get_top_crates()


@perf
def part2(init, moves):
    """Solve part 2"""
    state = CrateState(init)
    for move in moves:
        state.process_move_by_multiple_crates(move)
    return state.get_top_crates()


def solve(init_input, moves_input):
    """Solve the puzzle for the given input"""
    init_data = parse_init(init_input)
    moves = parse_moves(moves_input)
    solution1 = part1(deepcopy(init_data), moves)
    solution2 = part2(deepcopy(init_data), moves)
    return solution1, solution2


if __name__ == "__main__":
    init_input = (PUZZLE_DIR / "data-init.txt").read_text().strip()
    moves_input = (PUZZLE_DIR / "data-moves.txt").read_text().strip()
    solutions = solve(init_input, moves_input)
    print("\n".join(str(solution) for solution in solutions))
