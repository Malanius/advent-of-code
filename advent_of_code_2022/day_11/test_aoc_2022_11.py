from collections import deque
import pathlib
import pytest
import aoc_2022_11 as solver
from aoc_2022_11 import play_rounds, parse, Monkey, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example-2.txt").read_text().strip()
    return parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert len(example) == 4, "Should have 4 monkeys"

    monkey0 = example[0]
    assert monkey0.id == 0, "Monkey 0 should have id 0"
    assert monkey0.items == deque([79, 98]), "Monkey 0 should have items 79, 98"
    assert monkey0.operation == "old * 19", "Monkey 0 should have operation old * 19"
    assert monkey0.test_divisible_by == 23, "Monkey 0 should test divisible by 23"
    assert monkey0.test_true_target == 2, "Monkey 0 should throw to monkey 2 if true"
    assert monkey0.test_false_target == 3, "Monkey 0 should throw to monkey 3 if false"

    monkey1 = example[1]
    assert monkey1.id == 1, "Monkey 1 should have id 1"
    assert monkey1.items == deque(
        [54, 65, 75, 74]
    ), "Monkey 1 should have items 54, 65, 75, 74"
    assert monkey1.operation == "old + 6", "Monkey 1 should have operation old + 6"
    assert monkey1.test_divisible_by == 19, "Monkey 1 should test divisible by 19"
    assert monkey1.test_true_target == 2, "Monkey 1 should throw to monkey 2 if true"
    assert monkey1.test_false_target == 0, "Monkey 1 should throw to monkey 0 if false"

    monkey2 = example[2]
    assert monkey2.id == 2, "Monkey 2 should have id 2"
    assert monkey2.items == deque([79, 60, 97]), "Monkey 2 should have items 79, 60, 97"
    assert monkey2.operation == "old * old", "Monkey 2 should have operation old * old"
    assert monkey2.test_divisible_by == 13, "Monkey 2 should test divisible by 13"
    assert monkey2.test_true_target == 1, "Monkey 2 should throw to monkey 1 if true"
    assert monkey2.test_false_target == 3, "Monkey 2 should throw to monkey 3 if false"

    monkey3 = example[3]
    assert monkey3.id == 3, "Monkey 3 should have id 3"
    assert monkey3.items == deque([74]), "Monkey 3 should have items 74"
    assert monkey3.operation == "old + 3", "Monkey 3 should have operation old + 3"
    assert monkey3.test_divisible_by == 17, "Monkey 3 should test divisible by 17"
    assert monkey3.test_true_target == 0, "Monkey 3 should throw to monkey 0 if true"
    assert monkey3.test_false_target == 1, "Monkey 3 should throw to monkey 1 if false"


def test_example_inventories_one_round(example):
    play_rounds(example, 1)
    assert example[0].items == deque(
        [20, 23, 27, 26]
    ), "Monkey 0 should have items 20, 23, 27, 26"
    assert example[1].items == deque(
        [2080, 25, 167, 207, 401, 1046]
    ), "Monkey 1 should have items 2080, 25, 167, 207, 401, 1046"
    assert len(example[2].items) == 0, "Monkey 2 should have no items"
    assert len(example[3].items) == 0, "Monkey 3 should have no items"


def test_example_inventories_twenty_rounds(example):
    play_rounds(example, 20)
    assert example[0].items == deque(
        [10, 12, 14, 26, 34]
    ), "Monkey 0 should have items 10, 12, 14, 26, 34"
    assert example[1].items == deque(
        [245, 93, 53, 199, 115]
    ), "Monkey 1 should have items 245, 93, 53, 199, 115"
    assert len(example[2].items) == 0, "Monkey 2 should have no items"
    assert len(example[3].items) == 0, "Monkey 3 should have no items"


def test_example_inspects(example):
    play_rounds(example, 20)
    assert example[0].inspects == 101, "Monkey 0 should have inspected 101 items"
    assert example[1].inspects == 95, "Monkey 1 should have inspected 95 items"
    assert example[2].inspects == 7, "Monkey 2 should have inspected 7 items"
    assert example[3].inspects == 105, "Monkey 3 should have inspected 105 items"


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert part2(example2) == ...
