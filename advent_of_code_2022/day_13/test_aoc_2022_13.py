import pathlib
import pytest
import aoc_2022_13 as solver
from aoc_2022_13 import Pair

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_part1():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse_part1(puzzle_input)


@pytest.fixture
def example_part2():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse_part2(puzzle_input)


@pytest.fixture
def data_part1():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse_part1(puzzle_input)


def test_parse_example_part1(example_part1):
    """Test that input is parsed properly"""
    assert list(example_part1) == [
        Pair([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]),
        Pair([[1], [2, 3, 4]], [[1], 4]),
        Pair([9], [[8, 7, 6]]),
        Pair([[4, 4], 4, 4], [[4, 4], 4, 4, 4]),
        Pair([7, 7, 7, 7], [7, 7, 7]),
        Pair([], [3]),
        Pair([[[]]], [[]]),
        Pair([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]),
    ]


def test_parse_example_part2(example_part2):
    assert example_part2 == [
        [1, 1, 3, 1, 1],
        [1, 1, 5, 1, 1],
        [[1], [2, 3, 4]],
        [[1], 4],
        [9],
        [[8, 7, 6]],
        [[4, 4], 4, 4],
        [[4, 4], 4, 4, 4],
        [7, 7, 7, 7],
        [7, 7, 7],
        [],
        [3],
        [[[]]],
        [[]],
        [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
        [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
    ]


def test_part1_example(example_part1):
    """Test part 1 on example input"""
    assert solver.part1(example_part1) == 13


def test_part1_data(data_part1):
    """Test part 1 on puzzle input"""
    assert solver.part1(data_part1) == 6101


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
