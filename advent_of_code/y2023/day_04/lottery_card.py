from typing import TypedDict


class LotteryCard(TypedDict):
    id: int
    winning_numbers: list[int]
    card_numbers: list[int]
    matching_numbers: int
    count: int