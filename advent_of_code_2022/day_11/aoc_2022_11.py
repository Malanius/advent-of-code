import logging
import pathlib
from collections import deque
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from advent_of_code_2022.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


@dataclass
class Monkey:
    id: int
    items: Optional[deque] = None
    operation: Optional[str] = None
    test_divisible_by: Optional[int] = None
    test_true_target: Optional[int] = None
    test_false_target: Optional[int] = None


def parse(puzzle_input: str) -> dict[int, Monkey]:
    """Parse input"""
    lines = puzzle_input.splitlines()
    monkeys = {}
    current_monkey = 0
    for line in lines:
        match line.split():
            case ["Monkey", id]:
                current_monkey = int(id[:-1])  # remove colon
                monkeys[current_monkey] = Monkey(current_monkey)
                logging.debug(f"Created new monkey {current_monkey}:")
            case ["Starting", "items:", *items]:
                items = "".join(items).split(",")
                items = deque(int(item) for item in items)
                monkeys[current_monkey].items = items
                logging.debug(f"  Monkey {current_monkey} has items {items}")
            case ["Operation:", *operation]:
                operation = " ".join(operation)
                monkeys[current_monkey].operation = operation
                logging.debug(f"  Monkey {current_monkey} has operation: {operation}")
            case ["Test:", "divisible", "by", n]:
                monkeys[current_monkey].test_divisible_by = int(n)
                logging.debug(f"  Monkey {current_monkey} tests divisible by {n}:")
            case ["If", "true:", "throw", "to", "monkey", n]:
                monkeys[current_monkey].test_true_target = int(n)
                logging.debug(f"    Monkey {current_monkey} tests true throws to {n}")
            case ["If", "false:", "throw", "to", "monkey", n]:
                monkeys[current_monkey].test_false_target = int(n)
                logging.debug(f"    Monkey {current_monkey} tests false throws to {n}")
    logging.debug(monkeys)
    return monkeys


@perf
def part1(data):
    """Solve part 1"""


@perf
def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
