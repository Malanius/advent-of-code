import re
from dataclasses import dataclass
from typing import Generator

BLUEPRINT_PATTERN = re.compile(
    r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
)


@dataclass
class Blueprint:
    id: int
    ore_bot_cost_ores: int
    clay_bot_cost_ores: int
    obsidian_bot_cost_ores: int
    obsidian_bot_cost_clay: int
    geode_bot_cost_ores: int
    geode_bot_cost_obsidian: int

    def __hash__(self) -> int:
        return hash(self.id)

    @property
    def max_ore_cost(self) -> int:
        return max(
            self.ore_bot_cost_ores,
            self.clay_bot_cost_ores,
            self.obsidian_bot_cost_ores,
            self.geode_bot_cost_ores,
        )

    @property
    def max_clay_cost(self) -> int:
        return self.obsidian_bot_cost_clay

    @property
    def max_obsidian_cost(self) -> int:
        return self.geode_bot_cost_obsidian


Blueprints = Generator[Blueprint, None, None]
