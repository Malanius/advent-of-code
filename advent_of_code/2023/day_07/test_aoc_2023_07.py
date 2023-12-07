import pathlib

import aoc_2023_07 as solver
import pytest
from hand import Hand, Kind

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> str:
    return (PUZZLE_DIR / "example1.txt").read_text().strip()


@pytest.fixture
def example2() -> str:
    return (PUZZLE_DIR / "example2.txt").read_text().strip()


@pytest.fixture
def data():
    return (PUZZLE_DIR / "data.txt").read_text().strip()


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    data = solver.parse_part1(example1)
    assert data == [
        Hand(cards="32T3K", bid=765, sortable_cards="32V3Y", kind=Kind.ONE_PAIR),
        Hand(cards="T55J5", bid=684, sortable_cards="V55W5", kind=Kind.THREE_OF_A_KIND),
        Hand(cards="KK677", bid=28, sortable_cards="YY677", kind=Kind.TWO_PAIRS),
        Hand(cards="KTJJT", bid=220, sortable_cards="YVWWV", kind=Kind.TWO_PAIRS),
        Hand(cards="QQQJA", bid=483, sortable_cards="XXXWZ", kind=Kind.THREE_OF_A_KIND),
    ]


def test_part1_example(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == 6440


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 248453531


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
