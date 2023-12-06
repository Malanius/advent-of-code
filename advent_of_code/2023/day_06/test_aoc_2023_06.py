import pathlib
import pytest
import aoc_2023_06 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example() -> list[solver.Race]:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [
        {"record_distance": 9, "time_limit": 7},
        {"record_distance": 40, "time_limit": 15},
        {"record_distance": 200, "time_limit": 30},
    ]


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 288


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 4403592


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
