import pathlib

import aoc_2022_14 as solver
import pytest

from advent_of_code_2022.day_14.grid import Grid

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def sample_grid() -> Grid:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data_grid() -> Grid:
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example-2.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_part1_example1(sample_grid):
    """Test part 1 on example input"""
    assert solver.part1(sample_grid) == 24


def test_part1_data(data_grid):
    """Test part 1 on example input"""
    assert solver.part1(data_grid) == 665


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
