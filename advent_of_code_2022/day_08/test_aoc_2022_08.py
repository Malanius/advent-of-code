import pathlib
import pytest
import aoc_2022_08 as solver
from aoc_2022_08 import Tree

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
        [Tree(3), Tree(0), Tree(3), Tree(7), Tree(3)],
        [Tree(2), Tree(5), Tree(5), Tree(1), Tree(2)],
        [Tree(6), Tree(5), Tree(3), Tree(3), Tree(2)],
        [Tree(3), Tree(3), Tree(5), Tree(4), Tree(9)],
        [Tree(3), Tree(5), Tree(3), Tree(9), Tree(0)],
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
