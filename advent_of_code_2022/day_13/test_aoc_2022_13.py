import pathlib
import pytest
import aoc_2022_13 as solver
from aoc_2022_13 import Pair

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly"""
    assert list(example) == [
        Pair([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]),
        Pair([[1], [2, 3, 4]], [[1], 4]),
        Pair([9], [[8, 7, 6]]),
        Pair([[4, 4], 4, 4], [[4, 4], 4, 4, 4]),
        Pair([7, 7, 7, 7], [7, 7, 7]),
        Pair([], [3]),
        Pair([[[]]], [[]]),
        Pair([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]),
    ]


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 13


def test_part1_data(data):
    """Test part 1 on puzzle input"""
    assert solver.part1(data) == 6101


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
