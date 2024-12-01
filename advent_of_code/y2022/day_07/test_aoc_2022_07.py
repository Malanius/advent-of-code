import pathlib

import pytest

import advent_of_code.y2022.day_07.aoc_2022_07 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example() -> solver.FileSystem:
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def data() -> solver.FileSystem:
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example.root.size == 48381165, "Root size is wrong"
    assert len(example.root.subdirs) == 2, "Root should have 2 subdirs"
    assert len(example.root.files) == 2, "Root should have 2 files"
    d_dir = example.root.subdirs["d"]
    assert d_dir, "d dir should exist"
    assert d_dir.parent == example.root, "d dir should have root as parent"
    assert d_dir.size == 24933642, "d dir size is wrong"
    assert len(d_dir.subdirs) == 0, "d dir should have no subdirs"
    assert len(d_dir.files) == 4, "d dir should have 4 files"
    a_dir = example.root.subdirs["a"]
    assert a_dir, "a dir should exist"
    assert a_dir.parent == example.root, "a dir should have root as parent"
    assert a_dir.size == 94853, "a dir size is wrong"
    assert len(a_dir.subdirs) == 1, "a dir should have 1 subdir"
    assert len(a_dir.files) == 3, "a dir should have 3 files"
    e_dir = a_dir.subdirs["e"]
    assert e_dir, "e dir should exist"
    assert e_dir.parent == a_dir, "e dir should have a dir as parent"
    assert e_dir.size == 584, "e dir size is wrong"
    assert len(e_dir.subdirs) == 0, "e dir should have no subdirs"
    assert len(e_dir.files) == 1, "e dir should have 3 files"


def test_part1_example(example):
    """Test part 1 on example input"""
    assert solver.part1(example) == 95437


def test_part1_data(data):
    """Test part 1 on example input"""
    assert solver.part1(data) == 1428881


def test_part2_example(example):
    """Test part 2 on example input"""
    assert solver.part2(example) == 24933642
