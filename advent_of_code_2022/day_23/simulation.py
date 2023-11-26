from collections import deque
from copy import deepcopy
from dataclasses import dataclass, field
from advent_of_code_2022.day_23.coords import Coord, Direction
from advent_of_code_2022.day_23.elements import Tile

from advent_of_code_2022.day_23.grid import Grid

DIRECTION_CHECKS = {
    Direction.NORTH: [Direction.NORTH, Direction.NORTH_EAST, Direction.NORTH_WEST],
    Direction.SOUTH: [Direction.SOUTH, Direction.SOUTH_EAST, Direction.SOUTH_WEST],
    Direction.WEST: [Direction.WEST, Direction.NORTH_WEST, Direction.SOUTH_WEST],
    Direction.EAST: [Direction.EAST, Direction.NORTH_EAST, Direction.SOUTH_EAST],
}


@dataclass
class Simulation:
    grid: Grid
    interatve: bool = False
    elves_to_move: set[Coord] = field(default_factory=set)
    claims: list[Coord] = field(default_factory=list)
    direction_proposals: deque[Direction] = field(
        default_factory=lambda: deque(
            [
                Direction.NORTH,
                Direction.SOUTH,
                Direction.WEST,
                Direction.EAST,
            ]
        )
    )

    def _check_surroundings(self) -> None:
        """Check all elves surrounding tiles for other elf presence.
        If there is an elf, add it to the list of elves to move."""
        for elf in self.grid.elves:
            for direction in Direction:
                coord = elf + direction.value
                if not self.grid.is_empty(coord):
                    self.elves_to_move.add(coord)
                    break

    def _propose_moves(self) -> None:
        for elf in self.elves_to_move:
            directions = deepcopy(self.direction_proposals)
            while directions:
                direction = directions.popleft()
                check_directions = DIRECTION_CHECKS[direction]
                are_all_empty = all(
                    [self.grid.is_empty(elf + d.value) for d in check_directions]
                )
                if are_all_empty:
                    proposed_coord = elf + direction.value
                    tile = self.grid.elements[proposed_coord]
                    assert isinstance(tile, Tile)
                    tile.claims += 1
                    self.grid.elements[elf].
                    self.claims.append(proposed_coord)
                    break

    def _move_elves(self) -> None:
        pass

    def _clear_claims(self) -> None:
        pass

    def _rotate_proposals(self) -> None:
        pass

    def run(self, rounds=10) -> None:
        for _ in range(rounds):
            self._check_surroundings()
            self._propose_moves()
            self._move_elves()
            self._clear_claims()
            self._rotate_proposals()
