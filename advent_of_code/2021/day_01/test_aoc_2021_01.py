import pathlib
import pytest
import aoc_2021_01 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part1(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 7


def test_part2(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 5
