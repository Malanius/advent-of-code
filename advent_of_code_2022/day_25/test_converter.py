import pytest

from advent_of_code_2022.day_25.converter import dec_to_snafu, snafu_to_dec


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
def test_snafu_to_dec(input: str, expected: int) -> None:
    assert snafu_to_dec(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (1747, "1=-0-2"),
        (906, "12111"),
        (198, "2=0="),
        (11, "21"),
        (201, "2=01"),
        (31, "111"),
        (1257, "20012"),
        (32, "112"),
        (353, "1=-1="),
        (107, "1-12"),
        (7, "12"),
        (3, "1="),
        (37, "122"),
    ],
)
def test_dec_to_snafu(input: int, expected: str) -> None:
    assert dec_to_snafu(input) == expected
