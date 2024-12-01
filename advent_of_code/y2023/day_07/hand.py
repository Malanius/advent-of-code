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

    def _get_kind(self):
        card_counts = Counter(self.cards)

        # Check for High Card
        if len(card_counts) == 5:
            self.kind = Kind.HIGH_CARD
            return

        # Check for One Pair
        if len(card_counts) == 4:
            self.kind = Kind.ONE_PAIR
            return

        # Check for Two Pairs or Three of a Kind
        if len(card_counts) == 3:
            if 2 in card_counts.values():
                self.kind = Kind.TWO_PAIRS
            else:
                self.kind = Kind.THREE_OF_A_KIND
            return

        # Check for Full House or Four of a Kind
        if len(card_counts) == 2:
            if 2 in card_counts.values():
                self.kind = Kind.FULL_HOUSE
            else:
                self.kind = Kind.FOUR_OF_A_KIND
            return

        # Check for Five of a Kind
        self.kind = Kind.FIVE_OF_A_KIND


@dataclass
class NormalHand(Hand):
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
