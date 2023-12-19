import pathlib

import aoc_2023_10 as solver
import pytest
from pipe import Pipe, PipeType

from advent_of_code.common.two_d.coord import Coord

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""


@pytest.fixture
def example2():
    return """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    start_coord, pipe_map = solver.parse(example1)
    assert start_coord == Coord(1, 1)
    assert pipe_map == {
        Coord(1, 0): Pipe(type=PipeType.L_BEND, start=False),
        Coord(0, 0): Pipe(type=PipeType.HORIZONTAL, start=False),
        Coord(2, 1): Pipe(type=PipeType.HORIZONTAL, start=False),
        Coord(4, 0): Pipe(type=PipeType.BEND_7, start=False),
        Coord(2, 0): Pipe(type=PipeType.VERTICAL, start=False),
        Coord(3, 0): Pipe(type=PipeType.F_BEND, start=False),
        Coord(0, 1): Pipe(type=PipeType.BEND_7, start=False),
        Coord(1, 1): Pipe(type=PipeType.F_BEND, start=True),
        Coord(3, 1): Pipe(type=PipeType.BEND_7, start=False),
        Coord(4, 1): Pipe(type=PipeType.VERTICAL, start=False),
        Coord(0, 2): Pipe(type=PipeType.L_BEND, start=False),
        Coord(1, 2): Pipe(type=PipeType.VERTICAL, start=False),
        Coord(2, 2): Pipe(type=PipeType.BEND_7, start=False),
        Coord(3, 2): Pipe(type=PipeType.VERTICAL, start=False),
        Coord(4, 2): Pipe(type=PipeType.VERTICAL, start=False),
        Coord(0, 3): Pipe(type=PipeType.HORIZONTAL, start=False),
        Coord(1, 3): Pipe(type=PipeType.L_BEND, start=False),
        Coord(2, 3): Pipe(type=PipeType.HORIZONTAL, start=False),
        Coord(3, 3): Pipe(type=PipeType.J_BEND, start=False),
        Coord(4, 3): Pipe(type=PipeType.VERTICAL, start=False),
        Coord(0, 4): Pipe(type=PipeType.L_BEND, start=False),
        Coord(1, 4): Pipe(type=PipeType.VERTICAL, start=False),
        Coord(2, 4): Pipe(type=PipeType.HORIZONTAL, start=False),
        Coord(3, 4): Pipe(type=PipeType.J_BEND, start=False),
        Coord(4, 4): Pipe(type=PipeType.F_BEND, start=False),
    }


def test_parse_example2(example2):
    """Test that input is parsed properly"""
    start_coord, pipe_map = solver.parse(example2)
    assert start_coord == Coord(0, 2)
    assert pipe_map == {
        Coord(1, 2): Pipe(type=PipeType.J_BEND, start=False),
        Coord(0, 0): Pipe(type=PipeType.BEND_7, start=False),
        Coord(1, 0): Pipe(type=PipeType.HORIZONTAL, start=False),
        Coord(4, 0): Pipe(type=PipeType.HORIZONTAL, start=False),
        Coord(3, 0): Pipe(type=PipeType.BEND_7, start=False),
        Coord(2, 0): Pipe(type=PipeType.F_BEND, start=False),
        Coord(0, 1): Pipe(type=PipeType.GROUND, start=False),
        Coord(1, 1): Pipe(type=PipeType.F_BEND, start=False),
        Coord(2, 1): Pipe(type=PipeType.J_BEND, start=False),
        Coord(3, 1): Pipe(type=PipeType.VERTICAL, start=False),
        Coord(4, 1): Pipe(type=PipeType.BEND_7, start=False),
        Coord(0, 2): Pipe(type=PipeType.F_BEND, start=True),
        Coord(2, 2): Pipe(type=PipeType.L_BEND, start=False),
        Coord(3, 2): Pipe(type=PipeType.L_BEND, start=False),
        Coord(4, 2): Pipe(type=PipeType.BEND_7, start=False),
        Coord(0, 3): Pipe(type=PipeType.VERTICAL, start=False),
        Coord(1, 3): Pipe(type=PipeType.F_BEND, start=False),
        Coord(2, 3): Pipe(type=PipeType.HORIZONTAL, start=False),
        Coord(3, 3): Pipe(type=PipeType.HORIZONTAL, start=False),
        Coord(4, 3): Pipe(type=PipeType.J_BEND, start=False),
        Coord(0, 4): Pipe(type=PipeType.L_BEND, start=False),
        Coord(1, 4): Pipe(type=PipeType.J_BEND, start=False),
        Coord(2, 4): Pipe(type=PipeType.GROUND, start=False),
        Coord(3, 4): Pipe(type=PipeType.L_BEND, start=False),
        Coord(4, 4): Pipe(type=PipeType.J_BEND, start=False),
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    input = solver.parse(example1)
    assert solver.part1(input) == 4


def test_part1_example2(example2):
    """Test part 1 on example input"""
    input = solver.parse(example2)
    assert solver.part1(input) == 8


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 6860


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
