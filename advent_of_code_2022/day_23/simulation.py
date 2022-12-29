from dataclasses import dataclass, field
from advent_of_code_2022.day_23.coords import Coord, Direction

from advent_of_code_2022.day_23.grid import Grid


@dataclass
class Simulation:
    grid: Grid
    interatve: bool = False
    elves_to_move: set[Coord] = field(default_factory=set)
    claims: list[Coord] = field(default_factory=list)

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
        pass

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
