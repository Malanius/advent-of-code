import pathlib

import pytest

from advent_of_code_2022.day_02.aoc_2022_02 import (
    Hand,
    Outcome,
    get_outcome,
    is_draw,
    is_win,
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


def test_is_win():
    """Test that is_win works properly"""
    assert is_win(Hand.ROCK, Hand.SCISSORS)
    assert is_win(Hand.PAPER, Hand.ROCK)
    assert is_win(Hand.SCISSORS, Hand.PAPER)
    assert not is_win(Hand.SCISSORS, Hand.ROCK)
    assert not is_win(Hand.ROCK, Hand.PAPER)
    assert not is_win(Hand.PAPER, Hand.SCISSORS)
    assert not is_win(Hand.ROCK, Hand.ROCK)
    assert not is_win(Hand.PAPER, Hand.PAPER)
    assert not is_win(Hand.SCISSORS, Hand.SCISSORS)


def test_is_draw():
    """Test that is_draw works properly"""
    assert is_draw(Hand.ROCK, Hand.ROCK)
    assert is_draw(Hand.PAPER, Hand.PAPER)
    assert is_draw(Hand.SCISSORS, Hand.SCISSORS)
    assert not is_draw(Hand.SCISSORS, Hand.ROCK)
    assert not is_draw(Hand.ROCK, Hand.PAPER)
    assert not is_draw(Hand.PAPER, Hand.SCISSORS)
    assert not is_draw(Hand.ROCK, Hand.SCISSORS)
    assert not is_draw(Hand.PAPER, Hand.ROCK)
    assert not is_draw(Hand.SCISSORS, Hand.PAPER)


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
