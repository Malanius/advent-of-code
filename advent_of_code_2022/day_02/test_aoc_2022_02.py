import pathlib
import pytest
import advent_of_code_2022.day_02.aoc_2022_02 as aoc_2022_02

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc_2022_02.parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly"""
    assert example == ["A Y", "B X", "C Z"]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc_2022_02.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc_2022_02.part2(example2) == ...
