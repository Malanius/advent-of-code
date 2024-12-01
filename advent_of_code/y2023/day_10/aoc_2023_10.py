import logging
import pathlib
from pprint import pformat

from arguments import init_args
from pipe import Pipe, PipeMap, PipeType, determine_start_pipe_type

from advent_of_code.common.two_d.coord import Coord
from advent_of_code.common.two_d.direction4 import Direction4
from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_pipe_loop(data: tuple[Coord, PipeMap]) -> set[Coord]:
    start_coord, pipe_map = data
    current_pipe = pipe_map[start_coord]
    loop_pipes: set[Coord] = {start_coord}
    current_coord = start_coord
    moving_direction = current_pipe.get_connecting_directions()[0]

    logging.debug(f"start moving direction: {moving_direction}")

    current_coord = current_coord + moving_direction.value
    current_pipe = pipe_map[current_coord]

    while not current_pipe.start:
        current_pipe = pipe_map[current_coord]
        moving_direction = current_pipe.get_next_direction(moving_direction)
        current_coord = current_coord + moving_direction.value
        loop_pipes.add(current_coord)

    logging.debug(f"loop_pipes: {loop_pipes}")
    return loop_pipes

type Data = tuple[PipeMap, set[Coord]]

def parse(puzzle_input: str) -> Data:
    """Parse input"""
    lines = puzzle_input.splitlines()
    pipe_map = {}
    start_coord = Coord(-1, -1)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            coord = Coord(x, y)
            if char == "S":
                start_coord = coord
                continue
            pipe_map[coord] = Pipe(PipeType(char))

    start_pipe_type = determine_start_pipe_type(pipe_map, start_coord)
    pipe_map[start_coord] = Pipe(PipeType(start_pipe_type), start=True)
    loop_pipes = get_pipe_loop((start_coord, pipe_map))

    logging.debug(f"start: {start_coord}")
    logging.debug(f"start pipe type: {start_pipe_type}")
    logging.debug(pformat(pipe_map))

    return pipe_map, loop_pipes


@perf
def part1(data: Data) -> int:
    """Solve part 1"""
    _, loop_pipes = data
    return int(len(loop_pipes) / 2)


EDGES: set[PipeType] = {
    # WHY???
    # PipeType.L_BEND,
    # PipeType.J_BEND,
    PipeType.F_BEND,
    PipeType.BEND_7,
    PipeType.VERTICAL,
}


def count_edges(
    coord: Coord, direction, pipe_map: PipeMap, loop_pipes: set[Coord]
) -> int:
    curent_coord = coord + direction.value
    edges: set[Coord] = set()
    while True:
        current_pipe = pipe_map.get(curent_coord, Pipe(PipeType.GROUND))
        if curent_coord in loop_pipes and current_pipe.type in EDGES:
            edges.add(curent_coord)
        curent_coord = curent_coord + direction.value
        if curent_coord not in pipe_map:
            break
    logging.debug(f"count_edges: {coord} {direction} = {len(edges)}")
    return len(edges)


@perf
def part2(data: Data) -> int:
    """Solve part 2"""
    pipe_map, loop_pipes = data
    enclosed: set[Coord] = set()

    for coord in pipe_map.keys():
        logging.debug(f"checking {coord}")
        if coord in loop_pipes:
            continue  # skip loop pipes
        loop_edges_right = count_edges(coord, Direction4.RIGHT, pipe_map, loop_pipes)
        loop_edges_left = count_edges(coord, Direction4.LEFT, pipe_map, loop_pipes)
        if loop_edges_right % 2 != 0 and loop_edges_left % 2 != 0:
            logging.debug(f"enclosed: {coord}")
            enclosed.add(coord)

    return len(enclosed)


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
