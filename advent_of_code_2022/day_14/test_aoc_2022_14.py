import pathlib
import textwrap

import aoc_2022_14 as solver
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def simulation() -> solver.Simulation:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example-2.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(simulation):
    """Test that input is parsed properly"""
    assert str(simulation) == textwrap.dedent(
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


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
