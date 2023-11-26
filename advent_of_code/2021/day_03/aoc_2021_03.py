import pathlib
from typing import TypedDict


import pandas as pd
from pandas.core.frame import DataFrame

PUZZLE_DIR = pathlib.Path(__file__).parent


class BitCount(TypedDict):
    zeroes: int
    ones: int


def parse(puzzle_input: str):
    """Parse input"""
    lines = puzzle_input.splitlines()
    data = [list(line) for line in lines]
    return data


def get_bit_counts(data: list[list[str]]) -> list[BitCount]:
    df = pd.DataFrame(data)
    bit_counts: BitCount = []
    for column in df:
        counts = df[column].value_counts()
        bit_counts.append({"zeroes": counts["0"], "ones": counts["1"]})
    return bit_counts


def get_most_common_bit(bit_count: BitCount):
    if bit_count["ones"] > bit_count["zeroes"]:
        return "1"
    elif bit_count["ones"] == bit_count["zeroes"]:
        return "1"
    else:
        return "0"


def get_least_common_bit(bit_count: BitCount):
    if bit_count["ones"] > bit_count["zeroes"]:
        return "0"
    elif bit_count["ones"] == bit_count["zeroes"]:
        return "0"
    else:
        return "1"


def get_gamma_value(bit_counts: list[BitCount]) -> int:
    most_common_bits: str = ""
    for bit_count in bit_counts:
        most_common_bits += get_most_common_bit(bit_count)
    gamma = int(most_common_bits, 2)
    return gamma


def get_sigma_value(bit_counts: list[BitCount]) -> int:
    least_common_bits: str = ""
    for bit_count in bit_counts:
        least_common_bits += get_least_common_bit(bit_count)
    sigma = int(least_common_bits, 2)
    return sigma


def part1(data: list[list[str]]):
    """Solve part 1"""
    bit_counts = get_bit_counts(data)
    gamma = get_gamma_value(bit_counts)
    epsiolon = get_sigma_value(bit_counts)
    return gamma * epsiolon


def filter_out_least_common_bits(df: DataFrame, index: int = 0):
    if len(df) == 1:
        return df
    else:
        counts = df[index].value_counts()
        bit_count = {"zeroes": counts["0"], "ones": counts["1"]}
        least_common_bit = get_least_common_bit(bit_count)
        df = df[df[index] != least_common_bit]
        print(df)
        print("---")
        return filter_out_least_common_bits(df, index + 1)


def filter_out_most_common_bits(df: DataFrame, index: int = 0) -> DataFrame:
    if len(df) == 1:
        return df
    else:
        counts = df[index].value_counts()
        bit_count = {"zeroes": counts["0"], "ones": counts["1"]}
        most_common_bit = get_most_common_bit(bit_count)
        df = df[df[index] != most_common_bit]
        print(df)
        print("---")
        return filter_out_most_common_bits(df, index + 1)


def part2(data: list[list[str]]):
    """Solve part 2"""
    df = pd.DataFrame(data)
    oxygen_bits = filter_out_least_common_bits(df).values.tolist()[0]
    scrubber_bits = filter_out_most_common_bits(df).values.tolist()[0]
    print(f"O2 bits: {oxygen_bits}")
    print(f"Scrubber bits: {scrubber_bits}")
    oxygen_value = int("".join(oxygen_bits), 2)
    scrubber_value = int("".join(scrubber_bits), 2)
    print(f"O2 value: {oxygen_value}")
    print(f"Scrubber value: {scrubber_value}")
    return scrubber_value * oxygen_value


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("--- Solutions ---")
    print("\n".join(str(solution) for solution in solutions))
