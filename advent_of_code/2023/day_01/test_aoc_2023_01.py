import pathlib

import aoc_2023_01 as solver
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example1):
    """Test that input is parsed properly"""
    assert example1 == ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


def test_part1_example(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == 142


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 54667


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
