import pathlib

import pytest

import advent_of_code.y2022.day_19.aoc_2022_19 as solver
from advent_of_code.y2022.day_19.blueprint import Blueprint
from advent_of_code.y2022.day_19.inventory import Inventory

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example: list[Blueprint]):
    """Test that input is parsed properly"""
    assert len(example) == 2

    assert example[0].id == 1
    assert example[0].ore_bot_cost == Inventory(ore=4)
    assert example[0].clay_bot_cost == Inventory(ore=2)
    assert example[0].obsidian_bot_cost == Inventory(ore=3, clay=14)
    assert example[0].geode_bot_cost == Inventory(ore=2, obsidian=7)

    assert example[1].id == 2
    assert example[1].ore_bot_cost == Inventory(ore=2)
    assert example[1].clay_bot_cost == Inventory(ore=3)
    assert example[1].obsidian_bot_cost == Inventory(ore=3, clay=8)
    assert example[1].geode_bot_cost == Inventory(ore=3, obsidian=12)


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 33


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 1550


def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 3472


def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == 18630
