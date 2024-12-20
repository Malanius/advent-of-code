import pathlib

import aoc_2023_15 as solver
import pytest

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
        "rn=1",
        "cm-",
        "qp=3",
        "cm=2",
        "qp-",
        "pc=4",
        "ot=9",
        "ab=5",
        "pc-",
        "pc=6",
        "ot=7",
    ]


def test_hash():
    """Test hash_str"""
    assert solver.hash("HASH") == 52


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 1320


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 510801


def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 145


def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == 212763
