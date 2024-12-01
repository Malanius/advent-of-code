from dataclasses import dataclass, field
import pathlib
import logging

from advent_of_code.util.perf import perf

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

    def get_states_during_cycles(self, start: int = 20, step: int = 40) -> list[int]:
        """Get the state of the register at a given cycle"""
        return self.states_during[start - 1 :: step]

    def get_signal_strength_during_cycles(
        self, start: int = 20, step: int = 40
    ) -> list[int]:
        """Get the signal strength at a given cycle"""
        enumerated = enumerate(self.states_during, 1)
        strengts = [cycle * state for cycle, state in enumerated]
        return strengts[start - 1 :: step]


@dataclass
class Screen:
    width: int = 40
    height: int = 6
    cycle: int = 0
    pixels: list[list[str]] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Initialize the screen"""
        self.pixels = [["." for _ in range(self.width)] for _ in range(self.height)]

    def __str__(self) -> str:
        """Print the screen"""
        return "\n".join("".join(row) for row in self.pixels)

    def tick(self) -> None:
        """Tick the clock"""
        self.cycle += 1
        logging.debug(f"tick: Cycle {self.cycle}")

    def process_signal(self, signal: int) -> None:
        """Process a signal"""
        row = self.cycle // self.width
        col = self.cycle % self.width
        sprite_center = signal
        sprite_left = sprite_center - 1
        sprite_right = sprite_center + 1
        logging.debug(
            f"cycle: {self.cycle} row: {row}, col: {col}, sprite_center: {sprite_center}, sprite_left: {sprite_left}, sprite_right: {sprite_right}"
        )
        # if sprite shape covers actual screen possition, set it to "#"
        if col == sprite_center or col == sprite_left or col == sprite_right:
            logging.debug(f"setting pixel at row: {row}, col: {col} to #")
            self.pixels[row][col] = "#"
        self.tick()

    def process_signals(self, signals: list[int]) -> None:
        """Process a list of signals"""
        for signal in signals:
            self.process_signal(signal)


def parse(puzzle_input: str) -> list[str]:
    """Parse input"""
    return puzzle_input.splitlines()


@perf
def part1(data: list[str]) -> int:
    """Solve part 1"""
    cpu = Cpu()
    cpu.process_instructions(data)
    return sum(cpu.get_signal_strength_during_cycles())


@perf
def part2(data: list[str]) -> str:
    """Solve part 2"""
    cpu = Cpu()
    cpu.process_instructions(data)
    screen = Screen()
    screen.process_signals(cpu.states_during)
    return str(screen)


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
