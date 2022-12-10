from dataclasses import dataclass, field
import pathlib
import logging

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


@dataclass
class Cpu:
    reg_x: int = 1
    cycles: int = 0
    states_during: list[int] = field(default_factory=list)

    def tick(self) -> None:
        """Tick the clock"""
        self.cycles += 1
        self.states_during.append(self.reg_x)
        logging.debug(f"tick: Cycle {self.cycles}, X: {self.reg_x}")

    def noop(self) -> None:
        """No operation, takes one cycle to complete"""
        self.tick()

    def addx(self, value: int) -> None:
        """Add value to register, completes after two cycles"""
        self.tick()
        self.tick()
        self.reg_x += value

    def execute(self, instruction: str) -> None:
        """Execute instruction"""
        logging.debug(f"--- Executing instruction: {instruction} ---")
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
