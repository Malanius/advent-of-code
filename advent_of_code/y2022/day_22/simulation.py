import logging
import os
import sys
import time
from dataclasses import dataclass
from typing import Literal

from advent_of_code.y2022.day_22.coord import Coord
from advent_of_code.y2022.day_22.elements import Star, Tile
from advent_of_code.y2022.day_22.grid import Grid
from advent_of_code.y2022.day_22.instructions import Instruction
from advent_of_code.y2022.day_22.player import Player


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
        y, x = self.player.coords()
        passed_tile = self.grid.grid[y][x]
        if not isinstance(passed_tile, Tile):
            raise ValueError("Player path not on tile!")
        passed_tile.passed = True
        passed_tile.passed_direction = self.player.facing
        logging.debug(f"Marked {x}, {y} as visited")

    def _print_state(self, clear: bool = True, partial: bool = True) -> None:
        if not self.interactive:
            return

        current_coords = self.player.coords
        grid = self.grid.partial_str(current_coords) if partial else str(self.grid)
        sys.stdout.write(f"{grid}\r")
        sys.stdout.flush()
        time.sleep(0.25)
        if clear:
            os.system("clear")
        else:
            print()

    def _rotate_player(self, turn: Literal["R", "L", "-"]) -> None:
        if turn == "-":
            logging.debug("Reached final coordinates {self.player.coords}")
            self.grid.grid[self.player.coords.y][self.player.coords.x] = Star()
            return
        self.player.turn(turn)
        logging.debug(f"Rotated player to {self.player.facing}")
        logging.debug(
            f"Player at: {self.player.coords}, on: {self.player.standing_on!r}"
        )
        self._print_state()

    def _move_player(self, steps) -> None:
        for _ in range(steps):
            new_coords = self.player.coords + Coord(*self.player.facing.value)

            current_element = self.player.standing_on
            if not isinstance(current_element, Tile):
                raise ValueError(f"Player is not on air! {current_element!r}")

            if current_element.edges:
                current_coords = self.player.coords
                self.grid.grid[current_coords.y][current_coords.x] = (
                    self.player.standing_on
                )
                new_coords = self.grid.wraps_to(current_coords, self.player.facing)
                self.grid.grid[current_coords.y][current_coords.x] = self.player
                logging.debug(f"Wrapping to {new_coords}")

            element = self.grid.grid[new_coords.y][new_coords.x]
            if not self.player.can_move_to(element):
                self.player.crashed = True
                self._print_state()
                self.player.crashed = False
                logging.debug(f"Can't move to '{element}' at {new_coords}")
                return

            self.grid.grid[self.player.coords.y][self.player.coords.x] = (
                self.player.standing_on
            )
            self.player.standing_on = self.grid.grid[new_coords.y][new_coords.x]
            self._mark_passed()
            self.grid.grid[new_coords.y][new_coords.x] = self.player
            self.player.move_to(new_coords)
            logging.debug(
                f"Player at: {self.player.coords}, on: {self.player.standing_on!r}"
            )
            self._print_state()

    def run(self) -> None:
        if self.interactive:
            os.system("clear")
        for steps, turn in self.instructions:
            self._move_player(steps)
            self._rotate_player(turn)
        self._print_state(clear=False, partial=False)
