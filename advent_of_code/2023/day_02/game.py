from typing import TypedDict


class DrawSet(TypedDict, total=False):
    red: int
    green: int
    blue: int


class ParsedGame(TypedDict):
    id: int
    draws: list[DrawSet]
