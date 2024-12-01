import pathlib
from collections import deque

import pytest

import advent_of_code.y2022.day_05.aoc_2022_05 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_init():
    puzzle_input = (PUZZLE_DIR / "example-init.txt").read_text().strip()
    return solver.parse_init(puzzle_input)


@pytest.fixture
def example_moves():
    puzzle_input = (PUZZLE_DIR / "example-moves.txt").read_text().strip()
    return solver.parse_moves(puzzle_input)


@pytest.fixture
def data_init():
    puzzle_input = (PUZZLE_DIR / "data-init.txt").read_text().strip()
    return solver.parse_init(puzzle_input)


@pytest.fixture
def data_moves():
    puzzle_input = (PUZZLE_DIR / "data-moves.txt").read_text().strip()
    return solver.parse_moves(puzzle_input)


def test_parse_init(example_init):
    """Test that init input is parsed properly"""
    assert example_init == {
        1: deque(["Z", "N"]),
        2: deque(["M", "C", "D"]),
        3: deque(["P"]),
    }


def test_parse_moves(example_moves):
    """Test that moves input is parsed properly"""
    assert example_moves == [
        solver.Move(1, 2, 1),
        solver.Move(3, 1, 3),
        solver.Move(2, 2, 1),
        solver.Move(1, 1, 2),
    ]


def test_part1_example(example_init, example_moves):
    """Test part 1 on example input"""
    assert solver.part1(example_init, example_moves) == "CMZ"


def test_part1_data(data_init, data_moves):
    """Test part 1 on example input"""
    assert solver.part1(data_init, data_moves) == "PSNRGBTFT"


def test_part2_example(example_init, example_moves):
    """Test part 2 on example input"""
    assert solver.part2(example_init, example_moves) == "MCD"


def test_part2_data(data_init, data_moves):
    """Test part 2 on example input"""
    assert solver.part2(data_init, data_moves) == "BNTZFPMMW"
