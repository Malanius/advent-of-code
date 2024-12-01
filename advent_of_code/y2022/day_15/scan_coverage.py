import logging

from advent_of_code.y2022.day_15.coord import Boundaries
from advent_of_code.y2022.day_15.sensor import Sensor

ScanCoverage = list[tuple[int, int]]


def blend_coverage_ranges(ranges: ScanCoverage) -> ScanCoverage:
    """Blend the overlapping ranges together"""
    ranges = sorted(ranges, key=lambda x: x[0])
    blended_ranges = [ranges[0]]
    for start, end in ranges:
        logging.debug(f"Blended: {blended_ranges}")
        logging.debug(f"Current: {start, end}")

        last_start, last_end = blended_ranges[-1]
        if start <= last_end + 1 and end >= last_end:
            blended_ranges[-1] = (last_start, end)
        elif start <= last_end and end <= last_end:
            continue
        else:
            blended_ranges.append((start, end))

    return blended_ranges


def get_sensors_coverage_at_row(sensors: set[Sensor], row: int):
    """Get the coverage of the sensors at the given row"""
    coverage_ranges = [
        sensor.get_coverage_at_row(row)
        for sensor in sensors
        if sensor.get_coverage_at_row(row)
    ]
    logging.debug(f"Coverage ranges: {coverage_ranges}")
    # not sure why, but mypy doesn't see the None check in the list comprehension
    blended_ranges = blend_coverage_ranges(coverage_ranges)  # type: ignore[arg-type]
    logging.debug(f"Blended ranges: {blended_ranges}")
    return blended_ranges


def get_scan_coverage_bounds(sensors: set[Sensor]) -> Boundaries:
    """Get the boundaries of the scan coverage"""
    min_x = min(sensor.coord.x - sensor.scan_range for sensor in sensors)
    max_x = max(sensor.coord.x + sensor.scan_range for sensor in sensors)
    min_y = min(sensor.coord.y - sensor.scan_range for sensor in sensors)
    max_y = max(sensor.coord.y + sensor.scan_range for sensor in sensors)
    logging.debug(f"Scan bounds: {min_x, max_x, min_y, max_y}")
    return Boundaries(min_x, max_x, min_y, max_y)


def is_covered(coverage: ScanCoverage, x: int) -> bool:
    """Check if the given x coordinate is covered"""
    for start, end in coverage:
        if start <= x <= end:
            return True
    return False
