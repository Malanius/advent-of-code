from collections import deque
import pathlib
import pytest
import aoc_2022_11 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example-2.txt").read_text().strip()
    return solver.parse(puzzle_input)


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


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
