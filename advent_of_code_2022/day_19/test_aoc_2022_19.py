import pathlib

import pytest

from advent_of_code_2022.day_19.aoc_2022_19 import Blueprints, parse, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return parse(puzzle_input)


def test_parse_example(example: Blueprints):
    """Test that input is parsed properly"""
    bluprints = list(example)
    assert len(bluprints) == 2

    assert bluprints[0].id == 1
    assert bluprints[0].ore_bot_cost_ores == 4
    assert bluprints[0].clay_bot_cost_ores == 2
    assert bluprints[0].obsidian_bot_cost_ores == 3
    assert bluprints[0].obsidian_bot_cost_clay == 14
    assert bluprints[0].geode_bot_cost_ores == 2
    assert bluprints[0].geode_bot_cost_obsidian == 7

    assert bluprints[1].id == 2
    assert bluprints[1].ore_bot_cost_ores == 2
    assert bluprints[1].clay_bot_cost_ores == 3
    assert bluprints[1].obsidian_bot_cost_ores == 3
    assert bluprints[1].obsidian_bot_cost_clay == 8
    assert bluprints[1].geode_bot_cost_ores == 3
    assert bluprints[1].geode_bot_cost_obsidian == 12


@pytest.mark.skip(reason="Not implemented")
def test_part1_example(example):
    """Test part 1 on example input"""
    assert part1(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_data(data):
    """Test part 1 on data input"""
    assert part1(data) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert part2(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert part2(data) == ...
