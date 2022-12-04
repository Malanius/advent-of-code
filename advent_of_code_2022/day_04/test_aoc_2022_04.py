import pathlib

import aoc_2022_04 as solver
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example-2.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly"""
    assert example == [
        (range(2, 4), range(6, 8)),
        (range(2, 3), range(4, 5)),
        (range(5, 7), range(7, 9)),
        (range(2, 8), range(3, 7)),
        (range(6, 6), range(4, 6)),
        (range(2, 6), range(4, 8)),
    ]


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 2


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
