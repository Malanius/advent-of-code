import pathlib
import textwrap

import pytest

from advent_of_code_2022.day_14.grid import Grid

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def grid() -> Grid:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return Grid.bootstrap(puzzle_input)


def test_parse_example(grid):
    """Test that input is parsed properly"""
    assert str(grid) == textwrap.dedent(
        """\
        ......+...
        ..........
        ..........
        ..........
        ....#...##
        ....#...#.
        ..###...#.
        ........#.
        ........#.
        #########."""
    )
