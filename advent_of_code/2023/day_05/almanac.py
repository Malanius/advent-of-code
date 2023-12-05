from typing import TypedDict


class Almanac(TypedDict):
    """Almanac"""

    seeds: list[int]
    seeds_ranges: list[range]
    seedToSoilMap: dict[range, range]
    soilToFertilizerMap: dict[range, range]
    fertilizerToWaterMap: dict[range, range]
    waterToLightMap: dict[range, range]
    lightToTemperatureMap: dict[range, range]
    temparatureToHumidityMap: dict[range, range]
    humidityToLocationMap: dict[range, range]

class SeedInfo(TypedDict):
    """Seed Info"""
    seed: int
    soil: int
    fertilizer: int
    water: int
    light: int
    temperature: int
    humidity: int
    location: int