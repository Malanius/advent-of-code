import pathlib
import pytest
import aoc_2023_02 as solver

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
            "draws": [
                {"blue": 3, "red": 4},
                {"red": 1, "green": 2, "blue": 6},
                {"green": 2},
            ],
        },
        {
            "id": 2,
            "draws": [
                {"blue": 1, "green": 2},
                {"green": 3, "blue": 4, "red": 1},
                {"green": 1, "blue": 1},
            ],
        },
        {
            "id": 3,
            "draws": [
                {"green": 8, "blue": 6, "red": 20},
                {"blue": 5, "red": 4, "green": 13},
                {"green": 5, "red": 1},
            ],
        },
        {
            "id": 4,
            "draws": [
                {"green": 1, "red": 3, "blue": 6},
                {"green": 3, "red": 6},
                {"green": 3, "blue": 15, "red": 14},
            ],
        },
        {
            "id": 5,
            "draws": [
                {"red": 6, "blue": 1, "green": 3},
                {"blue": 2, "red": 1, "green": 2},
            ],
        },
    ]


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 8


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 2545


def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 2286


def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == 78111
