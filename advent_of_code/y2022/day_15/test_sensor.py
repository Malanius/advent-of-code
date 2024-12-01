import pytest
from coord import Coord
from sensor import Sensor


@pytest.fixture
def sensor() -> Sensor:
    return Sensor(Coord(6, 6), 5)


@pytest.mark.parametrize(
    "y, expected",
    [
        (0, None),
        (1, (6, 6)),
        (2, (5, 7)),
        (3, (4, 8)),
        (4, (3, 9)),
        (5, (2, 10)),
        (6, (1, 11)),
        (7, (2, 10)),
        (8, (3, 9)),
        (9, (4, 8)),
        (10, (5, 7)),
        (11, (6, 6)),
        (12, None),
    ],
    ids=[
        "y=0, out of range",
        "y=1",
        "y=2",
        "y=3",
        "y=4",
        "y=5",
        "y=6, full range",
        "y=7",
        "y=8",
        "y=9",
        "y=10",
        "y=11",
        "y=12, out of range",
    ],
)
def test_get_coverage_at_y(sensor: Sensor, y: int, expected: tuple[int, int]):
    assert sensor.get_coverage_at_row(y) == expected
