import logging
import pathlib
from copy import deepcopy

from advent_of_code_2022.day_14.grid import Grid
from advent_of_code_2022.day_14.simulation import Simulation
from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent

logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input: str, interactive: bool = False) -> Grid:
    """Parse input"""
    simulation = Grid.construct(puzzle_input, interactive)
    return simulation


@perf
def part1(grid: Grid, interactive: bool = False):
    """Solve part 1"""
    simulation = Simulation(grid, interactive=interactive)
    simulation.run()
    return simulation.sand_count


@perf
def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    interactive = True
    data = parse(puzzle_input, interactive)
    solution1 = part1(deepcopy(data), interactive)
    solution2 = part2(deepcopy(data))
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
