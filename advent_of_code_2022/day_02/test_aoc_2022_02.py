import pathlib
import pytest
import advent_of_code_2022.day_02.aoc_2022_02 as aoc_2022_02

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return aoc_2022_02.parse(puzzle_input)


def test_parse_example1(example):
    """Test that input is parsed properly"""
    assert example == ["A Y", "B X", "C Z"]


def test_is_win():
    """Test that is_win works properly"""
    assert aoc_2022_02.is_win(aoc_2022_02.Hand.ROCK, aoc_2022_02.Hand.SCISSORS)
    assert aoc_2022_02.is_win(aoc_2022_02.Hand.PAPER, aoc_2022_02.Hand.ROCK)
    assert aoc_2022_02.is_win(aoc_2022_02.Hand.SCISSORS, aoc_2022_02.Hand.PAPER)
    assert not aoc_2022_02.is_win(aoc_2022_02.Hand.SCISSORS, aoc_2022_02.Hand.ROCK)
    assert not aoc_2022_02.is_win(aoc_2022_02.Hand.ROCK, aoc_2022_02.Hand.PAPER)
    assert not aoc_2022_02.is_win(aoc_2022_02.Hand.PAPER, aoc_2022_02.Hand.SCISSORS)
    assert not aoc_2022_02.is_win(aoc_2022_02.Hand.ROCK, aoc_2022_02.Hand.ROCK)
    assert not aoc_2022_02.is_win(aoc_2022_02.Hand.PAPER, aoc_2022_02.Hand.PAPER)
    assert not aoc_2022_02.is_win(aoc_2022_02.Hand.SCISSORS, aoc_2022_02.Hand.SCISSORS)


def test_is_draw():
    """Test that is_draw works properly"""
    assert aoc_2022_02.is_draw(aoc_2022_02.Hand.ROCK, aoc_2022_02.Hand.ROCK)
    assert aoc_2022_02.is_draw(aoc_2022_02.Hand.PAPER, aoc_2022_02.Hand.PAPER)
    assert aoc_2022_02.is_draw(aoc_2022_02.Hand.SCISSORS, aoc_2022_02.Hand.SCISSORS)
    assert not aoc_2022_02.is_draw(aoc_2022_02.Hand.SCISSORS, aoc_2022_02.Hand.ROCK)
    assert not aoc_2022_02.is_draw(aoc_2022_02.Hand.ROCK, aoc_2022_02.Hand.PAPER)
    assert not aoc_2022_02.is_draw(aoc_2022_02.Hand.PAPER, aoc_2022_02.Hand.SCISSORS)
    assert not aoc_2022_02.is_draw(aoc_2022_02.Hand.ROCK, aoc_2022_02.Hand.SCISSORS)
    assert not aoc_2022_02.is_draw(aoc_2022_02.Hand.PAPER, aoc_2022_02.Hand.ROCK)
    assert not aoc_2022_02.is_draw(aoc_2022_02.Hand.SCISSORS, aoc_2022_02.Hand.PAPER)


def test_part1_example1(example):
    """Test part 1 on example input"""
    assert aoc_2022_02.part1(example) == 15

def test_play_win():
    """Test that play win works properly"""
    assert aoc_2022_02.play_win(aoc_2022_02.Hand.ROCK) == aoc_2022_02.Hand.PAPER
    assert aoc_2022_02.play_win(aoc_2022_02.Hand.PAPER) == aoc_2022_02.Hand.SCISSORS
    assert aoc_2022_02.play_win(aoc_2022_02.Hand.SCISSORS) == aoc_2022_02.Hand.ROCK

def test_play_draw():
    """Test that play draw works properly"""
    assert aoc_2022_02.play_draw(aoc_2022_02.Hand.ROCK) == aoc_2022_02.Hand.ROCK
    assert aoc_2022_02.play_draw(aoc_2022_02.Hand.PAPER) == aoc_2022_02.Hand.PAPER
    assert aoc_2022_02.play_draw(aoc_2022_02.Hand.SCISSORS) == aoc_2022_02.Hand.SCISSORS

def test_play_lose():
    """Test that play lose works properly"""
    assert aoc_2022_02.play_loss(aoc_2022_02.Hand.ROCK) == aoc_2022_02.Hand.SCISSORS
    assert aoc_2022_02.play_loss(aoc_2022_02.Hand.PAPER) == aoc_2022_02.Hand.ROCK
    assert aoc_2022_02.play_loss(aoc_2022_02.Hand.SCISSORS) == aoc_2022_02.Hand.PAPER

def test_part2_example2(example):
    """Test part 2 on example input"""
    assert aoc_2022_02.part2(example) == 12
