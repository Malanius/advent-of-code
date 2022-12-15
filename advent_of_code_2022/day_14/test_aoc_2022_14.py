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
def sample_grid_bedrock() -> Grid:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input, bedrock=True)


@pytest.fixture
def data_grid_bedrock() -> Grid:
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input, bedrock=True)


def test_part1_example(sample_grid):
    """Test part 1 on example input"""
    assert solver.part1(sample_grid) == 24


def test_part1_data(data_grid):
    """Test part 1 on example input"""
    assert solver.part1(data_grid) == 665


def test_part2_example(sample_grid_bedrock):
    """Test part 1 on example input"""
    assert solver.part1(sample_grid_bedrock) == 93

@pytest.mark.skip(reason="Way too slow")
def test_part2_data(data_grid_bedrock):
    """Test part 1 on example input"""
    assert solver.part1(data_grid_bedrock) == 25434
