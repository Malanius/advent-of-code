import logging
import pathlib
from collections import deque
from copy import deepcopy
from dataclasses import dataclass
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
    inspects: int = 0

    def inspect(self, item: int) -> int:
        """Inspect item"""
        assert self.operation is not None
        self.inspects += 1
        logging.debug(f"  Monkey inspects an item with a worry level of {item}.")
        old = item
        new = eval(self.operation)
        logging.debug(f"    Worry level is increased to {new}.")
        bored = new // 3
        logging.debug(
            f"    Monkey gets bored with item. Worry level is divided by 3 to {bored}."
        )
        return bored

    def test(self, worry: int) -> bool:
        """Test item"""
        assert self.test_divisible_by is not None
        divisible = worry % self.test_divisible_by == 0
        logging.debug(
            f"    Current worry level is{'' if divisible else ' not'} divisible by {self.test_divisible_by}."
        )
        return divisible

    def throw(self, target: "Monkey", item: int):
        """Throw item to target monkey"""
        assert target.items is not None
        logging.debug(
            f"    Item with worry level {item} is thrown to monkey {target.id}."
        )
        target.items.append(item)

    def play_round(self, monkeys: dict[int, "Monkey"]):
        """Play one round of the monkey business game"""
        logging.debug(f"Monkey {self.id}:")
        while self.items:
            item = self.items.popleft()
            item = self.inspect(item)
            if self.test(item):
                target = self.test_true_target
            else:
                target = self.test_false_target
            assert target is not None
            self.throw(monkeys[target], item)


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
            case ["Operation:", "new", "=", *operation]:
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


def play_rounds(monkeys: dict[int, Monkey], rounds: int):
    """Play rounds of the monkey business game"""
    for i in range(rounds):
        logging.debug(f"--- Round {i + 1}: ---")
        for monkey in monkeys.values():
            monkey.play_round(monkeys)
        logging.debug("")
        for monkey in monkeys.values():
            logging.debug(f"Monkey {monkey.id}: {monkey.items}")
        logging.debug("")
        for monkey in monkeys.values():
            logging.debug(
                f"Monkey {monkey.id} inspected items {monkey.inspects} times."
            )
        logging.debug("")


@perf
def part1(data):
    """Solve part 1"""
    play_rounds(data, 20)
    monkeys_activity = sorted(
        [monkey.inspects for monkey in data.values()], reverse=True
    )
    monkey_bussiness = monkeys_activity[0] * monkeys_activity[1]
    return monkey_bussiness


@perf
def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(deepcopy(data))
    solution2 = part2(deepcopy(data))
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
