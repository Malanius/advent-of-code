import pathlib
import pytest
import aoc_2022_12 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example-2.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example: solver.ParsedInput):
    """Test that input is parsed properly"""
    assert example["start"] == (0, 0)
    assert example["end"] == (2, 5)
    assert example["grid"] == [
        ["a", "a", "b", "q", "p", "o", "n", "m"],
        ["a", "b", "c", "r", "y", "x", "x", "l"],
        ["a", "c", "c", "s", "z", "z", "x", "k"],
        ["a", "c", "c", "t", "u", "v", "w", "j"],
        ["a", "b", "d", "e", "f", "g", "h", "i"],
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
