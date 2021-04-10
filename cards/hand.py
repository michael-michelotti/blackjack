from .card import Card
import functools


class Hand:
    def __init__(self, *cards):
        self.cards = list(cards)
        self._value = None

    def __repr__(self):
        if self.cards:
            return f'Hand({", ".join(repr(card) for card in self._cards)})'
        return f'Hand(empty)'

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self.cards[item]

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, new_cards):
        if not all(isinstance(card, Card) for card in new_cards):
            raise TypeError('Every member of a Hand must be a Card.')
        self._cards = new_cards

    @property
    def value(self):
        ace_11_value = sum(card.value for card in self._cards)
        if ace_11_value > 21 and any(card.rank == 'A' for card in self._cards):
            ace_1_value = functools.reduce(self.calc_value_with_ace, self._cards)
            self._value = ace_1_value
        self._value = ace_11_value
        return self._value

    @staticmethod
    def calc_value_with_ace(card):
        if card.rank == 'A':
            return 1
        return card.value

    def render(self):
        return f'{"".join(card.render() for card in self._cards)}'

    def receive_cards(self, cards):
        self.cards.extend(cards)
