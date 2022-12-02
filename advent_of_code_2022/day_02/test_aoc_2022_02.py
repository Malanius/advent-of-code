import pathlib

import pytest

from advent_of_code_2022.day_02.aoc_2022_02 import (
    Hand,
    Outcome,
    get_outcome,
    parse,
    part1,
    part2,
    play_draw,
    play_loss,
    play_win,
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


def test_play_win():
    """Test that play win works properly"""
    assert play_win(Hand.ROCK) == Hand.PAPER
    assert play_win(Hand.PAPER) == Hand.SCISSORS
    assert play_win(Hand.SCISSORS) == Hand.ROCK


def test_play_draw():
    """Test that play draw works properly"""
    assert play_draw(Hand.ROCK) == Hand.ROCK
    assert play_draw(Hand.PAPER) == Hand.PAPER
    assert play_draw(Hand.SCISSORS) == Hand.SCISSORS


def test_play_lose():
    """Test that play lose works properly"""
    assert play_loss(Hand.ROCK) == Hand.SCISSORS
    assert play_loss(Hand.PAPER) == Hand.ROCK
    assert play_loss(Hand.SCISSORS) == Hand.PAPER


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
