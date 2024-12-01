from collections import defaultdict

import pytest
from pipe import Pipe, PipeMap, PipeType, determine_start_pipe_type

from advent_of_code.common.two_d.coord import Coord
from advent_of_code.common.two_d.direction4 import Direction4


def test_vertical_pipe():
    pipe = Pipe(PipeType.VERTICAL)
    assert pipe.get_next_direction(moving_direction=Direction4.UP) == Direction4.UP
    assert pipe.get_next_direction(moving_direction=Direction4.DOWN) == Direction4.DOWN
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.RIGHT)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.LEFT)


def test_horizontal_pipe():
    pipe = Pipe(PipeType.HORIZONTAL)
    assert (
        pipe.get_next_direction(moving_direction=Direction4.RIGHT) == Direction4.RIGHT
    )
    assert pipe.get_next_direction(moving_direction=Direction4.LEFT) == Direction4.LEFT
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.UP)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.DOWN)


def test_L_pipe():
    pipe = Pipe(PipeType("L"))
    assert pipe.get_next_direction(moving_direction=Direction4.DOWN) == Direction4.RIGHT
    assert pipe.get_next_direction(moving_direction=Direction4.LEFT) == Direction4.UP
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.UP)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.RIGHT)


def test_J_pipe():
    pipe = Pipe(PipeType("J"))
    assert pipe.get_next_direction(moving_direction=Direction4.RIGHT) == Direction4.UP
    assert pipe.get_next_direction(moving_direction=Direction4.DOWN) == Direction4.LEFT
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.UP)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.LEFT)


def test_F_pipe():
    pipe = Pipe(PipeType("F"))
    assert pipe.get_next_direction(moving_direction=Direction4.UP) == Direction4.RIGHT
    assert pipe.get_next_direction(moving_direction=Direction4.LEFT) == Direction4.DOWN
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.DOWN)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.RIGHT)


def test_7_pipe():
    pipe = Pipe(PipeType("7"))
    assert pipe.get_next_direction(moving_direction=Direction4.UP) == Direction4.LEFT
    assert pipe.get_next_direction(moving_direction=Direction4.RIGHT) == Direction4.DOWN
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.DOWN)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.LEFT)


def test_ground_pipe():
    pipe = Pipe(PipeType.GROUND)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.UP)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.DOWN)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.RIGHT)
    with pytest.raises(ValueError):
        pipe.get_next_direction(moving_direction=Direction4.LEFT)


# Test map is first example
#   01234
#  0.....
#  1.F-7.
#  2.|.|.
#  3.L-J.
#  4.....
test_map: PipeMap = defaultdict[Coord, Pipe](lambda: Pipe(PipeType.GROUND))
test_map.update(
    {
        Coord(1, 1): Pipe(type=PipeType.F_BEND),
        Coord(1, 2): Pipe(type=PipeType.VERTICAL),
        Coord(1, 3): Pipe(type=PipeType.L_BEND),
        Coord(2, 1): Pipe(type=PipeType.HORIZONTAL),
        Coord(2, 3): Pipe(type=PipeType.HORIZONTAL),
        Coord(3, 1): Pipe(type=PipeType.BEND_7),
        Coord(3, 2): Pipe(type=PipeType.VERTICAL),
        Coord(3, 3): Pipe(type=PipeType.J_BEND),
    }
)


def test_determine_pipe_type():
    assert determine_start_pipe_type(test_map, Coord(1, 2)) == PipeType.VERTICAL
    assert determine_start_pipe_type(test_map, Coord(2, 1)) == PipeType.HORIZONTAL
    assert determine_start_pipe_type(test_map, Coord(1, 1)) == PipeType.F_BEND
    assert determine_start_pipe_type(test_map, Coord(1, 3)) == PipeType.L_BEND
    assert determine_start_pipe_type(test_map, Coord(3, 3)) == PipeType.J_BEND
    assert determine_start_pipe_type(test_map, Coord(3, 1)) == PipeType.BEND_7
