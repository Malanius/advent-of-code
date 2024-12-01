from functools import cache

# import logging
from typing import Optional

from advent_of_code.y2022.day_19.blueprint import Blueprint
from advent_of_code.y2022.day_19.inventory import Inventory
from advent_of_code.y2022.day_19.material import Material

build_strategies: list[Optional[Material]] = [
    Material.GEODE,
    Material.OBSIDIAN,
    Material.CLAY,
    Material.ORE,
    None,
]


def can_build_bot(
    blueprint: Blueprint, inventory: Inventory, robots: Inventory, material: Material
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


@cache
def get_max_geodes(
    time_left: int,
    blueprint: Blueprint,
    inv_ore: int = 0,
    inv_clay: int = 0,
    inv_obsidian: int = 0,
    rob_ore: int = 1,
    rob_clay: int = 0,
    rob_obsidian: int = 0,
    rob_geode: int = 0,
) -> int:
    """Get the maximum number of geodes that can be collected"""

    if time_left == 0:
        return 0

    max_geodes = 0
    for strategy in build_strategies:
        if time_left == 1 and strategy is not None:
            continue  # building on last turn is a waste

        current_inventory = Inventory(
            inv_ore,
            inv_clay,
            inv_obsidian,
        )
        robots = Inventory(
            rob_ore,
            rob_clay,
            rob_obsidian,
            rob_geode,
        )
        built_robots = Inventory()

        match strategy:
            case Material.ORE:
                if can_build_bot(blueprint, current_inventory, robots, Material.ORE):
                    current_inventory -= blueprint.ore_bot_cost
                    built_robots = Inventory(ore=1)
                else:
                    continue

            case Material.CLAY:
                if can_build_bot(blueprint, current_inventory, robots, Material.CLAY):
                    current_inventory -= blueprint.clay_bot_cost
                    built_robots = Inventory(clay=1)
                else:
                    continue

            case Material.OBSIDIAN:
                if can_build_bot(
                    blueprint, current_inventory, robots, Material.OBSIDIAN
                ):
                    current_inventory -= blueprint.obsidian_bot_cost
                    built_robots = Inventory(obsidian=1)
                else:
                    continue

            case Material.GEODE:
                if can_build_bot(blueprint, current_inventory, robots, Material.GEODE):
                    current_inventory -= blueprint.geode_bot_cost
                    built_robots = Inventory(geode=1)
                else:
                    continue

        current_inventory += robots
        robots += built_robots
        # trim inventory to maximum prices, no need to keep more than that, limits cache search space
        trimmed_ore = min(current_inventory.ore, blueprint.max_ore_cost)
        trimmed_clay = min(current_inventory.clay, blueprint.max_clay_cost)
        trimmed_obsidian = min(current_inventory.obsidian, blueprint.max_obsidian_cost)

        branch_score = current_inventory.geode + get_max_geodes(
            time_left - 1,
            blueprint,
            current_inventory.ore,
            current_inventory.clay,
            current_inventory.obsidian,
            # trimmed_ore,
            # trimmed_clay,
            # trimmed_obsidian,
            robots.ore,
            robots.clay,
            robots.obsidian,
            robots.geode,
        )

        max_geodes = max(max_geodes, branch_score)
        # logging.debug(
        #     f'"T: {time_left}", "I: {current_inventory}", "R: {robots}", "M: {max_geodes}"'
        # )
    return max_geodes
