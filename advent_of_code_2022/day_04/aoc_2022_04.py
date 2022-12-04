from collections import namedtuple
import pathlib

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input: str) -> list[tuple[range, range]]:
    """Parse input"""
    data = []
    for line in puzzle_input.splitlines():
        section1, section2 = line.split(",")
        start1, end1 = section1.split("-")
        start2, end2 = section2.split("-")
        data.append((range(int(start1), int(end1)), range(int(start2), int(end2))))
    return data


def is_fully_overlapping(plan1: range, plan2: range) -> bool:
    """Check if two plans are fully overlapping"""
    plan1_set = set(range(plan1.start, plan1.stop + 1))
    plan2_set = set(range(plan2.start, plan2.stop + 1))
    return plan1_set.issubset(plan2_set) or plan2_set.issubset(plan1_set)

@perf
def part1(data: list[tuple[range, range]]) -> int:
    """Solve part 1"""
    return sum(is_fully_overlapping(*plans) for plans in data)


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
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
