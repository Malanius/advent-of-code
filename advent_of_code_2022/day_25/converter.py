import logging


SNAFU_BASE = 5


def index_to_num(number: int, index: int):
    if index == 0:
        return number

    return number * SNAFU_BASE**index


def snafu_to_dec(snafu: str) -> int:
    numbers = []

    # reverse the nuybmer to get index as exponent
    enumerated = enumerate(reversed(snafu))

    for index, char in enumerated:
        match char:
            case "=":
                numbers.append(index_to_num(-2, index))
            case "-":
                numbers.append(index_to_num(-1, index))
            case _:
                numbers.append(index_to_num(int(char), index))

    converted = sum(numbers)
    logging.debug(f"Converted {snafu} snf to {converted} dec")
    return converted
