import logging
from collections import deque
from dataclasses import dataclass, field

from advent_of_code_2022.day_19.blueprint import Blueprint
from advent_of_code_2022.day_19.inventory import Inventory
from advent_of_code_2022.day_19.material import Material
from advent_of_code_2022.day_19.robots import Robots

build_priorities: list[Material] = [
    Material.GEODE,
    Material.OBSIDIAN,
    Material.CLAY,
    Material.ORE,
]


@dataclass
class Factory:
    blueprint: Blueprint
    build_queue: deque[Material] = field(default_factory=deque)
    inventory: Inventory = field(default_factory=Inventory)
    robots: Robots = field(default_factory=Robots)

    def __post_init__(self):
        logging.debug(f"Factory created: {self!r}")

    def _can_build_bot(self, material: Material) -> bool:
        """Check if we have enough resources to build a robot"""
        match material:
            case Material.ORE:
                return (
                    self.inventory.ore >= self.blueprint.ore_bot_cost_ores
                    and self.robots.ore_bots < self.blueprint.max_ore_cost
                )
            case Material.CLAY:
                return (
                    self.inventory.ore >= self.blueprint.clay_bot_cost_ores
                    and self.robots.clay_bots < self.blueprint.max_clay_cost
                )
            case Material.OBSIDIAN:
                return (
                    self.inventory.ore >= self.blueprint.obsidian_bot_cost_ores
                    and self.inventory.clay >= self.blueprint.obsidian_bot_cost_clay
                    and self.robots.obsidian_bots < self.blueprint.max_obsidian_cost
                )
            case Material.GEODE:
                return (
                    self.inventory.ore >= self.blueprint.geode_bot_cost_ores
                    and self.inventory.obsidian
                    >= self.blueprint.geode_bot_cost_obsidian
                )

    def _spend_build_resources(self, material: Material):
        """Spend resources to build a robot"""
        cost_str = ""
        match material:
            case Material.ORE:
                cost = self.blueprint.ore_bot_cost_ores
                self.inventory.ore -= cost
                cost_str = f"{cost} ore"
            case Material.CLAY:
                cost = self.blueprint.clay_bot_cost_ores
                self.inventory.ore -= cost
                cost_str = f"{cost} ore"
            case Material.OBSIDIAN:
                cost_ores = self.blueprint.obsidian_bot_cost_ores
                cost_clay = self.blueprint.obsidian_bot_cost_clay
                self.inventory.ore -= cost_ores
                self.inventory.clay -= cost_clay
                cost_str = f"{cost_ores} ore and {cost_clay} clay"
            case Material.GEODE:
                cost_ores = self.blueprint.geode_bot_cost_ores
                cost_obsidian = self.blueprint.geode_bot_cost_obsidian
                self.inventory.ore -= cost_ores
                self.inventory.obsidian -= cost_obsidian
                cost_str = f"{cost_ores} ore and {cost_obsidian} obsidian"
            case _:
                raise ValueError(f"Unknown material {material}")
        logging.debug(
            f"Spent {cost_str} to start building {material}-collecting robot."
        )

    def _queue_build(
        self,
    ):
        """Queue a build affordable material collection robot"""
        for material in build_priorities:
            if self._can_build_bot(material):
                self._spend_build_resources(material)
                self.build_queue.append(material)

    def _collect_materials(self):
        """Collect materials for all robots"""
        for material, robot_count in self.robots.counts():
            self.inventory.add_material(material, robot_count)
            if robot_count > 0:
                logging.debug(
                    f"""{robot_count} {material}-collecting robot(s) collects {robot_count} {material}; you now have {self.inventory.get_material_stock(material)} {material}."""
                )

    def _finish_build(self):
        """Finish building a robot"""
        if not self.build_queue:
            return
        material = self.build_queue.popleft()
        self.robots.add_robot(material)
        count = self.robots.get_material_robots_stock(material)
        logging.debug(
            f"The new {material}-collecting robot is ready; you now have {count} of them."
        )

    def play_round(self):
        """Play one round of the game"""
        self._queue_build()
        self._collect_materials()
        self._finish_build()
