from dataclasses import dataclass

from advent_of_code_2022.day_19.material import Material


@dataclass
class Robots:
    ore_bots: int = 1
    clay_bots: int = 0
    obsidian_bots: int = 0
    geode_bots: int = 0

    def counts(self) -> list[tuple[Material, int]]:
        return [
            (Material.ORE, self.ore_bots),
            (Material.CLAY, self.clay_bots),
            (Material.OBSIDIAN, self.obsidian_bots),
            (Material.GEODE, self.geode_bots),
        ]

    def add_robot(self, material: Material):
        match material:
            case Material.ORE:
                self.ore_bots += 1
            case Material.CLAY:
                self.clay_bots += 1
            case Material.OBSIDIAN:
                self.obsidian_bots += 1
            case Material.GEODE:
                self.geode_bots += 1

    def get_material_robots_stock(self, material: Material) -> int:
        match material:
            case Material.ORE:
                return self.ore_bots
            case Material.CLAY:
                return self.clay_bots
            case Material.OBSIDIAN:
                return self.obsidian_bots
            case Material.GEODE:
                return self.geode_bots
