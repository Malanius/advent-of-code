import pathlib

import aoc_2022_01
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc_2022_01.parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly"""
    assert (
        example
        == """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    )


def test_part1_example1(example):
    """Test part 1 on example input"""
    assert aoc_2022_01.part1(example) == 24_000


def test_part2_example2(example):
    """Test part 2 on example input"""
    assert aoc_2022_01.part2(example) == 45_000
