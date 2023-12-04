import pathlib
import pytest
import aoc_2023_04 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [
        {
            "id": 1,
            "winning_numbers": [41, 48, 83, 86, 17],
            "card_numbers": [83, 86, 6, 31, 17, 9, 48, 53],
            "matching_numbers": 4,
            "count": 1,
        },
        {
            "id": 2,
            "winning_numbers": [13, 32, 20, 16, 61],
            "card_numbers": [61, 30, 68, 82, 17, 32, 24, 19],
            "matching_numbers": 2,
            "count": 1,
        },
        {
            "id": 3,
            "winning_numbers": [1, 21, 53, 59, 44],
            "card_numbers": [69, 82, 63, 72, 16, 21, 14, 1],
            "matching_numbers": 2,
            "count": 1,
        },
        {
            "id": 4,
            "winning_numbers": [41, 92, 73, 84, 69],
            "card_numbers": [59, 84, 76, 51, 58, 5, 54, 83],
            "matching_numbers": 1,
            "count": 1,
        },
        {
            "id": 5,
            "winning_numbers": [87, 83, 26, 28, 32],
            "card_numbers": [88, 30, 70, 12, 93, 22, 82, 36],
            "matching_numbers": 0,
            "count": 1,
        },
        {
            "id": 6,
            "winning_numbers": [31, 18, 13, 56, 72],
            "card_numbers": [74, 77, 10, 23, 35, 67, 36, 11],
            "matching_numbers": 0,
            "count": 1,
        },
    ]


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 13


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 19135


def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 30


def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == 5704953
