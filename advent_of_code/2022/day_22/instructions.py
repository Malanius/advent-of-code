import re
from typing import Literal

Instruction = tuple[int, Literal["L", "R", "-"]]


def parse_instructions(puzzle_input: str) -> list[Instruction]:
    """Parse input to isntructions"""
    instructions = []
    steps = re.split(r"[LR]", puzzle_input)
    turns = re.split(r"\d+", puzzle_input)[1:]
    for step, turn in zip(steps, turns):
        instructions.append((int(step), turn if turn else "-"))
    return instructions
