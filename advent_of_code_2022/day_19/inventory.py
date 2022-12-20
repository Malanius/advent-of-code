from dataclasses import dataclass


@dataclass(frozen=True)
class Inventory:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __hash__(self) -> int:
        return hash((self.ore, self.clay, self.obsidian, self.geode))

    def __add__(self, other: "Inventory") -> "Inventory":
        return Inventory(
            self.ore + other.ore,
            self.clay + other.clay,
            self.obsidian + other.obsidian,
            self.geode + other.geode,
        )

    def __sub__(self, other: "Inventory") -> "Inventory":
        ore = self.ore - other.ore
        clay = self.clay - other.clay
        obsidian = self.obsidian - other.obsidian
        geode = self.geode - other.geode
        if ore < 0 or clay < 0 or obsidian < 0 or geode < 0:
            raise ValueError("Cannot have negative inventory")

        return Inventory(ore, clay, obsidian, geode)

    def copy(self):
        return Inventory(self.ore, self.clay, self.obsidian, self.geode)
