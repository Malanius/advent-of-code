import pathlib
import textwrap

import pytest
from advent_of_code_2022.day_23.coords import Coord
from advent_of_code_2022.day_23.elements import Elf


from advent_of_code_2022.day_23.grid import Grid


PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_grid() -> Grid:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text()
    return Grid.construct(puzzle_input)


@pytest.mark.parametrize(
    "row, col",
    # fmt: off
    [
        (0,4),                              # ....#..
        (1,2),(1,3),(1,4), (1,6),           # ..###.#
        (2,0), (2,4), (2,6),                # #...#.#
        (3,1), (3,5), (3,6),                # .#...##
        (4,0), (4,2), (4,3), (4,4),         # #.###..
        (5,0), (5,1), (5,3), (5,5), (5,6),  # ##.#.##
        (6,1),(6,4)                         # .#..#..
    ],
    # fmt: on
)
def test_elf_possition(example_grid: Grid, row: int, col: int) -> None:
    coord = Coord(row, col)
    element = example_grid.elements[coord]
    assert isinstance(element, Elf)


def test_min_row(example_grid: Grid) -> None:
    assert example_grid.min_row == 0


def test_max_row(example_grid: Grid) -> None:
    assert example_grid.max_row == 6


def test_min_col(example_grid: Grid) -> None:
    assert example_grid.min_col == 0


def test_max_col(example_grid: Grid) -> None:
    assert example_grid.max_col == 6


def test_elves_count(example_grid: Grid) -> None:
    assert example_grid.elves_count == 22
