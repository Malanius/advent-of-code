import pathlib

import aoc_2023_07 as solver
import pytest
from hand import Hand, Kind

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example() -> list[Hand]:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [
        Hand(cards="32T3K", bid=765, sortable_cards="32V3Y", kind=Kind.ONE_PAIR),
        Hand(cards="T55J5", bid=684, sortable_cards="V55W5", kind=Kind.THREE_OF_A_KIND),
        Hand(cards="KK677", bid=28, sortable_cards="YY677", kind=Kind.TWO_PAIRS),
        Hand(cards="KTJJT", bid=220, sortable_cards="YVWWV", kind=Kind.TWO_PAIRS),
        Hand(cards="QQQJA", bid=483, sortable_cards="XXXWZ", kind=Kind.THREE_OF_A_KIND),
    ]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
