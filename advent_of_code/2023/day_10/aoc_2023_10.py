import logging
import pathlib
from collections import defaultdict
from copy import deepcopy
from pprint import pformat
from advent_of_code.common.two_d.direction4 import Direction4

from arguments import init_args
from pipe import Pipe, PipeMap, PipeType, determine_start_pipe_type

from advent_of_code.common.two_d.coord import Coord
from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse(puzzle_input: str) -> tuple[Coord, PipeMap]:
    """Parse input"""
    lines = puzzle_input.splitlines()
    pipe_map = defaultdict[Coord, Pipe](lambda: Pipe(PipeType.GROUND))
    start_coord = Coord(-1, -1)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == ".":
                continue
            coord = Coord(x, y)
            if char == "S":
                start_coord = coord
                continue
            pipe_map[coord] = Pipe(PipeType(char))

    # using deepcopy to avoid mutating the original pipe_map defaultdict in determine_start_pipe_type
    # as each get method call will add a new key to the defaultdict
    start_pipe_type = determine_start_pipe_type(deepcopy(pipe_map), start_coord)
    pipe_map[start_coord] = Pipe(PipeType(start_pipe_type), start=True)

    logging.debug(f"start: {start_coord}")
    logging.debug(f"start pipe type: {start_pipe_type}")
    logging.debug(pformat(pipe_map))

    return start_coord, pipe_map


@perf
def part1(data: tuple[Coord, PipeMap]) -> int:
    """Solve part 1"""
    start_coord, pipe_map = data
    loop_pipes = []
    current_pipe = pipe_map[start_coord]
    current_coord = start_coord
    moving_direction = current_pipe.get_connecting_directions()[0]

    logging.debug(f"start moving direction: {moving_direction}")

    current_coord = current_coord + moving_direction.value
    current_pipe = pipe_map[current_coord]

    while not current_pipe.start:
        current_pipe = pipe_map[current_coord]
        moving_direction = current_pipe.get_next_direction(moving_direction)
        current_coord = current_coord + moving_direction.value
        loop_pipes.append(current_pipe)

    logging.debug(f"loop_pipes: {loop_pipes}")
    return int(len(loop_pipes) / 2)


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
