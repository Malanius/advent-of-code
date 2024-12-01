import pathlib
from copy import deepcopy

import pytest

import advent_of_code.y2022.day_08.aoc_2022_08 as solver
from advent_of_code.y2022.day_08.aoc_2022_08 import Tree, VisibilityDirection

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [
        [Tree(3), Tree(0), Tree(3), Tree(7), Tree(3)],
        [Tree(2), Tree(5), Tree(5), Tree(1), Tree(2)],
        [Tree(6), Tree(5), Tree(3), Tree(3), Tree(2)],
        [Tree(3), Tree(3), Tree(5), Tree(4), Tree(9)],
        [Tree(3), Tree(5), Tree(3), Tree(9), Tree(0)],
    ]


def test_find_tallest():
    """Test that tallest tree is found properly"""
    assert solver.find_tallest([Tree(3), Tree(0), Tree(3), Tree(7), Tree(3)]) == 3
    assert solver.find_tallest([Tree(2), Tree(5), Tree(5), Tree(1), Tree(2)]) == 1
    assert solver.find_tallest([Tree(6), Tree(5), Tree(3), Tree(3), Tree(2)]) == 0
    assert solver.find_tallest([Tree(3), Tree(3), Tree(5), Tree(4), Tree(9)]) == 4
    assert solver.find_tallest([Tree(3), Tree(5), Tree(3), Tree(9), Tree(0)]) == 3


def test_count_visibility_from_left(example):
    """Test that visibility is counted properly"""
    data = deepcopy(example)
    solver.calculate_visibility_from_left(data)
    assert sum(1 for tree in solver.flatten(data) if tree.is_visible) == 11


def test_count_visibility_from_right(example):
    """Test that visibility is counted properly"""
    data = deepcopy(example)
    solver.calculate_visibility_from_right(data)
    assert sum(1 for tree in solver.flatten(data) if tree.is_visible) == 11


def test_count_visibility_from_top(example):
    """Test that visibility is counted properly"""
    data = deepcopy(example)
    solver.calculate_visibility_from_top(data)
    assert sum(1 for tree in solver.flatten(data) if tree.is_visible) == 10


def test_count_visibility_from_bottom(example):
    """Test that visibility is counted properly"""
    data = deepcopy(example)
    solver.calculate_visibility_from_bottom(data)
    assert sum(1 for tree in solver.flatten(data) if tree.is_visible) == 8


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 21


def test_part1_data(data):
    """Test part 1 on actual input"""
    assert solver.part1(data) == 1843


def test_count_seen_trees_left(example):
    """Test that visible trees are counted properly"""
    data = deepcopy(example)
    solver.calculate_visible_trees_left(data)
    direction = VisibilityDirection.LEFT
    assert data[0][0].seen_trees[direction] == 0
    assert data[0][1].seen_trees[direction] == 1
    assert data[0][2].seen_trees[direction] == 2
    assert data[0][3].seen_trees[direction] == 3
    assert data[0][4].seen_trees[direction] == 1

    assert data[1][0].seen_trees[direction] == 0
    assert data[1][1].seen_trees[direction] == 1
    assert data[1][2].seen_trees[direction] == 1
    assert data[1][3].seen_trees[direction] == 1
    assert data[1][4].seen_trees[direction] == 2


def test_count_seen_trees_right(example):
    """Test that visible trees are counted properly"""
    data = deepcopy(example)
    solver.count_visible_trees_right(data)
    direction = VisibilityDirection.RIGHT
    assert data[0][0].seen_trees[direction] == 2
    assert data[0][1].seen_trees[direction] == 1
    assert data[0][2].seen_trees[direction] == 1
    assert data[0][3].seen_trees[direction] == 1
    assert data[0][4].seen_trees[direction] == 0

    assert data[1][0].seen_trees[direction] == 1
    assert data[1][1].seen_trees[direction] == 1
    assert data[1][2].seen_trees[direction] == 2
    assert data[1][3].seen_trees[direction] == 1
    assert data[1][4].seen_trees[direction] == 0


def test_count_seen_trees_top(example):
    """Test that visible trees are counted properly"""
    data = deepcopy(example)
    solver.count_visible_trees_top(data)
    direction = VisibilityDirection.TOP
    assert data[4][0].seen_trees[direction] == 1
    assert data[4][1].seen_trees[direction] == 2
    assert data[4][2].seen_trees[direction] == 1
    assert data[4][3].seen_trees[direction] == 4
    assert data[4][4].seen_trees[direction] == 1

    assert data[3][0].seen_trees[direction] == 1
    assert data[3][1].seen_trees[direction] == 1
    assert data[3][2].seen_trees[direction] == 2
    assert data[3][3].seen_trees[direction] == 3
    assert data[3][4].seen_trees[direction] == 3


def test_count_seen_trees_bottom(example):
    """Test that visible trees are counted properly"""
    data = deepcopy(example)
    solver.count_visible_trees_bottom(data)
    direction = VisibilityDirection.BOTTOM
    assert data[0][0].seen_trees[direction] == 2
    assert data[0][1].seen_trees[direction] == 1
    assert data[0][2].seen_trees[direction] == 1
    assert data[0][3].seen_trees[direction] == 4
    assert data[0][4].seen_trees[direction] == 3

    assert data[1][0].seen_trees[direction] == 1
    assert data[1][1].seen_trees[direction] == 1
    assert data[1][2].seen_trees[direction] == 2
    assert data[1][3].seen_trees[direction] == 1
    assert data[1][4].seen_trees[direction] == 1


def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 8


def test_part2_data(data):
    """Test part 2 on actual input"""
    assert solver.part2(data) == 180_000
