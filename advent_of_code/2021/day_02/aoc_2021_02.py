import pathlib
from dataclasses import dataclass
from typing import Literal, TypedDict

import parse

PUZZLE_DIR = pathlib.Path(__file__).parent


class MoveInstruction(TypedDict):
    direction: str
    unit: int


@dataclass
class Submarine:
    horizontal_position: int
    depth: int
    commands: list[str]
    pattern = "{direction} {unit:d}"

    def parse_instruction(self, command: str) -> MoveInstruction:
        match = parse.search(self.pattern, command)
        return match.named

    def move(self, direction: Literal["forward", "down", "up"], unit: int):
        if direction == "forward":
            self.horizontal_position += unit
        # NOTE: down and up are switched as we're under water
        if direction == "down":
            self.depth += unit
        if direction == "up":
            self.depth -= unit

    def run(self):
        """Run the commands"""
        for command in self.commands:
            instruction = self.parse_instruction(command)
            self.move(instruction["direction"], instruction["unit"])

    def get_position(self):
        """Get position of the submarine"""
        return self.horizontal_position * self.depth


@dataclass
class AimingSubmarine(Submarine):
    aim: int

    def move(self, direction: Literal["forward", "down", "up"], unit: int):
        if direction == "forward":
            self.horizontal_position += unit
            self.depth += self.aim * unit
        # NOTE: down and up are switched as we're under water
        if direction == "down":
            self.aim += unit
        if direction == "up":
            self.aim -= unit


def parse_input(puzzle_input: str) -> list[str]:
    return puzzle_input.splitlines()


def part1(data: list[str]) -> int:
    """Solve part 1"""
    submarine = Submarine(0, 0, data)
    submarine.run()
    return submarine.get_position()


def part2(data: list[str]) -> int:
    """Solve part 2"""
    submarine = AimingSubmarine(0, 0, data, 0)
    submarine.run()
    return submarine.get_position()


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
