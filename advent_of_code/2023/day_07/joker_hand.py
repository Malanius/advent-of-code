from collections import Counter
from dataclasses import dataclass

from hand import Kind


@dataclass
class JokerHand:
    cards: str
    bid: int
    sortable_cards: str = ""
    kind: Kind = Kind.HIGH_CARD

    def __post_init__(self):
        self._make_sortable()
        self._get_kind()
        if "J" in self.cards:
            self._use_jokers()
            self._get_kind()

    def _use_jokers(self):
        """Use joker to make hand better"""

        # We have all jokers, make it as strong as possible
        if self.cards == "JJJJJ":
            self.cards = "AAAAA"
            return

        counts = Counter(self.cards)

        most_common_cards = counts.most_common()
        most_common_cards = sorted(
            most_common_cards, key=lambda x: (x[1], x[0]), reverse=True
        )

        highest_most_common_card = most_common_cards[0][0]
        if highest_most_common_card == "J":
            highest_most_common_card = most_common_cards[1][0]
        
        self.cards = self.cards.replace("J", highest_most_common_card)

    def _make_sortable(self):
        """Convert hand to sortable string"""
        cards = self.cards.replace("A", "Z")
        cards = cards.replace("K", "Y")
        cards = cards.replace("Q", "X")
        cards = cards.replace("T", "V")
        cards = cards.replace("J", "0")
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
