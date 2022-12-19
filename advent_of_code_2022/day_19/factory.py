import logging
from collections import deque
from dataclasses import dataclass, field

from advent_of_code_2022.day_19.blueprint import Blueprint
from advent_of_code_2022.day_19.material import Material


@dataclass
class Factory:
    blueprint: Blueprint
    build_queue: deque[Material] = field(default_factory=deque)
    build_priority: list[Material] = field(
        default_factory=lambda: [
            Material.GEODE,
            Material.OBSIDIAN,
            Material.CLAY,
            Material.ORE,
        ]
    )
    inventory: dict[Material, int] = field(
        default_factory=lambda: {
            Material.ORE: 0,
            Material.CLAY: 0,
            Material.OBSIDIAN: 0,
            Material.GEODE: 0,
        }
    )
    robots: dict[Material, int] = field(
        default_factory=lambda: {
            Material.ORE: 1,  # Start with one ore robot
            Material.CLAY: 0,
            Material.OBSIDIAN: 0,
            Material.GEODE: 0,
        }
    )

    def _can_build_bot(self, material: Material) -> bool:
        """Check if we have enough resources to build a robot"""
        match material:
            case Material.ORE:
                return self.inventory[Material.ORE] >= self.blueprint.ore_bot_cost_ores
            case Material.CLAY:
                return self.inventory[Material.ORE] >= self.blueprint.clay_bot_cost_ores
            case Material.OBSIDIAN:
                return (
                    self.inventory[Material.ORE]
                    >= self.blueprint.obsidian_bot_cost_ores
                    and self.inventory[Material.CLAY]
                    >= self.blueprint.obsidian_bot_cost_clay
                )
            case Material.GEODE:
                return (
                    self.inventory[Material.ORE] >= self.blueprint.geode_bot_cost_ores
                    and self.inventory[Material.OBSIDIAN]
                    >= self.blueprint.geode_bot_cost_obsidian
                )

    def _spend_build_resources(self, material: Material):
        """Spend resources to build a robot"""
        cost_str = ""
        match material:
            case Material.ORE:
                cost = self.blueprint.ore_bot_cost_ores
                self.inventory[Material.ORE] -= cost
                cost_str = f"{cost} ore"
            case Material.CLAY:
                cost = self.blueprint.clay_bot_cost_ores
                self.inventory[Material.ORE] -= cost
                cost_str = f"{cost} ore"
            case Material.OBSIDIAN:
                cost_ores = self.blueprint.obsidian_bot_cost_ores
                cost_clay = self.blueprint.obsidian_bot_cost_clay
                self.inventory[Material.ORE] -= cost_ores
                self.inventory[Material.CLAY] -= cost_clay
                cost_str = f"{cost_ores} ore and {cost_clay} clay"
            case Material.GEODE:
                cost_ores = self.blueprint.geode_bot_cost_ores
                cost_obsidian = self.blueprint.geode_bot_cost_obsidian
                self.inventory[Material.ORE] -= cost_ores
                self.inventory[Material.OBSIDIAN] -= cost_obsidian
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
        for material in self.build_priority:
            if self._can_build_bot(material):
                self._spend_build_resources(material)
                self.build_queue.append(material)
                break

    def _collect_materials(self):
        """Collect materials for the next robot"""
        for material, robot_count in self.robots.items():
            self.inventory[material] += robot_count
            if robot_count > 0:
                logging.debug(
                    f"""{robot_count} {material}-collecting robot(s) collects {robot_count} {material}; you now have {self.inventory[material]} {material}."""
                )

    def play_round(self):
        """Play one round of the game"""
        self._queue_build()
        self._collect_materials()
