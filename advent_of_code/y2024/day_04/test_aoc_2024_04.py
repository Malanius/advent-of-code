import pathlib
import pytest

from advent_of_code.common.two_d.coord import Coord
from advent_of_code.y2024.day_04 import aoc_2024_04 as solver

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
    assert example == {
        Coord(0, 0): "M",
        Coord(1, 0): "M",
        Coord(2, 0): "M",
        Coord(3, 0): "S",
        Coord(4, 0): "X",
        Coord(5, 0): "X",
        Coord(6, 0): "M",
        Coord(7, 0): "A",
        Coord(8, 0): "S",
        Coord(9, 0): "M",
        Coord(0, 1): "M",
        Coord(1, 1): "S",
        Coord(2, 1): "A",
        Coord(3, 1): "M",
        Coord(4, 1): "X",
        Coord(5, 1): "M",
        Coord(6, 1): "S",
        Coord(7, 1): "M",
        Coord(8, 1): "S",
        Coord(9, 1): "A",
        Coord(0, 2): "A",
        Coord(1, 2): "M",
        Coord(2, 2): "X",
        Coord(3, 2): "S",
        Coord(4, 2): "X",
        Coord(5, 2): "M",
        Coord(6, 2): "A",
        Coord(7, 2): "A",
        Coord(8, 2): "M",
        Coord(9, 2): "M",
        Coord(0, 3): "M",
        Coord(1, 3): "S",
        Coord(2, 3): "A",
        Coord(3, 3): "M",
        Coord(4, 3): "A",
        Coord(5, 3): "S",
        Coord(6, 3): "M",
        Coord(7, 3): "S",
        Coord(8, 3): "M",
        Coord(9, 3): "X",
        Coord(0, 4): "X",
        Coord(1, 4): "M",
        Coord(2, 4): "A",
        Coord(3, 4): "S",
        Coord(4, 4): "A",
        Coord(5, 4): "M",
        Coord(6, 4): "X",
        Coord(7, 4): "A",
        Coord(8, 4): "M",
        Coord(9, 4): "M",
        Coord(0, 5): "X",
        Coord(1, 5): "X",
        Coord(2, 5): "A",
        Coord(3, 5): "M",
        Coord(4, 5): "M",
        Coord(5, 5): "X",
        Coord(6, 5): "X",
        Coord(7, 5): "A",
        Coord(8, 5): "M",
        Coord(9, 5): "A",
        Coord(0, 6): "S",
        Coord(1, 6): "M",
        Coord(2, 6): "S",
        Coord(3, 6): "M",
        Coord(4, 6): "S",
        Coord(5, 6): "A",
        Coord(6, 6): "S",
        Coord(7, 6): "X",
        Coord(8, 6): "S",
        Coord(9, 6): "S",
        Coord(0, 7): "S",
        Coord(1, 7): "A",
        Coord(2, 7): "X",
        Coord(3, 7): "A",
        Coord(4, 7): "M",
        Coord(5, 7): "A",
        Coord(6, 7): "S",
        Coord(7, 7): "A",
        Coord(8, 7): "A",
        Coord(9, 7): "A",
        Coord(0, 8): "M",
        Coord(1, 8): "A",
        Coord(2, 8): "M",
        Coord(3, 8): "M",
        Coord(4, 8): "M",
        Coord(5, 8): "X",
        Coord(6, 8): "M",
        Coord(7, 8): "M",
        Coord(8, 8): "M",
        Coord(9, 8): "M",
        Coord(0, 9): "M",
        Coord(1, 9): "X",
        Coord(2, 9): "M",
        Coord(3, 9): "X",
        Coord(4, 9): "A",
        Coord(5, 9): "X",
        Coord(6, 9): "M",
        Coord(7, 9): "A",
        Coord(8, 9): "S",
        Coord(9, 9): "X",
    }


@pytest.mark.skip(reason="Not implemented")
def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
