import pathlib
import pytest
from advent_of_code.common.two_d.coord import Coord
import aoc_2023_03 as solver

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
        Coord(0, 0): "4",
        Coord(1, 0): "6",
        Coord(2, 0): "7",
        Coord(5, 0): "1",
        Coord(6, 0): "1",
        Coord(7, 0): "4",
        Coord(3, 1): "*",
        Coord(2, 2): "3",
        Coord(3, 2): "5",
        Coord(6, 2): "6",
        Coord(7, 2): "3",
        Coord(8, 2): "3",
        Coord(6, 3): "#",
        Coord(0, 4): "6",
        Coord(1, 4): "1",
        Coord(2, 4): "7",
        Coord(3, 4): "*",
        Coord(5, 5): "+",
        Coord(7, 5): "5",
        Coord(8, 5): "8",
        Coord(2, 6): "5",
        Coord(3, 6): "9",
        Coord(4, 6): "2",
        Coord(6, 7): "7",
        Coord(7, 7): "5",
        Coord(8, 7): "5",
        Coord(3, 8): "$",
        Coord(5, 8): "*",
        Coord(1, 9): "6",
        Coord(2, 9): "6",
        Coord(3, 9): "4",
        Coord(5, 9): "5",
        Coord(6, 9): "9",
        Coord(7, 9): "8",
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
