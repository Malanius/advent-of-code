import logging
import pathlib

from advent_of_code.util.perf import perf
from advent_of_code.y2022.day_14.arguments import init_args
from advent_of_code.y2022.day_14.grid import Grid
from advent_of_code.y2022.day_14.simulation import Simulation

PUZZLE_DIR = pathlib.Path(__file__).parent

logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input: str, interactive: bool = False, bedrock: bool = False) -> Grid:
    """Parse input"""
    return Grid.construct(puzzle_input, interactive, bedrock)


@perf
def part1(grid: Grid, interactive: bool = False):
    """Solve part 1"""
    simulation = Simulation(grid, interactive=interactive)
    simulation.run()
    return simulation.sand_count


@perf
def part2(grid: Grid, interactive: bool = False) -> int:
    """Solve part 2"""
    simulation = Simulation(grid, interactive=interactive, bedrock=True)
    simulation.run()
    return simulation.sand_count


def solve(puzzle_input: str, interactive_part: int | None) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input, interactive_part is not None)
    solution1 = part1(data, interactive_part == 1)

    data = parse(puzzle_input, interactive_part is not None, bedrock=True)
    solution2 = part2(data, interactive_part == 2)
    return solution1, solution2


if __name__ == "__main__":
    args = init_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    data_file = "example.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()

    solutions = solve(puzzle_input, args.interactive)
    print("\n".join(str(solution) for solution in solutions))
