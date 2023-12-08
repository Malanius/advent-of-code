import pathlib
import pytest
import aoc_2023_08 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1() -> dict[str, str]:
    puzzle_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
    return solver.parse(puzzle_input)


@pytest.fixture
def example2() -> dict[str, str]:
    puzzle_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
    return solver.parse(puzzle_input)


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {
        "AAA": ("BBB", "CCC"),
        "BBB": ("DDD", "EEE"),
        "CCC": ("ZZZ", "GGG"),
        "DDD": ("DDD", "DDD"),
        "EEE": ("EEE", "EEE"),
        "GGG": ("GGG", "GGG"),
        "ZZZ": ("ZZZ", "ZZZ"),
        "instructions": "RL",
    }


def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert example2 == {
        "AAA": ("BBB", "BBB"),
        "BBB": ("AAA", "ZZZ"),
        "ZZZ": ("ZZZ", "ZZZ"),
        "instructions": "LLR",
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == 2

def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert solver.part1(example2) == 6

def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 12643


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example1):
    """Test part 2 on example input"""
    assert solver.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_data(data):
    """Test part 2 on data input"""
    assert solver.part2(data) == ...
