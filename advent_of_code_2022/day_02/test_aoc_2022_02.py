import pathlib

import pytest

from advent_of_code_2022.day_02.aoc_2022_02 import (
    Hand,
    Outcome,
    convert_hand,
    get_outcome,
    parse,
    part1,
    part2,
    play_hand,
)

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly"""
    assert example == ["A Y", "B X", "C Z"]


def test_part1_example1(example):
    """Test part 1 on example input"""
    assert part1(example) == 15


def test_part2_example2(example):
    """Test part 2 on example input"""
    assert part2(example) == 12


def test_part1_data():
    """Test part 1 on data input"""
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    assert part1(parse(puzzle_input)) == 11475


def test_part2_data():
    """Test part 2 on data input"""
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    assert part2(parse(puzzle_input)) == 16862


def test_get_outcome():
    """Test that get_outcome works properly"""
    assert get_outcome(Hand.ROCK, Hand.ROCK) == Outcome.DRAW
    assert get_outcome(Hand.PAPER, Hand.PAPER) == Outcome.DRAW
    assert get_outcome(Hand.SCISSORS, Hand.SCISSORS) == Outcome.DRAW

    assert get_outcome(Hand.SCISSORS, Hand.ROCK) == Outcome.LOSS
    assert get_outcome(Hand.ROCK, Hand.PAPER) == Outcome.LOSS
    assert get_outcome(Hand.PAPER, Hand.SCISSORS) == Outcome.LOSS

    assert get_outcome(Hand.ROCK, Hand.SCISSORS) == Outcome.WIN
    assert get_outcome(Hand.PAPER, Hand.ROCK) == Outcome.WIN
    assert get_outcome(Hand.SCISSORS, Hand.PAPER) == Outcome.WIN


def test_play_hand():
    """Test that play_hand works properly"""
    assert play_hand(Hand.ROCK, Outcome.DRAW) == Hand.ROCK
    assert play_hand(Hand.PAPER, Outcome.DRAW) == Hand.PAPER
    assert play_hand(Hand.SCISSORS, Outcome.DRAW) == Hand.SCISSORS

    assert play_hand(Hand.ROCK, Outcome.LOSS) == Hand.SCISSORS
    assert play_hand(Hand.PAPER, Outcome.LOSS) == Hand.ROCK
    assert play_hand(Hand.SCISSORS, Outcome.LOSS) == Hand.PAPER

    assert play_hand(Hand.ROCK, Outcome.WIN) == Hand.PAPER
    assert play_hand(Hand.PAPER, Outcome.WIN) == Hand.SCISSORS
    assert play_hand(Hand.SCISSORS, Outcome.WIN) == Hand.ROCK


def test_convert_hand():
    """Test that convert_hand works properly"""
    assert convert_hand("A") == Hand.ROCK
    assert convert_hand("B") == Hand.PAPER
    assert convert_hand("C") == Hand.SCISSORS

    assert convert_hand("X") == Hand.ROCK
    assert convert_hand("Y") == Hand.PAPER
    assert convert_hand("Z") == Hand.SCISSORS

    with pytest.raises(ValueError):
        convert_hand("D")

    with pytest.raises(ValueError):
        convert_hand("")

    with pytest.raises(ValueError):
        convert_hand("1")
