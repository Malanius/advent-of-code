import logging
from collections import deque
from dataclasses import dataclass, field

from advent_of_code_2022.day_19.blueprint import Blueprint
from advent_of_code_2022.day_19.material import Material


@dataclass
class Factory:
    blueprint: Blueprint
    build_queue: deque[Material] = field(default_factory=deque)
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
        self._collect_materials()
