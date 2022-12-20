import logging
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


def can_build_bot(
    blueprint: Blueprint, inventory: Inventory, robots: Inventory, material: Material
) -> bool:
    """Check if we have enough resources to build a robot"""
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


def get_max_geodes(
    time_left: int,
    blueprint: Blueprint,
    inventory: Inventory = Inventory(),
    robots: Inventory = Inventory(ore=1),
) -> int:
    """Get the maximum number of geodes that can be collected"""

    if time_left == 0:
        logging.debug(f"T: {time_left} I: {inventory} R: {robots}")
        return 0

    max_geodes = 0
    for strategy in build_strategies:
        if time_left == 1 and strategy is not None:
            continue  # building on last turn is a waste

        current_inventory = inventory.copy()
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

        max_geodes = current_inventory.geode + max(
            max_geodes,
            get_max_geodes(
                time_left - 1,
                blueprint,
                current_inventory + robots,
                robots + built_robots,
            ),
        )
    return max_geodes
