import pathlib
import pytest
import aoc_2022_08 as solver

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
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
