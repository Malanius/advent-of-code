import pathlib
import textwrap

import pytest
from advent_of_code_2022.day_22.coord import Coord

from advent_of_code_2022.day_22.grid import Grid


PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_grid() -> Grid:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text()
    parts = puzzle_input.split("\n\n")
    return Grid.construct(parts[0])


def test_parse(example_grid: Grid) -> None:
    """Test that input is parsed properly"""
    assert str(example_grid) == textwrap.dedent(
        """\
                ...#    
                .#..    
                #...    
                ....    
        ...#.......#    
        ........#...    
        ..#....#....    
        ..........#.    
                ...#....
                .....#..
                .#......
                ......#."""
    )
    assert example_grid.start_coords == Coord(0, 8)


def test_edge_marking(example_grid: Grid) -> None:
    assert len(example_grid.edge_points) == 44


def test_row_bounds(example_grid: Grid) -> None:
    assert example_grid._row_bounds(Coord(0, 0)) == (Coord(0, 8), Coord(0, 11))
    assert example_grid._row_bounds(Coord(1, 0)) == (Coord(1, 8), Coord(1, 11))
    assert example_grid._row_bounds(Coord(2, 0)) == (Coord(2, 8), Coord(2, 11))
    assert example_grid._row_bounds(Coord(3, 0)) == (Coord(3, 8), Coord(3, 11))
    assert example_grid._row_bounds(Coord(4, 0)) == (Coord(4, 0), Coord(4, 11))
    assert example_grid._row_bounds(Coord(5, 0)) == (Coord(5, 0), Coord(5, 11))
    assert example_grid._row_bounds(Coord(6, 0)) == (Coord(6, 0), Coord(6, 11))
    assert example_grid._row_bounds(Coord(7, 0)) == (Coord(7, 0), Coord(7, 11))
    assert example_grid._row_bounds(Coord(8, 0)) == (Coord(8, 8), Coord(8, 15))
    assert example_grid._row_bounds(Coord(9, 0)) == (Coord(9, 8), Coord(9, 15))
    assert example_grid._row_bounds(Coord(10, 0)) == (Coord(10, 8), Coord(10, 15))
    assert example_grid._row_bounds(Coord(11, 0)) == (Coord(11, 8), Coord(11, 15))
