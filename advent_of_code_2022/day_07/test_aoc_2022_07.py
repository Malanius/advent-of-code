import pathlib
import pytest
import aoc_2022_07 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example-1.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example-2.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
