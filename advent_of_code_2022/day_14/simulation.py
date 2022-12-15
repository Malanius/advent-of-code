import logging
from dataclasses import dataclass, field
import os
import sys
import time

from advent_of_code_2022.day_14.direction import Direction
from advent_of_code_2022.day_14.elements import Air, Grain
from advent_of_code_2022.day_14.grid import Grid


@dataclass
class Simulation:
    grid: Grid
    bedrock: bool = False
    visited_airs: list[Air] = field(default_factory=list)
    interactive: bool = False
    sand_count: int = 0

    def _spawn_sand(self) -> None:
        gen_x, gen_y = self.grid.generator_coords
        gen_x -= self.grid.offset_x
        logging.debug(f"Spawning sand at {gen_x}, {gen_y}")
        self.current_grain = Grain((gen_x, gen_y))

    def _mark_visited(self) -> None:
        gen_x, gen_y = self.grid.generator_coords
        gen_x -= self.grid.offset_x
        if self.current_grain.coords == (gen_x, gen_y):
            return
        x, y = self.current_grain.coords
        logging.debug(f"Marking {x}, {y} as visited")
        visited_air = Air(visited=True, transparent=self.grid.transparent_air)
        self.visited_airs.append(visited_air)
        self.grid.grid[y][x] = visited_air

    def _move_grain(self, direction: Direction) -> None:
        self._mark_visited()
        self.current_grain.move(direction)
        new_x, new_y = self.current_grain.coords
        logging.debug(f"Moving grain in {direction} to {new_x}, {new_y}")
        self.grid.grid[new_y][new_x] = self.current_grain

    def _mark_resting(self) -> None:
        x, y = self.current_grain.coords
        logging.debug(f"Marking grain as resting at {x}, {y}")
        self.current_grain.is_resting = True

    def _print_state(self, clear: bool = True, partial: bool = True) -> None:
        current_y = self.current_grain.coords[1]
        grid = self.grid.partial_str(current_y) if partial else str(self.grid)
        sys.stdout.write(f"{grid}\n\n")
        sys.stdout.write(f"Sand count: {self.sand_count}\n")
        sys.stdout.flush()
        time.sleep(0.1)
        if clear:
            os.system("clear")

    def _pour_sand(self) -> None:
        self._spawn_sand()
        gen_x, gen_y = self.grid.generator_coords
        gen_x -= self.grid.offset_x
        while True:
            x, y = self.current_grain.coords
            logging.debug(f"Current grain coords: {x}, {y}")

            if self.interactive:
                self._print_state()

            can_move_down = self.current_grain.can_move_to(self.grid.grid[y + 1][x])
            if can_move_down:
                self._move_grain(Direction.DOWN)
                continue

            can_move_down_left = self.current_grain.can_move_to(
                self.grid.grid[y + 1][x - 1]
            )
            if can_move_down_left:
                self._move_grain(Direction.DOWN_LEFT)
                continue

            can_move_down_right = self.current_grain.can_move_to(
                self.grid.grid[y + 1][x + 1]
            )
            if can_move_down_right:
                self._move_grain(Direction.DOWN_RIGHT)
                continue

            self._mark_resting()
            self._clear_air()
            self.sand_count += 1

            if self.current_grain.coords == (gen_x, gen_y):
                logging.debug("Sand reached generator")
                gen_x, gen_y = self.grid.generator_coords
                gen_x -= self.grid.offset_x
                self.grid.grid[gen_y][gen_x] = Grain((gen_x, gen_y), is_resting=True)
                raise IndexError

            break

    def _clear_air(self) -> None:
        for air in self.visited_airs:
            air.visited = False

    def run(self) -> None:
        if self.interactive:
            os.system("clear")
        while True:
            try:
                self._pour_sand()
            except IndexError:
                self._print_state(clear=False, partial=False)
                break
