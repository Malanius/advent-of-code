import pathlib
import pytest
import aoc_2022_09 as solver
from aoc_2022_09 import Direction, MoveCommand, Head

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example-2.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [
        MoveCommand(Direction("R"), 4),
        MoveCommand(Direction("U"), 4),
        MoveCommand(Direction("L"), 3),
        MoveCommand(Direction("D"), 1),
        MoveCommand(Direction("R"), 4),
        MoveCommand(Direction("D"), 1),
        MoveCommand(Direction("L"), 5),
        MoveCommand(Direction("R"), 2),
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
