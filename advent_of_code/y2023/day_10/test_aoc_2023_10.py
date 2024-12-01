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
def example3():
    return """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""


@pytest.fixture
def example4():
    return """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    pipe_map, _ = solver.parse(example1)
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
    pipe_map, _ = solver.parse(example2)
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


def test_part2_example3(example3):
    """Test part 2 on example input"""
    input = solver.parse(example3)
    assert solver.part2(input) == 4


def test_part2_example4(example4):
    """Test part 2 on example input"""
    input = solver.parse(example4)
    assert solver.part2(input) == 10


def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == 343
