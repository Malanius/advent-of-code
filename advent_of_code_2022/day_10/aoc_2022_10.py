from dataclasses import dataclass, field
import pathlib

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent


@dataclass
class Cpu:
    reg_x: int = 1
    cycles: int = 0
    states: list[int] = field(default_factory=list)

    def noop(self) -> None:
        """No operation, takes one cycle to complete"""
        self.cycles += 1
        self.states.append(self.reg_x)

    def addx(self, value: int) -> None:
        """Add value to register, takes two cycles to complete"""
        self.noop()
        self.cycles += 1
        self.reg_x += value
        self.states.append(self.reg_x)

    def execute(self, instruction: str) -> None:
        """Execute instruction"""
        match instruction.split():
            case ["noop"]:
                self.noop()
            case ["addx", value]:
                self.addx(int(value))
            case _:
                raise ValueError(f"Unknown instruction: {instruction}")

    def process_instructions(self, instructions: list[str]) -> None:
        """Process a list of instructions"""
        for instruction in instructions:
            self.execute(instruction)


def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.splitlines()


@perf
def part1(data):
    """Solve part 1"""


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
