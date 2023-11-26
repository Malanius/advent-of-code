import re
from dataclasses import dataclass
from typing import Generator

from advent_of_code.day_19.inventory import Inventory
from advent_of_code.day_19.material import Material

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

    @property
    def costs(self) -> dict[Material, Inventory]:
        return {
            Material.ORE: self.ore_bot_cost,
            Material.CLAY: self.clay_bot_cost,
            Material.OBSIDIAN: self.obsidian_bot_cost,
            Material.GEODE: self.geode_bot_cost,
        }
