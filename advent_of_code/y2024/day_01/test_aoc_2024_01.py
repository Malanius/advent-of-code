import pathlib
import pytest
from advent_of_code.y2024.day_01 import aoc_2024_01 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == (
        [3, 4, 2, 1, 3, 3],
        [4, 3, 5, 3, 9, 3],
    )


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 11


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 2164381


def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 31


def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == 20719933
