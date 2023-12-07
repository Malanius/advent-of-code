from collections import Counter
from dataclasses import dataclass
from enum import Enum


class Kind(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclass
class Hand:
    cards: str
    bid: int
    sortable_cards: str = ""
    kind: Kind = Kind.HIGH_CARD

    def __post_init__(self):
        self._get_kind()
        self._make_sortable()

    def _make_sortable(self):
        """Convert hand to sortable string"""
        cards = self.cards.replace("A", "Z")
        cards = cards.replace("K", "Y")
        cards = cards.replace("Q", "X")
        cards = cards.replace("J", "W")
        cards = cards.replace("T", "V")
        self.sortable_cards = cards

    def _get_kind(self):
        counts = Counter(self.cards)
        # High card
        if len(counts) == 5:
            self.kind = Kind.HIGH_CARD
            return
        # One pair
        if len(counts) == 4:
            self.kind = Kind.ONE_PAIR
            return
        # Two pairs
        if len(counts) == 3:
            if 2 in counts.values():
                self.kind = Kind.TWO_PAIRS
                return
        # Three of a kind
            self.kind = Kind.THREE_OF_A_KIND
            return
        # Full house
        if len(counts) == 2:
            if 2 in counts.values():
                self.kind = Kind.FULL_HOUSE
                return
        # Four of a kind
            self.kind = Kind.FOUR_OF_A_KIND
            return
        # Five of a kind
        self.kind = Kind.FIVE_OF_A_KIND