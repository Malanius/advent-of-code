import pathlib
import pytest
import advent_of_code_2022.day_03.aoc_2022_03 as aoc_2022_03

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc_2022_03.parse_part1(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc_2022_03.parse_part2(puzzle_input)


def test_parse1_example(example1):
    """Test that input is parsed properly"""
    assert list(example1) == [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        ("PmmdzqPrV", "vPwwTWBwg"),
        ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"),
        ("ttgJtRGJ", "QctTZtZT"),
        ("CrZsJsPPZsGz", "wwsLwLmpwMDw"),
    ]


def test_parse2_example(example2):
    """Test that input is parsed properly"""
    assert list(example2) == [
        [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        ],
        [
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ],
    ]


def test_part1_example(example1):
    """Test part 1 on example input"""
    assert aoc_2022_03.part1(example1) == 157


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc_2022_03.part2(example2) == ...
