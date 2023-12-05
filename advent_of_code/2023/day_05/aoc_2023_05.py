import logging
import pathlib
from pprint import pformat

from almanac import Almanac
from arguments import init_args

from advent_of_code.util.perf import perf

PUZZLE_DIR = pathlib.Path(__file__).parent
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse_seeds(line: str) -> list[int]:
    """Parse seeds from a line"""
    return [int(seed) for seed in line.split(":")[1].split()]


def parse_map(lines: list[str]) -> dict[range, range]:
    mapping: dict[range, range] = {}
    for line in lines:
        if "map" in line:
            continue

        dest_range_start, source_range_start, range_length = [
            int(num) for num in line.split()
        ]
        mapping[range(source_range_start, source_range_start + range_length)] = range(
            dest_range_start, dest_range_start + range_length
        )

    return mapping


def parse(puzzle_input: str) -> Almanac:
    """Parse input"""
    parts = puzzle_input.split("\n\n")
    almanac: Almanac = {
        "seeds": parse_seeds(parts[0]),
        "seedToSoilMap": parse_map(parts[1].splitlines()),
        "soilToFertilizerMap": parse_map(parts[2].splitlines()),
        "fertilizerToWaterMap": parse_map(parts[3].splitlines()),
        "waterToLightMap": parse_map(parts[4].splitlines()),
        "lightToTemperatureMap": parse_map(parts[5].splitlines()),
        "temparatureToHumidityMap": parse_map(parts[6].splitlines()),
        "humidityToLocationMap": parse_map(parts[7].splitlines()),
    }

    logging.debug(pformat(almanac))
    return almanac


def find_in_map(mapping: dict[range, range], value: int) -> int:
    for source_range, dest_range in mapping.items():
        if value in source_range:
            return value - source_range.start + dest_range.start

    return value


@perf
def part1(data: Almanac):
    """Solve part 1"""
    locations = set()
    for seed in data["seeds"]:
        soil = find_in_map(data["seedToSoilMap"], seed)
        fertilizer = find_in_map(data["soilToFertilizerMap"], soil)
        water = find_in_map(data["fertilizerToWaterMap"], fertilizer)
        light = find_in_map(data["waterToLightMap"], water)
        temperature = find_in_map(data["lightToTemperatureMap"], light)
        humidity = find_in_map(data["temparatureToHumidityMap"], temperature)
        location = find_in_map(data["humidityToLocationMap"], humidity)
        logging.debug(
            (
                f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, "
                f"water {water}, light {light}, temperature {temperature}, "
                f"humidity {humidity}, location {location}."
            )
        )
        locations.add(location)

    return min(locations)

@perf
def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    args = init_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    data_file = "example.txt" if not args.data else "data.txt"
    puzzle_input = (PUZZLE_DIR / data_file).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
