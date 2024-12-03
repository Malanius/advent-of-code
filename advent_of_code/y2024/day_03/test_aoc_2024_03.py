import pathlib
import pytest

from advent_of_code.y2024.day_03 import aoc_2024_03 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_1():
    puzzle_input = (PUZZLE_DIR / "example_1.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example_2():
    puzzle_input = (PUZZLE_DIR / "example_2.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example_1, example_2):
    """Test that input is parsed properly"""
    assert example_1 == [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    ]
    assert example_2 == [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ]


def test_part1_example(example_1):
    """Test part 1 on example input"""
    assert solver.part1(example_1) == 161


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 166630675


def test_part2_example(example_2):
    """Test part 2 on example input"""
    assert solver.part2(example_2) == 48


def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == 93465710
