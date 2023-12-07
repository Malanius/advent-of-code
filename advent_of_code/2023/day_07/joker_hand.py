from collections import Counter
from dataclasses import dataclass

from hand import Hand


@dataclass
class JokerHand(Hand):
    def __post_init__(self):
        self._make_sortable()
        self._get_kind()
        if "J" in self.cards:
            self._use_jokers()
            self._get_kind()

    def _make_sortable(self):
        """Convert hand to sortable string"""
        cards = self.cards.replace("A", "Z")
        cards = cards.replace("K", "Y")
        cards = cards.replace("Q", "X")
        cards = cards.replace("T", "V")
        cards = cards.replace("J", "0")
        self.sortable_cards = cards

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
