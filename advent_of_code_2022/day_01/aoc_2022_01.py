import pathlib

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input: str) -> str:
    """Parse input"""
    return puzzle_input


def count_calories_per_elf(data: str) -> list[int]:
    """Count calories per elf"""
    totals: list[int] = []
    carried: int = 0
    for line in data.splitlines():
        if line == "":
            totals.append(carried)
            carried = 0
        else:
            carried += int(line)
    totals.append(carried)
    return totals


@perf
def part1(data: str) -> int:
    """Find out how many calories top elf has"""
    totals = count_calories_per_elf(data)
    return max(totals)


@perf
def part2(data: str) -> int:
    """Find out how many calories top 3 elfs have"""
    totals = count_calories_per_elf(data)
    top_three = sorted(totals, reverse=True)[:3]
    print(top_three)
    return sum(top_three)


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
