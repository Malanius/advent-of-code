import pytest

from advent_of_code_2022.day_25.converter import snafu_to_dec


@pytest.mark.parametrize(
    "input, expected",
    [
        ("1=-0-2", 1747),
        ("12111", 906),
        ("2=0=", 198),
        ("21", 11),
        ("2=01", 201),
        ("111", 31),
        ("20012", 1257),
        ("112", 32),
        ("1=-1=", 353),
        ("1-12", 107),
        ("12", 7),
        ("1=", 3),
        ("122", 37),
    ],
)
def test_snafu_to_dec(input: str, expected: int):
    assert snafu_to_dec(input) == expected
