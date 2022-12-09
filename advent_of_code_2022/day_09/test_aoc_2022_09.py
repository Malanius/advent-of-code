import pathlib
import pytest
import aoc_2022_09 as solver
from aoc_2022_09 import Direction, MoveCommand, Knot, process_moves

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


def test_head_moves(example):
    """Test that head moves properly"""
    head = Knot()
    process_moves(example, head)
    assert head.visited == [
        (0, 0),  # Start
        # fmt: off
        (1, 0), (2, 0), (3, 0), (4, 0),  # R 4
        (4, 1), (4, 2), (4, 3), (4, 4),  # U 4
        (3, 4), (2, 4), (1, 4),  # L 3
        (1, 3),  # D 1
        (2, 3), (3, 3), (4, 3), (5, 3),  # R 4
        (5, 2),  # D 1
        (4, 2), (3, 2), (2, 2), (1, 2), (0, 2),  # L 5
        (1, 2), (2, 2),  # R 2
        # fmt: on
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
