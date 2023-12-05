import pathlib

import aoc_2023_05 as solver
import pytest
from almanac import Almanac

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example() -> Almanac:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data() -> Almanac:
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == {
        "seeds": [79, 14, 55, 13],
        "seedToSoilMap": {range(98, 100): range(50, 52), range(50, 98): range(52, 100)},
        "soilToFertilizerMap": {
            range(52, 54): range(37, 39),
            range(15, 52): range(0, 37),
            range(0, 15): range(39, 54),
        },
        "fertilizerToWaterMap": {
            range(0, 7): range(42, 49),
            range(53, 61): range(49, 57),
            range(11, 53): range(0, 42),
            range(7, 11): range(57, 61),
        },
        "waterToLightMap": {range(18, 25): range(88, 95), range(25, 95): range(18, 88)},
        "lightToTemperatureMap": {
            range(77, 100): range(45, 68),
            range(45, 64): range(81, 100),
            range(64, 77): range(68, 81),
        },
        "temparatureToHumidityMap": {
            range(69, 70): range(0, 1),
            range(0, 69): range(1, 70),
        },
        "humidityToLocationMap": {
            range(93, 97): range(56, 60),
            range(56, 93): range(60, 97),
        },
    }


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 35


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 226172555


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
