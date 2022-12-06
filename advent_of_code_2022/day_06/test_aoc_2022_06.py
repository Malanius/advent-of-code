import pathlib
import pytest
import aoc_2022_06 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def data():
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    return puzzle_input


@pytest.mark.parametrize(
    "input, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_part1_examples(input, expected):
    """Test part 1 on example input"""
    assert solver.part1(input) == expected


def test_part1_data(data):
    """Test part 1 on data input"""
    assert solver.part1(data) == 1766


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
