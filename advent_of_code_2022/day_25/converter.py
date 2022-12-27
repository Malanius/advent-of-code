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


def dec_to_snafu(dec: int) -> str:
    snafu = []

    while dec > 0:
        remainder = dec % SNAFU_BASE

        # we can't have a number greater than 2 in snafu
        if remainder > 2:
            remainder -= SNAFU_BASE  # so we subtract the base to get a negative number
            dec += SNAFU_BASE  # and reflect that in remaining dec

        match remainder:
            case -2:
                snafu.append("=")
            case -1:
                snafu.append("-")
            case _:
                snafu.append(str(remainder))

        dec = dec // SNAFU_BASE

    converted = "".join(reversed(snafu))
    logging.debug(f"Converted {dec} dec to {converted} snf")
    return converted
