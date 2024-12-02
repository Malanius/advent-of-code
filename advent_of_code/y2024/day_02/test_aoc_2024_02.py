import pathlib
import pytest

from advent_of_code.y2024.day_02 import aoc_2024_02 as solver

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
    assert example == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_is_safe_report():
    assert solver.is_safe_report([7, 6, 4, 2, 1]) is True
    assert solver.is_safe_report([1, 2, 7, 8, 9]) is False
    assert solver.is_safe_report([9, 7, 6, 2, 1]) is False
    assert solver.is_safe_report([1, 3, 2, 4, 5]) is False
    assert solver.is_safe_report([8, 6, 4, 4, 1]) is False
    assert solver.is_safe_report([1, 3, 6, 7, 9]) is True


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 2


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 660


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
