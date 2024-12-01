import pathlib
import time


PUZZLE_DIR = pathlib.Path(__file__).parent


def parse(puzzle_input: str) -> list[int]:
    """Parse input"""
    splitted = puzzle_input.split(',')
    return [int(value) for value in splitted]


# Not fastest way to run, but write, let's hope part 2 is not for more days...
def part1(data: list[int], days: int) -> int:
    """Solve part 1"""
    start = time.perf_counter()
    for i in range(0, days):
        # print(f"Day {i:>2}: {data}")
        new_data: list[int] = []
        births: list[int] = []
        for fish_timer in data:
            if fish_timer == 0:
                new_data.append(6)
                births.append(8)
                continue
            timer = fish_timer - 1
            new_data.append(timer)
        data = new_data + births
    end = time.perf_counter()
    print(f"Solved {days} days in {(end - start) * 1_000:0.4f} ms")
    return len(data)


def part2(data: list[int], days: int):
    """Solve part 2"""
    start = time.perf_counter()

    # TODO: is there better way to do this?
    # Is anyone surprised that numbers can be keys like me?
    data_dict = {}
    for fish in data:
        if fish in data_dict:
            data_dict[fish] += 1
        else:
            data_dict[fish] = 1

    # NOTE: not so pretty, but working and fast!
    for i in range(0, days):
        # print(f"Day {i:>2}: {data_dict}")

        # Count births before the tick
        births = 0
        if 0 in data_dict:
            births = data_dict[0]

        # Shift all keys by -1
        data_dict = {key-1: value for (key, value) in data_dict.items()}

        # Convert any -1 fishes to 6
        if -1 in data_dict:
            if 6 in data_dict:
                data_dict[6] += data_dict[-1]
            else:
                data_dict[6] = data_dict[-1]
            data_dict.pop(-1)

        # Finally add baby fishes
        # No need to check for key since they will go to 7 on next tick
        data_dict[8] = births

    end = time.perf_counter()
    print(f"Solved {days} days in {(end - start) * 1_000:0.4f} ms")
    return sum([value for value in data_dict.values()])


def solve(puzzle_input: str):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data, days=80)
    solution2 = part2(data, days=256)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
