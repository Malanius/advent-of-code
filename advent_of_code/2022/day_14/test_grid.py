import pathlib
import textwrap

import pytest

from advent_of_code.day_14.grid import Grid

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def grid() -> Grid:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return Grid.construct(puzzle_input)

@pytest.fixture
def grid_bedrock() -> Grid:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return Grid.construct(puzzle_input, bedrock=True)



def test_parse_part1(grid):
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

def test_parse_part2(grid_bedrock):
    """Test that input is parsed properly"""
    assert str(grid_bedrock) == textwrap.dedent(
        """\
        ............+............
        .........................
        .........................
        .........................
        ..........#...##.........
        ..........#...#..........
        ........###...#..........
        ..............#..........
        ..............#..........
        ......#########..........
        .........................
        #########################"""
    )
