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


def test_parse(grid: Grid):
    """Test that input is parsed properly"""
    assert str(grid) == textwrap.dedent(
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
    assert grid.start_coords == Coord(0, 8)


def test_edge_marking(grid: Grid):
    assert len(grid.edge_points) == 44
