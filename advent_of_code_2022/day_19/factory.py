import logging
from collections import deque
from dataclasses import dataclass, field
from typing import Optional

from advent_of_code_2022.day_19.blueprint import Blueprint
from advent_of_code_2022.day_19.inventory import Inventory
from advent_of_code_2022.day_19.material import Material

build_strategies: list[Optional[Material]] = [
    Material.GEODE,
    Material.OBSIDIAN,
    Material.CLAY,
    Material.ORE,
    None,
]


@dataclass
class Factory:
    blueprint: Blueprint
    time_left: int
    build_strategy: Optional[Material] = None
    build_queue: deque[Material] = field(default_factory=deque)
    inventory: Inventory = field(default_factory=Inventory)
    robots: Inventory = field(default_factory=Inventory)

    def __post_init__(self):
        logging.debug(f"Factory created: {self!r}")

    def __hash__(self) -> int:
        return hash((self.blueprint, self.inventory, self.robots))

    def _can_build_bot(self, material: Material) -> bool:
        """Check if we have enough resources to build a robot"""
        match material:
            case Material.ORE:
                return (
                    self.inventory.ore >= self.blueprint.ore_bot_cost.ore
                    and self.robots.ore < self.blueprint.max_ore_cost
                )
            case Material.CLAY:
                return (
                    self.inventory.ore >= self.blueprint.clay_bot_cost.ore
                    and self.robots.clay < self.blueprint.max_clay_cost
                )
            case Material.OBSIDIAN:
                return (
                    self.inventory.ore >= self.blueprint.obsidian_bot_cost.ore
                    and self.inventory.clay >= self.blueprint.obsidian_bot_cost.clay
                    and self.robots.obsidian < self.blueprint.max_obsidian_cost
                )
            case Material.GEODE:
                return (
                    self.inventory.ore >= self.blueprint.geode_bot_cost.ore
                    and self.inventory.obsidian
                    >= self.blueprint.geode_bot_cost.obsidian
                )

    def _spend_build_resources(self, material: Material):
        """Spend resources to build a robot"""
        cost = Inventory()
        match material:
            case Material.ORE:
                cost = self.blueprint.ore_bot_cost
            case Material.CLAY:
                cost = self.blueprint.clay_bot_cost
            case Material.OBSIDIAN:
                cost = self.blueprint.obsidian_bot_cost
            case Material.GEODE:
                cost = self.blueprint.geode_bot_cost
            case _:
                raise ValueError(f"Unknown material {material}")
        self.inventory -= cost
        logging.debug(f"Spent {cost} to start building {material}-collecting robot.")

    def _queue_build(
        self,
    ):
        """Queue a build affordable material collection robot"""
        material = self.build_strategy
        if material is None:
            return
        if self._can_build_bot(material):
            self._spend_build_resources(material)
            self.build_queue.append(material)

    def _collect_materials(self):
        """Collect materials for all robots"""
        collected = Inventory(
            self.robots.ore, self.robots.clay, self.robots.obsidian, self.robots.geode
        )
        self.inventory += collected

    def _finish_build(self):
        """Finish building a robot"""
        if not self.build_queue:
            return
        material = self.build_queue.popleft()
        created_robots = Inventory()
        match material:
            case Material.ORE:
                created_robots = Inventory(ore=1)
            case Material.CLAY:
                created_robots = Inventory(clay=1)
            case Material.OBSIDIAN:
                created_robots = Inventory(obsidian=1)
            case Material.GEODE:
                created_robots = Inventory(geode=1)
            case _:
                raise ValueError(f"Unknown robot {material}")
        self.robots += created_robots
        logging.debug(
            f"The new {material}-collecting robot is ready; you now have {self.robots}."
        )

    def _play_round(self):
        """Play one round of the game"""
        logging.debug(f"== T-{self.time_left} ==")
        self._queue_build()
        self._collect_materials()
        self._finish_build()
        logging.debug(f"")

    def get_max_geodes(self) -> int:
        """Get the maximum number of geodes that can be collected"""

        if self.time_left == 0:
            return 0

        geodes = 0
        for strategy in build_strategies:
            factory = Factory(
                blueprint=self.blueprint,
                time_left=self.time_left - 1,
                build_strategy=strategy,
                inventory=self.inventory.copy(),
                robots=self.robots.copy(),
            )
            factory._play_round()
            geodes = max(geodes, factory.get_max_geodes())
        return geodes
