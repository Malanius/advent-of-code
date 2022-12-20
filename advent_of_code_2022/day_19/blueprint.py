import re
from dataclasses import dataclass
from typing import Generator

from advent_of_code_2022.day_19.inventory import Inventory

BLUEPRINT_PATTERN = re.compile(
    r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
)


@dataclass
class Blueprint:
    id: int
    ore_bot_cost: Inventory
    clay_bot_cost: Inventory
    obsidian_bot_cost: Inventory
    geode_bot_cost: Inventory

    def __hash__(self) -> int:
        return hash(self.id)

    def __post_init__(self):
        self.max_ore_cost = max(
            self.ore_bot_cost.ore,
            self.clay_bot_cost.ore,
            self.obsidian_bot_cost.ore,
            self.geode_bot_cost.ore,
        )
        self.max_clay_cost = self.obsidian_bot_cost.clay
        self.max_obsidian_cost = self.geode_bot_cost.obsidian


Blueprints = Generator[Blueprint, None, None]
