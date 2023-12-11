import pathlib

import aoc_2023_09 as solver
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example() -> solver.Sequences:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data() -> solver.Sequences:
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example: solver.Sequences):
    """Test that input is parsed properly"""
    assert example == [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45],
    ]


def test_part1_example(example: solver.Sequences):
    """Test part 1 on example input"""
    assert solver.part1(example) == 114


def test_part1_data(data: solver.Sequences):
    """Test part 1 on data input"""
    assert solver.part1(data) == 1708206096


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example: solver.Sequences):
    """Test part 2 on example input"""
    assert solver.part2(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data: solver.Sequences):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
