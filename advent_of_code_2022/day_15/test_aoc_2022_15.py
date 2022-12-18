import pathlib

import aoc_2022_15 as solver
import pytest

from advent_of_code_2022.day_15.coord import Coord

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
    assert example == {
        Coord(9, 16): Coord(10, 16),
        Coord(13, 2): Coord(15, 3),
        Coord(12, 14): Coord(10, 16),
        Coord(10, 20): Coord(10, 16),
        Coord(14, 17): Coord(10, 16),
        Coord(8, 7): Coord(2, 10),
        Coord(2, 0): Coord(2, 10),
        Coord(0, 11): Coord(2, 10),
        Coord(20, 14): Coord(25, 17),
        Coord(17, 20): Coord(21, 22),
        Coord(16, 7): Coord(15, 3),
        Coord(14, 3): Coord(15, 3),
        Coord(20, 1): Coord(15, 3),
    }


def test_part1_example1(example):
    """Test part 1 on example input"""
    assert solver.part1(example, 10) == 26


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data, 2_000_000) == 5511201


def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 56000011


def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data, 4_000_000) == 11318723411840
