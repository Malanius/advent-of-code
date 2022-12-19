from attr import dataclass

from advent_of_code_2022.day_19.material import Material


@dataclass
class Inventory:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def add_material(self, material: Material, count: int):
        match material:
            case Material.ORE:
                self.ore += count
            case Material.CLAY:
                self.clay += count
            case Material.OBSIDIAN:
                self.obsidian += count
            case Material.GEODE:
                self.geode += count

    def get_material_stock(self, material: Material) -> int:
        match material:
            case Material.ORE:
                return self.ore
            case Material.CLAY:
                return self.clay
            case Material.OBSIDIAN:
                return self.obsidian
            case Material.GEODE:
                return self.geode
