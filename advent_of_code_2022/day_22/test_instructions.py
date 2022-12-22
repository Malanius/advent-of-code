import pathlib

import pytest

from advent_of_code_2022.day_22.instructions import Instruction, parse_instructions

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def instructions() -> list[Instruction]:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text()
    parts = puzzle_input.split("\n\n")
    return parse_instructions(parts[1])


def test_parse(instructions: str):
    """Test that input is parsed properly"""
    assert instructions == [
        (10, "R"),
        (5, "L"),
        (5, "R"),
        (10, "L"),
        (4, "R"),
        (5, "L"),
        (5, "-"),
    ]
