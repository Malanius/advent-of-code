import pathlib
import pytest
import aoc_2022_10 as solver

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def sample():
    puzzle_input = """noop
addx 3
addx -5"""
    return solver.parse(puzzle_input)


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return solver.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example-2.txt").read_text().strip()
    return solver.parse(puzzle_input)


def test_parse_sample(sample):
    """Test that input is parsed properly"""
    assert sample == ["noop", "addx 3", "addx -5"]

def test_sample_execution(sample):
    """Test that sample input is executed properly"""
    cpu = solver.Cpu()
    cpu.process_instructions(sample)
    assert cpu.reg_x == -1, "Register X should be -1"
    assert cpu.cycles == 5, "Should take 5 cycles to complete"
    assert cpu.states == [1, 1, 4, 4, -1], "Should have correct states"

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert solver.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert solver.part2(example2) == ...
