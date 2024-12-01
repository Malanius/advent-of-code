import pathlib

import pytest

import advent_of_code.y2022.day_25.aoc_2022_25 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == "2=-1=0"


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == "2-21=02=1-121-2-11-0"


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
