import logging
import os
import sys
import time
from dataclasses import dataclass, field
from typing import Literal
from advent_of_code_2022.day_22.coord import Coord

from advent_of_code_2022.day_22.elements import Air
from advent_of_code_2022.day_22.grid import Grid
from advent_of_code_2022.day_22.instructions import Instruction
from advent_of_code_2022.day_22.player import Player


@dataclass
class Simulation:
    grid: Grid
    instructions: list[Instruction]
    interactive: bool = False

    def __post_init__(self) -> None:
        if not self.grid.start_coords:
            raise ValueError("No start coords found in grid!")
        self.player = Player(self.grid.start_coords)
        self.player.standing_on = self.grid.grid[self.player.coords.y][
            self.player.coords.x
        ]
        self.grid.grid[self.player.coords.y][self.player.coords.x] = self.player

    def _mark_passed(self) -> None:
        x, y = self.player.coords()
        logging.debug(f"Marking {x}, {y} as visited")
        passed_air = Air(passed=True, passed_direction=self.player.facing)
        self.grid.grid[y][x] = passed_air

    def _print_state(self, clear: bool = True, partial: bool = True) -> None:
        if not self.interactive:
            return

        current_y = self.player.coords.y
        grid = self.grid.partial_str(current_y) if partial else str(self.grid)
        sys.stdout.write(f"{grid}\n\n")
        sys.stdout.flush()
        time.sleep(0.25)
        if clear:
            os.system("clear")

    def _rotate_player(self, turn: Literal["R", "L", "-"]) -> None:
        if turn == "-":
            return
        self.player.turn(turn)
        self._print_state()
        logging.debug(f"Rotated player to {self.player.facing}")

    def _move_player(self, steps) -> None:
        for _ in range(steps):
            if self.interactive:
                new_coords = self.player.coords + Coord(*self.player.facing.value)

                current_element = self.player.standing_on
                if not isinstance(current_element, Air):
                    raise ValueError(f"Player is not on air! {current_element!r}")

                if current_element.is_edge:
                    current_coords = self.player.coords
                    self.grid.grid[current_coords.y][
                        current_coords.x
                    ] = self.player.standing_on
                    new_coords = self.grid.wraps_to(current_coords, self.player.facing)
                    logging.debug(f"Wrapping to {new_coords}")

                element = self.grid.grid[new_coords.y][new_coords.x]
                if not self.player.can_move_to(element):
                    logging.debug(f"Can't move to '{element}' at {new_coords}")
                    return

                self._mark_passed()
                self.player.standing_on = self.grid.grid[new_coords.y][new_coords.x]
                self.grid.grid[new_coords.y][new_coords.x] = self.player
                self.player.move_to(new_coords)
                self._print_state()

    def run(self) -> None:
        if self.interactive:
            os.system("clear")
        for steps, turn in self.instructions:
            self._move_player(steps)
            self._rotate_player(turn)
            logging.debug(f"Player at: {self.player.coords}")
        self._print_state(clear=False, partial=False)
