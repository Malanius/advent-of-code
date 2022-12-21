from dataclasses import dataclass, field, replace
from typing import Generator, Optional
import logging

from advent_of_code_2022.day_19.blueprint import Blueprint
from advent_of_code_2022.day_19.inventory import Inventory
from advent_of_code_2022.day_19.material import Material

build_strategies: list[Material] = [
    Material.ORE,
    Material.CLAY,
    Material.OBSIDIAN,
    Material.GEODE,
]


def can_build_bot(
    material: Material, blueprint: Blueprint, inventory: Inventory, robots: Inventory
) -> bool:
    """Check if we have enough resources to build a robot and enough robots to cover maximal costs"""
    match material:
        case Material.ORE:
            return (
                inventory.ore >= blueprint.ore_bot_cost.ore
                and robots.ore < blueprint.max_ore_cost
            )
        case Material.CLAY:
            return (
                inventory.ore >= blueprint.clay_bot_cost.ore
                and robots.clay < blueprint.max_clay_cost
            )
        case Material.OBSIDIAN:
            return (
                inventory.ore >= blueprint.obsidian_bot_cost.ore
                and inventory.clay >= blueprint.obsidian_bot_cost.clay
                and robots.obsidian < blueprint.max_obsidian_cost
            )
        case Material.GEODE:
            return (
                inventory.ore >= blueprint.geode_bot_cost.ore
                and inventory.obsidian >= blueprint.geode_bot_cost.obsidian
            )


@dataclass(frozen=True)
class FactoryState:
    time_left: int
    blueprint: Blueprint = field(repr=False)
    inventory: Inventory = Inventory()
    robots: Inventory = Inventory(ore=1)

    def trim_invetory(self, inventory: Inventory, time_left: int) -> Inventory:
        """Trim inventory to maximal costs"""
        max_ore_cost = self.blueprint.max_ore_cost
        max_clay_cost = self.blueprint.max_clay_cost
        max_obsidian_cost = self.blueprint.max_obsidian_cost
        return Inventory(
            ore=min(inventory.ore, max_ore_cost + max_ore_cost * time_left),
            clay=min(inventory.clay, max_clay_cost + max_clay_cost * time_left),
            obsidian=min(
                inventory.obsidian, max_obsidian_cost + max_obsidian_cost * time_left
            ),
            geode=inventory.geode,
        )

    def next_states(self) -> Generator["FactoryState", None, None]:
        """Get all possible next states"""
        for material in build_strategies:
            time_left = self.time_left
            inventory = self.inventory
            robots = self.robots
            logging.debug(f"---")
            logging.debug(f"{time_left:2d}: Trying to build {material} robot")

            # do not try building robot for which we don't collect materials yet
            if material == Material.OBSIDIAN and robots.clay == 0:
                logging.debug(
                    f"{time_left:2d}: Not collecting materias for {material} robot yet"
                )
                continue
            if material == Material.GEODE and robots.obsidian == 0:
                logging.debug(
                    f"{time_left:2d}: Not collecting materias for {material} robot yet"
                )
                continue

            while time_left:
                # wait until enough resources to build given robot
                if can_build_bot(material, self.blueprint, inventory, robots):
                    logging.debug(f"{time_left:2d}: Building {material} robot")
                    break

                time_left -= 1
                inventory += robots  # collect resources
                logging.debug(f"{time_left:2d}: I({inventory}), R({robots})")

            if time_left:
                time_left -= 1
                inventory -= self.blueprint.costs[material]  # pay for robot
                gained_robots = Inventory(**{material: 1})
                inventory += robots  # collect resources
                logging.debug(f"{time_left:2d}: I({inventory}), R({robots})")
                yield replace(
                    self,
                    time_left=time_left,
                    inventory=self.trim_invetory(inventory, time_left),
                    robots=robots + gained_robots,
                )


def get_max_geodes_opt(
    time_left: int,
    blueprint: Blueprint,
) -> int:
    """Get the maximum number of geodes that can be collected"""
    initial = FactoryState(time_left=time_left, blueprint=blueprint)
    logging.debug(f"Initial state: {initial}")

    to_visit = [initial]
    visited = set()
    max_geodes = -1
    best_state = None
    while to_visit:
        state = to_visit.pop()
        if state in visited:
            logging.debug(f"Already visited: {state}")
            continue
        visited.add(state)
        if state.inventory.geode > max_geodes:
            max_geodes = state.inventory.geode
            best_state = state
            logging.debug(f"New best state: {best_state}")
        for next_state in state.next_states():
            logging.debug(next_state)
            to_visit.append(next_state)
    logging.debug(f"Best state: {best_state}")
    return max_geodes
