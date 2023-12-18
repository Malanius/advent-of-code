import logging
from collections import defaultdict
from dataclasses import dataclass
from enum import StrEnum

from advent_of_code.common.two_d.coord import Coord
from advent_of_code.common.two_d.direction4 import Direction4

type PipeMap = defaultdict[Coord, Pipe]


class PipeType(StrEnum):
    """
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    """

    VERTICAL = "|"
    HORIZONTAL = "-"
    L_BEND = "L"
    J_BEND = "J"
    BEND_7 = "7"
    F_BEND = "F"
    GROUND = "."


@dataclass
class Pipe:
    type: PipeType
    start: bool = False

    def get_next_direction(self, moving_direction: Direction4) -> Direction4:
        match (self.type, moving_direction):
            # | Vertical pipes
            case (PipeType.VERTICAL, Direction4.UP):
                return Direction4.UP
            case (PipeType.VERTICAL, Direction4.DOWN):
                return Direction4.DOWN

            # - Horizontal pipes
            case (PipeType.HORIZONTAL, Direction4.RIGHT):
                return Direction4.RIGHT
            case (PipeType.HORIZONTAL, Direction4.LEFT):
                return Direction4.LEFT

            # L 90-degree bend connecting north and east.
            case (PipeType.L_BEND, Direction4.DOWN):
                return Direction4.RIGHT
            case (PipeType.L_BEND, Direction4.LEFT):
                return Direction4.UP

            # J 90-degree bend connecting north and west.
            case (PipeType.J_BEND, Direction4.DOWN):
                return Direction4.LEFT
            case (PipeType.J_BEND, Direction4.RIGHT):
                return Direction4.UP

            # F 90-degree bend connecting south and east.
            case (PipeType.F_BEND, Direction4.UP):
                return Direction4.RIGHT
            case (PipeType.F_BEND, Direction4.LEFT):
                return Direction4.DOWN

            # 7 90-degree bend connecting south and west.
            case (PipeType.BEND_7, Direction4.UP):
                return Direction4.LEFT
            case (PipeType.BEND_7, Direction4.RIGHT):
                return Direction4.DOWN

            # Invalid incoming direction
            case (_, _):
                raise ValueError(
                    f"Invalid pipe type {self.type} with direction {moving_direction}"
                )


def determine_start_pipe_type(pipe_map: PipeMap, start_coord: Coord) -> PipeType:
    """Determine start pipe type"""
    # UP, DOWN, RIGHT, LEFT
    connects = []
    for moving_direction in Direction4:
        coord = start_coord + moving_direction.value
        possilbe_pipe = pipe_map[coord]
        try:
            logging.debug(f"Trying {possilbe_pipe} at {coord} with {moving_direction}")
            possilbe_pipe.get_next_direction(moving_direction)
            connects.append(True)
            logging.debug(f"Found connecting pipe at {coord}")
        except ValueError:
            connects.append(False)

    logging.debug(f"connects: {connects}")

    match connects:
        case [False, False, True, True]:
            return PipeType.HORIZONTAL
        case [True, True, False, False]:
            return PipeType.VERTICAL
        case [True, False, True, False]:
            return PipeType("L")
        case [False, True, True, False]:
            return PipeType("F")
        case [True, False, False, True]:
            return PipeType("J")
        case [False, True, False, True]:
            return PipeType("7")
        case _:
            raise ValueError(f"Invalid start pipe type {connects}")
