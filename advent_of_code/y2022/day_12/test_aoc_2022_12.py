import pathlib

import pytest

import advent_of_code.y2022.day_12.aoc_2022_12 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example() -> solver.ParsedInput:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data() -> solver.ParsedInput:
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example: solver.ParsedInput) -> None:
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


def test_part1_example(example: solver.ParsedInput) -> None:
    """Test part 1 on example input"""
    assert solver.part1(example) == 31


def test_part1_data(data: solver.ParsedInput) -> None:
    """Test part 1 on example input"""
    assert solver.part1(data) == 520


def test_part2_example2(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 29


def test_part2_data(data):
    """Test part 2 on example input"""
    assert solver.part2(data) == 508
