from typing import TypedDict


class Almanac(TypedDict):
    """Almanac"""

    seeds: list[int]
    seedToSoilMap: dict[range, range]
    soilToFertilizerMap: dict[range, range]
    fertilizerToWaterMap: dict[range, range]
    waterToLightMap: dict[range, range]
    lightToTemperatureMap: dict[range, range]
    temparatureToHumidityMap: dict[range, range]
    humidityToLocationMap: dict[range, range]