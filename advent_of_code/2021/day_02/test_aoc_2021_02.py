import pathlib
import pytest
import aoc_2021_02 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse_input(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly"""
    assert example == [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
    ]


def test_part1_example1(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 150


def test_part2_example2(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 900
