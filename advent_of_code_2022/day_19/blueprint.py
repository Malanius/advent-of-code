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


Blueprints = Generator[Blueprint, None, None]
